# Level 12 — Concepts Reference

## Easy

### TF-IDF + Cosine Similarity
- `TfidfVectorizer` → text → sparse vectors weighted by word rarity
- `cosine_similarity` → 0 (unrelated) to 1 (identical)

### Retrieval
- Embed docs + query → rank by cosine → return top-k
- This is the "R" in RAG — find relevant context first

### Chunking
- Split long docs into overlapping chunks (LLM context limit)
- `step = chunk_size - overlap` — keeps context between chunks

## Medium

### Vector Store
- Store doc → vector pairs; query → rank by similarity
- No external DB needed — numpy + sklearn suffices

### Reranking
- First-pass retrieval is fast but imprecise
- Boost: `score + 0.1 × (query words in doc)` → re-sort

### Hybrid Search
- Keyword score (exact word match) + semantic score (TF-IDF cosine)
- `0.5 × keyword + 0.5 × semantic` — best of both worlds

## Hard

### RAG Pipeline
- retrieve → generate: find doc → template answer referencing it
- The "G" can be an LLM or a simple template

### RAG Evaluation
- % of questions where correct doc is retrieved in top-k
- Like accuracy — measures retrieval quality

### Query Rewriting
- Expand abbreviations before searching (ML → machine learning)
- Better query → better retrieval
