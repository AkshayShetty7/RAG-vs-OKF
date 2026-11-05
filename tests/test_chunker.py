
from src.common.document_loader import load_documents
from src.rag.chunker import DocumentChunker


def test_chunker():

    documents = load_documents("data/source_documents")

    chunker = DocumentChunker(
        chunk_size=50,
        chunk_overlap=10
    )

    chunks = chunker.chunk_document(documents[0])

    assert len(chunks) > 0

    for chunk in chunks:
        assert chunk.document_id == "DOC-PAT-001"
        assert chunk.text.strip()
        assert chunk.start_line <= chunk.end_line

    print("\nCHUNKING SUCCESSFUL")
    print("Number of chunks:", len(chunks))

    for chunk in chunks:
        print("\nChunk ID:", chunk.chunk_id)
        print("Section:", chunk.section)
        print("Text:", chunk.text)


if __name__ == "__main__":
    test_chunker()
