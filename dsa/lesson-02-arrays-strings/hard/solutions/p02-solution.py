"""
SOLUTION: Max Subarray (Kadane) (Hard)
==============================
cur = best sum of a subarray that MUST end here = max(x, cur + x).
best = the best cur ever seen. O(n) time, O(1) space.
"""
def max_subarray(nums: list) -> int:
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)      # extend or restart — never max(0,...)
        best = max(best, cur)
    return best

if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-3, -1, -2]) == -1
    assert max_subarray([7]) == 7
    print("All tests passed!")
