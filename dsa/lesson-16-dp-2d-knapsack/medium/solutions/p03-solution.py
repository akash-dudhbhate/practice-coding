"""
SOLUTION: Coin Change 2 — Count Combinations (Medium)
======================================================
dp[a] = number of combinations summing to a. COINS OUTER, amount
inner: coin c is fully folded in before the next coin is seen, so
{1,2,2} and {2,1,2} collapse to one combination. (Amount-outer
would count permutations: (5, [1,2,5]) -> 9 instead of 4.)
This is secretly the same dp[i][w] 2D table compressed to one row,
iterated UPWARD because unlimited use is intended.
"""


def coin_change_count(amount: int, coins: list[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1                              # one way to make nothing
    for c in coins:                        # outer loop: per coin
        for a in range(c, amount + 1):     # upward = unbounded use of c
            dp[a] += dp[a - c]
    return dp[amount]


if __name__ == "__main__":
    assert coin_change_count(5, [1, 2, 5]) == 4
    assert coin_change_count(3, [2]) == 0
    assert coin_change_count(10, [10]) == 1
    assert coin_change_count(0, [1, 2]) == 1
    assert coin_change_count(4, [1, 2, 3]) == 4   # 1+1+1+1, 1+1+2, 2+2, 1+3
    assert coin_change_count(7, [2, 3]) == 1      # only {2,2,3}
    print("All tests passed!")
