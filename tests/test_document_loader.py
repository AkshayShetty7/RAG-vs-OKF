
from pathlib import Path

from src.common.document_loader import load_documents


def test_document_loader():

    root = "data/source_documents"

    documents = load_documents(root)

    assert len(documents) >= 1

    doc = documents[0]

    assert doc.document_id == "DOC-PAT-001"
    assert doc.title == "Patient Medical Record 001"
    assert len(doc.sections) >= 1

    print("\nDocument loaded successfully!")
    print("ID:", doc.document_id)
    print("Title:", doc.title)
    print("Sections:", len(doc.sections))
    print("Content length:", len(doc.content))


if __name__ == "__main__":
    test_document_loader()
