"""
LESSON 07 — Linked Lists
EASY P03 — Find the Middle
============================================

CONCEPT:
  Fast & slow pointers: slow hops 1 node, fast hops 2. When fast falls
  off the end, slow has covered half the distance — it sits exactly on
  the middle node. No counting, no length, O(1) space. On even-length
  lists this loop yields the SECOND middle node.

PROBLEM:
  Write `find_middle(head) -> int` returning the VALUE of the middle
  node. For even length return the second of the two middles:
  1->2->3->4 -> 3. Use the fast/slow pattern (both start at head;
  while fast and fast.next, advance 1 vs 2).

TRY THIS INPUT:
  ```python
  print(find_middle(build_list([1, 2, 3, 4, 5])))
  print(find_middle(build_list([1, 2, 3, 4])))
  print(find_middle(build_list([1])))
  print(find_middle(build_list([1, 2])))
  ```

EXPECTED OUTPUT:
  ```
  3
  3
  1
  2
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
