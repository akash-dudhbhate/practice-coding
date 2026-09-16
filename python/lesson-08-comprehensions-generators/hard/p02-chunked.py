"""
LESSON 08 — Comprehensions & Generators
HARD P02 — Chunked Generator
============================================

CONCEPT:
  Generators are great for streaming: collect items into a small
  buffer, yield it when full, and remember to yield the leftover
  partial chunk at the end.

PROBLEM:
  Write a generator function `chunked(iterable, size)` that yields
  lists of `size` items from `iterable`. The last chunk may be
  smaller.

TRY THIS INPUT:
  ```python
  print(list(chunked([1, 2, 3, 4, 5], 2)))
  print(list(chunked([], 3)))
  ```

EXPECTED OUTPUT:
  ```
  [[1, 2], [3, 4], [5]]
  []
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
