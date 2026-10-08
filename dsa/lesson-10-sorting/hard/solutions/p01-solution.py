"""
SOLUTION: Counting Sort with Negative Offset (Hard)
============================================
No comparisons at all: count occurrences into an array indexed
by (value - min_value), then walk the counts array in order and
emit each value count[v] times. O(n + k), k = max - min + 1.
Handles negatives ONLY because of the offset — counting_sort
indexed directly by value would crash on -3.
"""
def counting_sort(arr: list) -> list:
    if not arr:
        return []
    lo, hi = min(arr), max(arr)
    counts = [0] * (hi - lo + 1)     # index = value - lo
    for v in arr:
        counts[v - lo] += 1
    out = []
    for offset, c in enumerate(counts):
        out.extend([offset + lo] * c)
    return out

if __name__ == "__main__":
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]
    assert counting_sort([-3, 1, -1, 2]) == [-3, -1, 1, 2]
    assert counting_sort([]) == []
    assert counting_sort([5]) == [5]
    assert counting_sort([-5, -5, -5]) == [-5, -5, -5]
    assert counting_sort([0, -1, 1, 0]) == [-1, 0, 0, 1]
    print("All tests passed!")
