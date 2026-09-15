"""
SOLUTION: Find Pair (Hard)
============================
Return indices of first pair that sum to target. None if no pair.
"""
def find_pair(nums: list, target: int) -> tuple:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

if __name__ == "__main__":
    assert find_pair([2, 7, 11, 15], 9) == (0, 1)
    assert find_pair([1, 2, 3], 10) is None
    print("All tests passed!")
