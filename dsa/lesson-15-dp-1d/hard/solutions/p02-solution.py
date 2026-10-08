"""
SOLUTION: Longest Increasing Subsequence (Hard)
================================================
O(n^2): dp[i] = LIS length ENDING at i; extend any earlier smaller
element. Answer is max(dp) — the LIS can end anywhere.
(An O(n log n) patience-sorting variant exists; see the commented
version below — worth mentioning in interviews.)
"""
import bisect


def length_of_lis(nums: list[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    dp = [1] * n                          # every element alone is an LIS
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# O(n log n): tails[k] = smallest possible tail value of an
# increasing subsequence of length k+1. len(tails) is the answer.
def length_of_lis_nlogn(nums: list[int]) -> int:
    tails = []
    for x in nums:
        i = bisect.bisect_left(tails, x)   # strict increase -> bisect_left
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


if __name__ == "__main__":
    for fn in (length_of_lis, length_of_lis_nlogn):
        assert fn([10, 9, 2, 5, 3, 7, 101, 18]) == 4
        assert fn([0, 1, 0, 3, 2, 3]) == 4
        assert fn([7, 7, 7, 7]) == 1
        assert fn([]) == 0
        assert fn([1]) == 1
        assert fn([4, 10, 4, 3, 8, 9]) == 3
        assert fn([3, 2, 1]) == 1
    print("All tests passed!")
