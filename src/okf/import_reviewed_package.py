
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "okf_review_package"
DATA = ROOT / "data" / "okf_data"


def read_json(path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main():
    required = [
        "entities.json",
        "facts.json",
        "relationships.json",
        "document_links.json",
    ]

    for filename in required:
        if not (PACKAGE / filename).is_file():
            raise FileNotFoundError(
                f"Missing reviewed package file: {filename}"
            )

    # Read the reviewed package without modifying it.
    entity_package = read_json(PACKAGE / "entities.json")
    fact_package = read_json(PACKAGE / "facts.json")
    relationship_package = read_json(PACKAGE / "relationships.json")
    links_package = read_json(PACKAGE / "document_links.json")

    # Convert entities to the existing graph-engine schema.
    entities = []
    for item in entity_package["entities"]:
        entity = dict(item)
        entity["entity_id"] = item["id"]
        entity["entity_type"] = item.get("type")
        entities.append(entity)

    entity_ids = {item["entity_id"] for item in entities}

    # Convert relationships and preserve all original metadata.
    all_relationships = []
    graph_relationships = []
    review_relationships = []

    for item in relationship_package["relationships"]:
        relationship = dict(item)

        relationship["relationship_id"] = item["id"]
        relationship["source_entity_id"] = item["source"]
        relationship["target_entity_id"] = item["target"]
        relationship["relation_type"] = item["relationship_type"]

        # Adapt evidence field names without discarding original fields.
        normalized_evidence = []

        for original in item.get("evidence", []):
            evidence = dict(original)
            evidence["section"] = (
                original.get("section_title")
                or original.get("section_number")
            )
            normalized_evidence.append(evidence)

        relationship["evidence"] = normalized_evidence
        all_relationships.append(relationship)

        status = item.get("verification", {}).get("status")

        endpoints_exist = (
            item["source"] in entity_ids
            and item["target"] in entity_ids
        )

        has_evidence = any(
            evidence.get("document_id")
            and evidence.get("section")
            and evidence.get("evidence_text", "").strip()
            for evidence in normalized_evidence
        )

        if (
            status == "verified_primary_evidence"
            and endpoints_exist
            and has_evidence
        ):
            graph_relationships.append(relationship)
        else:
            review_relationships.append(relationship)

    # Save graph-ready data and preserve the complete candidate set.
    write_json(
        DATA / "entities" / "entities.json",
        entities,
    )

    write_json(
        DATA / "relationships" / "relationships.json",
        graph_relationships,
    )

    write_json(
        DATA / "relationships" / "relationships_all_candidates.json",
        all_relationships,
    )

    write_json(
        DATA / "relationships" / "relationships_review_required.json",
        review_relationships,
    )

    # Retain facts and document links in their original package schema.
    write_json(
        DATA / "knowledge" / "facts.json",
        fact_package,
    )

    write_json(
        DATA / "provenance" / "document_links.json",
        links_package,
    )

    print("\nOKF PACKAGE IMPORT")
    print("------------------")
    print(f"Entities imported: {len(entities)}")
    print(f"All relationship candidates: {len(all_relationships)}")
    print(f"Graph-ready primary relationships: {len(graph_relationships)}")
    print(f"Relationships held for review: {len(review_relationships)}")
    print(f"Facts retained: {len(fact_package['facts'])}")
    print(f"Document links retained: {len(links_package['links'])}")

    print("\nOutput files:")
    print("  data/okf_data/entities/entities.json")
    print("  data/okf_data/relationships/relationships.json")
    print("  data/okf_data/relationships/relationships_all_candidates.json")
    print("  data/okf_data/relationships/relationships_review_required.json")
    print("  data/okf_data/knowledge/facts.json")
    print("  data/okf_data/provenance/document_links.json")


if __name__ == "__main__":
    main()
