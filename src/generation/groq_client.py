import truststore

truststore.inject_into_ssl()

import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


class GroqGenerator:

    def __init__(self, model="openai/gpt-oss-120b"):
        api_key = os.environ.get("GROQ_API_KEY")

        if not api_key:
            raise EnvironmentError(
                "GROQ_API_KEY not found. Check your .env file."
            )

        self.client = Groq(api_key=api_key)
        self.model = model

    def generate_with_usage(self, question, evidence):

        context_parts = []

        for i, item in enumerate(evidence, start=1):
            chunk = item["chunk"]

            context_parts.append(
                f"""
Evidence {i}
Document ID: {chunk.document_id}
Section: {chunk.section}
Lines: {chunk.start_line}-{chunk.end_line}

Content:
{chunk.text}
"""
            )

        context = "\n".join(context_parts)

        system_prompt = """
You are a document-grounded question answering system.

Answer using ONLY the supplied evidence.

Rules:
1. Never invent facts.
2. If evidence is insufficient, say so explicitly.
3. Cite document IDs and section names.
4. Distinguish facts from inferences.
5. Be concise and precise.
6. Do not provide medical advice.
"""

        user_prompt = f"""
Question:
{question}

Retrieved evidence:
{context}

Provide your answer with document and section citations.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0,
            max_completion_tokens=1000
        )

        answer = response.choices[0].message.content

        # Capture actual usage reported by the Groq API.
        usage = response.usage

        token_usage = None

        if usage is not None:
            details = getattr(
                usage, "completion_tokens_details", None
            )

            reasoning_tokens = (
                getattr(details, "reasoning_tokens", None)
                if details is not None else None
            )

            token_usage = {
                "prompt_tokens": usage.prompt_tokens,
                "completion_tokens": usage.completion_tokens,
                "total_tokens": usage.total_tokens,
                "reasoning_tokens": reasoning_tokens
            }

        return {
            "answer": answer,
            "token_usage": token_usage
        }

    # Preserve compatibility with existing code that expects a string.
    def generate(self, question, evidence):
        result = self.generate_with_usage(question, evidence)
        return result["answer"]