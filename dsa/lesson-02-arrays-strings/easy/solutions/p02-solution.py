"""
SOLUTION: Max Min One Pass (Easy)
==============================
Track both extremes in a single scan -> O(n), one pass.
"""
def max_min(nums: list) -> tuple:
    hi = lo = nums[0]
    for x in nums[1:]:
        if x > hi:
            hi = x
        if x < lo:
            lo = x
    return hi, lo

if __name__ == "__main__":
    assert max_min([3, 1, 4, 1, 5]) == (5, 1)
    assert max_min([7]) == (7, 7)
    assert max_min([-2, -9, -4]) == (-2, -9)
    print("All tests passed!")
