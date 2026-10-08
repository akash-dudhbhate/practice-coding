"""
SOLUTION: Edit Distance (Hard)
===============================
dp[i][j] = min ops turning a[:i] into b[:j].
  match    -> dp[i-1][j-1]            (free)
  mismatch -> 1 + min(delete dp[i-1][j], insert dp[i][j-1],
                      substitute dp[i-1][j-1])
Base borders are REAL costs: dp[i][0]=i deletes, dp[0][j]=j inserts.
"""


def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i                     # delete all i chars
    for j in range(n + 1):
        dp[0][j] = j                     # insert all j chars
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],       # delete
                                   dp[i][j - 1],       # insert
                                   dp[i - 1][j - 1])   # substitute
    return dp[m][n]


if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
    assert min_distance("", "") == 0
    assert min_distance("a", "ab") == 1
    assert min_distance("abc", "") == 3
    assert min_distance("", "abc") == 3
    assert min_distance("kitten", "sitting") == 3
    assert min_distance("flaw", "lawn") == 2
    assert min_distance("abc", "abc") == 0
    print("All tests passed!")
