
import json
from pathlib import Path

from src.rag.embedder import Embedder
from src.rag.vector_store import VectorStore
from src.rag.chunker import Chunk


def test_vector_search():

    index_dir = Path("data/rag_data")

    assert (index_dir / "faiss.index").exists()
    assert (index_dir / "chunks.json").exists()

    chunk_data = json.loads(
        (index_dir / "chunks.json").read_text(
            encoding="utf-8"
        )
    )

    chunks = [
        Chunk(**item) for item in chunk_data
    ]

    embedder = Embedder()

    vector_store = VectorStore(
        dimension=768
    )

    vector_store.chunks = chunks
    vector_store.load(index_dir / "faiss.index")

    query = "What allergies are recorded for patient PAT-001?"

    query_embedding = embedder.encode_query(query)

    results = vector_store.search(
        query_embedding,
        top_k=3
    )

    assert len(results) > 0

    print("\nVECTOR SEARCH SUCCESSFUL")

    for result in results:
        print("\nScore:", round(result["score"], 4))
        print("Document:", result["chunk"].document_id)
        print("Section:", result["chunk"].section)
        print("Text:", result["chunk"].text)


if __name__ == "__main__":
    test_vector_search()
