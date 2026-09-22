"""
LESSON 12 — Decorators
MEDIUM P02 — @cache Decorator (Memoization)
============================================

CONCEPT:
  Memoization stores computed results in a dict keyed by the arguments.
  The dict lives in the decorator's closure, so it persists between
  calls — repeated calls with the same args skip the real work.

PROBLEM:
  Write a decorator `cache(func)` that keeps a private dict. On each
  call, if `args` was seen before return the stored result; otherwise
  compute, store, and return it. Apply it to `slow_square(n)` that
  prints "computing ..." and returns n * n — the second call with the
  same n should NOT print again.

TRY THIS INPUT:
  ```python
  print(slow_square(4))
  print(slow_square(4))   # cached — no "computing" line
  ```

EXPECTED OUTPUT:
  ```
    computing 4...
  16
  16
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
