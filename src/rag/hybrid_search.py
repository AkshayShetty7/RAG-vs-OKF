class HybridSearch:
    def __init__(self, vector_store, bm25_search):
        self.vector_store = vector_store
        self.bm25_search = bm25_search

    def search(
        self,
        query,
        query_embedding,
        top_k=20,
        dense_top_k=20,
        bm25_top_k=20,
        rrf_k=60
    ):
        dense_results = self.vector_store.search(
            query_embedding,
            top_k=dense_top_k
        )

        bm25_results = self.bm25_search.search(
            query,
            top_k=bm25_top_k
        )

        fused_scores = {}
        chunk_lookup = {}

        for results in [dense_results, bm25_results]:
            for rank, result in enumerate(results, start=1):
                chunk = result["chunk"]
                chunk_id = chunk.chunk_id

                fused_scores[chunk_id] = (
                    fused_scores.get(chunk_id, 0)
                    + 1 / (rrf_k + rank)
                )

                chunk_lookup[chunk_id] = chunk

        ranked = sorted(
            fused_scores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        return [
            {
                "chunk": chunk_lookup[chunk_id],
                "score": score
            }
            for chunk_id, score in ranked[:top_k]
        ]