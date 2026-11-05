import json
import re
import yaml
from pathlib import Path
from collections import defaultdict, Counter


ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "data/okf_data/provenance/source_registry.json"
OUTPUT_DIR = ROOT / "data/okf_data/provenance"


def read_frontmatter(path):
    text = path.read_text(encoding="utf-8-sig")

    if not text.startswith("---"):
        raise ValueError(f"Missing YAML frontmatter: {path.name}")

    parts = text.split("---", 2)

    if len(parts) < 3:
        raise ValueError(f"Malformed YAML frontmatter: {path.name}")

    metadata = yaml.safe_load(parts[1])

    if not isinstance(metadata, dict):
        raise ValueError(f"Frontmatter must be a YAML mapping: {path.name}")

    return metadata


def main():
    with REGISTRY_PATH.open("r", encoding="utf-8") as f:
        registry = json.load(f)

    known_doc_ids = {doc["document_id"] for doc in registry}

    entity_sources = defaultdict(list)
    document_links = []
    source_metadata = []
    missing_related_docs = []
    missing_entity_lists = []

    for doc in registry:
        path = ROOT / doc["file_path"]
        metadata = read_frontmatter(path)

        doc_id = metadata.get("doc_id", metadata.get("document_id"))

        if doc_id != doc["document_id"]:
            raise ValueError(
                f"Document ID mismatch in {path.name}: "
                f"manifest={doc['document_id']}, frontmatter={doc_id}"
            )

        entities = metadata.get("entities", []) or []
        related_docs = metadata.get("related_docs", []) or []

        if not isinstance(entities, list):
            raise ValueError(f"'entities' must be a list in {path.name}")

        if not isinstance(related_docs, list):
            raise ValueError(f"'related_docs' must be a list in {path.name}")

        for entity_id in entities:
            entity_id = str(entity_id).strip()

            if not entity_id:
                continue

            entity_sources[entity_id].append(doc_id)

        for related_id in related_docs:
            related_id = str(related_id).strip()

            if related_id not in known_doc_ids:
                missing_related_docs.append({
                    "source_document_id": doc_id,
                    "referenced_document_id": related_id
                })
            else:
                document_links.append({
                    "source_document_id": doc_id,
                    "related_document_id": related_id
                })

        source_metadata.append({
            "document_id": doc_id,
            "title": metadata.get("title", doc["title"]),
            "folder": metadata.get("folder", doc["folder"]),
            "version": metadata.get("version", doc["version"]),
            "synthetic": metadata.get("synthetic"),
            "entities": entities,
            "related_docs": related_docs
        })

        if not entities:
            missing_entity_lists.append(doc_id)

    entity_registry = [
        {
            "entity_id": entity_id,
            "source_document_ids": sorted(set(source_ids))
        }
        for entity_id, source_ids in sorted(entity_sources.items())
    ]

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    outputs = {
        "entity_registry.json": entity_registry,
        "document_links.json": document_links,
        "source_metadata.json": source_metadata
    }

    for filename, data in outputs.items():
        with (OUTPUT_DIR / filename).open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    print("\nSOURCE METADATA EXTRACTION")
    print("-------------------------")
    print(f"Documents processed: {len(source_metadata)}")
    print(f"Unique entity IDs: {len(entity_registry)}")
    print(f"Declared document links: {len(document_links)}")
    print(f"Unresolved document references: {len(missing_related_docs)}")
    print(f"Documents without entity declarations: {len(missing_entity_lists)}")

    if missing_related_docs:
        print("\nUNRESOLVED DOCUMENT REFERENCES:")
        for item in missing_related_docs:
            print(
                f"  {item['source_document_id']} -> "
                f"{item['referenced_document_id']}"
            )

    if missing_entity_lists:
        print("\nDocuments with no declared entities:")
        print(", ".join(missing_entity_lists))

    print("\nEntity counts by prefix:")
    counts = Counter(
        entity["entity_id"].split("-")[0]
        for entity in entity_registry
    )

    for prefix, count in sorted(counts.items()):
        print(f"  {prefix}: {count}")

    print("\nOUTPUT FILES:")
    for filename in outputs:
        print(f"  data/okf_data/provenance/{filename}")


if __name__ == "__main__":
    main()
