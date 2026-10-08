"""
LESSON 16 — 2D DP & Knapsack
MEDIUM P02 — Longest Common Subsequence
============================================

CONCEPT:
  Two-sequence DP: dp[i][j] = LCS length of prefixes a[:i], b[:j].
  If the last chars match, extend the diagonal: dp[i-1][j-1] + 1.
  Otherwise the answer comes from skipping a char on ONE side:
  max(dp[i-1][j], dp[i][j-1]). Base row/col = 0 (empty prefix
  shares nothing).

PROBLEM:
  Write `longest_common_subsequence(a: str, b: str) -> int`
  returning the length of the longest subsequence common to both
  strings (chars in order, NOT necessarily contiguous).

TRY THIS INPUT:
  ```python
  print(longest_common_subsequence("abcde", "ace"))
  print(longest_common_subsequence("abc", "abc"))
  print(longest_common_subsequence("abc", "def"))
  ```

EXPECTED OUTPUT:
  ```
  3
  3
  0
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
