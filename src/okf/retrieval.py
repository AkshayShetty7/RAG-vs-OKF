import json
import re
from pathlib import Path
from types import SimpleNamespace

from rank_bm25 import BM25Okapi


def tokenize(text):
    return re.findall(r"[a-zA-Z0-9_-]+", str(text).lower())


class OKFRetriever:
    def __init__(self):
        base = Path("data/okf_data")

        facts_path = base / "knowledge" / "facts.json"
        entities_path = base / "entities" / "entities.json"
        relationships_path = base / "relationships" / "relationships.json"

        for path in [facts_path, entities_path, relationships_path]:
            if not path.exists():
                raise FileNotFoundError(
                    f"Required OKF data file not found: {path}"
                )

        self.facts = json.loads(
            facts_path.read_text(encoding="utf-8")
        )["facts"]

        entities_data = json.loads(
            entities_path.read_text(encoding="utf-8")
        )
        self.entities = (
            entities_data
            if isinstance(entities_data, list)
            else entities_data["entities"]
        )

        relationships_data = json.loads(
            relationships_path.read_text(encoding="utf-8")
        )
        self.relationships = (
            relationships_data
            if isinstance(relationships_data, list)
            else relationships_data["relationships"]
        )

        self.entity_lookup = {}
        self.entity_types = {}

        for entity in self.entities:
            entity_id = entity.get("id") or entity.get("entity_id")
            name = entity.get("name", "")

            if entity_id:
                self.entity_lookup[entity_id] = str(name)
                self.entity_types[entity_id] = (
                    entity.get("type") or entity.get("entity_type", "")
                )

        self.fact_documents = []

        for fact in self.facts:
            subject = fact.get("subject", {})
            evidence = fact.get("evidence", {})

            searchable_text = " ".join([
                str(subject),
                str(fact.get("predicate", "")),
                str(fact.get("object", "")),
                str(fact.get("object_entity_ids", [])),
                str(fact.get("entity_ids_in_evidence", [])),
                str(fact.get("source_document_id", "")),
                str(fact.get("section_title", "")),
                str(evidence.get("text", "")),
            ])

            self.fact_documents.append(searchable_text)

        self.fact_bm25 = BM25Okapi([
            tokenize(text) for text in self.fact_documents
        ])

        self.graph_relationships = [
            relationship
            for relationship in self.relationships
            if relationship.get("verification", {}).get("status")
            == "verified_primary_evidence"
            and relationship.get("source")
            and relationship.get("target")
            and isinstance(relationship.get("target"), str)
            and relationship.get("evidence")
        ]

        # Discover authoritative documents from protocol metadata.
        # Example: PRO-001 -> HO-02 through the primary_doc fact.
        self.primary_documents = {}

        for fact in self.facts:
            subject = fact.get("subject", {})
            subject_id = (
                subject.get("id")
                if isinstance(subject, dict)
                else None
            )

            if (
                subject_id
                and fact.get("predicate") == "primary_doc"
                and isinstance(fact.get("object"), str)
            ):
                self.primary_documents[subject_id] = fact["object"]

        self.last_anchors = []

    def identify_entities(self, question):
        question_lower = question.lower()
        found = []

        for entity_id, name in self.entity_lookup.items():
            if re.search(
                rf"(?<![a-zA-Z0-9_-]){re.escape(entity_id.lower())}(?![a-zA-Z0-9_-])",
                question_lower,
            ):
                found.append(entity_id)
                continue

            if name and len(name) >= 4 and name.lower() in question_lower:
                found.append(entity_id)

        return sorted(set(found))

    def _make_fact_candidate(self, fact, score, priority=0):
        evidence = fact.get("evidence", {})
        evidence_text = evidence.get("text", "")

        if not evidence_text.strip():
            return None

        document_id = fact.get("source_document_id", "Unknown")
        section = fact.get("section_title", "Unknown section")
        line = evidence.get("line") or 1

        chunk = SimpleNamespace(
            document_id=document_id,
            section=section,
            start_line=int(line),
            end_line=int(line),
            text=evidence_text,
        )

        return {
            "chunk": chunk,
            "score": float(score),
            "priority": int(priority),
            "source_type": "fact",
            "source_id": fact.get("fact_id"),
        }

    def _make_relationship_candidate(self, relationship, evidence, score):
        evidence_text = evidence.get("evidence_text", "")

        if not evidence_text.strip():
            return None

        source = relationship["source"]
        target = relationship["target"]
        predicate = relationship["relationship_type"]

        structured_context = (
            f"Structured relationship: {source} --{predicate}--> {target}\n"
            f"Source passage: {evidence_text}"
        )

        line = evidence.get("line") or 1

        chunk = SimpleNamespace(
            document_id=evidence.get("document_id", "Unknown"),
            section=evidence.get("section_title", "Unknown section"),
            start_line=int(line),
            end_line=int(line),
            text=structured_context,
        )

        return {
            "chunk": chunk,
            "score": float(score),
            "priority": 0,
            "source_type": "relationship",
            "source_id": relationship.get("id"),
        }

    def _is_policy_question(self, question):
        policy_terms = {
            "policy",
            "protocol",
            "requirement",
            "requirements",
            "procedure",
            "compliance",
            "guideline",
            "guidelines",
        }

        question_tokens = set(tokenize(question))
        return bool(question_tokens.intersection(policy_terms))

    def _get_policy_facts(self, anchors, question):
        """
        Return facts belonging to an explicitly identified protocol's
        authoritative source section.

        This is generic: it discovers the primary document from the
        primary_doc metadata instead of hardcoding PRO-001 or HO-02.
        """
        if not self._is_policy_question(question):
            return []

        protocol_anchors = [
            anchor
            for anchor in anchors
            if self.entity_types.get(anchor) == "protocol"
        ]

        selected = []

        for protocol_id in protocol_anchors:
            primary_document = self.primary_documents.get(protocol_id)

            if not primary_document:
                continue

            for fact in self.facts:
                subject = fact.get("subject", {})
                subject_id = (
                    subject.get("id")
                    if isinstance(subject, dict)
                    else None
                )

                section = fact.get("section_title", "")
                source_document = fact.get("source_document_id", "")

                if (
                    subject_id == protocol_id
                    and source_document == primary_document
                    and protocol_id in section
                ):
                    selected.append(fact)

        return selected

    def retrieve(self, question, top_k=5):
        query_tokens = tokenize(question)

        if not query_tokens:
            self.last_anchors = []
            return []

        anchors = self.identify_entities(question)
        self.last_anchors = anchors

        fact_scores = self.fact_bm25.get_scores(query_tokens)

        candidates = []
        policy_facts = self._get_policy_facts(anchors, question)

        policy_fact_ids = {
            fact.get("fact_id")
            for fact in policy_facts
        }

        # First add authoritative policy-section facts.
        # They receive priority over related examples and metadata.
        for fact in policy_facts:
            index = next(
                (
                    i for i, item in enumerate(self.facts)
                    if item.get("fact_id") == fact.get("fact_id")
                ),
                None,
            )

            if index is None:
                continue

            candidate = self._make_fact_candidate(
                fact,
                score=float(fact_scores[index]) + 30.0,
                priority=2,
            )

            if candidate:
                candidates.append(candidate)

        # Retrieve other relevant facts.
        for index, fact in enumerate(self.facts):
            if fact.get("fact_id") in policy_fact_ids:
                continue

            score = float(fact_scores[index])

            subject = fact.get("subject", {})
            subject_id = (
                subject.get("id")
                if isinstance(subject, dict)
                else None
            )

            object_ids = set(fact.get("object_entity_ids", []))
            evidence_ids = set(fact.get("entity_ids_in_evidence", []))

            if anchors:
                # Strongest: the fact is directly about the queried entity.
                if subject_id in anchors:
                    score += 12.0

                # Moderate: the queried entity is a structured object link.
                if object_ids.intersection(anchors):
                    score += 4.0

                # Weak: the entity is only mentioned in the evidence passage.
                if evidence_ids.intersection(anchors):
                    score += 0.5

                # Do not discard incidental mentions, but do not give them
                # the same importance as direct subject/object matches.
                if not (
                    subject_id in anchors
                    or object_ids.intersection(anchors)
                    or evidence_ids.intersection(anchors)
                ):
                    continue

            candidate = self._make_fact_candidate(fact, score)

            if candidate:
                candidates.append(candidate)

        # Retrieve directly connected primary-evidence graph edges.
        # This baseline still does not perform multi-hop graph expansion.
        if anchors:
            for relationship in self.graph_relationships:
                source = relationship["source"]
                target = relationship["target"]

                if source not in anchors and target not in anchors:
                    continue

                for evidence in relationship.get("evidence", []):
                    if evidence.get("role") != "primary":
                        continue

                    if not evidence.get("evidence_text"):
                        continue

                    relationship_text = " ".join([
                        source,
                        relationship["relationship_type"],
                        target,
                        evidence.get("evidence_text", ""),
                    ])

                    overlap = len(
                        set(query_tokens).intersection(
                            set(tokenize(relationship_text))
                        )
                    )

                    candidate = self._make_relationship_candidate(
                        relationship,
                        evidence,
                        4.0 + overlap,
                    )

                    if candidate:
                        candidates.append(candidate)

        # Priority first, then lexical/anchor relevance.
        candidates.sort(
            key=lambda item: (
                item.get("priority", 0),
                item["score"],
            ),
            reverse=True,
        )

        selected = []
        seen = set()

        for candidate in candidates:
            chunk = candidate["chunk"]

            key = (
                chunk.document_id,
                chunk.start_line,
                chunk.text,
            )

            if key in seen:
                continue

            seen.add(key)
            selected.append(candidate)

            if len(selected) >= top_k:
                break

        return selected
