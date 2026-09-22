"""
LESSON 12 — Decorators
HARD P03 — Stacked Decorators (@log + @timer)
============================================

CONCEPT:
  Decorators stack bottom-up: `@log` over `@timer` over `process` means
  `process = log(timer(process))`. The outermost decorator runs first,
  and each layer adds its own behavior around the next.

PROBLEM:
  Write two decorators:
    - `log(func)` — prints f"[LOG] {func.__name__}({args}, {kwargs})"
      then returns the call result
    - `timer(func)` — times the call and prints
      f"[TIMER] {func.__name__} took {elapsed:.4f}s"
  Stack BOTH on `process(n)` (log on top) that sleeps 0.05s and
  returns n * 2.

TRY THIS INPUT:
  ```python
  print(process(5))
  ```

EXPECTED OUTPUT:
  ```
  [LOG] process((5,), {})
  [TIMER] process took 0.05xx s
  10
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
