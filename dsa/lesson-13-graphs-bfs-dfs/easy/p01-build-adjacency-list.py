"""
LESSON 13 — Graphs: BFS & DFS
EASY P01 — Build an Adjacency List
============================================

CONCEPT:
  Interview problems hand you `n` vertices and an edge list
  [(0,1),(0,2),...]. Before ANY traversal you must convert it to an
  adjacency dict: vertex -> [neighbors]. Two traps: (1) undirected
  edges go BOTH ways, (2) vertices with no edges still exist — they
  must appear as keys with empty lists, or later loops KeyError.

PROBLEM:
  Write `build_adjacency(n, edges) -> dict` for an UNDIRECTED graph.
  Keys: every vertex 0..n-1. Values: neighbor lists in edge order
  (don't sort). For each edge (a, b) append b to adj[a] AND a to adj[b].

TRY THIS INPUT:
  ```python
  print(build_adjacency(4, [(0,1),(0,2),(1,3)]))
  print(build_adjacency(3, []))
  print(build_adjacency(2, [(0,1)]))
  ```

EXPECTED OUTPUT:
  ```
  {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
  {0: [], 1: [], 2: []}
  {0: [1], 1: [0]}
  ```

CHECK: python3 check.py easy/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
