
"""
Run the frozen evaluation dataset through the existing RAG and OKF pipelines.

From the project root:

    python -m src.evaluation.run_benchmark --system both

With a separate output directory:

    python -m src.evaluation.run_benchmark \
        --system both \
        --dataset data/evaluation/evaluation_dataset_FINAL.json \
        --output-dir outputs/benchmark_with_usage

Features:
- Checkpoints after every question.
- Skips questions that have already succeeded.
- Retries questions that previously failed.
- Captures actual Groq API token usage.
- Exports JSONL, CSV, and summary JSON files.
"""

import argparse
import csv
import json
import sys
import time

from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------
# PROJECT ROOT
# ---------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


# ---------------------------------------------------------
# EVIDENCE SERIALIZATION
# ---------------------------------------------------------

def evidence_record(item):
    """
    Convert retrieved evidence into a JSON-serializable record.
    """

    chunk = item.get("chunk")

    if chunk is None:
        return {
            "source_type": item.get("source_type"),
            "source_id": item.get("source_id"),
            "score": item.get("score"),
            "text": item.get("text", "")
        }

    return {
        "source_type": item.get("source_type", "chunk"),
        "source_id": item.get(
            "source_id",
            getattr(chunk, "chunk_id", None)
        ),
        "score": (
            float(item["score"])
            if item.get("score") is not None
            else None
        ),
        "priority": item.get("priority"),
        "document_id": getattr(chunk, "document_id", None),
        "section": getattr(chunk, "section", None),
        "start_line": getattr(chunk, "start_line", None),
        "end_line": getattr(chunk, "end_line", None),
        "text": getattr(chunk, "text", "")
    }


# ---------------------------------------------------------
# TOKEN USAGE NORMALIZATION
# ---------------------------------------------------------

def normalize_token_usage(token_usage):
    """
    Normalize token usage returned by GroqGenerator.

    Returns None if usage is unavailable.
    """

    if not isinstance(token_usage, dict):
        return None

    prompt_tokens = token_usage.get("prompt_tokens")
    completion_tokens = token_usage.get("completion_tokens")
    total_tokens = token_usage.get("total_tokens")
    reasoning_tokens = token_usage.get("reasoning_tokens")

    # Do not silently treat missing usage as zero.
    if (
        prompt_tokens is None
        or completion_tokens is None
        or total_tokens is None
    ):
        return None

    return {
        "prompt_tokens": int(prompt_tokens),
        "completion_tokens": int(completion_tokens),
        "total_tokens": int(total_tokens),
        "reasoning_tokens": (
            int(reasoning_tokens)
            if reasoning_tokens is not None
            else None
        )
    }


# ---------------------------------------------------------
# CHECKPOINT HANDLING
# ---------------------------------------------------------

def successful_ids(path):
    """
    Return question IDs that have successful records.

    Failed questions are deliberately not included so that
    they can be retried.
    """

    done = set()

    if path.exists():

        with path.open("r", encoding="utf-8") as f:

            for line in f:

                try:
                    row = json.loads(line)

                    if row.get("status") == "success":
                        done.add(row["question_id"])

                except (json.JSONDecodeError, KeyError):
                    continue

    return done


# ---------------------------------------------------------
# CSV EXPORT
# ---------------------------------------------------------

def export_csv(jsonl_path, csv_path):
    """
    Export benchmark JSONL records to CSV.

    Includes per-question token usage.
    """

    fields = [
        "question_id",
        "category",
        "question",
        "reference_answer",
        "answer",
        "status",
        "latency_seconds",

        "prompt_tokens",
        "completion_tokens",
        "total_tokens",
        "reasoning_tokens",

        "retrieved_document_ids",
        "retrieved_evidence_count",
        "error"
    ]

    with jsonl_path.open("r", encoding="utf-8") as src, \
            csv_path.open(
                "w",
                newline="",
                encoding="utf-8-sig"
            ) as dst:

        writer = csv.DictWriter(
            dst,
            fieldnames=fields
        )

        writer.writeheader()

        for line in src:

            try:
                row = json.loads(line)

            except json.JSONDecodeError:
                continue

            evidence = row.get("evidence", [])

            doc_ids = sorted({
                e.get("document_id")
                for e in evidence
                if e.get("document_id")
            })

            usage = row.get("token_usage") or {}

            writer.writerow({

                "question_id": row.get("question_id"),
                "category": row.get("category"),
                "question": row.get("question"),
                "reference_answer": row.get("reference_answer"),
                "answer": row.get("answer"),
                "status": row.get("status"),
                "latency_seconds": row.get("latency_seconds"),

                "prompt_tokens": usage.get("prompt_tokens"),
                "completion_tokens": usage.get("completion_tokens"),
                "total_tokens": usage.get("total_tokens"),
                "reasoning_tokens": usage.get("reasoning_tokens"),

                "retrieved_document_ids": json.dumps(doc_ids),
                "retrieved_evidence_count": len(evidence),
                "error": row.get("error")
            })


