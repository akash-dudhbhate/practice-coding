"""
SOLUTION: Wildcard Matching (Hard)
===================================
dp[i][j] = does p[:j] match all of s[:i]?
  p[j-1] char or '?': dp[i][j] = dp[i-1][j-1] and char-match
  p[j-1] == '*':      dp[i][j] = dp[i-1][j] (star eats s[i-1], stays)
                                 or dp[i][j-1] (star matches empty)
Base: dp[0][0] = True; dp[0][j] = True only while p[:j] is all '*'.
"""


def is_match_wildcard(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n + 1):            # '*'s can match empty s
        dp[0][j] = dp[0][j - 1] and p[j - 1] == "*"
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # else: stays False
    return dp[m][n]


if __name__ == "__main__":
    assert is_match_wildcard("aa", "a") is False
    assert is_match_wildcard("aa", "*") is True
    assert is_match_wildcard("cb", "?a") is False
    assert is_match_wildcard("adceb", "*a*b") is True
    assert is_match_wildcard("acdcb", "a*c?b") is False
    assert is_match_wildcard("abc", "***") is True
    assert is_match_wildcard("", "*") is True
    assert is_match_wildcard("", "?") is False
    assert is_match_wildcard("", "a") is False
    assert is_match_wildcard("abc", "abc") is True
    assert is_match_wildcard("a", "aa") is False
    print("All tests passed!")
