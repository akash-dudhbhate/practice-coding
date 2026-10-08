"""
LESSON 14 — Graph Algorithms
HARD P01 — Dijkstra's Shortest Path
============================================

CONCEPT:
  BFS minimizes hop count; Dijkstra minimizes TOTAL WEIGHT. Same wave
  of discovery, but the queue becomes a MIN-HEAP keyed by distance:
  pop the cheapest-known vertex (its distance is final — non-negative
  weights mean no later detour could improve it), then RELAX: offer
  each neighbor dist[v] + w, keep it if smaller. Stale heap entries
  (a vertex pushed with an old, larger distance) get skipped by
  `if d > dist[v]: continue`.

PROBLEM:
  Write `dijkstra(n, edges, src) -> list` for DIRECTED weighted edges
  (a, b, w) meaning a -w-> b. Return dist[v] for all v in range(n),
  float("inf") for unreachable. dist[src] = 0.

TRY THIS INPUT:
  ```python
  edges = [(0,1,5),(0,2,1),(2,1,2),(1,3,1),(2,3,5)]
  print(dijkstra(4, edges, 0))
  print(dijkstra(3, [(0,1,2)], 0))
  print(dijkstra(3, [(0,1,2),(0,2,5)], 1))
  ```

EXPECTED OUTPUT:
  ```
  [0, 3, 1, 4]
  [0, 2, inf]
  [inf, 0, inf]
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
