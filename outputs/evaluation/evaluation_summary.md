# RAG vs OKF Evaluation

- Dataset: `evaluation_dataset_FINAL.json` (100 questions)
- Source corpus documents: 39

## Preliminary execution metrics

| Metric | RAG | OKF |
|---|---:|---:|
| Successful unique questions | 100 | 100 |
| Failed attempts | 9 | 0 |
| Retry attempts after first | 9 | 0 |
| Mean latency (s) | 15.457 | 8.532 |
| Median latency (s) | 15.494 | 9.293 |
| P95 latency (s) | 20.169 | 12.33 |
| Mean input tokens | N/A | N/A |
| Mean output tokens | N/A | N/A |
| Mean total tokens | N/A | N/A |

## Interpretation notes

- Document precision/recall in `evaluation_inputs.csv` are automatic **document-level** measures based on expected document IDs and document IDs present in each successful result's evidence array.
- These measures do not prove that a retrieved passage supports the answer. Use `evidence_review.csv` for human relevance/support judgments and `required_fact_review.csv` for required-fact coverage.
- Answer correctness, completeness, citation accuracy, faithfulness, hallucination counts, and abstention judgments require human review. Do not treat lexical overlap as semantic correctness.
- Latency is computed from successful per-question result records only. P95 uses the nearest-rank method.
- Attempt failure rate is failed JSONL records divided by all attempt records. Eventual completion rate counts unique questions with a successful result.
- Token usage and API cost are reported only if actual provider usage fields exist in the result records. This script never estimates actual token counts or cost from text length.

## Human annotation instructions

Fill the blank columns in the three review CSV files. Score each system's answer independently and, where possible, have a second reviewer score a sample to measure agreement.

- Correctness (0-4): 0 wrong; 1 mostly wrong; 2 partially correct; 3 substantially correct with minor errors; 4 fully correct.
- Completeness (0-4): 0 omits nearly all required facts; 1 major omissions; 2 about half; 3 minor omissions; 4 includes all required facts and qualifiers.
- Citation accuracy (0-4): 0 citations absent/incorrect; 1 mostly wrong; 2 mixed; 3 mostly correct; 4 all cited sources/sections accurately identify support.
- Faithfulness (0-4): 0 unsupported or contradictory; 1 mostly unsupported; 2 mixed support; 3 largely supported; 4 every material factual claim is supported by the cited/retrieved evidence.
- Binary columns: enter `yes` or `no`. Use abstention fields only after checking the question's `answerability` value.
- For `evidence_review.csv`, mark relevance and required-fact support per retrieved evidence item. For `required_fact_review.csv`, mark whether the retrieved evidence covers each gold required fact.

## Score calculations after annotation

- Answer Quality Score = mean((correctness + completeness) / 8 * 100).
- Evidence Grounding Score = mean((citation accuracy + faithfulness) / 8 * 100).
- Evidence precision = relevant retrieved evidence items / all retrieved evidence items, based on human labels.
- Required-fact evidence recall = required facts covered by retrieved evidence / all required facts.
- Document precision/recall are reported separately from passage/fact-level evidence precision/recall.
- Reliability is reported as completion rate, attempt failure rate, retry rate, and appropriate-abstention rate; do not collapse these without predeclared weights.
- Complexity results are grouped by the dataset's category labels; report sample sizes with every category.

## Missing coverage

- RAG: 0 questions without successful results: none
- OKF: 0 questions without successful results: none

**Token/cost limitation:** no actual token-usage fields were found in the current result records. The current shared Groq generator returns only answer text, so provider usage metadata is not preserved. Add response `usage` fields to the generator return value and persist them in the benchmark result JSONL before reporting token/cost metrics.
