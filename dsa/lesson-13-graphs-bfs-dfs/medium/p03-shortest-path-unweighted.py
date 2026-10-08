"""
LESSON 13 — Graphs: BFS & DFS
MEDIUM P03 — Shortest Path in an Unweighted Graph
============================================

CONCEPT:
  BFS expands in rings, so the FIRST time the target pops, its level
  IS the shortest distance — nothing shorter could be left undiscovered.
  Track distance as a dict (dist[nxt] = dist[v] + 1) or enqueue
  (vertex, dist) pairs. `dist` doubles as the visited set. CRITICAL:
  it must be a queue — a stack turns this into DFS and distances lie.

PROBLEM:
  Write `shortest_distance(adj, start, target) -> int`: fewest hops
  from start to target, -1 if unreachable, 0 if start == target.

TRY THIS INPUT:
  ```python
  sq = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}     # a square
  print(shortest_distance(sq, 0, 3))
  print(shortest_distance(sq, 0, 0))
  print(shortest_distance({0:[1],1:[0],2:[]}, 0, 2))
  print(shortest_distance({0:[1],1:[0,2],2:[1,3],3:[2]}, 0, 3))
  ```

EXPECTED OUTPUT:
  ```
  2
  0
  -1
  3
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
