"""
LESSON 06 — Stacks & Queues
HARD P01 — Sliding Window Maximum (Monotonic Deque)
============================================

CONCEPT:
  Lesson 05's window + a MONOTONIC DEQUE holding indices whose values
  are in decreasing order. Front of deque = current window's max.
  Per step: (1) evict indices that slid out the left (front);
  (2) evict all values smaller than the newcomer (back — useless
  forever); (3) push the new index; (4) once window is full, record
  nums[dq[0]]. Each index enters and leaves once → O(n).

PROBLEM:
  Write a function `max_sliding_window(nums: list[int], k: int) ->
  list[int]` returning the maximum of every contiguous window of
  size k, in order.

TRY THIS INPUT:
  ```python
  print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
  print(max_sliding_window([1], 1))
  print(max_sliding_window([9, 11], 2))
  print(max_sliding_window([4, 3, 2, 1], 2))
  ```

EXPECTED OUTPUT:
  ```
  [3, 3, 5, 5, 6, 7]
  [1]
  [11]
  [4, 3, 2]
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
