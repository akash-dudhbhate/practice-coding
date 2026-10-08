"""
LESSON 08 — Recursion & Backtracking
MEDIUM P02 — Permutations (All Orderings)
============================================

CONCEPT:
  Same choose/explore/unchoose skeleton as subsets, but the CHOICE SET
  is different: not "include or skip index i" but "pick any element not
  yet used". Track a used[] flag array (or pass the remaining pool);
  choose a number, recurse, then undo both the append and the flag.

PROBLEM:
  Write `permutations(nums: list) -> list` returning every ordering of
  nums — n! results — in any order. permutations([1,2,3]) returns all
  6 orderings; each element used exactly once per path; no duplicates.
  Elements are distinct.

TRY THIS INPUT:
  ```python
  print(sorted(map(tuple, permutations([1, 2, 3]))))
  print(permutations([1]))
  ```

EXPECTED OUTPUT:
  ```
  [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
  [[1]]
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
