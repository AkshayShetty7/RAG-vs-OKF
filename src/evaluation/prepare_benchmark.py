import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

OUTPUT = ROOT / "data" / "benchmark" / "questions.json"

questions = [
    {
        "question_id": "Q01",
        "question": "What medication allergy is recorded for patient PAT-001?",
        "expected_document_ids": ["PR-01"],
        "expected_entity_ids": ["PAT-001"],
        "retrieval_type": "single_document"
    },
    {
        "question_id": "Q02",
        "question": "What medication caused anaphylaxis in patient PAT-007, and what was the recorded reaction?",
        "expected_document_ids": ["HO-08", "PR-07"],
        "expected_entity_ids": ["PAT-007", "MED-016"],
        "retrieval_type": "multi_document"
    },
    {
        "question_id": "Q03",
        "question": "What medication combination was associated with severe hyperkalemia in patient PAT-001?",
        "expected_document_ids": ["DG-01", "MP-01", "MP-07"],
        "expected_entity_ids": ["PAT-001", "MED-004", "MED-008"],
        "retrieval_type": "multi_document"
    },
    {
        "question_id": "Q04",
        "question": "What are the medication reconciliation requirements under PRO-001?",
        "expected_document_ids": ["HO-02", "DG-08", "HO-07"],
        "expected_entity_ids": ["PRO-001"],
        "retrieval_type": "multi_document"
    }
]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT.open("w", encoding="utf-8") as f:
    json.dump(questions, f, indent=4, ensure_ascii=False)

print("BENCHMARK QUESTIONS SAVED")
print("-------------------------")
print(f"Questions: {len(questions)}")
print(f"Output: {OUTPUT.relative_to(ROOT)}")
