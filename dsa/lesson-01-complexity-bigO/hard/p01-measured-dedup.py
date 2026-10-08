"""
LESSON 01 — Time/Space Complexity & Big-O
HARD P01 — Measured Dedup (Naive vs Set)
============================================

CONCEPT:
  `x not in list` is a hidden O(n) scan — inside a loop it makes dedup
  O(n²). A set answers `in` in O(1) average, so the same dedup is O(n).
  Count the comparisons to PROVE it.

PROBLEM:
  Write two functions, each returning (deduped_list, ops_count):

  `dedup_naive(nums)` — keep a `result` list; for each x, scan result
      element by element (count EVERY element comparison); append x if
      not found.

  `dedup_set(nums)` — keep a `seen` set; for each x, do ONE membership
      check (count it as 1 op); append x to result if not seen.

  For [1,2,2,3]: naive does 0+1+2+2 = 5 comparisons; set does 4 checks.

TRY THIS INPUT:
  ```python
  print(dedup_naive([1, 2, 2, 3]))
  print(dedup_set([1, 2, 2, 3]))
  print(dedup_naive([1, 2, 3, 4, 5]))
  ```

EXPECTED OUTPUT:
  ```
  ([1, 2, 3], 5)
  ([1, 2, 3], 4)
  ([1, 2, 3, 4, 5], 10)
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
