"""
LESSON 06 — Stacks & Queues
MEDIUM P01 — Next Greater Element
============================================

CONCEPT:
  MONOTONIC STACK. Keep a stack of indices whose elements are still
  waiting for their answer (values decreasing top-down). When a new
  element is bigger than the stack top's element, POP — the new element
  IS that top's "next greater." Each index is pushed and popped once
  → O(n) instead of the O(n²) scan-rightward brute force.

PROBLEM:
  Write a function `next_greater(nums: list[int]) -> list[int]` that
  returns a list where ans[i] is the first element to the right of
  nums[i] that is strictly greater, or -1 if none exists.

TRY THIS INPUT:
  ```python
  print(next_greater([2, 1, 2, 4, 3]))
  print(next_greater([1, 2, 3, 4]))
  print(next_greater([4, 3, 2, 1]))
  print(next_greater([5, 5, 5]))
  ```

EXPECTED OUTPUT:
  ```
  [4, 2, 4, -1, -1]
  [2, 3, 4, -1]
  [-1, -1, -1, -1]
  [-1, -1, -1]
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
