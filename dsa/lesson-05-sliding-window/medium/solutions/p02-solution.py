"""
SOLUTION: Max Consecutive Ones With K Flips (Medium)
==========================================
Variable window: longest window with at most k zeros.
Expand right; while zeros > k, shrink left. Record after shrink
(window always valid at that point) → O(n).
"""
def longest_ones(nums, k):
    left, zeros, best = 0, 0, 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zeros += 1                  # enter: track zeros in window
        while zeros > k:                # invalid → shrink
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

if __name__ == "__main__":
    assert longest_ones([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    assert longest_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
    assert longest_ones([1,1,1], 0) == 3
    assert longest_ones([0,0,0], 1) == 1
    assert longest_ones([1,0,1,0,1], 1) == 3   # only ONE zero may be flipped
    print("All tests passed!")
