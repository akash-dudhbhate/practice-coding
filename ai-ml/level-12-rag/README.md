# Level 12 — RAG Systems

## What You'll Learn
- Text similarity via TF-IDF + cosine
- Document retrieval — find relevant docs for a query
- Text chunking — split docs into context-window-sized pieces
- In-memory vector store
- Reranking — boost initial retrieval results
- Hybrid search — keyword + semantic combined
- Simple RAG pipeline (retrieve → generate)
- RAG evaluation and query rewriting

## Prerequisites
- Level 11 (prompt concepts)

## Problems

### Easy
1. `easy/p01-similarity.py` — `similarity()` → TF-IDF + cosine
2. `easy/p02-simple-retrieval.py` — `retrieve()` → top-k docs
3. `easy/p03-chunking.py` — `chunk_text()` → overlapping chunks

### Medium
4. `medium/p01-vector-store.py` — `vector_store()` → embed + search
5. `medium/p02-reranking.py` — `rerank()` → keyword-boost re-score
6. `medium/p03-hybrid-search.py` — `hybrid_search()` → keyword + semantic

### Hard
7. `hard/p01-rag-pipeline.py` — `rag()` → retrieve → template answer
8. `hard/p02-rag-eval.py` — `evaluate_rag()` → retrieval accuracy
9. `hard/p03-query-rewriting.py` — `rewrite_query()` → expand abbreviations

### Project
`project/` — Build a mini RAG system on your own docs.

## Verify

```bash
python3 check.py easy/p01
python3 check.py all
```
