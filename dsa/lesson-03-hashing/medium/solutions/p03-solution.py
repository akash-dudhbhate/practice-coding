"""
SOLUTION: Array Intersection (Medium)
=====================================
set(a) & set(b) is the unique common values in O(n + m). Sorted for a
deterministic result.
"""
def intersection(nums1: list, nums2: list) -> list:
    return sorted(set(nums1) & set(nums2))

if __name__ == "__main__":
    assert intersection([1, 2, 2, 1], [2, 2]) == [2]
    assert intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
    assert intersection([1, 2], [3, 4]) == []
    assert intersection([], [1]) == []
    print("All tests passed!")
