"""
LESSON 16 — 2D DP & Knapsack
HARD P01 — Edit Distance
============================================

CONCEPT:
  Two-sequence DP with three operations instead of one choice:
  dp[i][j] = min ops to turn a[:i] into b[:j]. Match → free
  diagonal move. Mismatch → 1 + min(delete a[i-1] = dp[i-1][j],
  insert b[j-1] = dp[i][j-1], substitute = dp[i-1][j-1]).
  BASE TRAP: dp[i][0] = i and dp[0][j] = j — empty-prefix
  conversions cost real deletes/inserts, NOT zero.

PROBLEM:
  Write `min_distance(word1: str, word2: str) -> int` returning the
  minimum number of insert/delete/substitute operations (each on a
  single character) to convert word1 into word2.

TRY THIS INPUT:
  ```python
  print(min_distance("horse", "ros"))
  print(min_distance("intention", "execution"))
  print(min_distance("", "abc"))
  ```

EXPECTED OUTPUT:
  ```
  3
  5
  3
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
