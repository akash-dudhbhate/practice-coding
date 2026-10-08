"""
SOLUTION: Coin Change — Fewest Coins (Medium)
==============================================
dp[a] = fewest coins summing to a; dp[a] = 1 + min(dp[a-c]) over
c <= a. Seed unreachable cells with INF (amount+1 suffices: no
answer can exceed `amount` 1-coins). INF never wins a min, and
1 + INF for unreachable predecessors stays big — correct.
"""


def coin_change(coins: list[int], amount: int) -> int:
    INF = amount + 1
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1], 2) == 2
    assert coin_change([186, 419, 83, 408], 6249) == 20
    assert coin_change([1, 3, 4], 6) == 2    # greedy 4+1+1 fails; DP finds 3+3
    assert coin_change([2, 5, 10], 0) == 0
    print("All tests passed!")
