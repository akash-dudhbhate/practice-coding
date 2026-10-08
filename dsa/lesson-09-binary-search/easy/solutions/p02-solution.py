"""
SOLUTION: First Occurrence / Lower Bound (Easy)
============================================
When nums[mid] >= target, mid is a candidate answer — record it,
then keep searching the LEFT half for an earlier hit. The last
recorded candidate is the first occurrence.
"""
def first_occurrence(nums: list, target: int) -> int:
    lo, hi = 0, len(nums) - 1
    answer = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            answer = mid     # candidate — but an earlier one may exist
            hi = mid - 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return answer

if __name__ == "__main__":
    assert first_occurrence([1, 2, 2, 2, 3, 4], 2) == 1
    assert first_occurrence([1, 2, 2, 2, 3, 4], 4) == 5
    assert first_occurrence([1, 2, 2, 2, 3, 4], 9) == -1
    assert first_occurrence([2, 2, 2], 2) == 0
    assert first_occurrence([], 3) == -1
    assert first_occurrence([1, 1, 2, 3], 1) == 0
    print("All tests passed!")
