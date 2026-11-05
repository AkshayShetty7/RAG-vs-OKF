from sentence_transformers import CrossEncoder


class Reranker:
    def __init__(self, model_name="BAAI/bge-reranker-base"):
        print(f"Loading reranker: {model_name}")
        self.model = CrossEncoder(model_name)
        print("Reranker loaded.")

    def rerank(self, query: str, results: list, top_k: int = 5):
        if not results:
            return []

        pairs = [
            (query, result["chunk"].text)
            for result in results
        ]

        scores = self.model.predict(pairs)

        reranked = []

        for result, score in zip(results, scores):
            reranked.append({
                "chunk": result["chunk"],
                "score": float(score)
            })

        reranked.sort(
            key=lambda item: item["score"],
            reverse=True
        )

        return reranked[:top_k]