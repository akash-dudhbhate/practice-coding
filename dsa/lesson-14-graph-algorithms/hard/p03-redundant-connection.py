"""
LESSON 14 — Graph Algorithms
HARD P03 — Redundant Connection
============================================

CONCEPT:
  The graph is a tree (n vertices, n-1 edges, all connected) plus ONE
  extra undirected edge — so it has exactly one cycle, and removing
  the right edge restores the tree. Union-Find makes it a one-liner:
  process edges in input order; the first edge whose endpoints ALREADY
  share a set (`union` returns False) is the one that closed the
  cycle — and since order is respected, that's automatically the LAST
  such edge the problem wants. Vertices are 1-indexed: UnionFind(n+1).

PROBLEM:
  Write `find_redundant_connection(edges) -> list` returning the edge
  [a, b] to remove so the graph becomes a tree. Input: list of
  undirected pairs on vertices 1..n.

TRY THIS INPUT:
  ```python
  print(find_redundant_connection([(1,2),(1,3),(2,3)]))
  print(find_redundant_connection([(1,2),(2,3),(3,4),(1,4),(1,5)]))
  print(find_redundant_connection([(1,2),(2,3),(3,1)]))
  ```

EXPECTED OUTPUT:
  ```
  [2, 3]
  [1, 4]
  [3, 1]
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
