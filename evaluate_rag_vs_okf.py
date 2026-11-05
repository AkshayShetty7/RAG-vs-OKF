#!/usr/bin/env python3
"""
Paired RAG vs OKF evaluation helper.

Inputs:
  evaluation_dataset_FINAL.json
  rag_results.jsonl
  okf_results.jsonl

Outputs:
  evaluation_inputs.csv          one row per system/question; human answer review
  evidence_review.csv            one row per retrieved evidence item; human relevance review
  required_fact_review.csv       one row per system/required fact; human retrieval coverage review
  preliminary_metrics.csv        automatically measurable metrics
  evaluation_summary.md          preliminary summary and annotation instructions

Run from project root:
  python evaluate_rag_vs_okf.py ^
    --dataset evaluation_dataset_FINAL.json ^
    --rag outputs/benchmark_token_tracking/rag_results.jsonl ^
    --okf outputs/benchmark_token_tracking/okf_results.jsonl ^
    --output-dir outputs/evaluation

After filling the three review CSV files, run again with:
  python evaluate_rag_vs_okf.py ... --include-human-scores
The script will then also produce human_scored_metrics.csv.
"""

import argparse
import csv
import json
import math
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path


SYSTEMS = ("rag", "okf")
EXPECTED_QUESTION_IDS = {f"Q{i:03d}" for i in range(1, 101)}


def read_jsonl(path):
    rows = []
    with Path(path).open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            if line.strip():
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise ValueError(f"Invalid JSON in {path}, line {line_no}: {exc}")
    return rows


def read_json(path):
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)


