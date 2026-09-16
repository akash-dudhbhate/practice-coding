# Level 16 — Concepts Reference

## The "Real RAG" mental model

```
  docs  ──embed──► vectors ──► VectorStore.add()
  query ──embed──► vector  ──► VectorStore.query(k) ──► top-k chunks
                                                      │
                                           prompt = context + question
                                                      │
                                                  answer string
```

Same shape as `sentence-transformers` + FAISS/Chroma — we just swap
the embedder for `TfidfVectorizer` and the DB for numpy.

## Easy

### Embeddings
- `TfidfVectorizer().fit_transform(texts)` → sparse matrix; `.toarray()` → dense
- L2-normalize each row → unit vectors → **dot product == cosine similarity**

### Cosine vs all docs
- `doc_matrix @ query_vec` → one score per doc in a single matmul
- Normalize both sides first (don't assume inputs are pre-normalized)

### Chunking + metadata
- `step = size - overlap`; stop once a chunk reaches the end
- Keep `{id, text, start, end}` per chunk — offsets let answers cite sources

## Medium

### VectorStore
- `.add(texts)` → embed + store; `.query(q_vec, k)` → `[(idx, score)]`
- `fit_transform` on the FIRST add, `transform` on later adds
  (the embedding model is fixed at ingest time — same as real DBs)
- Expose `.vec` (fitted vectorizer) and `.texts` (raw strings)

### Ingest
- raw docs → overlapping chunks → `store.add(chunk_texts)` → count added
- Embedding happens inside `add` — ingest just orchestrates

### Retrieve
- `vec.transform([query])` → `store.query` → map `idx` → `store.texts[idx]`

## Hard

### RAG answer
- retrieve → stuff chunks into a prompt → generate
- No LLM here: a template answer that cites the top chunk stands in;
  the pipeline shape is what matters

### Hit-rate eval
- For each test query: does ANY expected keyword appear in top-k chunks?
- `hits / n_queries` — the standard quick metric for retrieval quality

### Hybrid fusion
- dense score (cosine) + keyword score (BM25-ish):
  `Σ idf(t) · f·(k1+1) / (f + k1·(1 - b + b·dl/avgdl))`
- `idf(t) = log((N - df + 0.5) / (df + 0.5) + 1)`, `k1=1.5`, `b=0.75`
- Max-normalize each score vector → `fused = α·dense + (1-α)·keyword` → re-rank
- Keyword rescues exact-term matches that dense vectors miss
