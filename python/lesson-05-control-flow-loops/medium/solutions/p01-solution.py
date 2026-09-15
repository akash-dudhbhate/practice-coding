"""
SOLUTION: First Even (Medium)
===============================
Return the first even number using break. None if none found.
"""
def first_even(nums: list) -> int:
    for n in nums:
        if n % 2 == 0:
            return n
    return None

if __name__ == "__main__":
    assert first_even([1, 3, 4, 5]) == 4
    assert first_even([1, 3, 5]) is None
    assert first_even([]) is None
    print("All tests passed!")
