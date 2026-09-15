"""
SOLUTION: Tuple Stats (Hard)
=============================
Given a tuple of numbers, return (min, max, average). Handle empty.
"""
def tuple_stats(nums: tuple) -> tuple:
    if not nums:
        return (None, None, 0.0)
    return (min(nums), max(nums), sum(nums) / len(nums))

if __name__ == "__main__":
    assert tuple_stats((1, 2, 3)) == (1, 3, 2.0)
    assert tuple_stats(()) == (None, None, 0.0)
    assert tuple_stats((5,)) == (5, 5, 5.0)
    print("All tests passed!")
