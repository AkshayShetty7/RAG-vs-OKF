
import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension):
        self.index = faiss.IndexFlatIP(dimension)
        self.chunks = []

    def add(self, embeddings, chunks):

        embeddings = np.asarray(
            embeddings,
            dtype=np.float32
        )

        if len(embeddings) != len(chunks):
            raise ValueError(
                "Number of embeddings must match number of chunks"
            )

        if len(embeddings) == 0:
            return

        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(self, query_embedding, top_k=5):

        if self.index.ntotal == 0:
            return []

        query_embedding = np.asarray(
            query_embedding,
            dtype=np.float32
        )

        scores, indices = self.index.search(
            query_embedding,
            min(top_k, self.index.ntotal)
        )

        results = []

        for score, index in zip(scores[0], indices[0]):

            if index < 0:
                continue

            results.append({
                "chunk": self.chunks[index],
                "score": float(score)
            })

        return results

    def save(self, index_path):
        faiss.write_index(self.index, str(index_path))

    def load(self, index_path):
        self.index = faiss.read_index(str(index_path))
