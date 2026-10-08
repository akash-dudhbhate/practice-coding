"""
LESSON 08 — Recursion & Backtracking
MEDIUM P01 — Subsets (All 2^n)
============================================

CONCEPT:
  The include/skip decision tree: at index i you branch twice — take
  nums[i] into the path, or don't. Every leaf is one subset; with n
  elements there are exactly 2^n leaves. When recording a mutated path,
  append path.copy() — a raw path.append into results aliases the live
  list and every entry ends up identical.

PROBLEM:
  Write `subsets(nums: list) -> list` returning ALL subsets (the power
  set), in any order. subsets([1,2]) must contain [], [1], [2], [1,2]
  — 4 lists total. subsets([]) -> [[]]. Elements are distinct.

TRY THIS INPUT:
  ```python
  print(sorted(map(sorted, subsets([1, 2]))))
  print(len(subsets([1, 2, 3])))
  print(subsets([]))
  ```

EXPECTED OUTPUT:
  ```
  [[], [1], [1, 2], [2]]
  8
  [[]]
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
