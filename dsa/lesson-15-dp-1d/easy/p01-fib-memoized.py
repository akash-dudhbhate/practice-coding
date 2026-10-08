"""
LESSON 15 — 1D Dynamic Programming
EASY P01 — Fibonacci, Memoized
============================================

CONCEPT:
  fib(n) = fib(n-1) + fib(n-2) recomputes the same subproblems
  exponentially many times: fib(3) twice, fib(2) three times inside
  fib(5) alone. Memoization (cache the result of each n) collapses
  ~2^n calls down to ~n. This is the whole idea of DP in miniature.

PROBLEM:
  Write `fib(n: int) -> int` returning the nth Fibonacci number:
  fib(0) = 0, fib(1) = 1. It must run fast for n up to 50+ — a naive
  recursive solution will hang on fib(50).

TRY THIS INPUT:
  ```python
  print(fib(0))
  print(fib(10))
  print(fib(50))
  ```

EXPECTED OUTPUT:
  ```
  0
  55
  12586269025
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
