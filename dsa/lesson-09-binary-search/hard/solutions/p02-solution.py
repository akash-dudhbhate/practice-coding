"""
SOLUTION: Find Minimum in Rotated Sorted Array (Hard)
============================================
Compare nums[mid] to nums[hi]:
  nums[mid] > nums[hi]  → the dip (minimum) is strictly right of mid
  nums[mid] <= nums[hi] → mid is on/inside the low half, minimum is
                          at mid or left of it
Loop with lo < hi so we never overshoot the minimum itself.
"""
def find_min_rotated(nums: list) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1           # minimum is strictly right of mid
        else:
            hi = mid               # mid might BE the minimum — keep it
    return nums[lo]

if __name__ == "__main__":
    assert find_min_rotated([3, 4, 5, 1, 2]) == 1
    assert find_min_rotated([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min_rotated([11, 13, 15, 17]) == 11
    assert find_min_rotated([2, 1]) == 1
    assert find_min_rotated([1]) == 1
    assert find_min_rotated([2, 3, 4, 5, 1]) == 1
    print("All tests passed!")
