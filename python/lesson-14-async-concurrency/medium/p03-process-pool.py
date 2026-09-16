"""
LESSON 14 — Async & Concurrency
MEDIUM P03 — ProcessPoolExecutor
============================================

CONCEPT:
  Processes (not threads) get around the GIL for CPU-bound work —
  each worker is a separate interpreter running truly in parallel.

PROBLEM:
  Write a `square(n)` function returning n * n, designed to run
  across a ProcessPoolExecutor for numbers 1-20. (The check will
  map it over that range in a process pool.)

TRY THIS INPUT:
  ```python
  print(square(5))
  ```

EXPECTED OUTPUT:
  ```
  25
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
