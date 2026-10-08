"""
SOLUTION: Min Path Sum (Easy)
==============================
dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1]).
Borders are forced prefix sums — no choice on the first row/col.
Written here by mutating a copy of the grid (in-place style).
"""


def min_path_sum(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [row[:] for row in grid]            # don't mutate caller's grid
    for c in range(1, n):
        dp[0][c] += dp[0][c - 1]             # first row: forced from left
    for r in range(1, m):
        dp[r][0] += dp[r - 1][0]             # first col: forced from above
        for c in range(1, n):
            dp[r][c] += min(dp[r - 1][c], dp[r][c - 1])
    return dp[m - 1][n - 1]


if __name__ == "__main__":
    assert min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
    assert min_path_sum([[1, 2, 3], [4, 5, 6]]) == 12
    assert min_path_sum([[7]]) == 7
    assert min_path_sum([[1, 2], [1, 1]]) == 3
    assert min_path_sum([[5, 0, 1], [1, 0, 5]]) == 10   # path: right, down, right = 5+0+0+5
    print("All tests passed!")
