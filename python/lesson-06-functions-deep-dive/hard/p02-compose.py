"""
LESSON 06 — Functions Deep Dive
HARD P02 — Compose
============================================

CONCEPT:
  Functions can return other functions. Composing means chaining two
  functions so the output of one feeds into the other.

PROBLEM:
  Write a function `compose(f, g)` that returns a new function which
  computes `f(g(x))` — apply `g` first, then `f`.

TRY THIS INPUT:
  ```python
  h = compose(lambda x: x + 1, lambda x: x * 2)
  print(h(3))
  ```

EXPECTED OUTPUT:
  ```
  7
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
