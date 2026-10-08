"""
LESSON 08 — Recursion & Backtracking
HARD P01 — N-Queens (All Boards)
============================================

CONCEPT:
  Place one queen per row — recursion depth IS the row. At row r, try
  every column c: skip if c, r-c, or r+c is already claimed (columns +
  the two diagonal families are each constant-valued). Choose: place
  queen + mark all three sets. Explore: recurse to r+1. Unchoose:
  remove all three marks. Depth n with pruning = the classic board
  backtracker.

PROBLEM:
  Write `solve_n_queens(n: int) -> list` returning ALL valid boards.
  A board is a list of n strings of length n with "Q" and ".".
  solve_n_queens(4) has exactly 2 answers; solve_n_queens(1) -> [["Q"]];
  solve_n_queens(2) -> [] (no valid arrangement exists).

TRY THIS INPUT:
  ```python
  for board in solve_n_queens(4):
      print(*board, sep="\n"); print()
  print(solve_n_queens(1))
  print(solve_n_queens(2))
  ```

EXPECTED OUTPUT:
  ```
  .Q..
  ...Q
  Q...
  ..Q.
  <blank>
  ..Q.
  Q...
  ...Q
  .Q..
  <blank>
  ['Q']
  []
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