def write_csv(path, rows, fieldnames=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def p95(values):
    """Nearest-rank 95th percentile."""
    if not values:
        return None
    ordered = sorted(values)
    return ordered[max(0, math.ceil(0.95 * len(ordered)) - 1)]


def safe_mean(values):
    return statistics.mean(values) if values else None


def fmt(value, digits=3):
    return "N/A" if value is None else round(value, digits)


def unique_doc_ids(evidence):
    return sorted({
        str(item.get("document_id")).strip()
        for item in (evidence or [])
        if item.get("document_id")
    })


def extract_usage(obj, found=None):
    """Look recursively for provider usage fields; never estimate tokens."""
    if found is None:
        found = {}
    if isinstance(obj, dict):
        for key, value in obj.items():
            key_l = key.lower()
            if key_l in {
                "prompt_tokens", "input_tokens", "completion_tokens",
                "output_tokens", "total_tokens", "total_cost", "cost_usd"
            } and isinstance(value, (int, float)):
                found[key_l] = value
            extract_usage(value, found)
    elif isinstance(obj, list):
        for value in obj:
            extract_usage(value, found)
    return found


def normalize_bool(value):
    if isinstance(value, bool):
        return value
    value = str(value or "").strip().lower()
    if value in {"yes", "y", "true", "1"}:
        return True
    if value in {"no", "n", "false", "0"}:
        return False
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--rag", required=True)
    parser.add_argument("--okf", required=True)
    parser.add_argument("--output-dir", default="outputs/evaluation")
    parser.add_argument("--include-human-scores", action="store_true")
    args = parser.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    dataset = read_json(args.dataset)
    questions = dataset.get("questions", [])
    if not questions:
        raise ValueError("Dataset JSON must contain a non-empty 'questions' array.")

    q_by_id = {q["question_id"]: q for q in questions}
    if len(q_by_id) != len(questions):
        raise ValueError("Duplicate question_id values found in evaluation dataset.")

    result_paths = {"rag": args.rag, "okf": args.okf}
    all_rows = {}
    latest_success = {}
    attempts = {}
    failures = {}

    for system in SYSTEMS:
        rows = read_jsonl(result_paths[system])
        all_rows[system] = rows
        attempts[system] = Counter(r.get("question_id") for r in rows)
        failures[system] = Counter(
            r.get("question_id") for r in rows
            if str(r.get("status", "")).lower() != "success"
        )
        successful = [r for r in rows if str(r.get("status", "")).lower() == "success"]
        # JSONL append order is used as the available attempt order.
        # If timestamps are present, choose the latest timestamp instead.
        successful.sort(key=lambda r: str(r.get("started_at_utc", "")))
        latest_success[system] = {}
        for row in successful:
            latest_success[system][row.get("question_id")] = row

    evaluation_rows = []
    evidence_rows = []
    fact_rows = []
    preliminary_rows = []
    usage_present = False

    for system in SYSTEMS:
        rows = all_rows[system]
        success_map = latest_success[system]
        successful_ids = set(success_map)
        missing_ids = set(q_by_id) - successful_ids
        extra_ids = set(successful_ids) - set(q_by_id)

        for qid, q in q_by_id.items():
            result = success_map.get(qid, {})
            answer = result.get("answer", "")
            evidence = result.get("evidence", []) or []
            expected_docs = set(q.get("supporting_document_ids", []))
            retrieved_docs = set(unique_doc_ids(evidence))
            overlap = expected_docs & retrieved_docs

            doc_precision = len(overlap) / len(retrieved_docs) if retrieved_docs else 0.0
            doc_recall = len(overlap) / len(expected_docs) if expected_docs else None
            doc_f1 = (
                2 * doc_precision * doc_recall / (doc_precision + doc_recall)
                if doc_recall is not None and (doc_precision + doc_recall) > 0
                else 0.0 if doc_recall is not None else None
            )

            latency = result.get("latency_seconds")
            usage = extract_usage(result)
            if usage:
                usage_present = True

            evaluation_rows.append({
                "system": system,
                "question_id": qid,
                "category": q.get("category", ""),
                "answerability": q.get("answerability", ""),
                "question": q.get("question", ""),
                "reference_answer": q.get("reference_answer", ""),
                "answer": answer,
                "expected_document_ids": ";".join(sorted(expected_docs)),
                "retrieved_document_ids": ";".join(sorted(retrieved_docs)),
                "document_precision_auto": doc_precision,
                "document_recall_auto": doc_recall,
                "document_f1_auto": doc_f1,
                "latency_seconds": latency,
                "attempt_count": attempts[system].get(qid, 0),
                "failed_attempt_count": failures[system].get(qid, 0),
                "answer_correctness_0_to_4": "",
                "answer_completeness_0_to_4": "",
                "hallucinated_factual_claims_count": "",
                "total_factual_claims_count": "",
                "citation_accuracy_0_to_4": "",
                "faithfulness_0_to_4": "",
                "answer_abstained_yes_no": "",
                "abstention_appropriate_yes_no": "",
                "reviewer_notes": "",
            })

            for idx, item in enumerate(evidence, 1):
                evidence_rows.append({
                    "system": system,
                    "question_id": qid,
                    "evidence_rank": idx,
                    "source_id": item.get("source_id", ""),
                    "document_id": item.get("document_id", ""),
                    "section": item.get("section", ""),
                    "retrieval_score": item.get("score", ""),
                    "evidence_text": item.get("text", ""),
                    "relevant_to_question_yes_no": "",
                    "supports_at_least_one_required_fact_yes_no": "",
                    "cited_in_answer_yes_no": "",
                    "reviewer_notes": "",
                })

            for fact in q.get("required_facts", []):
                fact_rows.append({
                    "system": system,
                    "question_id": qid,
                    "category": q.get("category", ""),
                    "required_fact": fact,
                    "retrieved_evidence_covers_fact_yes_no": "",
                    "answer_includes_fact_yes_no": "",
                    "reviewer_notes": "",
                })

        latencies = [
            float(r["latency_seconds"])
            for r in success_map.values()
            if r.get("latency_seconds") is not None
        ]
        unique_success_count = len(successful_ids)
        total_attempts = len(rows)
        failed_attempts = sum(failures[system].values())
        usage_rows = [extract_usage(r) for r in success_map.values()]
        usage_rows = [u for u in usage_rows if u]
        input_tokens = [
            u.get("prompt_tokens", u.get("input_tokens"))
            for u in usage_rows
            if u.get("prompt_tokens", u.get("input_tokens")) is not None
        ]
        output_tokens = [
            u.get("completion_tokens", u.get("output_tokens"))
            for u in usage_rows
            if u.get("completion_tokens", u.get("output_tokens")) is not None
        ]
        total_tokens = [u.get("total_tokens") for u in usage_rows if u.get("total_tokens") is not None]

        preliminary_rows.append({
            "system": system,
            "question_count_in_dataset": len(q_by_id),
            "successful_unique_questions": unique_success_count,
            "missing_question_ids": ";".join(sorted(missing_ids)),
            "unexpected_question_ids": ";".join(sorted(extra_ids)),
            "jsonl_records_attempts": total_attempts,
            "failed_attempts": failed_attempts,
            "retry_attempts_after_first": sum(max(0, n - 1) for n in attempts[system].values()),
            "eventual_completion_rate": unique_success_count / len(q_by_id),
            "attempt_failure_rate": failed_attempts / total_attempts if total_attempts else None,
            "mean_latency_seconds": safe_mean(latencies),
            "median_latency_seconds": statistics.median(latencies) if latencies else None,
            "p95_latency_seconds": p95(latencies),
            "min_latency_seconds": min(latencies) if latencies else None,
            "max_latency_seconds": max(latencies) if latencies else None,
            "mean_input_tokens": safe_mean(input_tokens),
            "mean_output_tokens": safe_mean(output_tokens),
            "mean_total_tokens": safe_mean(total_tokens),
            "token_usage_available": bool(usage_rows),
        })

    write_csv(out / "evaluation_inputs.csv", evaluation_rows)
    write_csv(out / "evidence_review.csv", evidence_rows)
    write_csv(out / "required_fact_review.csv", fact_rows)
    write_csv(out / "preliminary_metrics.csv", preliminary_rows)

    lines = [
        "# RAG vs OKF Evaluation",
        "",
        f"- Dataset: `{Path(args.dataset).name}` ({len(q_by_id)} questions)",
        f"- Source corpus documents: {dataset.get('source_corpus', {}).get('source_document_count', 'not specified')}",
        "",
        "## Preliminary execution metrics",
        "",
        "| Metric | RAG | OKF |",
        "|---|---:|---:|",
    ]
    metrics = [
        ("Successful unique questions", "successful_unique_questions"),
        ("Failed attempts", "failed_attempts"),
        ("Retry attempts after first", "retry_attempts_after_first"),
        ("Mean latency (s)", "mean_latency_seconds"),
        ("Median latency (s)", "median_latency_seconds"),
        ("P95 latency (s)", "p95_latency_seconds"),
        ("Mean input tokens", "mean_input_tokens"),
        ("Mean output tokens", "mean_output_tokens"),
        ("Mean total tokens", "mean_total_tokens"),
    ]
    by_system = {r["system"]: r for r in preliminary_rows}
    for label, key in metrics:
        lines.append(f"| {label} | {fmt(by_system['rag'].get(key))} | {fmt(by_system['okf'].get(key))} |")
    lines += [
        "",
        "## Interpretation notes",
        "",
        "- Document precision/recall in `evaluation_inputs.csv` are automatic **document-level** measures based on expected document IDs and document IDs present in each successful result's evidence array.",
        "- These measures do not prove that a retrieved passage supports the answer. Use `evidence_review.csv` for human relevance/support judgments and `required_fact_review.csv` for required-fact coverage.",
        "- Answer correctness, completeness, citation accuracy, faithfulness, hallucination counts, and abstention judgments require human review. Do not treat lexical overlap as semantic correctness.",
        "- Latency is computed from successful per-question result records only. P95 uses the nearest-rank method.",
        "- Attempt failure rate is failed JSONL records divided by all attempt records. Eventual completion rate counts unique questions with a successful result.",
        "- Token usage and API cost are reported only if actual provider usage fields exist in the result records. This script never estimates actual token counts or cost from text length.",
        "",
        "## Human annotation instructions",
        "",
        "Fill the blank columns in the three review CSV files. Score each system's answer independently and, where possible, have a second reviewer score a sample to measure agreement.",
        "",
        "- Correctness (0-4): 0 wrong; 1 mostly wrong; 2 partially correct; 3 substantially correct with minor errors; 4 fully correct.",
        "- Completeness (0-4): 0 omits nearly all required facts; 1 major omissions; 2 about half; 3 minor omissions; 4 includes all required facts and qualifiers.",
        "- Citation accuracy (0-4): 0 citations absent/incorrect; 1 mostly wrong; 2 mixed; 3 mostly correct; 4 all cited sources/sections accurately identify support.",
        "- Faithfulness (0-4): 0 unsupported or contradictory; 1 mostly unsupported; 2 mixed support; 3 largely supported; 4 every material factual claim is supported by the cited/retrieved evidence.",
        "- Binary columns: enter `yes` or `no`. Use abstention fields only after checking the question's `answerability` value.",
        "- For `evidence_review.csv`, mark relevance and required-fact support per retrieved evidence item. For `required_fact_review.csv`, mark whether the retrieved evidence covers each gold required fact.",
        "",
        "## Score calculations after annotation",
        "",
        "- Answer Quality Score = mean((correctness + completeness) / 8 * 100).",
        "- Evidence Grounding Score = mean((citation accuracy + faithfulness) / 8 * 100).",
        "- Evidence precision = relevant retrieved evidence items / all retrieved evidence items, based on human labels.",
        "- Required-fact evidence recall = required facts covered by retrieved evidence / all required facts.",
        "- Document precision/recall are reported separately from passage/fact-level evidence precision/recall.",
        "- Reliability is reported as completion rate, attempt failure rate, retry rate, and appropriate-abstention rate; do not collapse these without predeclared weights.",
        "- Complexity results are grouped by the dataset's category labels; report sample sizes with every category.",
        "",
        "## Missing coverage",
        "",
    ]
    for system in SYSTEMS:
        success_ids = set(latest_success[system])
        missing = sorted(set(q_by_id) - success_ids)
        lines.append(f"- {system.upper()}: {len(missing)} questions without successful results: {', '.join(missing) if missing else 'none'}")
    if not usage_present:
        lines += [
            "",
            "**Token/cost limitation:** no actual token-usage fields were found in the current result records. The current shared Groq generator returns only answer text, so provider usage metadata is not preserved. Add response `usage` fields to the generator return value and persist them in the benchmark result JSONL before reporting token/cost metrics.",
        ]

    (out / "evaluation_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    if args.include_human_scores:
        answer_rows = list(csv.DictReader((out / "evaluation_inputs.csv").open("r", encoding="utf-8-sig", newline="")))
        ev_rows = list(csv.DictReader((out / "evidence_review.csv").open("r", encoding="utf-8-sig", newline="")))
        fact_review_rows = list(csv.DictReader((out / "required_fact_review.csv").open("r", encoding="utf-8-sig", newline="")))
        human = []
        for system in SYSTEMS:
            ar = [r for r in answer_rows if r["system"] == system]
            def numeric_avg(field, denom=None):
                vals = []
                for r in ar:
                    try:
                        vals.append(float(r[field]))
                    except (ValueError, TypeError, KeyError):
                        pass
                return safe_mean(vals)
            correctness = numeric_avg("answer_correctness_0_to_4")
            completeness = numeric_avg("answer_completeness_0_to_4")
            citation = numeric_avg("citation_accuracy_0_to_4")
            faithfulness = numeric_avg("faithfulness_0_to_4")
            answer_scores = [
                (float(r["answer_correctness_0_to_4"]) + float(r["answer_completeness_0_to_4"])) / 8 * 100
                for r in ar
                if r.get("answer_correctness_0_to_4", "").strip()
                and r.get("answer_completeness_0_to_4", "").strip()
            ]
            grounding_scores = [
                (float(r["citation_accuracy_0_to_4"]) + float(r["faithfulness_0_to_4"])) / 8 * 100
                for r in ar
                if r.get("citation_accuracy_0_to_4", "").strip()
                and r.get("faithfulness_0_to_4", "").strip()
            ]
            ev_yes = sum(normalize_bool(r.get("relevant_to_question_yes_no")) is True for r in ev_rows if r["system"] == system)
            ev_total = sum(bool(r.get("relevant_to_question_yes_no", "").strip()) for r in ev_rows if r["system"] == system)
            fact_yes = sum(normalize_bool(r.get("retrieved_evidence_covers_fact_yes_no")) is True for r in fact_review_rows if r["system"] == system)
            fact_total = sum(bool(r.get("retrieved_evidence_covers_fact_yes_no", "").strip()) for r in fact_review_rows if r["system"] == system)
            abstention_labels = [
                normalize_bool(r.get("abstention_appropriate_yes_no"))
                for r in ar
                if str(r.get("abstention_appropriate_yes_no", "")).strip()
            ]
            abstention_labels = [x for x in abstention_labels if x is not None]
            hallucinated = []
            factual_claims = []
            for r in ar:
                try:
                    hallucinated.append(float(r["hallucinated_factual_claims_count"]))
                    factual_claims.append(float(r["total_factual_claims_count"]))
                except (ValueError, TypeError, KeyError):
                    pass
            hallucination_rate = (
                sum(hallucinated) / sum(factual_claims)
                if factual_claims and sum(factual_claims) > 0 else None
            )
            human.append({
                "system": system,
                "mean_correctness_0_to_4": correctness,
                "mean_completeness_0_to_4": completeness,
                "answer_quality_score_0_to_100": safe_mean(answer_scores),
                "mean_citation_accuracy_0_to_4": citation,
                "mean_faithfulness_0_to_4": faithfulness,
                "evidence_grounding_score_0_to_100": safe_mean(grounding_scores),
                "human_evidence_precision": ev_yes / ev_total if ev_total else None,
                "required_fact_evidence_recall": fact_yes / fact_total if fact_total else None,
                "hallucinated_claim_rate": hallucination_rate,
                "appropriate_abstention_rate_on_reviewed_questions": safe_mean([1.0 if x else 0.0 for x in abstention_labels]),
                "abstention_reviewed_questions": len(abstention_labels),
                "answer_quality_scored_questions": len(answer_scores),
                "grounding_scored_questions": len(grounding_scores),
            })
        write_csv(out / "human_scored_metrics.csv", human)

        complexity_rows = []
        for system in SYSTEMS:
            for category in sorted({r.get("category", "") for r in answer_rows}):
                group = [r for r in answer_rows if r["system"] == system and r.get("category", "") == category]
                scored = [
                    (float(r["answer_correctness_0_to_4"]) + float(r["answer_completeness_0_to_4"])) / 8 * 100
                    for r in group
                    if r.get("answer_correctness_0_to_4", "").strip()
                    and r.get("answer_completeness_0_to_4", "").strip()
                ]
                group_latencies = []
                for r in group:
                    try:
                        group_latencies.append(float(r["latency_seconds"]))
                    except (ValueError, TypeError, KeyError):
                        pass
                complexity_rows.append({
                    "system": system,
                    "category": category,
                    "question_count": len(group),
                    "answer_quality_score_0_to_100": safe_mean(scored),
                    "mean_latency_seconds": safe_mean(group_latencies),
                    "scored_answer_count": len(scored),
                })
        write_csv(out / "complexity_breakdown.csv", complexity_rows)

    print(f"Evaluation files written to: {out.resolve()}")
    print("Review evaluation_summary.md before interpreting the results.")
    print("Fill evaluation_inputs.csv, evidence_review.csv, and required_fact_review.csv for human scoring.")
    if args.include_human_scores:
        print("Human-scored metrics written to human_scored_metrics.csv.")


if __name__ == "__main__":
    main()
