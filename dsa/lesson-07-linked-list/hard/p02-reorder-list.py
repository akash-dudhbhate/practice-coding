"""
LESSON 07 — Linked Lists
HARD P02 — Reorder List (L0 -> Ln -> L1 -> Ln-1)
============================================

CONCEPT:
  Composition: this problem is three moves you already own. (1) Find
  the middle with fast/slow — stop one step early so `slow` ends on
  the FIRST middle. (2) Cut: `second = slow.next; slow.next = None`.
  (3) Reverse the second half, then interleave the two halves. Each
  stage is a solved pattern; the skill is wiring them together. O(n)
  time, O(1) space, in place.

PROBLEM:
  Write `reorder_list(head) -> None` that rearranges the list IN PLACE
  to L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ... Do not create new
  nodes and do not convert to a Python list. The checker walks the
  same head object after you return — mutate the chain itself.
  1->2->3->4 -> 1->4->2->3.  1->2->3->4->5 -> 1->5->2->4->3.

TRY THIS INPUT:
  ```python
  h = build_list([1, 2, 3, 4]); reorder_list(h); print(to_list(h))
  h = build_list([1, 2, 3, 4, 5]); reorder_list(h); print(to_list(h))
  ```

EXPECTED OUTPUT:
  ```
  [1, 4, 2, 3]
  [1, 5, 2, 4, 3]
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
