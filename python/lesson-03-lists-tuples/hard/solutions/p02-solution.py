"""
SOLUTION: Second Largest (Hard)
================================
Return the second largest unique value. None if fewer than 2 unique values.
"""
def second_largest(nums: list) -> int:
    unique = list(set(nums))
    if len(unique) < 2:
        return None
    unique.sort(reverse=True)
    return unique[1]

if __name__ == "__main__":
    assert second_largest([5, 1, 4, 4, 3]) == 4
    assert second_largest([1, 1, 1]) is None
    assert second_largest([3, 1]) == 1
    print("All tests passed!")
