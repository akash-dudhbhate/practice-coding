"""
LESSON 01 — Time/Space Complexity & Big-O
HARD P02 — Fib Call Count
============================================

CONCEPT:
  Naive recursive fib is O(2^n) because every call spawns TWO more
  calls — the call count roughly doubles each level. fib(5) makes 15
  calls; fib(10) makes 177; fib(50) makes ~a trillion.

PROBLEM:
  Write a function `fib_with_count(n: int) -> tuple` returning
  (fib(n), total_calls) where total_calls counts every recursive call
  made (including the top-level call). Use plain recursion — no
  memoization, we WANT to see the explosion.

TRY THIS INPUT:
  ```python
  print(fib_with_count(0))
  print(fib_with_count(1))
  print(fib_with_count(5))
  print(fib_with_count(10))
  ```

EXPECTED OUTPUT:
  ```
  (0, 1)
  (1, 1)
  (5, 15)
  (55, 177)
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
