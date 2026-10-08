"""
SOLUTION: Merge Overlapping Intervals (Easy)
============================================
Sort by start, then sweep: if the interval overlaps the top of `merged`
(start <= its end), extend it with max of ends; else append a new one.
O(n log n) for the sort, O(n) sweep.
"""
def merge(intervals):
    merged = []
    for s, e in sorted(intervals):            # sorted() doesn't mutate caller's list
        if merged and s <= merged[-1][1]:     # overlaps the interval being built
            merged[-1][1] = max(merged[-1][1], e)   # max: nested intervals can't shrink it
        else:
            merged.append([s, e])
    return merged

if __name__ == "__main__":
    assert merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert merge([[1,4],[4,5]]) == [[1,5]]            # touching merges
    assert merge([[1,4],[2,3]]) == [[1,4]]            # nested swallowed
    assert merge([[2,6],[1,3]]) == [[1,6]]            # unsorted input
    assert merge([[5,7]]) == [[5,7]]
    assert merge([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]]
    print("All tests passed!")
