"""
LESSON 07 — Linked Lists
MEDIUM P02 — Detect a Cycle (Floyd's)
============================================

CONCEPT:
  On a looping list, a fast walker (2 hops) and a slow walker (1 hop)
  MUST eventually meet — fast gains exactly one node per step inside
  the loop, like lapping a slower runner on a track. If there's no
  cycle, fast runs off the end (hits None). Identity matters: compare
  nodes with `is`, never by value. O(n) time, O(1) space.

PROBLEM:
  Write `has_cycle(head) -> bool`. A list "has a cycle" if following
  .next eventually returns to an earlier node instead of reaching None.
  The checker builds real cyclic structures — your job is only the
  two-pointer walk. Return False for None and for lists that end.

TRY THIS INPUT:
  ```python
  # 1 -> 2 -> 3 -> 4, tail.next = node(2)   -> True
  # 1 -> 2, tail.next = head                -> True
  # 1 -> 2 -> 3 -> None                     -> False
  print(has_cycle(cyclic))     # True
  print(has_cycle(normal))     # False
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
