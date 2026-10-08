"""
SOLUTION: Search in Rotated Sorted Array (Hard)
============================================
Every [lo, hi] window has at least one fully-sorted side.
Identify the sorted side (nums[lo] <= nums[mid] → left is sorted),
then check whether target lies inside that side's value range.
If yes, keep it; if no, it must be in the other half.
"""
def search_rotated(nums: list, target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:          # left half is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1               # target inside the sorted half
            else:
                lo = mid + 1
        else:                              # right half is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1               # target inside the sorted half
            else:
                hi = mid - 1
    return -1

if __name__ == "__main__":
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
    assert search_rotated([1, 3], 3) == 1
    assert search_rotated([5, 1, 3], 5) == 0
    assert search_rotated([3, 1], 1) == 1
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 4) == 0
    print("All tests passed!")
