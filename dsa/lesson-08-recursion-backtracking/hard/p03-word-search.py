"""
LESSON 08 — Recursion & Backtracking
HARD P03 — Word Search in a Grid
============================================

CONCEPT:
  The purest choose/explore/unchoose: from a cell matching word[0],
  recursively try the 4 neighbors for word[1]. A cell can't repeat
  within one path — mark it visited by overwriting (e.g. "#"), then
  RESTORE it after the recursive call so sibling paths can use it.
  Try every cell as a starting point. Stop early: first char mismatch
  or out-of-bounds prunes instantly.

PROBLEM:
  Write `exist(board: list, word: str) -> bool`. board is a list of
  lists of single-char strings; the word must be traceable through
  adjacent (N/S/E/W) cells, each used at most once. On
  [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]:
  "ABCCED" -> True, "SEE" -> True, "ABCB" -> False (B can't repeat).

TRY THIS INPUT:
  ```python
  b = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
  print(exist(b, "ABCCED"))
  print(exist(b, "SEE"))
  print(exist(b, "ABCB"))
  print(exist([["a"]], "a"))
  ```

EXPECTED OUTPUT:
  ```
  True
  True
  False
  True
  ```

CHECK: python3 check.py hard/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
