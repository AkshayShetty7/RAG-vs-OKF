
import json
from pathlib import Path
from dataclasses import asdict

from src.common.document_loader import load_documents
from src.rag.chunker import DocumentChunker
from src.rag.embedder import Embedder
from src.rag.vector_store import VectorStore


SOURCE_DIR = "data/source_documents"
INDEX_DIR = Path("data/rag_data")

MODEL_NAME = "BAAI/bge-base-en-v1.5"


def build_index():

    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading source documents...")

    documents = load_documents(SOURCE_DIR)

    if not documents:
        raise ValueError("No documents found.")

    print("Documents loaded:", len(documents))

    print("Creating chunks...")

    chunker = DocumentChunker(
        chunk_size=700,
        chunk_overlap=120
    )

    chunks = []

    for document in documents:
        chunks.extend(
            chunker.chunk_document(document)
        )

    if not chunks:
        raise ValueError("No chunks generated.")

    print("Total chunks:", len(chunks))

    print("Loading embedding model...")

    embedder = Embedder(MODEL_NAME)

    print("Generating embeddings...")

    embeddings = embedder.encode_documents(
        [chunk.text for chunk in chunks]
    )

    print("Embedding shape:", embeddings.shape)

    vector_store = VectorStore(
        dimension=embeddings.shape[1]
    )

    vector_store.add(embeddings, chunks)

    vector_store.save(INDEX_DIR / "faiss.index")

    chunk_data = [
        asdict(chunk) for chunk in chunks
    ]

    (INDEX_DIR / "chunks.json").write_text(
        json.dumps(chunk_data, indent=2),
        encoding="utf-8"
    )

    print("\nFAISS INDEX CREATED SUCCESSFULLY")
    print("Documents:", len(documents))
    print("Chunks:", len(chunks))
    print("Embedding dimensions:", embeddings.shape[1])
    print("Index path:", INDEX_DIR / "faiss.index")


if __name__ == "__main__":
    build_index()
