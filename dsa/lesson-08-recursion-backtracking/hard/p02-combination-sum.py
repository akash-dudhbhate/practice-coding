"""
LESSON 08 — Recursion & Backtracking
HARD P02 — Combination Sum
============================================

CONCEPT:
  Backtracking with a "never look back" rule: recurse on (i, remaining)
  and only ever try candidates[j] for j >= i. Recursing with the SAME
  j allows unlimited reuse of that candidate; never revisiting j < i
  is what prevents [2,3] and [3,2] both appearing. Prune early when
  remaining < 0; record a copy when remaining == 0.

PROBLEM:
  Write `combination_sum(candidates: list, target: int) -> list`
  returning all unique combinations summing to target (elements may
  repeat; each combo in ascending index order so [2,2,3] appears once,
  never also as [2,3,2]). candidates distinct positive ints.
  combination_sum([2,3,6,7], 7) -> [[2,2,3],[7]] any order.

TRY THIS INPUT:
  ```python
  print(sorted(map(sorted, combination_sum([2, 3, 6, 7], 7))))
  print(combination_sum([2], 1))
  print(sorted(map(sorted, combination_sum([2, 3, 5], 8))))
  ```

EXPECTED OUTPUT:
  ```
  [[2, 2, 3], [7]]
  []
  [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
