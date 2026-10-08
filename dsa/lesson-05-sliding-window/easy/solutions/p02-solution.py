"""
SOLUTION: Averages of All Windows (Easy)
==========================================
Fixed window — keep running sum, append sum/k per slide.
"""
def window_averages(nums, k):
    if k > len(nums) or k <= 0:
        return []
    window_sum = sum(nums[:k])
    averages = [window_sum / k]
    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        averages.append(window_sum / k)
    return averages

if __name__ == "__main__":
    assert window_averages([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]
    assert window_averages([5, 5, 5], 3) == [5.0]
    assert window_averages([1, 3, 5, 7, 9], 5) == [5.0]
    assert window_averages([1, 2], 3) == []
    print("All tests passed!")
