"""
SOLUTION: Sort a Nearly-Sorted Array (Hard)
============================================
Each element is within k of its final spot, so the next output
element is always inside the current k+1-element window. Keep
that window in a min-heap: push until the heap holds k+1 items,
then each subsequent element enters and the smallest leaves into
the output. Drain the heap at the end. O(n log k).
"""
import heapq


def sort_nearly_sorted(arr: list, k: int) -> list:
    out = []
    heap = []
    it = iter(arr)
    for x in it:                        # fill the first window
        heapq.heappush(heap, x)
        if len(heap) > k:
            break
    for x in it:                        # slide: push new, pop smallest
        out.append(heapq.heappushpop(heap, x))
    while heap:
        out.append(heapq.heappop(heap))
    return out

if __name__ == "__main__":
    assert sort_nearly_sorted([6, 5, 3, 2, 8, 10, 9], 3) == [2, 3, 5, 6, 8, 9, 10]
    assert sort_nearly_sorted([2, 1, 3], 1) == [1, 2, 3]
    assert sort_nearly_sorted([], 3) == []
    assert sort_nearly_sorted([1], 1) == [1]
    assert sort_nearly_sorted([10, 9, 8, 7, 6], 4) == [6, 7, 8, 9, 10]
    assert sort_nearly_sorted([3, 2, 1, 5, 4, 7, 6], 2) == [1, 2, 3, 4, 5, 6, 7]
    print("All tests passed!")
