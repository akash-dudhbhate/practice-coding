"""
LESSON 04 — Two Pointers
MEDIUM P03 — 3-Sum (sorted + two pointers)
============================================

CONCEPT:
  Sort the array, fix each element nums[i], then run sorted pair-sum
  on the subarray after i looking for -nums[i]. Skip duplicate values
  for i (and skip duplicate pairs) so no triplet is reported twice.
  O(n^2) total — the hashing trick can't do this in O(1) space.

PROBLEM:
  Write a function `three_sum(nums: list) -> list` returning ALL
  unique triplets [a, b, c] with a + b + c == 0. Each triplet sorted
  ascending; the list of triplets sorted. No duplicate triplets.

TRY THIS INPUT:
  ```python
  print(three_sum([-1, 0, 1, 2, -1, -4]))
  print(three_sum([0, 1, 1]))
  print(three_sum([0, 0, 0]))
  ```

EXPECTED OUTPUT:
  ```
  [[-1, -1, 2], [-1, 0, 1]]
  []
  [[0, 0, 0]]
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
