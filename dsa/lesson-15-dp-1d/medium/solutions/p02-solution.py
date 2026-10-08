"""
SOLUTION: Min Cost Climbing Stairs (Medium)
============================================
dp[i] = min toll to STAND on stair i = cost[i] + min(dp[i-1], dp[i-2]).
Base: start at 0 or 1 is free -> dp[0] = cost[0], dp[1] = cost[1].
Answer: the top is PAST the last stair -> min(dp[n-1], dp[n-2]).
"""


def min_cost(cost: list[int]) -> int:
    n = len(cost)
    prev2, prev1 = cost[0], cost[1]     # dp[i-2], dp[i-1]
    for i in range(2, n):
        prev2, prev1 = prev1, cost[i] + min(prev1, prev2)
    return min(prev1, prev2)


if __name__ == "__main__":
    assert min_cost([10, 15, 20]) == 15
    assert min_cost([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    assert min_cost([0, 0, 1]) == 0
    assert min_cost([1, 2]) == 1
    assert min_cost([10, 15]) == 10
    assert min_cost([0, 2, 2, 1]) == 2
    print("All tests passed!")
