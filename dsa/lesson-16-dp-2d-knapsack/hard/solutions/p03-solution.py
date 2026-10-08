"""
SOLUTION: Burst Balloons (Hard)
================================
Interval DP. Pad with 1s: A = [1] + nums + [1].
dp[i][j] = max coins bursting balloons strictly BETWEEN walls i,j.
Pick k in (i, j) as the LAST to burst: its neighbors are the fixed
walls i and j, so it pays A[i]*A[k]*A[j] and the sides dp[i][k],
dp[k][j] are independent. Fill by increasing interval length.
"""


def max_coins(nums: list[int]) -> int:
    A = [1] + nums + [1]                 # sentinel walls
    n = len(A)
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n):           # interval length (at least 1 balloon)
        for i in range(n - length):
            j = i + length
            for k in range(i + 1, j):    # k = LAST balloon burst in (i, j)
                cur = A[i] * A[k] * A[j] + dp[i][k] + dp[k][j]
                if cur > dp[i][j]:
                    dp[i][j] = cur
    return dp[0][n - 1] if n > 2 else 0  # empty nums -> 0


if __name__ == "__main__":
    assert max_coins([3, 1, 5, 8]) == 167
    assert max_coins([1, 5]) == 10
    assert max_coins([9]) == 9
    assert max_coins([]) == 0
    assert max_coins([1, 2, 3]) == 12
    assert max_coins([7, 9]) == 72       # burst 7 first: 1*7*9=63, then 9: 1*9*1=9 -> 72
    print("All tests passed!")
