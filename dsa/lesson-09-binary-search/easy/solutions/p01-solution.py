"""
SOLUTION: Classic Binary Search (Easy)
============================================
lo/hi bracket the search space. Each step probes mid and discards
the half that can't hold the target. Loop while lo <= hi so a
one-element range still gets checked.
"""
def binary_search(nums: list, target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1     # target is strictly right of mid
        else:
            hi = mid - 1     # target is strictly left of mid
    return -1

if __name__ == "__main__":
    assert binary_search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert binary_search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([], 1) == -1
    assert binary_search([1, 2, 3], 1) == 0
    assert binary_search([1, 2, 3], 3) == 2
    print("All tests passed!")
