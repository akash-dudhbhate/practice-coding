"""
SOLUTION: Search Insert Position (Easy)
============================================
Lower bound: the first index i where nums[i] >= target. If target
is present that's its index; if absent it's exactly the slot where
insertion keeps the array sorted. No separate "found" branch —
the loop always converges to the answer.
"""
def search_insert(nums: list, target: int) -> int:
    lo, hi = 0, len(nums)  # hi = len: insertion point can be the end
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1     # mid can't be the answer
        else:
            hi = mid         # mid could be the answer — keep it
    return lo                # first index with nums[i] >= target

if __name__ == "__main__":
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    assert search_insert([1], 0) == 0
    assert search_insert([1], 1) == 0
    assert search_insert([], 5) == 0
    print("All tests passed!")
