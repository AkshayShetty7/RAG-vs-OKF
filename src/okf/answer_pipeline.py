from src.okf.retrieval import OKFRetriever
from src.generation.groq_client import GroqGenerator


class OKFPipeline:
    def __init__(self):
        self.retriever = OKFRetriever()
        self.generator = GroqGenerator()

    def answer(self, question):
        evidence = self.retriever.retrieve(
            question=question,
            top_k=5,
        )

        if not evidence:
            return {
                "question": question,
                "answer": "Insufficient relevant evidence was retrieved.",
                "evidence": [],
                "entities": self.retriever.last_anchors,
                "token_usage": None
            }

        generation = self.generator.generate_with_usage(
            question=question,
            evidence=evidence,
        )

        return {
            "question": question,
            "answer": generation["answer"],
            "evidence": evidence,
            "entities": self.retriever.last_anchors,
            "token_usage": generation["token_usage"]
        }