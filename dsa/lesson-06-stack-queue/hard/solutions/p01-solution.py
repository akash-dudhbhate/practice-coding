"""
SOLUTION: Sliding Window Maximum (Hard)
==========================================
Deque of indices whose values are strictly decreasing (front = max).
Each index enters once and leaves once → O(n) total, vs O(n·k) naive.
"""
from collections import deque

def max_sliding_window(nums, k):
    if k <= 0 or not nums:
        return []
    dq = deque()                      # indices; nums[dq] decreasing
    out = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:  # front slid out of the window
            dq.popleft()
        while dq and nums[dq[-1]] <= x:  # smaller = useless forever
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out

if __name__ == "__main__":
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert max_sliding_window([1], 1) == [1]
    assert max_sliding_window([9, 11], 2) == [11]
    assert max_sliding_window([4, 3, 2, 1], 2) == [4, 3, 2]
    assert max_sliding_window([1, 2, 3], 1) == [1, 2, 3]
    assert max_sliding_window([7, 7, 7], 2) == [7, 7]
    assert max_sliding_window([1, 2, 3], 3) == [3]
    print("All tests passed!")