# ---------------------------------------------------------
# TOKEN SUMMARY
# ---------------------------------------------------------

def calculate_token_summary(rows):
    """
    Calculate aggregate token statistics.

    Only successful records with actual usage metadata
    are included.

    A successful OKF response that did not call the LLM
    is not counted as a zero-token LLM generation.
    """

    successful_rows = [
        row for row in rows
        if row.get("status") == "success"
    ]

    usage_rows = [
        row["token_usage"]
        for row in successful_rows
        if isinstance(row.get("token_usage"), dict)
        and row["token_usage"].get("prompt_tokens") is not None
        and row["token_usage"].get("completion_tokens") is not None
        and row["token_usage"].get("total_tokens") is not None
    ]

    total_prompt_tokens = sum(
        usage["prompt_tokens"]
        for usage in usage_rows
    )

    total_completion_tokens = sum(
        usage["completion_tokens"]
        for usage in usage_rows
    )

    total_tokens = sum(
        usage["total_tokens"]
        for usage in usage_rows
    )

    reasoning_values = [
        usage["reasoning_tokens"]
        for usage in usage_rows
        if usage.get("reasoning_tokens") is not None
    ]

    total_reasoning_tokens = (
        sum(reasoning_values)
        if reasoning_values
        else None
    )

    generation_count = len(usage_rows)

    return {
        "llm_generation_count": generation_count,

        "successful_questions_without_usage": (
            len(successful_rows) - generation_count
        ),

        "total_prompt_tokens": total_prompt_tokens,

        "total_completion_tokens": total_completion_tokens,

        "total_tokens": total_tokens,

        "total_reasoning_tokens": total_reasoning_tokens,

        "average_prompt_tokens": (
            round(total_prompt_tokens / generation_count, 2)
            if generation_count else None
        ),

        "average_completion_tokens": (
            round(total_completion_tokens / generation_count, 2)
            if generation_count else None
        ),

        "average_total_tokens": (
            round(total_tokens / generation_count, 2)
            if generation_count else None
        ),

        "average_reasoning_tokens": (
            round(
                total_reasoning_tokens / len(reasoning_values),
                2
            )
            if reasoning_values else None
        ),

        "questions_with_reasoning_usage": len(reasoning_values)
    }


# ---------------------------------------------------------
# RUN ONE SYSTEM
# ---------------------------------------------------------

