"""
SOLUTION: Count Windows Meeting a Target (Easy)
==========================================
Fixed window — same running sum; count how many windows hit target.
"""
def count_windows_at_least(nums, k, target):
    if k > len(nums) or k <= 0:
        return 0
    window_sum = sum(nums[:k])
    count = 1 if window_sum >= target else 0
    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        if window_sum >= target:
            count += 1
    return count

if __name__ == "__main__":
    assert count_windows_at_least([1, 4, 2, 10, 2, 3, 1, 0, 20], 4, 15) == 5
    assert count_windows_at_least([1, 1, 1], 2, 3) == 0
    assert count_windows_at_least([3, 3, 3], 2, 5) == 2
    assert count_windows_at_least([1, 2], 3, 0) == 0
    print("All tests passed!")
