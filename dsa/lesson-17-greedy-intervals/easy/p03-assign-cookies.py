"""
LESSON 17 — Greedy & Intervals
EASY P03 — Assign Cookies (the purest greedy)
============================================

CONCEPT:
  Two sorted lists, two pointers. Sort greed factors and cookie sizes;
  give each child the SMALLEST cookie that satisfies them. This is
  provably optimal — a bigger cookie "wasted" on an easy child can't
  do better, since the easy child only needs the threshold.

PROBLEM:
  Write a function `find_content_children(g: list[int], s: list[int]) -> int`.
  g[i] is the minimum cookie size child i will accept; s[j] is cookie j's
  size. Each child gets at most one cookie, each cookie feeds at most one
  child. Return the maximum number of content children.

TRY THIS INPUT:
  ```python
  print(find_content_children([1,2,3], [1,1]))
  print(find_content_children([1,2], [1,2,3]))
  print(find_content_children([10,9,8,7], [5,6,7,8]))
  print(find_content_children([], [1,2]))
  ```

EXPECTED OUTPUT:
  ```
  1
  2
  2
  0
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
