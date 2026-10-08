"""
LESSON 16 — 2D DP & Knapsack
HARD P02 — Wildcard Matching
============================================

CONCEPT:
  Boolean two-sequence DP: dp[i][j] = does pattern p[:j] match all
  of s[:i]? Three cases:
    p[j-1] is a char or '?':  dp[i][j] = dp[i-1][j-1] and chars match
    p[j-1] == '*':            dp[i][j] = dp[i-1][j] or dp[i][j-1]
      (* consumes s[i-1] and stays, OR matches empty and is consumed)
  Base: dp[0][0] = True; dp[0][j] = True only while p[:j] is all '*'.

PROBLEM:
  Write `is_match_wildcard(s: str, p: str) -> bool` returning True
  if the ENTIRE string s matches pattern p, where '?' matches any
  single character and '*' matches any sequence (including empty).

TRY THIS INPUT:
  ```python
  print(is_match_wildcard("aa", "a"))
  print(is_match_wildcard("adceb", "*a*b"))
  print(is_match_wildcard("acdcb", "a*c?b"))
  ```

EXPECTED OUTPUT:
  ```
  False
  True
  False
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
