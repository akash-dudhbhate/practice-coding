"""
LESSON 08 — Recursion & Backtracking
EASY P03 — Power Function (Recursively)
============================================

CONCEPT:
  base^exp = base * base^(exp-1): the recursive promise computes
  base^(exp-1), you multiply one more base. Base case exp == 0 -> 1.
  (Bonus thinking: halving exp each call is O(log exp) — the naive
  exp-1 version is fine here; the trick is in EXTRA-PRACTICE.md.)

PROBLEM:
  Write `power(base, exp)` RECURSIVELY — no **, no pow(), no loops —
  for non-negative integer exp. power(2, 10) -> 1024.

TRY THIS INPUT:
  ```python
  print(power(2, 10))
  print(power(2, 0))
  print(power(3, 3))
  print(power(5, 1))
  ```

EXPECTED OUTPUT:
  ```
  1024
  1
  27
  5
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
