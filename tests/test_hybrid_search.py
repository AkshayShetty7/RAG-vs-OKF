import json
from pathlib import Path

from src.rag.chunker import Chunk
from src.rag.embedder import Embedder
from src.rag.vector_store import VectorStore
from src.rag.bm25_search import BM25Search
from src.rag.hybrid_search import HybridSearch


def test_hybrid_search():
    index_dir = Path("data/rag_data")

    chunk_data = json.loads(
        (index_dir / "chunks.json").read_text(encoding="utf-8")
    )
    chunks = [Chunk(**item) for item in chunk_data]

    embedder = Embedder()

    vector_store = VectorStore(dimension=768)
    vector_store.chunks = chunks
    vector_store.load(index_dir / "faiss.index")

    bm25_search = BM25Search(chunks)

    hybrid = HybridSearch(
        vector_store=vector_store,
        bm25_search=bm25_search
    )

    query = "What medication allergy is recorded for patient PAT-001?"
    query_embedding = embedder.encode_query(query)

    results = hybrid.search(
        query=query,
        query_embedding=query_embedding,
        top_k=5
    )

    assert len(results) > 0

    print("\nHYBRID SEARCH SUCCESSFUL")

    for result in results:
        chunk = result["chunk"]
        print("\nRRF score:", round(result["score"], 5))
        print("Document:", chunk.document_id)
        print("Section:", chunk.section)
        print("Text:", chunk.text)

    assert any(
        "MED-005" in result["chunk"].text
        for result in results
    )


if __name__ == "__main__":
    test_hybrid_search()