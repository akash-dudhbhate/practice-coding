"""
LESSON 12 — Decorators
EASY P02 — @timer Decorator
============================================

CONCEPT:
  Decorators shine for cross-cutting concerns like timing. Capture
  `time.time()` before and after the wrapped call, print the elapsed
  time, and still return the original result so callers don't notice.

PROBLEM:
  Write a decorator `timer(func)` that prints
  f"{func.__name__} took {elapsed:.4f}s" after each call and returns the
  function's result unchanged. Apply it to a `slow_function()` that
  sleeps 0.1s and returns "done".

TRY THIS INPUT:
  ```python
  print(slow_function())
  ```

EXPECTED OUTPUT:
  ```
  slow_function took 0.10xx s
  done
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
