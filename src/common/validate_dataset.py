
import json
from pathlib import Path

from src.common.document_loader import load_documents


SOURCE_DIR = Path("data/source_documents")
MANIFEST_PATH = SOURCE_DIR / "manifest.json"

EXPECTED_FOLDERS = {
    "01_patient_records",
    "02_diseases_guidelines",
    "03_medications_pharmacy",
    "04_laboratory_diagnostics",
    "05_hospital_operations",
}


def validate_dataset():

    errors = []
    documents = []

    # Check required folders
    for folder in EXPECTED_FOLDERS:
        if not (SOURCE_DIR / folder).is_dir():
            errors.append(f"Missing folder: {folder}")

    # Load documents
    try:
        documents = load_documents(str(SOURCE_DIR))
    except Exception as error:
        errors.append(f"Document loading failed: {error}")

    if not documents:
        errors.append("No Markdown documents found.")

    # Validate documents
    seen_ids = set()

    for doc in documents:

        if doc.document_id in seen_ids:
            errors.append(
                f"Duplicate document ID: {doc.document_id}"
            )

        seen_ids.add(doc.document_id)

        actual_folder = Path(doc.file_path).parent.name

        if doc.folder != actual_folder:
            errors.append(
                f"{doc.document_id}: incorrect folder metadata"
            )

        if not doc.content.strip():
            errors.append(
                f"Empty document: {doc.document_id}"
            )

    # Display errors
    if errors:
        print("\nDATASET VALIDATION FAILED")

        for error in errors:
            print("ERROR:", error)

        raise SystemExit(1)

    # Generate manifest
    manifest = []

    for doc in documents:

        manifest.append({
            "document_id": doc.document_id,
            "title": doc.title,
            "folder": doc.folder,
            "document_type": doc.document_type,
            "version": doc.version,
            "file_path": doc.file_path,
            "section_count": len(doc.sections),
            "character_count": len(doc.content),
        })

    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=4),
        encoding="utf-8"
    )

    print("\nDATASET VALIDATION SUCCESSFUL")
    print("-----------------------------")
    print("Documents:", len(documents))
    print("Unique IDs:", len(seen_ids))
    print("Manifest:", MANIFEST_PATH)


if __name__ == "__main__":
    validate_dataset()
