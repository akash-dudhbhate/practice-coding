"""
SOLUTION: Heap Ops Basics (Easy)
================================
heapify once; then push = heappush, pop = heappop (returns min),
peek = h[0] (reads the min without removing it). Pops come out
ascending — the heap's core promise.
"""
import heapq


def run_heap_ops(nums, ops):
    h = nums[:]
    heapq.heapify(h)
    out = []
    for op in ops:
        if op[0] == "push":
            heapq.heappush(h, op[1])
        elif op[0] == "pop":
            out.append(heapq.heappop(h))
        else:                      # "peek"
            out.append(h[0])
    return out


if __name__ == "__main__":
    assert run_heap_ops([5, 1, 3], [("push", 0), ("pop",), ("peek",), ("pop",)]) == [0, 1, 1]
    assert run_heap_ops([4, 2, 7], [("pop",), ("pop",), ("peek",)]) == [2, 4, 7]
    assert run_heap_ops([], [("push", 3), ("push", 1), ("pop",)]) == [1]
    assert run_heap_ops([9], [("peek",)]) == [9]
    print("All tests passed!")
