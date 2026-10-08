"""
SOLUTION: Container With Most Water (Medium)
============================================
The shorter side caps the height. Moving the taller pointer inward
only loses width with no possible height gain — a dead end. Always
move the pointer at the shorter bar.
"""
def max_area(height: list) -> int:
    L, R = 0, len(height) - 1
    best = 0
    while L < R:
        area = min(height[L], height[R]) * (R - L)
        best = max(best, area)
        if height[L] < height[R]:
            L += 1
        else:
            R -= 1
    return best

if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([2, 3, 4, 5, 18, 17, 6]) == 17
    assert max_area([]) == 0
    print("All tests passed!")
