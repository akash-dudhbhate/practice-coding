"""
LESSON 01 — Time/Space Complexity & Big-O
HARD P03 — Optimize Pair Sum (O(n^2) -> O(n))
============================================

CONCEPT:
  "Does any pair sum to target?" — the nested-loop version checks all
  pairs (O(n^2)); the set version stores each number and asks "is
  target - x already seen?" (O(n)). Same answer, massively less work.

PROBLEM:
  Write two functions, each returning (found: bool, ops_count: int):

  `pair_sum_slow(nums, target)` — nested loops over pairs (i, j) with
      i < j; count every comparison; early exit when found.

  `pair_sum_fast(nums, target)` — iterate once with a `seen` set;
      count every membership check; early exit when found.

  For [1,4,7,2,9] target 11: slow checks (1,4)(1,7)(1,2)(1,9)(4,7) =
  5 ops; fast checks complements of 1,4,7 = 3 ops.

TRY THIS INPUT:
  ```python
  print(pair_sum_slow([1, 4, 7, 2, 9], 11))
  print(pair_sum_fast([1, 4, 7, 2, 9], 11))
  print(pair_sum_slow([1, 2, 3], 10))
  print(pair_sum_fast([1, 2, 3], 10))
  ```

EXPECTED OUTPUT:
  ```
  (True, 5)
  (True, 3)
  (False, 3)
  (False, 3)
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
