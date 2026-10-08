"""
SOLUTION: Erase Minimum Overlapping Intervals (Medium)
======================================================
Activity selection: minimizing removals == maximizing kept
non-overlapping intervals. Sort by END; greedily keep the
earliest-ending interval that doesn't clash (s >= last_end).
Touching ends don't overlap. O(n log n).
"""
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    intervals = sorted(intervals, key=lambda iv: iv[1])   # earliest END first
    kept, last_end = 0, float("-inf")
    for s, e in intervals:
        if s >= last_end:               # compatible with what we kept
            kept += 1
            last_end = e
    return len(intervals) - kept

if __name__ == "__main__":
    assert erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert erase_overlap_intervals([[1,2],[1,2],[1,2]]) == 2
    assert erase_overlap_intervals([[1,2],[2,3]]) == 0
    assert erase_overlap_intervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) == 2
    assert erase_overlap_intervals([[1,10],[2,3],[4,5]]) == 1   # start-sort would say 2
    assert erase_overlap_intervals([[-52,31],[-73,-26],[82,97],[-65,-11],
                                    [-62,-49],[95,99],[58,95],[-31,49],
                                    [66,98],[-63,2],[30,47],[-40,-26]]) == 7
    assert erase_overlap_intervals([]) == 0
    print("All tests passed!")
