
from dataclasses import dataclass

from src.common.document_schema import Document


@dataclass
class Chunk:
    chunk_id: str
    document_id: str
    title: str
    section: str
    text: str
    start_line: int
    end_line: int


class DocumentChunker:

    def __init__(
        self,
        chunk_size: int = 700,
        chunk_overlap: int = 120
    ):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")

        if not 0 <= chunk_overlap < chunk_size:
            raise ValueError(
                "chunk_overlap must be >= 0 and < chunk_size"
            )

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def chunk_document(self, document: Document) -> list[Chunk]:

        chunks = []
        chunk_number = 0

        for section in document.sections:

            lines = section["text"].splitlines()

            # Initial approximation: one word = one token.
            # We'll replace this with actual tokenizer-based
            # counting before final benchmarking.
            words = []

            for line_number, line in enumerate(
                lines,
                start=section["start_line"]
            ):
                for word in line.split():
                    words.append((word, line_number))

            start = 0

            while start < len(words):

                end = min(
                    start + self.chunk_size,
                    len(words)
                )

                selected = words[start:end]

                if not selected:
                    break

                chunk_text = " ".join(
                    word for word, _ in selected
                )

                chunk_number += 1

                chunks.append(
                    Chunk(
                        chunk_id=(
                            f"{document.document_id}-"
                            f"CHUNK-{chunk_number:04d}"
                        ),
                        document_id=document.document_id,
                        title=document.title,
                        section=section["title"],
                        text=chunk_text,
                        start_line=selected[0][1],
                        end_line=selected[-1][1],
                    )
                )

                if end == len(words):
                    break

                start = end - self.chunk_overlap

        return chunks
