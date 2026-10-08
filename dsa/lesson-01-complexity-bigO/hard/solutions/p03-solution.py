"""
SOLUTION: Optimize Pair Sum (Hard)
==============================
Slow: check every pair i < j -> O(n^2) comparisons.
Fast: store seen values in a set, ask "is target - x seen?" -> O(n).
"""
def pair_sum_slow(nums: list, target) -> tuple:
    ops = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            ops += 1
            if nums[i] + nums[j] == target:
                return True, ops
    return False, ops

def pair_sum_fast(nums: list, target) -> tuple:
    seen = set()
    ops = 0
    for x in nums:
        ops += 1                  # one membership check = 1 op
        if target - x in seen:
            return True, ops
        seen.add(x)
    return False, ops

if __name__ == "__main__":
    assert pair_sum_slow([1, 4, 7, 2, 9], 11) == (True, 5)
    assert pair_sum_fast([1, 4, 7, 2, 9], 11) == (True, 3)
    assert pair_sum_slow([1, 2, 3], 10) == (False, 3)
    assert pair_sum_fast([1, 2, 3], 10) == (False, 3)
    print("All tests passed!")
