"""
SOLUTION: Kth Largest (Easy)
============================
Size-k MIN-heap of the best k so far; h[0] is the worst kept.
Newcomer beats it -> heapreplace. Answer sits on top at the end.
O(n log k), O(k) space — and it streams.
"""
import heapq


def kth_largest(nums, k):
    h = nums[:k]
    heapq.heapify(h)
    for x in nums[k:]:
        if x > h[0]:
            heapq.heapreplace(h, x)
    return h[0]


if __name__ == "__main__":
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert kth_largest([1], 1) == 1
    assert kth_largest([7, 7, 7], 2) == 7
    assert kth_largest([2, 1], 1) == 2
    assert kth_largest([-1, -5, -3], 2) == -3
    print("All tests passed!")
