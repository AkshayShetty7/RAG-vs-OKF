# RAG vs OKF – Comparative Knowledge Retrieval System

## 1. What This Project Does

This project implements and compares two knowledge retrieval approaches:

- **RAG (Retrieval-Augmented Generation):** Retrieves relevant document chunks using semantic vector search and keyword-based search before generating an answer using an LLM.
- **OKF (Structured Knowledge Retrieval):** Organizes information into entities, facts, and relationships, enabling structured and relationship-based knowledge retrieval.

Both approaches use the same clinical and hospital-domain dataset and the same LLM generation layer to evaluate their retrieval performance.

The project evaluates both systems using 100 benchmark questions across 39 source documents.

### Key Features

- Document-based question answering.
- Hybrid retrieval using FAISS and BM25.
- Embedding-based semantic search.
- Entity and fact-based knowledge retrieval.
- Relationship-based graph traversal.
- Evidence-based answer generation.
- Source document traceability.
- Comparative retrieval and performance evaluation.

---

## 2. Project Structure

```text
RAG-vs-OKF/
│
├── config/
│   └── settings.yaml
│
├── data/
│   ├── source_documents/
│   │   ├── 01_patient_records/
│   │   ├── 02_diseases_guidelines/
│   │   ├── 03_medications_pharmacy/
│   │   ├── 04_laboratory_diagnostics/
│   │   └── 05_hospital_operations/
│   │
│   ├── rag_data/
│   │   ├── chunks.json
│   │   └── faiss.index
│   │
│   ├── okf_data/
│   │   ├── entities/
│   │   ├── knowledge/
│   │   ├── relationships/
│   │   ├── provenance/
│   │   ├── indexes/
│   │   ├── concepts/
│   │   ├── knowledge_graph/
│   │   └── schemas/
│   │
│   ├── benchmark/
│   │   └── questions.json
│   │
│   └── evaluation/
│
├── src/
│   ├── common/
│   │   ├── document_loader.py
│   │   ├── document_schema.py
│   │   └── validate_dataset.py
│   │
│   ├── rag/
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   ├── vector_store.py
│   │   ├── bm25_search.py
│   │   ├── hybrid_search.py
│   │   ├── reranker.py
│   │   ├── build_index.py
│   │   └── answer_pipeline.py
│   │
│   ├── okf/
│   │   ├── retrieval.py
│   │   ├── graph_engine.py
│   │   ├── answer_pipeline.py
│   │   ├── source_registry.py
│   │   └── run_okf.py
│   │
│   ├── generation/
│   │   ├── groq_client.py
│   │   └── run_rag.py
│   │
│   └── evaluation/
│       ├── prepare_benchmark.py
│       └── run_benchmark.py
│
├── tests/
│   ├── test_chunker.py
│   ├── test_document_loader.py
│   ├── test_hybrid_search.py
│   ├── test_reranker.py
│   └── test_vector_search.py
│
├── outputs/
│   ├── benchmark/
│   ├── benchmark_token_tracking/
│   └── evaluation/
│
├── evaluate_rag_vs_okf.py
├── requirements.txt
└── README.md
```

---

## 3. System Architecture

### 3.1 RAG Architecture

RAG retrieves relevant text passages from the document collection and supplies them to an LLM for answer generation.

```text
          SOURCE DOCUMENTS
                  |
                  v
           DOCUMENT LOADER
                  |
                  v
             CHUNKING
          (700 words approx.)
                  |
                  v
          EMBEDDING GENERATION
          (BGE-base-en-v1.5)
                  |
                  v
            FAISS INDEX
                  |
                  |
             USER QUERY
                  |
          +-------+-------+
          |               |
          v               v
      VECTOR SEARCH    BM25 SEARCH
       (Top 20)          (Top 20)
          |               |
          +-------+-------+
                  |
                  v
            HYBRID SEARCH
                  |
                  v
                  RRF
                  |
                  v
              RERANKING
                  |
                  v
          TOP 5 DOCUMENT CHUNKS
                  |
                  v
              GROQ LLM
                  |
                  v
             FINAL ANSWER
```

**Main Components:**

- Document loading and text chunking.
- BGE embedding generation.
- FAISS vector similarity search.
- BM25 keyword retrieval.
- Reciprocal Rank Fusion (RRF).
- BGE cross-encoder reranking.
- LLM-based answer generation.

### 3.2 OKF Architecture

The OKF pipeline organizes extracted knowledge into entities, facts, and relationships. It retrieves relevant knowledge using entity identification, fact retrieval and relationship-based graph operations.

```text
          SOURCE DOCUMENTS
                  |
                  v
           DOCUMENT LOADER
                  |
                  v
          KNOWLEDGE EXTRACTION
                  |
          +-------+-------+
          |       |       |
          v       v       v
       ENTITIES  FACTS  RELATIONSHIPS
          |       |       |
          +-------+-------+
                  |
                  v
          KNOWLEDGE STORAGE
                  |
                  v
             KNOWLEDGE GRAPH
                  |
                  |
              USER QUERY
                  |
                  v
          ENTITY IDENTIFICATION
                  |
                  v
             FACT RETRIEVAL
                  |
                  v
        RELATIONSHIP RETRIEVAL
                  |
                  v
          GRAPH TRAVERSAL
                  |
                  v
          EVIDENCE RANKING
                  |
                  v
               GROQ LLM
                  |
                  v
             FINAL ANSWER
```

**Main Components:**

- Entity extraction and entity resolution.
- Atomic fact storage.
- Relationship extraction and verification.
- Knowledge graph construction.
- BM25-based fact retrieval.
- Graph traversal and relationship retrieval.
- Evidence ranking and provenance tracking.
- LLM-based answer generation.

### 3.3 Shared Generation Layer

Both systems use a common LLM generation layer powered by Groq.

**LLM Model:** `openai/gpt-oss-120b`

The retrieved evidence from either pipeline is passed to the generation layer, which produces the final answer with supporting source information.

---

## 4. Outcomes

Both systems were evaluated using the same clinical-domain dataset containing 39 source documents and a benchmark of 100 questions.

### 4.1 Retrieval Quality Comparison

| Metric | RAG | OKF |
|---|---:|---:|
| Document Recall | **76.4%** | 56.8% |
| Document F1 Score | **57.6%** | 47.2% |

### 4.2 Execution Performance

| Metric | RAG | OKF |
|---|---:|---:|
| Successful Unique Questions | 100 | 100 |
| Failed Attempts | 9 | 0 |
| Mean Latency | 15.457 s | 8.532 s |
| Median Latency | 15.494 s | 9.293 s |
| P95 Latency | 20.169 s | 12.33 s |

### 4.3 Key Observations

- **RAG** achieved higher document recall and document F1, indicating better document-level retrieval coverage in this evaluation.
- **OKF** recorded lower mean, median and P95 latency.
- RAG retrieved a larger proportion of the expected relevant documents.
- OKF demonstrated faster execution through structured fact and relationship retrieval.

### 4.4 Overall Outcome

The evaluation demonstrates different strengths in the two retrieval approaches.

RAG provides stronger document-level retrieval coverage, while OKF provides faster retrieval and execution in the reported benchmark.

The results highlight the trade-off between document-based retrieval and structured knowledge retrieval.

*Note: These are preliminary retrieval and execution metrics. Document-level recall and F1 do not independently establish answer correctness or factual accuracy. Human evidence and answer-quality evaluation is required for those conclusions.*
