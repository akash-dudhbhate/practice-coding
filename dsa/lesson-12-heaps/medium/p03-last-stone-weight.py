"""
LESSON 12 — Heaps
MEDIUM P03 — Last Stone Weight
============================================

CONCEPT:
  "Repeatedly grab the two LARGEST, put something back" is a
  max-heap loop — and Python only has a min-heap, so store negated
  weights: push -x, and un-negate pops with -heappop(h). Discipline:
  negate on the way in, un-negate on the way out.

PROBLEM:
  Write `last_stone_weight(stones) -> int`. Each turn smashes the
  two heaviest stones: equal -> both destroyed; else the lighter
  shatters and the heavier becomes |x-y|. Return the last stone's
  weight, or 0 if none remain.

TRY THIS INPUT:
  ```python
  print(last_stone_weight([2, 7, 4, 1, 8, 1]))
  print(last_stone_weight([1]))
  print(last_stone_weight([1, 1]))
  print(last_stone_weight([10, 4, 2, 10]))
  ```

EXPECTED OUTPUT:
  ```
  1
  1
  0
  2
  ```

CHECK: python3 check.py medium/p03
"""

import heapq

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
