"""
LEVEL 16 — Real RAG (Embeddings + Vector DB)
MEDIUM P02 — Ingest Pipeline
========================================

CONCEPT:
  Ingestion is the offline half of RAG: raw docs → chunks → vectors
  in the store. Long docs MUST be chunked first — embedding a whole
  article into one vector destroys recall (the query only matches
  the "average" of the doc).

PROBLEM:
  Write `ingest(store, raw_docs, size=100, overlap=20)` that:
    1. Chunks every doc into overlapping windows — same shape as
       easy/p03: {"id", "text", "start", "end"} per chunk
       (track the source doc index too if you like)
    2. Calls store.add(chunk_texts) — the store embeds internally
    3. Returns the total number of chunks added (int)

TRY THIS INPUT:
  ```python
  store = VectorStore()                 # from medium/p01
  n = ingest(store, RAW_DOCS)           # 3 docs, ~230-290 chars each
  print(n, len(store.texts))
  ```

EXPECTED OUTPUT:
  ```
  9 9        # each ~240-char doc → 3 chunks of size 100 (step 80)
  ```

HINT:
  Reuse your chunk_text loop; collect only chunk["text"] for add().

CHECK: python3 check.py medium/p02
"""

RAW_DOCS = [
    "Machine learning is a branch of artificial intelligence where models "
    "learn patterns from data instead of following explicit rules. "
    "Supervised learning trains on labeled examples, unsupervised learning "
    "finds hidden clusters, and reinforcement learning optimizes rewards.",

    "Paris is the capital of France and home to the Eiffel Tower, the "
    "Louvre museum, and countless cafes along the Seine. Visitors climb "
    "the tower at sunset for panoramic views, then stroll the "
    "Champs-Elysees toward the Arc de Triomphe.",

    "Great pasta starts with aggressively salted boiling water. Cook "
    "spaghetti until al dente, save a cup of starchy pasta water, then "
    "toss with the sauce so it clings to every strand. Finish with "
    "parmesan cheese and cracked black pepper.",
]

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# store = VectorStore()
# print(ingest(store, RAW_DOCS), "chunks stored")
