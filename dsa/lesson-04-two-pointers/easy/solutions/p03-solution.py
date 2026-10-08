"""
SOLUTION: Pair Sum on a Sorted Array (Easy)
===========================================
Sum too small -> left element can't work with anything -> L += 1.
Sum too big   -> right element can't work with anything -> R -= 1.
"""
def pair_sum_sorted(nums: list, target: int) -> list:
    L, R = 0, len(nums) - 1
    while L < R:
        s = nums[L] + nums[R]
        if s == target:
            return [L, R]
        if s < target:
            L += 1
        else:
            R -= 1
    return []

if __name__ == "__main__":
    assert pair_sum_sorted([2, 7, 11, 15], 9) == [0, 1]
    assert pair_sum_sorted([1, 2, 4, 7, 11], 9) == [1, 3]
    assert pair_sum_sorted([1, 3, 5], 10) == []
    assert pair_sum_sorted([1, 4], 5) == [0, 1]
    assert pair_sum_sorted([], 5) == []
    print("All tests passed!")
