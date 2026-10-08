"""
LESSON 07 — Linked Lists
MEDIUM P03 — Merge Two Sorted Lists
============================================

CONCEPT:
  The dummy-node trick: a fake head gives `tail` something to hang the
  first merged node on, so every splice is identical — no "is this the
  first one?" special case. Repeatedly take the smaller front node,
  then hook whichever list still has nodes with `tail.next = a or b`.
  You are RELINKING existing nodes, not copying values.

PROBLEM:
  Write `merge_two(a, b) -> Node` that merges two sorted lists into one
  sorted chain and returns its head. Use a dummy node + tail; reuse the
  input nodes (O(1) extra space). merge_two(1->2->4, 1->3->4) ->
  1->1->2->3->4->4. Handle empty inputs.

TRY THIS INPUT:
  ```python
  print(to_list(merge_two(build_list([1, 2, 4]), build_list([1, 3, 4]))))
  print(to_list(merge_two(None, build_list([1, 2]))))
  print(to_list(merge_two(None, None)))
  ```

EXPECTED OUTPUT:
  ```
  [1, 1, 2, 3, 4, 4]
  [1, 2]
  []
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
