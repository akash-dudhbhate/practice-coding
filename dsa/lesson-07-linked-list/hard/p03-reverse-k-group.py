"""
LESSON 07 — Linked Lists
HARD P03 — Reverse Nodes in k-Group
============================================

CONCEPT:
  Reversal, repeated: check there ARE k nodes ahead (count before you
  commit), reverse that block with the same prev/curr/nxt dance,
  splice it back between the previous group's tail and the next
  group's head. The node that was the group's head becomes its tail —
  keep a reference to it because IT links forward after the flip. A
  dummy makes the first group's splice identical to all others.

PROBLEM:
  Write `reverse_k_group(head, k) -> Node` reversing every contiguous
  block of exactly k nodes; a leftover tail shorter than k stays put.
  reverse_k_group(1->2->3->4->5, 2) -> 2->1->4->3->5.
  reverse_k_group(1->2->3->4->5, 3) -> 3->2->1->4->5 (4->5 untouched).
  Assume k >= 1.

TRY THIS INPUT:
  ```python
  print(to_list(reverse_k_group(build_list([1, 2, 3, 4, 5]), 2)))
  print(to_list(reverse_k_group(build_list([1, 2, 3, 4, 5]), 3)))
  print(to_list(reverse_k_group(build_list([1, 2, 3]), 5)))
  ```

EXPECTED OUTPUT:
  ```
  [2, 1, 4, 3, 5]
  [3, 2, 1, 4, 5]
  [1, 2, 3]
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
