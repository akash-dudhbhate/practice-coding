"""
LESSON 15 — 1D Dynamic Programming
HARD P03 — Partition Equal Subset Sum
============================================

CONCEPT:
  A reduction + a boolean DP. Two equal subsets exist iff some
  subset sums to total/2 — so it's subset-sum, a "can you reach"
  DP. reachable[s] = can we make sum s? Process numbers one at a
  time: reachable[s] |= reachable[s - x]. CRITICAL: iterate s
  DOWNWARD so each number is used at most once (0/1, not unbounded).

PROBLEM:
  Write `can_partition(nums: list[int]) -> bool` returning True if
  nums can be split into two subsets with equal sum. Every element
  is used at most once. If the total is odd the answer is instantly
  False.

TRY THIS INPUT:
  ```python
  print(can_partition([1, 5, 11, 5]))
  print(can_partition([1, 2, 3, 5]))
  print(can_partition([1, 1]))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  True
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
