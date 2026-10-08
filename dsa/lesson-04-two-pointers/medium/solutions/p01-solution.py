"""
SOLUTION: Remove Duplicates from Sorted Array (Medium)
======================================================
slow = next write slot for a unique value. Since sorted, a value is
new exactly when it differs from nums[slow - 1] (the last one kept).
"""
def remove_duplicates(nums: list) -> int:
    if not nums:
        return 0
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

if __name__ == "__main__":
    a = [1, 1, 2]
    assert remove_duplicates(a) == 2 and a[:2] == [1, 2]
    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates(b) == 5 and b[:5] == [0, 1, 2, 3, 4]
    assert remove_duplicates([]) == 0
    c = [1, 2, 3]
    assert remove_duplicates(c) == 3 and c[:3] == [1, 2, 3]
    print("All tests passed!")
