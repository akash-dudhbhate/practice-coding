"""
LESSON 12 — Heaps
HARD P02 — Task Scheduler
============================================

CONCEPT:
  Same task needs n cooldown slots between runs. Greedy: every
  slot, run the most-frequent AVAILABLE task — a max-heap on
  remaining counts (negated). Tasks on cooldown sit in a holding
  list until the cooldown expires, then rejoin the heap. When the
  heap is empty but cooldown tasks remain, that slot is IDLE —
  idle time is what makes the answer exceed len(tasks).

PROBLEM:
  Write `least_interval(tasks, n) -> int` — minimum total slots to
  finish all tasks. tasks is a list of uppercase letters.
  n=0 -> len(tasks) (no cooldown). Empty -> 0.

TRY THIS INPUT:
  ```python
  print(least_interval(['A','A','A','B','B','B'], 2))   # A B _ A B _ A B
  print(least_interval(['A','A','A','B','B','B'], 0))
  print(least_interval(['A','A','A','B','B','B','C','C','C'], 2))
  print(least_interval(['A','A','A','A','A','A','B','C','D','E','F','G'], 2))
  print(least_interval(['A'], 5))
  ```

EXPECTED OUTPUT:
  ```
  8
  6
  9
  16
  1
  ```

CHECK: python3 check.py hard/p02
"""

import heapq
from collections import Counter, deque

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
