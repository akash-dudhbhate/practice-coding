"""
SOLUTION: Max Sum of a Fixed Window (Easy)
==========================================
Fixed window — build first window, then slide: subtract leaver, add enterer.
"""
def max_sum_k(nums, k):
    window_sum = sum(nums[:k])
    best = window_sum
    for right in range(k, len(nums)):
        window_sum += nums[right]        # enters on the right
        window_sum -= nums[right - k]    # leaves on the left
        best = max(best, window_sum)
    return best

if __name__ == "__main__":
    assert max_sum_k([2, 1, 5, 1, 3, 2], 3) == 9
    assert max_sum_k([1, 2, 3, 4, 5], 2) == 9
    assert max_sum_k([5], 1) == 5
    assert max_sum_k([-1, -2, -3], 2) == -3   # all-negative works too
    print("All tests passed!")
