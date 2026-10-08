"""
SOLUTION: Find a Peak Element (Hard)
============================================
Nothing is sorted, yet binary search still works: edges are -inf,
so the array must rise somewhere. If nums[mid] < nums[mid+1] we're
climbing — a peak is guaranteed to the right. Otherwise we're
descending or AT a peak — one exists at mid or to the left.
"""
def find_peak(nums: list) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1           # uphill — peak must be right
        else:
            hi = mid               # downhill/peak — at mid or left
    return lo

if __name__ == "__main__":
    assert find_peak([1, 2, 3, 1]) == 2
    assert find_peak([1, 2, 1, 3, 5, 6, 4]) in (1, 5)
    assert find_peak([1]) == 0
    assert find_peak([1, 2]) == 1
    assert find_peak([3, 2, 1]) == 0
    assert find_peak([2, 1]) == 0
    print("All tests passed!")
