"""
LESSON 15 — 1D Dynamic Programming
HARD P01 — Word Break
============================================

CONCEPT:
  "Can you reach" phrasing on a string: dp[i] = can s[:i] be
  segmented? Then dp[i] = any(dp[j] and s[j:i] is a word) over all
  j < i. Top-down is equally natural: can_break(i) = can s[i:] be
  segmented — memoize on the index i or adversarial inputs like
  "aaaa...b" blow up exponentially.

PROBLEM:
  Write `word_break(s: str, wordDict: list[str]) -> bool` returning
  True if s can be segmented into a space-separated sequence of one
  or more dictionary words. Words may be reused. Return True for
  empty s.

TRY THIS INPUT:
  ```python
  print(word_break("leetcode", ["leet", "code"]))
  print(word_break("applepenapple", ["apple", "pen"]))
  print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
  ```

EXPECTED OUTPUT:
  ```
  True
  True
  False
  ```

CHECK: python3 check.py hard/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
