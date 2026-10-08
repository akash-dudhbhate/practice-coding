"""
LESSON 18 — Advanced Mix
HARD P03 — Largest Rectangle in Histogram
============================================

CONCEPT:
  Monotonic stack of indices with INCREASING heights. When a shorter
  bar arrives, pop taller bars — the popped bar's rectangle is bounded
  on the right by i and on the left by the new stack top. Width =
  i - left. Heights alone are useless on the stack; you need INDICES to
  compute widths. A sentinel bar of height 0 at the end flushes every
  pending rectangle.

PROBLEM:
  Write a function `largest_rectangle_area(heights: list[int]) -> int`
  returning the largest rectangle area contained in the histogram.
  heights[i] is the height of bar i; bars have width 1 and sit
  adjacent. Empty input returns 0.

TRY THIS INPUT:
  ```python
  print(largest_rectangle_area([2,1,5,6,2,3]))
  print(largest_rectangle_area([2,4]))
  print(largest_rectangle_area([1]))
  print(largest_rectangle_area([4,2,0,3,2,5]))
  print(largest_rectangle_area([]))
  ```

EXPECTED OUTPUT:
  ```
  10
  4
  1
  6
  0
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
