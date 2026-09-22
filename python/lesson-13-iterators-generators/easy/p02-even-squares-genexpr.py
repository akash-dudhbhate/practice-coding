"""
LESSON 13 — Iterators & Generators
EASY P02 — Even Squares Generator Expression
============================================

CONCEPT:
  A generator expression is like a list comprehension but with
  parentheses — it produces values lazily instead of building a list.
  `(x*x for x in ...)` yields each square only when asked.

PROBLEM:
  Create a generator expression named `even_squares` that produces the
  squares of the EVEN numbers from 0 to 20 (inclusive). In a `__main__`
  block, convert it to a list and print it.

TRY THIS INPUT:
  ```python
  print(list(even_squares))
  ```

EXPECTED OUTPUT:
  ```
  [0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
