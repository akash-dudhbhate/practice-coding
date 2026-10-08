"""
LESSON 05 — Sliding Window
EASY P02 — Averages of All Windows
============================================

CONCEPT:
  Same fixed window as P01, but instead of tracking a maximum you
  collect one value per window — the average. Keep a running sum as
  you slide, and append `window_sum / k` for each position.

PROBLEM:
  Write a function `window_averages(nums: list[int], k: int) -> list[float]`
  that returns a list of the averages of every contiguous window of
  size k, in order. If k > len(nums), return an empty list.

TRY THIS INPUT:
  ```python
  print(window_averages([1, 2, 3, 4], 2))
  print(window_averages([5, 5, 5], 3))
  print(window_averages([1, 2], 3))
  ```

EXPECTED OUTPUT:
  ```
  [1.5, 2.5, 3.5]
  [5.0]
  []
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
