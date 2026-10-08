"""
SOLUTION: Trapping Rain Water (Hard) — O(n) time, O(1) space
============================================================
Water at i = min(max_left, max_right) - height[i]. Carry running
maxima from both ends. Whichever side has the SMALLER max already
knows its bound (the other side can only be >= current max), so that
side's water is final — process it and move inward.
"""
def trap(height: list) -> int:
    if not height:
        return 0
    L, R = 0, len(height) - 1
    left_max, right_max = height[L], height[R]
    water = 0
    while L < R:
        if left_max < right_max:
            L += 1
            left_max = max(left_max, height[L])
            water += left_max - height[L]
        else:
            R -= 1
            right_max = max(right_max, height[R])
            water += right_max - height[R]
    return water

if __name__ == "__main__":
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([]) == 0
    assert trap([2, 0, 2]) == 2
    assert trap([3, 3, 3]) == 0
    print("All tests passed!")
