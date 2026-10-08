"""
LESSON 13 — Graphs: BFS & DFS
EASY P03 — DFS Traversal Order (Recursive Preorder)
============================================

CONCEPT:
  DFS dives: pick the first unvisited neighbor, recurse all the way
  down, backtrack, try the next neighbor. Recursive preorder = record
  the vertex the moment you enter it. The call stack IS the stack —
  that's why the recursive version is 5 lines. `seen` is what stops
  cyclic graphs from recursing forever.

PROBLEM:
  Write `dfs_order(adj, start) -> list` returning RECURSIVE preorder:
  record `v`, then recurse into `adj[v]` in stored order, skipping
  seen vertices. On the lesson graph this gives [0,1,3,2,4,5] — note
  it is NOT BFS's [0,1,2,3,4,5]. Disconnected vertices aren't reached.

TRY THIS INPUT:
  ```python
  adj = {0:[1,2], 1:[0,3], 2:[0,4,5], 3:[1], 4:[2], 5:[2]}
  print(dfs_order(adj, 0))
  print(dfs_order({0:[]}, 0))
  print(dfs_order({0:[1], 1:[0,2], 2:[1]}, 0))
  ```

EXPECTED OUTPUT:
  ```
  [0, 1, 3, 2, 4, 5]
  [0]
  [0, 1, 2]
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
