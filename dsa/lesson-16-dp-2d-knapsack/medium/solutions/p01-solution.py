"""
SOLUTION: 0/1 Knapsack (Medium)
================================
dp[i][w] = max value from items 0..i-1 with capacity w.
take-or-skip: dp[i][w] = max(dp[i-1][w], val + dp[i-1][w-wt]).
The 1-row version iterates w DOWNWARD so dp[w-wt] still holds the
previous row's value — upward would let items repeat (unbounded).
"""


def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wt, val = weights[i - 1], values[i - 1]    # row i decides item i-1
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]                 # skip
            if wt <= w:
                dp[i][w] = max(dp[i][w], val + dp[i - 1][w - wt])  # take
    return dp[n][capacity]


# Space-optimized equivalent — same answer, O(W) space
def knapsack_1d(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):   # DOWNWARD = 0/1
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
    return dp[capacity]


if __name__ == "__main__":
    for fn in (knapsack, knapsack_1d):
        assert fn([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9
        assert fn([2, 3, 4, 5], [3, 4, 5, 6], 5) == 7
        assert fn([4, 5, 6], [1, 2, 3], 3) == 0
        assert fn([1, 2, 3], [6, 10, 12], 5) == 22
        assert fn([1], [1], 0) == 0
        assert fn([], [], 10) == 0
    print("All tests passed!")
