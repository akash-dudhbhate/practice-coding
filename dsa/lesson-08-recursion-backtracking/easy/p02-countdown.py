"""
LESSON 08 — Recursion & Backtracking
EASY P02 — Countdown (Build a List Recursively)
============================================

CONCEPT:
  The contract matters: countdown(n) promises "a list [n..1]" — and it
  must return a list at EVERY depth, including the base. At level n you
  take the deeper list [n-1..1] and glue n onto the front. The base
  case's [] is the tail every level prepends onto.

PROBLEM:
  Write `countdown(n: int) -> list` RECURSIVELY (no loops) returning
  [n, n-1, ..., 1]. countdown(5) -> [5,4,3,2,1]; countdown(0) -> [].
  Assume n >= 0.

TRY THIS INPUT:
  ```python
  print(countdown(5))
  print(countdown(1))
  print(countdown(0))
  ```

EXPECTED OUTPUT:
  ```
  [5, 4, 3, 2, 1]
  [1]
  []
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
