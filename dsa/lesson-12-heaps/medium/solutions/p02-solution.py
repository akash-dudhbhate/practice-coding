"""
SOLUTION: Merge K Sorted Lists (Medium)
=======================================
Heap of size k = the frontier: (value, list_idx, elem_idx) per list.
Pop the smallest head, emit it, push that list's next element.
Indices make tuples unique — lists themselves are never compared.
O(N log k).
"""
import heapq


def merge_k_sorted(lists):
    h = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(h)
    out = []
    while h:
        v, i, j = heapq.heappop(h)
        out.append(v)
        if j + 1 < len(lists[i]):
            heapq.heappush(h, (lists[i][j + 1], i, j + 1))
    return out


if __name__ == "__main__":
    assert merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert merge_k_sorted([]) == []
    assert merge_k_sorted([[], [], [1]]) == [1]
    assert merge_k_sorted([[-2, -1, 0], [1], [0, 2]]) == [-2, -1, 0, 0, 1, 2]
    assert merge_k_sorted([[1, 1, 1], [1, 1]]) == [1, 1, 1, 1, 1]
    # bonus: the stdlib one-liner does the same thing
    assert list(heapq.merge([1, 4, 5], [1, 3, 4], [2, 6])) == [1, 1, 2, 3, 4, 4, 5, 6]
    print("All tests passed!")
