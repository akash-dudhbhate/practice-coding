"""
SOLUTION: Unique Paths (Easy)
==============================
dp[r][c] = dp[r-1][c] + dp[r][c-1] — arrive from top or left.
Border row/col all 1s. One-row version keeps O(n) space: each
cell accumulates "top" (old row[c]) + "left" (row[c-1]).
"""


def unique_paths(m: int, n: int) -> int:
    row = [1] * n                    # first row: only reachable from left
    for _ in range(1, m):
        for c in range(1, n):
            row[c] += row[c - 1]     # new row[c] = top + left
    return row[-1]


if __name__ == "__main__":
    assert unique_paths(3, 2) == 3
    assert unique_paths(3, 7) == 28
    assert unique_paths(7, 3) == 28
    assert unique_paths(1, 1) == 1
    assert unique_paths(1, 10) == 1
    assert unique_paths(10, 1) == 1
    assert unique_paths(3, 4) == 10
    print("All tests passed!")
