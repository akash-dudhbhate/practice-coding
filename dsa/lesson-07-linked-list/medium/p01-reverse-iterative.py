"""
LESSON 07 — Linked Lists
MEDIUM P01 — Reverse a Linked List (Iterative)
============================================

CONCEPT:
  Pointer surgery. Three pointers — prev (reversed-so-far), curr (node
  being flipped), nxt (rescued rest of list) — walk forward flipping
  every arrow. THE rescue line `nxt = curr.next` must run BEFORE
  `curr.next = prev`, or the rest of the list is lost forever.
  O(n) time, O(1) space.

PROBLEM:
  Write `reverse_list(head) -> Node` that reverses the list in place
  (relink the existing nodes — do NOT build new nodes or convert to a
  Python list) and returns the new head. 1->2->3->4->5 becomes
  5->4->3->2->1. Empty list returns None; single node returns itself.

TRY THIS INPUT:
  ```python
  print(to_list(reverse_list(build_list([1, 2, 3, 4, 5]))))
  print(to_list(reverse_list(None)))
  print(to_list(reverse_list(build_list([1]))))
  ```

EXPECTED OUTPUT:
  ```
  [5, 4, 3, 2, 1]
  []
  [1]
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
