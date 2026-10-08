"""
LESSON 13 — Graphs: BFS & DFS
HARD P02 — Rotting Oranges (Multi-Source BFS)
============================================

CONCEPT:
  Rot spreads from EVERY rotten cell simultaneously — that's not one
  BFS, it's all of them at once. Multi-source BFS: enqueue ALL rotten
  cells at level 0 BEFORE the loop. Each level = one minute. When the
  queue empties, minutes = max distance any fresh cell reached; any
  fresh cell left unreachable means the answer is -1. The grid is the
  graph again: 4-directional neighbors, marked visited by mutating
  (or a seen set + fresh counter).

PROBLEM:
  Write `oranges_rotting(grid) -> int` — minutes until no fresh
  oranges remain; -1 if some fresh orange can never rot. 2=rotten,
  1=fresh, 0=empty. A grid with no fresh oranges returns 0. You may
  mutate the grid.

TRY THIS INPUT:
  ```python
  print(oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]))
  print(oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]))
  print(oranges_rotting([[0,2]]))
  print(oranges_rotting([[1]]))
  ```

EXPECTED OUTPUT:
  ```
  4
  -1
  0
  -1
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
