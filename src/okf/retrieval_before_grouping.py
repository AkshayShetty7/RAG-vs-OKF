
import json
import re
from pathlib import Path
from types import SimpleNamespace
from collections import defaultdict

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

        for entity in self.entities:
            entity_id = entity.get("id") or entity.get("entity_id")
            name = entity.get("name", "")

            if entity_id:
                self.entity_lookup[entity_id] = str(name)

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

    def _make_fact_candidate(self, fact, score):
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
            f"Structured relationship: "
            f"{source} --{predicate}--> {target}\n"
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
            "source_type": "relationship",
            "source_id": relationship.get("id"),
        }

    def _query_intent(self, question):
        q = question.lower()

        if any(term in q for term in [
            "adverse reaction", "adverse event", "caused",
            "reaction", "hyperkalemia", "anaphylaxis",
            "side effect", "toxicity",
        ]):
            return "adverse_event"

        if any(term in q for term in [
            "allergy", "allergic", "anaphylactic",
        ]):
            return "allergy"

        if any(term in q for term in [
            "protocol", "requirements", "procedure",
            "policy", "reconciliation",
        ]):
            return "policy"

        return "general"

    def _fact_anchor_score(self, fact, anchors):
        if not anchors:
            return 0.0

        subject = fact.get("subject", {})
        subject_id = (
            subject.get("id") if isinstance(subject, dict) else None
        )

        object_ids = set(fact.get("object_entity_ids", []))
        evidence_ids = set(fact.get("entity_ids_in_evidence", []))

        score = 0.0

        if subject_id in anchors:
            score += 8.0

        if object_ids.intersection(anchors):
            score += 4.0

        # Incidental mentions are weaker than explicit subject/object links.
        if evidence_ids.intersection(anchors):
            score += 1.0

        return score

    def retrieve(self, question, top_k=5):
        query_tokens = tokenize(question)

        if not query_tokens:
            return []

        anchors = self.identify_entities(question)
        intent = self._query_intent(question)

        fact_scores = self.fact_bm25.get_scores(query_tokens)

        # Group facts extracted from the same source passage.
        passage_groups = defaultdict(list)

        for index, fact in enumerate(self.facts):
            evidence = fact.get("evidence", {})
            text = evidence.get("text", "")

            if not text.strip():
                continue

            document_id = fact.get("source_document_id", "Unknown")
            section = fact.get("section_title", "Unknown")
            line = evidence.get("line") or 1

            # Exact source passage is the deduplication key.
            key = (
                document_id,
                section,
                int(line),
                text,
            )

            score = float(fact_scores[index])
            score += self._fact_anchor_score(fact, anchors)

            predicate = str(fact.get("predicate", "")).lower()

            if intent == "adverse_event":
                if predicate in {
                    "adr", "drug", "patient", "severity",
                    "outcome", "reaction",
                }:
                    score += 5.0

                if "adr" in predicate or "reaction" in predicate:
                    score += 3.0

            elif intent == "allergy":
                if "allerg" in predicate:
                    score += 6.0

            elif intent == "policy":
                if document_id.startswith("HO-"):
                    score += 3.0

            passage_groups[key].append({
                "fact": fact,
                "score": score,
            })

        candidates = []

        for key, group in passage_groups.items():
            # Keep one candidate for each source passage.
            best = max(group, key=lambda item: item["score"])

            candidate = self._make_fact_candidate(
                best["fact"],
                best["score"],
            )

            if candidate:
                candidate["fact_ids"] = [
                    item["fact"].get("fact_id")
                    for item in group
                ]
                candidates.append(candidate)

        # Direct one-hop relationships only in this baseline.
        if anchors:
            for relationship in self.graph_relationships:
                source = relationship["source"]
                target = relationship["target"]

                if source not in anchors and target not in anchors:
                    continue

                for evidence in relationship.get("evidence", []):
                    if evidence.get("role") != "primary":
                        continue

                    text = evidence.get("evidence_text", "")

                    if not text.strip():
                        continue

                    relationship_text = " ".join([
                        source,
                        relationship["relationship_type"],
                        target,
                        text,
                    ])

                    overlap = len(
                        set(query_tokens).intersection(
                            set(tokenize(relationship_text))
                        )
                    )

                    score = 4.0 + overlap

                    candidate = self._make_relationship_candidate(
                        relationship,
                        evidence,
                        score,
                    )

                    if candidate:
                        candidates.append(candidate)

        candidates.sort(
            key=lambda item: item["score"],
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

        self.last_anchors = anchors
        self.last_intent = intent

        return selected
