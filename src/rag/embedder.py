
from sentence_transformers import SentenceTransformer


class Embedder:

    def __init__(
        self,
        model_name="BAAI/bge-base-en-v1.5"
    ):
        print(f"Loading embedding model: {model_name}")

        self.model = SentenceTransformer(model_name)

        print("Embedding model loaded.")

    def encode_documents(self, texts):
        return self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=True
        )

    def encode_query(self, query):
        return self.model.encode(
            [query],
            normalize_embeddings=True,
            convert_to_numpy=True
        )
