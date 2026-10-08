"""
LESSON 07 — Linked Lists
EASY P02 — Traverse and Collect
============================================

CONCEPT:
  There's no index and no len() on a linked list — traversal IS the
  API. `while head:` then `head = head.next` visits every node in
  order. This walker is the "to_list" half of the test bridge: it
  turns a chain back into a Python list you can assert on.

PROBLEM:
  Write `to_list(head) -> list` that walks the chain and returns the
  node values as a Python list in order. Return [] for an empty list
  (head is None). Define `Node`/`build_list` in this file too if you
  want to test locally — the checker builds nodes itself and only
  needs your function to read `.val` and `.next`.

TRY THIS INPUT:
  ```python
  print(to_list(build_list([1, 2, 3, 4])))
  print(to_list(None))
  print(to_list(build_list([9])))
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 3, 4]
  []
  [9]
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
