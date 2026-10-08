"""
LESSON 09 — Binary Search
HARD P03 — Find a Peak Element
============================================

CONCEPT:
  A peak is an element strictly greater than both neighbors
  (imagine nums[-1] = nums[len] = -inf). Binary search works even
  though NOTHING is sorted: if nums[mid] < nums[mid + 1], you're
  on an uphill slope — a peak MUST exist to the right. Otherwise
  a peak exists at mid or to the left.

PROBLEM:
  Write `find_peak(nums: list) -> int`: return the index of ANY
  peak element. nums[i] != nums[i+1] for all i. Must be O(log n).

TRY THIS INPUT:
  ```python
  print(find_peak([1, 2, 3, 1]))
  print(find_peak([1, 2, 1, 3, 5, 6, 4]))   # 1 or 5 both valid
  print(find_peak([1]))
  ```

EXPECTED OUTPUT:
  ```
  2
  5            (1 is also accepted by the checker)
  0
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
