"""
SOLUTION: Insert Interval (Medium)
==================================
Three explicit phases on the already-sorted disjoint list:
  1) intervals ending before newInterval starts → output as-is
  2) intervals overlapping it → absorb into newInterval (min start, max end)
  3) intervals after → output as-is
O(n), no re-sort needed.
"""
def insert(intervals, newInterval):
    result = []
    i, n = 0, len(intervals)
    start, end = newInterval[0], newInterval[1]

    # phase 1: entirely before the new interval
    while i < n and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    # phase 2: overlapping — grow the new interval to cover them
    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    result.append([start, end])

    # phase 3: entirely after
    result.extend(intervals[i:])
    return result

if __name__ == "__main__":
    assert insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert insert([], [5,7]) == [[5,7]]
    assert insert([[1,5]], [2,7]) == [[1,7]]          # absorbed entirely
    assert insert([[1,5]], [2,3]) == [[1,5]]          # nested inside existing
    assert insert([[5,8]], [1,3]) == [[1,3],[5,8]]    # insert before all
    assert insert([[1,3]], [4,6]) == [[1,3],[4,6]]    # insert after all
    print("All tests passed!")