def run_system(system, questions, output_dir, dataset_path):

    # Initialize the selected pipeline.
    if system == "rag":

        from src.rag.answer_pipeline import RAGPipeline

        pipeline = RAGPipeline()

    else:

        from src.okf.answer_pipeline import OKFPipeline

        pipeline = OKFPipeline()

    output_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    jsonl_path = output_dir / f"{system}_results.jsonl"

    csv_path = output_dir / f"{system}_results.csv"

    summary_path = output_dir / f"{system}_summary.json"

    done = successful_ids(jsonl_path)

    print(
        f"\n[{system.upper()}] "
        f"Already completed successfully: {len(done)}"
    )

    # Append mode preserves previous checkpoints.
    with jsonl_path.open("a", encoding="utf-8") as out:

        for index, q in enumerate(questions, start=1):

            qid = q["question_id"]

            if qid in done:
                continue

            start = time.perf_counter()

            record = {

                "question_id": qid,
                "category": q["category"],
                "question": q["question"],
                "reference_answer": q["reference_answer"],

                "required_document_count": (
                    q["required_document_count"]
                ),

                "supporting_document_ids": (
                    q["supporting_document_ids"]
                ),

                "system": system,

                "started_at_utc": (
                    datetime.now(timezone.utc).isoformat()
                )
            }

            try:

                # Execute the selected pipeline.
                result = pipeline.answer(q["question"])

                elapsed = time.perf_counter() - start

                # Normalize actual Groq API usage.
                token_usage = normalize_token_usage(
                    result.get("token_usage")
                )

                record.update({

                    "answer": result.get("answer", ""),

                    "evidence": [
                        evidence_record(item)
                        for item in result.get("evidence", [])
                    ],

                    "entities": result.get("entities", []),

                    "token_usage": token_usage,

                    "latency_seconds": round(elapsed, 4),

                    "status": "success",

                    "error": None
                })

                print(
                    f"[{system.upper()}] {qid} "
                    f"({index}/{len(questions)}) "
                    f"completed in {elapsed:.2f}s"
                )

                if token_usage is not None:

                    print(
                        f"    Tokens: "
                        f"prompt={token_usage['prompt_tokens']}, "
                        f"completion={token_usage['completion_tokens']}, "
                        f"total={token_usage['total_tokens']}"
                    )

                else:

                    print(
                        "    Token usage unavailable "
                        "or no LLM generation occurred."
                    )

            except Exception as exc:

                elapsed = time.perf_counter() - start

                record.update({

                    "answer": None,

                    "evidence": [],

                    "entities": [],

                    "token_usage": None,

                    "latency_seconds": round(elapsed, 4),

                    "status": "error",

                    "error": f"{type(exc).__name__}: {exc}"
                })

                print(
                    f"[{system.upper()}] "
                    f"{qid} ERROR: {record['error']}"
                )

            # Write each record immediately.
            # This preserves progress if execution stops.
            out.write(
                json.dumps(
                    record,
                    ensure_ascii=False
                ) + "\n"
            )

            out.flush()

    # -----------------------------------------------------
    # EXPORT CSV
    # -----------------------------------------------------

    export_csv(
        jsonl_path,
        csv_path
    )

    # -----------------------------------------------------
    # READ ALL RESULTS
    # -----------------------------------------------------

    rows = []

    with jsonl_path.open("r", encoding="utf-8") as f:

        for line in f:

            try:
                rows.append(json.loads(line))

            except json.JSONDecodeError:
                continue

    successful_count = sum(
        row.get("status") == "success"
        for row in rows
    )

    failed_count = sum(
        row.get("status") == "error"
        for row in rows
    )

    token_summary = calculate_token_summary(rows)

    # -----------------------------------------------------
    # SUMMARY JSON
    # -----------------------------------------------------

    summary = {

        "system": system,

        "dataset_file": str(
            dataset_path.relative_to(ROOT)
        ),

        "expected_questions": len(questions),

        "successful_records": successful_count,

        "failed_records": failed_count,

        "token_usage": token_summary,

        "results_jsonl": str(
            jsonl_path.relative_to(ROOT)
        ),

        "results_csv": str(
            csv_path.relative_to(ROOT)
        ),

        "generated_at_utc": (
            datetime.now(timezone.utc).isoformat()
        )
    }

    summary_path.write_text(
        json.dumps(
            summary,
            indent=2
        ),
        encoding="utf-8"
    )

    # -----------------------------------------------------
    # CONSOLE SUMMARY
    # -----------------------------------------------------

    print(f"\n[{system.upper()}] BENCHMARK SUMMARY")

    print(f"Successful questions: {successful_count}")

    print(f"Failed records: {failed_count}")

    print(
        f"LLM generations with usage: "
        f"{token_summary['llm_generation_count']}"
    )

    print(
        f"Total prompt tokens: "
        f"{token_summary['total_prompt_tokens']}"
    )

    print(
        f"Total completion tokens: "
        f"{token_summary['total_completion_tokens']}"
    )

    print(
        f"Total tokens: "
        f"{token_summary['total_tokens']}"
    )

    print(
        f"Average tokens per generation: "
        f"{token_summary['average_total_tokens']}"
    )

    print(
        f"\nSaved: {jsonl_path.relative_to(ROOT)}"
    )

    print(
        f"Saved: {csv_path.relative_to(ROOT)}"
    )

    print(
        f"Saved: {summary_path.relative_to(ROOT)}"
    )


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------

def main():

    parser = argparse.ArgumentParser(
        description="RAG vs OKF benchmark with token tracking"
    )

    parser.add_argument(
        "--system",
        choices=["rag", "okf", "both"],
        default="both"
    )

    parser.add_argument(
        "--dataset",
        default="data/evaluation/evaluation_dataset_FINAL.json"
    )

    parser.add_argument(
        "--output-dir",
        default="outputs/benchmark"
    )

    args = parser.parse_args()

    dataset_path = (
        ROOT / args.dataset
    ).resolve()

    output_dir = (
        ROOT / args.output_dir
    ).resolve()

    if not dataset_path.exists():

        raise FileNotFoundError(
            f"Dataset not found: {dataset_path}. "
            "Copy the final JSON into data/evaluation/ first."
        )

    data = json.loads(
        dataset_path.read_text(encoding="utf-8")
    )

    questions = (
        data.get("questions")
        if isinstance(data, dict)
        else data
    )

    if not isinstance(questions, list) or len(questions) != 100:

        raise ValueError(
            "Expected exactly 100 questions in the dataset."
        )

    required = {
        "question_id",
        "category",
        "question",
        "reference_answer",
        "required_document_count",
        "supporting_document_ids"
    }

    for i, q in enumerate(questions, 1):

        missing = required - set(q)

        if missing:

            raise ValueError(
                f"Question {i} missing fields: {sorted(missing)}"
            )

    if len({
        q["question_id"]
        for q in questions
    }) != 100:

        raise ValueError(
            "Question IDs are not unique."
        )

    print(
        "Dataset check passed: "
        "100 questions and 100 unique IDs."
    )

    print(
        f"Output directory: {output_dir}"
    )

    systems = (
        ["rag", "okf"]
        if args.system == "both"
        else [args.system]
    )

    for system in systems:

        run_system(
            system,
            questions,
            output_dir,
            dataset_path
        )


if __name__ == "__main__":

    main()
