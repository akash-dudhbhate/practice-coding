"""
LESSON 13 — Graphs: BFS & DFS
HARD P03 — Clone a Graph (DFS + Hashmap)
============================================

CONCEPT:
  Copying a graph means copying the SHAPE: same vals, same wiring,
  but every node a brand-new object. Two problems make this hard:
  (1) cycles — naive recursion loops forever; (2) shared neighbors —
  a diamond must clone to a diamond, not duplicate shared nodes.
  Both die to one weapon: a `orig -> clone` dict filled BEFORE
  recursing into neighbors. It is simultaneously the memo and the
  visited set.

PROBLEM:
  Write `clone_graph(node) -> Node`. The checker gives you a node
  object with `.val` and `.neighbors` (a list of node objects).
  Return the clone's entry node — every node in the copy must be a
  NEW object (`is` must fail against every original), with identical
  vals and neighbor wiring. `None` -> `None`.

TRY THIS INPUT:
  ```python
  # graph as adjacency list: node i (val i+1) has neighbors listed
  # adjacency = [[2,4],[1,3],[2,4],[1,3]]  (the classic 4-cycle)
  clone = clone_graph(node1)
  # BFS both: same vals/shape; every clone node `is not` its original
  ```

EXPECTED OUTPUT:
  ```
  a structurally identical graph made entirely of NEW node objects
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
