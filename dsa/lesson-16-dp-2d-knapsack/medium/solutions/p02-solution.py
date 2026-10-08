"""
SOLUTION: Longest Common Subsequence (Medium)
==============================================
dp[i][j] = LCS of a[:i], b[:j]. Match -> dp[i-1][j-1] + 1; else
max(dp[i-1][j], dp[i][j-1]). The (m+1)x(n+1) padding row/col is the
base case — without it, dp[i-1] at i=0 wraps to the bottom row.
"""


def longest_common_subsequence(a: str, b: str) -> int:
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    assert longest_common_subsequence("", "abc") == 0
    assert longest_common_subsequence("abc", "") == 0
    assert longest_common_subsequence("bsbininm", "jmjkbkjkv") == 1
    assert longest_common_subsequence("abcba", "babcab") == 4   # "abca"? no: "abcb"/"babc"... = 4
    print("All tests passed!")
