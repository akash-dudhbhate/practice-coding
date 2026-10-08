"""
LESSON 07 — Linked Lists
HARD P01 — Remove Nth Node From End (One Pass)
============================================

CONCEPT:
  "Nth from end" = maintain a gap of n between two pointers. Give fast
  an n-step head start; when fast falls off the end, slow sits just
  BEFORE the target — one splice removes it. The dummy node is what
  makes "the target IS the head" (n == length) look like every other
  removal. One pass, O(n) time, O(1) space.

PROBLEM:
  Write `remove_nth(head, n) -> Node` that removes the nth node from
  the END of the list in a single pass and returns the (possibly new)
  head. remove_nth(1->2->3->4->5, 2) -> 1->2->3->5. Removing the head
  must work: remove_nth(1->2, 2) -> 2. Assume 1 <= n <= length.

TRY THIS INPUT:
  ```python
  print(to_list(remove_nth(build_list([1, 2, 3, 4, 5]), 2)))
  print(to_list(remove_nth(build_list([1]), 1)))
  print(to_list(remove_nth(build_list([1, 2]), 2)))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3, 5]
  []
  [2]
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
