import json
import re
from pathlib import Path
from collections import defaultdict, deque


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "data" / "okf_data"
SOURCE_REGISTRY = DATA_DIR / "provenance" / "source_registry.json"
ENTITY_REGISTRY = DATA_DIR / "provenance" / "entity_registry.json"

ENTITIES_FILE = DATA_DIR / "entities" / "entities.json"
RELATIONSHIPS_FILE = DATA_DIR / "relationships" / "relationships.json"


def load_json(path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def normalize_text(text):
    return re.sub(r"\s+", " ", str(text)).strip().casefold()


class GraphValidator:

    def __init__(self):
        self.documents = {
            item["document_id"]: item
            for item in load_json(SOURCE_REGISTRY)
        }

        self.source_entity_ids = {
            item["entity_id"]
            for item in load_json(ENTITY_REGISTRY)
        }

    def validate(self, entities, relationships):
        errors = []
        warnings = []

        entity_map = {}

        for entity in entities:
            entity_id = entity.get("entity_id")

            if not entity_id:
                errors.append("Entity without entity_id.")
                continue

            if entity_id in entity_map:
                errors.append(f"Duplicate entity ID: {entity_id}")
                continue

            entity_map[entity_id] = entity

            if entity_id not in self.source_entity_ids:
                warnings.append(
                    f"{entity_id}: not declared in source frontmatter."
                )

        relationship_ids = set()

        for relationship in relationships:
            relationship_id = relationship.get("relationship_id")

            if not relationship_id:
                errors.append("Relationship without relationship_id.")
            elif relationship_id in relationship_ids:
                errors.append(
                    f"Duplicate relationship ID: {relationship_id}"
                )
            else:
                relationship_ids.add(relationship_id)

            source_id = relationship.get("source_entity_id")
            target_id = relationship.get("target_entity_id")
            relation_type = relationship.get("relation_type")

            if source_id not in entity_map:
                errors.append(
                    f"{relationship_id}: missing source entity {source_id}"
                )

            if target_id not in entity_map:
                errors.append(
                    f"{relationship_id}: missing target entity {target_id}"
                )

            if not relation_type:
                errors.append(
                    f"{relationship_id}: missing relation_type"
                )

            evidence_list = relationship.get("evidence", [])

            if not isinstance(evidence_list, list) or not evidence_list:
                errors.append(
                    f"{relationship_id}: no evidence supplied."
                )
                continue

            for evidence in evidence_list:
                doc_id = evidence.get("document_id")
                section = evidence.get("section")
                quote = evidence.get("evidence_text")

                if doc_id not in self.documents:
                    errors.append(
                        f"{relationship_id}: unknown document {doc_id}"
                    )
                    continue

                if not section:
                    errors.append(
                        f"{relationship_id}: evidence section missing."
                    )

                if not quote or not str(quote).strip():
                    errors.append(
                        f"{relationship_id}: evidence passage missing."
                    )
                    continue

                source_path = ROOT / self.documents[doc_id]["file_path"]
                source_text = source_path.read_text(encoding="utf-8-sig")

                if normalize_text(quote) not in normalize_text(source_text):
                    errors.append(
                        f"{relationship_id}: evidence passage not found "
                        f"in {doc_id}."
                    )

        return {
            "entity_count": len(entity_map),
            "relationship_count": len(relationships),
            "error_count": len(errors),
            "warning_count": len(warnings),
            "errors": errors,
            "warnings": warnings,
            "valid": len(errors) == 0
        }



class KnowledgeGraph:

    def __init__(self, entities, relationships):
        self.entities = {
            item["entity_id"]: item
            for item in entities
        }

        self.adjacency = defaultdict(list)

        for relationship in relationships:
            source_id = relationship["source_entity_id"]
            target_id = relationship["target_entity_id"]

            self.adjacency[source_id].append({
                "relationship": relationship,
                "neighbor_id": target_id,
                "traversal_direction": "forward",
            })

            self.adjacency[target_id].append({
                "relationship": relationship,
                "neighbor_id": source_id,
                "traversal_direction": "reverse",
            })

    def traverse(self, start_entity_id, max_depth=2):
        if start_entity_id not in self.entities:
            return []

        visited_states = {(start_entity_id, 0)}
        queue = deque([(start_entity_id, 0)])
        results = []

        while queue:
            current_id, depth = queue.popleft()

            if depth >= max_depth:
                continue

            for edge in self.adjacency[current_id]:
                neighbor_id = edge["neighbor_id"]
                next_depth = depth + 1

                results.append({
                    "from_entity": current_id,
                    "to_entity": neighbor_id,
                    "relationship": edge["relationship"],
                    "traversal_direction": edge["traversal_direction"],
                    "depth": next_depth,
                })

                state = (neighbor_id, next_depth)

                if state not in visited_states:
                    visited_states.add(state)
                    queue.append((neighbor_id, next_depth))

        return results


def main():
    if not ENTITIES_FILE.exists() or not RELATIONSHIPS_FILE.exists():
        print("GRAPH DATA NOT IMPORTED YET")
        print("--------------------------------")
        print("Expected files:")
        print(f"  {ENTITIES_FILE.relative_to(ROOT)}")
        print(f"  {RELATIONSHIPS_FILE.relative_to(ROOT)}")
        print("\nThe validator and graph engine are ready.")
        print("Import Claude's output before running graph validation.")
        return

    entities = load_json(ENTITIES_FILE)
    relationships = load_json(RELATIONSHIPS_FILE)

    validator = GraphValidator()
    report = validator.validate(entities, relationships)

    print("\nOKF GRAPH VALIDATION")
    print("-------------------")
    print(f"Entities: {report['entity_count']}")
    print(f"Relationships: {report['relationship_count']}")
    print(f"Errors: {report['error_count']}")
    print(f"Warnings: {report['warning_count']}")
    print(f"Valid: {report['valid']}")

    for error in report["errors"]:
        print(f"ERROR: {error}")

    for warning in report["warnings"]:
        print(f"WARNING: {warning}")

    if report["valid"]:
        graph = KnowledgeGraph(entities, relationships)
        print("\nGraph engine initialized successfully.")
        print(f"Connected entity nodes: {len(graph.entities)}")


if __name__ == "__main__":
    main()
