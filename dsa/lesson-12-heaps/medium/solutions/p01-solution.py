"""
SOLUTION: K Closest Points (Medium)
===================================
"k smallest by key" = MAX-heap of size k holding the best k so far.
Entries are (-d2, -x, -y) so the heap's top is the WORST kept point —
largest distance first, then largest x, then largest y. A candidate
evicts it iff the candidate's key is lexicographically better —
this makes TIES deterministic too, matching the (d2, x, y) output
ordering. O(n log k), O(k) space.
"""
import heapq


def k_closest(points, k):
    h = []                                       # max-heap via negation
    for x, y in points:
        d2 = x * x + y * y
        key = (-d2, -x, -y)                      # "worse" point = smaller tuple
        if len(h) < k:
            heapq.heappush(h, key)
        elif key > h[0]:                         # strictly better than worst kept
            heapq.heapreplace(h, key)
    out = [[-x, -y] for _, x, y in h]
    out.sort(key=lambda p: (p[0] * p[0] + p[1] * p[1], p[0], p[1]))
    return out


if __name__ == "__main__":
    assert k_closest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert k_closest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
    # dist tie: [1,0] and [0,1] both d2=1 — (x,y) picks [0,1]
    assert k_closest([[0, 0], [1, 0], [0, 1]], 2) == [[0, 0], [0, 1]]
    assert k_closest([[1, 1], [2, 2]], 2) == [[1, 1], [2, 2]]
    assert k_closest([[-5, -5]], 1) == [[-5, -5]]
    print("All tests passed!")
