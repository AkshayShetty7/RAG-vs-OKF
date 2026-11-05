import json
import hashlib
from pathlib import Path
from collections import Counter


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = PROJECT_ROOT / "data" / "source_documents" / "manifest.json"
OUTPUT_PATH = PROJECT_ROOT / "data" / "okf_data" / "provenance" / "source_registry.json"

EXPECTED_DOCUMENT_COUNT = 39


def main():
    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"Manifest not found: {MANIFEST_PATH}")

    with MANIFEST_PATH.open("r", encoding="utf-8") as file:
        documents = json.load(file)

    if len(documents) != EXPECTED_DOCUMENT_COUNT:
        raise ValueError(
            f"Expected {EXPECTED_DOCUMENT_COUNT} documents, "
            f"but manifest contains {len(documents)}."
        )

    document_ids = [doc["document_id"] for doc in documents]

    if len(document_ids) != len(set(document_ids)):
        raise ValueError("Duplicate document IDs found in manifest.")

    registry = []
    missing_files = []

    for doc in documents:
        source_path = PROJECT_ROOT / doc["file_path"]

        if not source_path.exists():
            missing_files.append(doc["file_path"])
            continue

        content = source_path.read_bytes()

        registry.append({
            "document_id": doc["document_id"],
            "title": doc["title"],
            "folder": doc["folder"],
            "document_type": doc["document_type"],
            "version": doc["version"],
            "file_path": doc["file_path"],
            "section_count": doc["section_count"],
            "character_count": doc["character_count"],
            "sha256": hashlib.sha256(content).hexdigest(),
            "file_size_bytes": len(content)
        })

    if missing_files:
        print("MISSING SOURCE FILES:")
        for path in missing_files:
            print(f"  - {path}")
        raise FileNotFoundError("Registry generation stopped.")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_PATH.open("w", encoding="utf-8") as file:
        json.dump(registry, file, indent=4, ensure_ascii=False)

    type_counts = Counter(doc["document_type"] for doc in registry)

    print("\nSOURCE REGISTRY VALIDATION SUCCESSFUL")
    print("-------------------------------------")
    print(f"Documents registered: {len(registry)}")
    print(f"Unique document IDs: {len(set(document_ids))}")
    print(f"All source files exist: Yes")
    print(f"SHA-256 hashes generated: {len(registry)}")
    print("\nDocuments by type:")

    for document_type, count in sorted(type_counts.items()):
        print(f"  {document_type}: {count}")

    print(f"\nRegistry saved to: {OUTPUT_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
