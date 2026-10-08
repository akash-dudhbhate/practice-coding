"""
LESSON 12 — Heaps
EASY P01 — Heap Ops Basics
============================================

CONCEPT:
  A Python list becomes a heap via heapq.heapify() — after that,
  h[0] is always the minimum. heappush adds (O(log n), sift-up),
  heappop removes the min (O(log n), sift-down), and peeking is
  just h[0] in O(1). Pops always come out in ascending order —
  that's the whole point of the structure.

PROBLEM:
  Write `run_heap_ops(nums, ops) -> list`. Heapify nums, then apply
  each op:
      ("push", x) -> heappush x
      ("pop",)    -> heappop, append result to output
      ("peek",)   -> read h[0], append to output (don't remove)
  Return the list of collected pop/peek results.

TRY THIS INPUT:
  ```python
  print(run_heap_ops([5, 1, 3], [("push", 0), ("pop",), ("peek",), ("pop",)]))
  print(run_heap_ops([4, 2, 7], [("pop",), ("pop",), ("peek",)]))
  print(run_heap_ops([], [("push", 3), ("push", 1), ("pop",)]))
  ```

EXPECTED OUTPUT:
  ```
  [0, 1, 1]
  [2, 4, 7]
  [1]
  ```

CHECK: python3 check.py easy/p01
"""

import heapq

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
