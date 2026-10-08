"""
SOLUTION: Minimum Size Subarray Sum (Medium)
==========================================
Variable window, inverted shape: while sum >= target, RECORD then
shrink (squeeze to smallest). Numbers are positive so shrinking
only ever lowers the sum → O(n).
"""
def min_subarray_len(target, nums):
    left, total, best = 0, 0, float("inf")
    for right in range(len(nums)):
        total += nums[right]                  # expand
        while total >= target:                # valid → squeeze
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float("inf") else best

if __name__ == "__main__":
    assert min_subarray_len(7, [2, 3, 1, 2, 4, 3]) == 2
    assert min_subarray_len(4, [1, 4, 4]) == 1
    assert min_subarray_len(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert min_subarray_len(15, [1, 2, 3, 4, 5]) == 5
    assert min_subarray_len(5, [1, 1, 1, 1]) == 0   # impossible → 0
    print("All tests passed!")
