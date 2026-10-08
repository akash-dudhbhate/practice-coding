"""
LESSON 05 — Sliding Window
EASY P03 — Count Windows Meeting a Target
============================================

CONCEPT:
  Fixed window again — this time each slide answers a yes/no question:
  "does this window's sum meet the target?" The window state (running
  sum) is identical; only what you record changes.

PROBLEM:
  Write a function `count_windows_at_least(nums: list[int], k: int,
  target: int) -> int` that counts how many contiguous windows of
  size k have a sum >= target. If k > len(nums), return 0.

TRY THIS INPUT:
  ```python
  print(count_windows_at_least([1, 4, 2, 10, 2, 3, 1, 0, 20], 4, 15))
  print(count_windows_at_least([1, 1, 1], 2, 3))
  print(count_windows_at_least([3, 3, 3], 2, 5))
  ```

EXPECTED OUTPUT:
  ```
  5
  0
  2
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
