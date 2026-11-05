import json
from pathlib import Path

from src.rag.chunker import Chunk
from src.rag.embedder import Embedder
from src.rag.vector_store import VectorStore
from src.rag.bm25_search import BM25Search
from src.rag.hybrid_search import HybridSearch
from src.rag.reranker import Reranker
from src.generation.groq_client import GroqGenerator


class RAGPipeline:
    def __init__(self):
        index_dir = Path("data/rag_data")

        chunk_data = json.loads(
            (index_dir / "chunks.json").read_text(encoding="utf-8")
        )

        self.chunks = [
            Chunk(**item) for item in chunk_data
        ]

        self.embedder = Embedder()

        self.vector_store = VectorStore(dimension=768)
        self.vector_store.chunks = self.chunks
        self.vector_store.load(index_dir / "faiss.index")

        self.bm25 = BM25Search(self.chunks)

        self.hybrid = HybridSearch(
            vector_store=self.vector_store,
            bm25_search=self.bm25,
        )

        self.reranker = Reranker()
        self.generator = GroqGenerator()

    def answer(self, question):
        query_embedding = self.embedder.encode_query(question)

        candidates = self.hybrid.search(
            query=question,
            query_embedding=query_embedding,
            dense_top_k=20,
            bm25_top_k=20,
            top_k=20,
        )

        ranked_evidence = self.reranker.rerank(
            query=question,
            results=candidates,
            top_k=5,
        )

        generation = self.generator.generate_with_usage(
            question=question,
            evidence=ranked_evidence,
        )

        return {
            "question": question,
            "answer": generation["answer"],
            "evidence": ranked_evidence,
            "token_usage": generation["token_usage"]
        }