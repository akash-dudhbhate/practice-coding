"""
SOLUTION: House Robber (Medium)
================================
dp[i] = max money from houses 0..i. At house i:
  rob it  -> nums[i] + dp[i-2]  (can't touch i-1)
  skip it -> dp[i-1]
Take the max. Rolling variables: only dp[i-1] and dp[i-2] are read.
"""


def rob(nums: list[int]) -> int:
    prev2 = prev1 = 0               # dp[i-2], dp[i-1]
    for x in nums:
        prev2, prev1 = prev1, max(prev1, x + prev2)
    return prev1


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([2, 1, 1, 2]) == 4
    assert rob([]) == 0
    assert rob([5]) == 5
    assert rob([0, 0, 0]) == 0
    assert rob([6, 6, 6, 6]) == 12
    print("All tests passed!")
