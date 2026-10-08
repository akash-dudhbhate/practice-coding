"""
SOLUTION: Last Stone Weight (Medium)
====================================
Max-heap via negation: store -w, un-negate at pop. Each round pops
the two heaviest; unequal -> push back the (negated) difference.
Loop while >= 2 stones; leftover is the answer (0 if empty).
"""
import heapq


def last_stone_weight(stones):
    h = [-s for s in stones]
    heapq.heapify(h)
    while len(h) >= 2:
        x = -heapq.heappop(h)          # heaviest
        y = -heapq.heappop(h)          # second heaviest
        if x != y:
            heapq.heappush(h, -(x - y))
    return -h[0] if h else 0


if __name__ == "__main__":
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1
    assert last_stone_weight([1]) == 1
    assert last_stone_weight([1, 1]) == 0
    assert last_stone_weight([2, 2]) == 0
    assert last_stone_weight([10, 4, 2, 10]) == 2
    assert last_stone_weight([3, 7, 2]) == 2     # 7&3->4, 4&2->2
    print("All tests passed!")
