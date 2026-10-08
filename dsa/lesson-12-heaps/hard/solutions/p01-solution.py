"""
SOLUTION: Median of a Stream (Hard)
===================================
Two heaps: lo = max-heap of lower half (negated), hi = min-heap of
upper half. Route each new value through lo into hi, then rebalance
so len(hi) <= len(lo). Median always lives at the two roots —
O(log n) per element, O(1) per read.
"""
import heapq


def running_medians(nums):
    lo, hi, out = [], [], []          # lo: negated max-heap; hi: min-heap
    for x in nums:
        heapq.heappush(lo, -x)
        heapq.heappush(hi, -heapq.heappop(lo))   # lo's max belongs in hi
        if len(hi) > len(lo):
            heapq.heappush(lo, -heapq.heappop(hi))   # rebalance back
        if len(lo) > len(hi):
            out.append(float(-lo[0]))
        else:
            out.append((-lo[0] + hi[0]) / 2)
    return out


if __name__ == "__main__":
    assert running_medians([1, 2, 3]) == [1.0, 1.5, 2.0]
    assert running_medians([5, 1, 4, 2, 3]) == [5.0, 3.0, 4.0, 3.0, 3.0]
    assert running_medians([]) == []
    assert running_medians([2]) == [2.0]
    assert running_medians([4, 1]) == [4.0, 2.5]
    assert running_medians([3, 3, 3]) == [3.0, 3.0, 3.0]
    assert running_medians([-1, -2]) == [-1.0, -1.5]
    print("All tests passed!")
