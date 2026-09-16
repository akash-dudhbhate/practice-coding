# Level 16 — Real RAG (Embeddings + Vector DB)

## What You'll Learn
- Sentence embeddings — text → dense vectors (`TfidfVectorizer` stands in for a neural embedder)
- Cosine similarity of one query against a whole doc matrix in a single matmul
- Chunking with metadata (offsets → citable sources)
- A `VectorStore` class with the same API shape as FAISS / Chroma
- Ingest pipeline: chunk → embed → add
- Retrieve: embed query → top-k chunk texts
- Full RAG answer: retrieve → build prompt → answer string
- RAG evaluation — hit-rate metric
- Hybrid retrieval — dense + BM25-ish keyword fusion

## Prerequisites
- Level 12 (TF-IDF RAG basics)

## Notes
- Uses ONLY `sklearn` + `numpy` — no external vector DB needed.
  `TfidfVectorizer` plays the role of `sentence-transformers`, and
  `VectorStore` plays the role of FAISS/Chroma. The code shape is
  identical to a real embedding + vector-DB stack, so everything you
  write here ports directly.
- Deterministic — fixed corpus, no randomness.

## Problems

### Easy
1. `easy/p01-embed.py` — `embed()` → L2-normalized embedding matrix
2. `easy/p02-cosine-all.py` — `cosine_all()` → query vs all docs at once
3. `easy/p03-chunk-metadata.py` — `chunk_text()` → overlapping chunks + offsets

### Medium
4. `medium/p01-vector-store.py` — `VectorStore` class → `.add()` / `.query()`
5. `medium/p02-ingest.py` — `ingest()` → chunk + embed + add → count
6. `medium/p03-retrieve.py` — `retrieve()` → embed query → top-k texts

### Hard
7. `hard/p01-rag-answer.py` — `rag_answer()` → retrieve → prompt → answer
8. `hard/p02-eval-rag.py` — `eval_rag()` → hit-rate metric
9. `hard/p03-hybrid.py` — `hybrid()` → dense + BM25-ish fusion

### Project
`project/` — Build a mini real-RAG pipeline over a knowledge base.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
