"""
LESSON 13 — Graphs: BFS & DFS
MEDIUM P01 — Count Connected Components
============================================

CONCEPT:
  A component is one blob of mutually-reachable vertices. Counting
  them: loop over ALL vertices; whenever you hit one not yet seen,
  that's a NEW component — count it and flood it (DFS or BFS) to mark
  everything inside. Vertices the flood never touches are isolated —
  each is its own component, which is why the loop is over range(n).

PROBLEM:
  Write `count_components(n, edges) -> int` for an undirected graph.
  Build the adjacency dict first (isolated vertices exist!), then
  flood-count. `count_components(5, [(0,1),(1,2),(3,4)])` is 2:
  {0,1,2} and {3,4}. `count_components(4, [])` is 4: a vertex with
  no edges is still a whole component by itself.

TRY THIS INPUT:
  ```python
  print(count_components(5, [(0,1),(1,2),(3,4)]))
  print(count_components(4, []))
  print(count_components(4, [(0,1),(2,3)]))
  print(count_components(3, [(0,1),(1,2),(0,2)]))   # triangle
  ```

EXPECTED OUTPUT:
  ```
  2
  4
  2
  1
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
