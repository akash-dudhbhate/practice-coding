"""
SOLUTION: Skip Negatives (Medium)
===================================
Return a new list of only non-negative numbers using continue.
"""
def skip_negatives(nums: list) -> list:
    result = []
    for n in nums:
        if n < 0:
            continue
        result.append(n)
    return result

if __name__ == "__main__":
    assert skip_negatives([1, -2, 3, -4, 5]) == [1, 3, 5]
    assert skip_negatives([-1, -2]) == []
    assert skip_negatives([]) == []
    print("All tests passed!")
