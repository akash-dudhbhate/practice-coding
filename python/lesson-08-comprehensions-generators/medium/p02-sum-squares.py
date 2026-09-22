"""
LESSON 08 — Comprehensions & Generators
MEDIUM P02 — Sum Squares Generator
============================================

CONCEPT:
  A generator expression `(x*x for x in range(n))` produces values
  lazily — no list is built in memory. `sum()` can consume it
  directly.

PROBLEM:
  Write a function `sum_squares(n)` that returns the sum of the
  squares of 0 through n-1 using a generator expression.

TRY THIS INPUT:
  ```python
  print(sum_squares(4))
  print(sum_squares(0))
  ```

EXPECTED OUTPUT:
  ```
  14
  0
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
