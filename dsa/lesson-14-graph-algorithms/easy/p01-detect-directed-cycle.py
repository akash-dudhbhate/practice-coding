"""
LESSON 14 — Graph Algorithms
EASY P01 — Detect a Cycle in a Directed Graph
============================================

CONCEPT:
  A directed graph is acyclic (a DAG) iff you can order its vertices so
  every edge points forward. Two ways to answer "is there a cycle?":
  (1) Kahn's — peel indegree-0 vertices; if you can't emit all n, the
  leftovers are stuck in cycles. (2) DFS with 3 colors — unseen /
  visiting / done; reaching a "visiting" vertex = back edge = cycle.

PROBLEM:
  Write `has_directed_cycle(n, edges) -> bool`. edges hold directed
  pairs (a, b) meaning a -> b. A self-loop (a, a) is a cycle.
  Undirected mutual edges (a,b)+(b,a) form a 2-cycle: True.

TRY THIS INPUT:
  ```python
  print(has_directed_cycle(3, [(0,1),(1,2),(2,0)]))
  print(has_directed_cycle(3, [(0,1),(1,2)]))
  print(has_directed_cycle(1, [(0,0)]))
  print(has_directed_cycle(4, [(0,1),(0,2),(1,3),(2,3)]))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  True
  False
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
