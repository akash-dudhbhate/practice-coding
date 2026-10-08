"""
SOLUTION: Unique Paths with Obstacles (Easy)
=============================================
Same as unique paths, but a wall (1) forces dp[r][c] = 0 — and on
the borders, a wall zeroes everything downstream: a border cell is
reachable only if it's open AND its predecessor was reachable.
"""


def unique_paths_with_obstacles(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = 1 if grid[0][0] == 0 else 0
    for c in range(1, n):                    # wall kills rest of row 0
        dp[0][c] = dp[0][c - 1] if grid[0][c] == 0 else 0
    for r in range(1, m):                    # wall kills rest of col 0
        dp[r][0] = dp[r - 1][0] if grid[r][0] == 0 else 0

    for r in range(1, m):
        for c in range(1, n):
            if grid[r][c] == 0:
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
            # walls stay 0
    return dp[m - 1][n - 1]


if __name__ == "__main__":
    assert unique_paths_with_obstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
    assert unique_paths_with_obstacles([[0, 1], [0, 0]]) == 1
    assert unique_paths_with_obstacles([[1]]) == 0
    assert unique_paths_with_obstacles([[0]]) == 1
    assert unique_paths_with_obstacles([[0, 0], [1, 1], [0, 0]]) == 0
    assert unique_paths_with_obstacles([[0, 1, 0]]) == 0   # wall in row 0 leaks nothing
    print("All tests passed!")
