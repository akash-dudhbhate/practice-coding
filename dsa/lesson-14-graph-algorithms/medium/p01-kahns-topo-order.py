"""
LESSON 14 — Graph Algorithms
MEDIUM P01 — Kahn's Topological Order
============================================

CONCEPT:
  Kahn's algorithm: compute indegree of every vertex; enqueue ALL
  indegree-0 vertices (no unmet prerequisites); loop — pop a vertex,
  append to order, decrement each neighbor's indegree, enqueue any
  that hits 0. The queue always holds "everything whose dependencies
  are already emitted." If len(order) < n at the end, the leftovers
  are inside/downstream of a cycle — return [].

PROBLEM:
  Write `kahn_order(n, edges) -> list` using Kahn's BFS specifically
  (indegrees + deque, not DFS postorder). edges hold directed pairs
  (a, b) meaning a -> b. Return any valid topo order, or [] on cycle.

TRY THIS INPUT:
  ```python
  print(kahn_order(4, [(0,1),(0,2),(1,3),(2,3)]))
  print(kahn_order(2, [(0,1),(1,0)]))
  print(kahn_order(4, [(1,0),(2,0),(3,1),(3,2)]))
  print(kahn_order(3, []))
  ```

EXPECTED OUTPUT:
  ```
  [0, 1, 2, 3]     # or [0, 2, 1, 3]
  []
  [3, 1, 2, 0]     # or [3, 2, 1, 0] — 3 must come before 1 and 2
  [0, 1, 2]        # any permutation
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
