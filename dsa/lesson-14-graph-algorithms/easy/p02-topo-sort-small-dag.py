"""
LESSON 14 — Graph Algorithms
EASY P02 — Topological Sort a Small DAG
============================================

CONCEPT:
  A topological order lists vertices so every edge a -> b has a BEFORE
  b. The simple construction: repeatedly emit any vertex with no
  un-emitted incoming edges (indegree 0), removing its outgoing edges.
  Any vertex can be first — there is no unique answer, so the checker
  VALIDATES the order rather than comparing it literally.

PROBLEM:
  Write `topo_order(n, edges) -> list` returning a permutation of
  range(n) where every edge (a,b) satisfies pos[a] < pos[b]. If the
  graph has a cycle, no valid order exists — return [].

TRY THIS INPUT:
  ```python
  print(topo_order(4, [(0,1),(1,2),(2,3)]))   # forced: [0,1,2,3]
  print(topo_order(3, [(0,1),(0,2)]))          # 0 first; 1,2 either order
  print(topo_order(3, [(0,1),(1,0)]))          # cycle -> []
  print(topo_order(2, []))                     # any order works
  ```

EXPECTED OUTPUT:
  ```
  [0, 1, 2, 3]
  [0, 1, 2]        # or [0, 2, 1]
  []
  [0, 1]           # or [1, 0]
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
