"""
LEVEL 12 — RAG Systems
EASY P03 — Text Chunking
========================================

CONCEPT:
  LLMs have a context window limit. Long documents must be split
  into chunks that fit. Overlap keeps context between chunks.

  "Hello world this is a test" → chunks of 50 chars, overlap 10:
    chunk 0: chars 0-50
    chunk 1: chars 40-90 (overlap of 10)
    ...

PROBLEM:
  Write `chunk_text(text, chunk_size, overlap)` that splits text
  into overlapping chunks. Returns list of chunk strings.

TRY THIS INPUT:
  ```python
  text = "Machine learning is a subset of artificial intelligence. It uses algorithms to learn patterns from data. Deep learning is a type of machine learning that uses neural networks with many layers."
  chunks = chunk_text(text, 50, 10)
  print(len(chunks))       # 5
  print(chunks[0])         # "Machine learning is a subset of artificial intelli"
  ```

EXPECTED OUTPUT:
  ```
  5
  Machine learning is a subset of artificial intelli
  al intelligence. It uses algorithms to learn patte
  earn patterns from data. Deep learning is a type o
  s a type of machine learning that uses neural netw
  eural networks with many layers.
  ```

HINT:
  start at 0, take text[i:i+chunk_size], step = chunk_size - overlap

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.


# === TEST ===
# c = chunk_text("a" * 200, 50, 10)
# print(len(c))
