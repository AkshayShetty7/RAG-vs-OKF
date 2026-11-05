
from src.okf.answer_pipeline import OKFPipeline


def main():
    pipeline = OKFPipeline()

    questions = [
        "What medication allergy is recorded for patient PAT-001?",

        "What medication caused anaphylaxis in patient PAT-007, "
        "and what was the recorded reaction?",

        "What medication combination was associated with severe "
        "hyperkalemia in patient PAT-001?",

        "What are the medication reconciliation requirements under PRO-001?"
    ]

    for question in questions:
        result = pipeline.answer(question)

        print("\n" + "=" * 80)
        print("\nQUESTION")
        print(result["question"])

        print("\nIDENTIFIED ENTITIES")
        print(result["entities"])

        print("\nGENERATED ANSWER")
        print(result["answer"])

        print("\nRETRIEVED EVIDENCE")

        for item in result["evidence"]:
            chunk = item["chunk"]

            print("\nSource type:", item["source_type"])
            print("Source ID:", item["source_id"])
            print("Document:", chunk.document_id)
            print("Section:", chunk.section)
            print("Line:", chunk.start_line)
            print("Retrieval score:", round(item["score"], 4))
            print("Evidence:", chunk.text)


if __name__ == "__main__":
    main()
