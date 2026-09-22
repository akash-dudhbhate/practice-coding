"""
LEVEL 16 — Real RAG (Embeddings + Vector DB)
EASY P03 — Chunking with Metadata
========================================

CONCEPT:
  Real pipelines track WHERE each chunk came from — character offsets
  and a chunk id — so answers can cite sources and chunks can be
  de-duped or mapped back to their parent document.

PROBLEM:
  Write `chunk_text(text, size=100, overlap=20)` that:
    1. Slides a window of `size` chars over `text`,
       step = size - overlap
    2. Stops once a chunk reaches the end of the text
    3. Returns a list of dicts, one per chunk:
         {"id": <int>, "text": <str>, "start": <int>, "end": <int>}
       where text[start:end] == the chunk's text

TRY THIS INPUT:
  ```python
  chunks = chunk_text("abcdefghijklmnopqrst" * 15, size=100, overlap=20)
  for c in chunks:
      print(c["id"], c["start"], c["end"], len(c["text"]))
  ```

EXPECTED OUTPUT:
  ```
  0 0 100 100
  1 80 180 100
  2 160 260 100
  3 240 300 60        # last chunk may be short
  ```

HINT:
  start at 0, advance by (size - overlap); end = min(start+size, len).
  break once end >= len(text) so you don't emit a redundant chunk.

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# for c in chunk_text("abcdefghijklmnopqrst" * 15, 100, 20):
#     print(c["id"], c["start"], c["end"], len(c["text"]))
