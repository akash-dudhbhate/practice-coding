"""
LESSON 06 — Stacks & Queues
HARD P02 — Largest Rectangle in a Histogram
============================================

CONCEPT:
  Monotonic INCREASING stack of bar indices. When a shorter bar arrives
  it "closes" taller bars: pop them, and the popped bar's max rectangle
  = its height × width, where width spans from the new stack top+1 to
  current i-1. Append a sentinel 0-height bar to flush the stack at
  the end. Each bar pushed/popped once → O(n).

PROBLEM:
  Write a function `largest_rectangle_area(heights: list[int]) -> int`
  returning the area of the largest axis-aligned rectangle inside the
  histogram. heights[i] is the bar height at position i; bars have
  width 1 and sit side by side.

TRY THIS INPUT:
  ```python
  print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))
  print(largest_rectangle_area([2, 4]))
  print(largest_rectangle_area([1, 1, 1, 1]))
  print(largest_rectangle_area([6, 2, 5, 4, 5, 1, 6]))
  ```

EXPECTED OUTPUT:
  ```
  10
  4
  4
  12
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
