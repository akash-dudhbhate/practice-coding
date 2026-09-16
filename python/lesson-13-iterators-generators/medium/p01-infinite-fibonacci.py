"""
LESSON 13 — Iterators & Generators
MEDIUM P01 — Infinite Fibonacci Generator
============================================

CONCEPT:
  Generators can be infinite — `while True` with `yield` is fine because
  values are only produced on demand. `itertools.islice` is how you take
  just the first N items from an infinite generator without hanging.

PROBLEM:
  Write a generator function `fibonacci()` that yields Fibonacci numbers
  forever: 0, 1, 1, 2, 3, 5, 8, ... In a `__main__` block, use
  `itertools.islice` to take and print the first 10.

TRY THIS INPUT:
  ```python
  from itertools import islice
  print(list(islice(fibonacci(), 10)))
  ```

EXPECTED OUTPUT:
  ```
  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
