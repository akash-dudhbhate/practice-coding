"""
LESSON 13 — Graphs: BFS & DFS
MEDIUM P02 — Number of Islands (Grid = Graph)
============================================

CONCEPT:
  A grid is a graph with IMPLICIT edges: cell (r,c) connects to
  (r±1,c) and (r,c±1) when in bounds and holding 1. Islands are
  connected components — so: scan every cell; when you find an
  unvisited 1, count += 1 and flood it (DFS/BFS), flipping each cell
  to 0 when you PUSH it (not when popped — else duplicates pile up).
  Mutating the grid doubles as the visited set for free.

PROBLEM:
  Write `num_islands(grid) -> int` counting islands of 1s connected
  4-directionally (NO diagonals). You may mutate the grid. All-water
  returns 0. Classic answer for the 4x5 example below is 3.

TRY THIS INPUT:
  ```python
  print(num_islands([[1,1,0,0,0],
                     [1,1,0,0,0],
                     [0,0,1,0,0],
                     [0,0,0,1,1]]))
  print(num_islands([[0,0],[0,0]]))
  print(num_islands([[1]]))
  ```

EXPECTED OUTPUT:
  ```
  3
  0
  1
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
