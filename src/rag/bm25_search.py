import re
from rank_bm25 import BM25Okapi


def tokenize(text: str) -> list[str]:
    return re.findall(r"\b[a-zA-Z0-9_-]+\b", text.lower())


class BM25Search:
    def __init__(self, chunks):
        self.chunks = chunks
        tokenized_chunks = [
            tokenize(chunk.text) for chunk in chunks
        ]
        self.index = BM25Okapi(tokenized_chunks)

    def search(self, query: str, top_k: int = 5):
        if not self.chunks:
            return []

        scores = self.index.get_scores(tokenize(query))

        ranked_indices = sorted(
            range(len(scores)),
            key=lambda i: scores[i],
            reverse=True
        )[:top_k]

        return [
            {
                "chunk": self.chunks[i],
                "score": float(scores[i])
            }
            for i in ranked_indices
        ]