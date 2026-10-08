"""
LESSON 15 — 1D Dynamic Programming
HARD P02 — Longest Increasing Subsequence
============================================

CONCEPT:
  dp[i] = length of the longest strictly increasing subsequence that
  ENDS at index i. For each i, look at every earlier j: if
  nums[j] < nums[i], you may extend that subsequence, so
  dp[i] = 1 + max(dp[j] over valid j). THE TRAP: the answer is
  max(dp), not dp[-1] — the best subsequence can end anywhere.

PROBLEM:
  Write `length_of_lis(nums: list[int]) -> int` returning the length
  of the longest strictly increasing subsequence (elements need NOT
  be contiguous). Return 0 for an empty list. O(n^2) is expected —
  an O(n log n) variant exists (patience sorting + bisect).

TRY THIS INPUT:
  ```python
  print(length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]))
  print(length_of_lis([0, 1, 0, 3, 2, 3]))
  print(length_of_lis([7, 7, 7, 7]))
  ```

EXPECTED OUTPUT:
  ```
  4
  4
  1
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
