"""
SOLUTION: Lomuto Partition (Medium)
============================================
pivot = arr[hi]. Invariant: arr[lo..i] are all <= pivot. Scan j
from lo to hi-1; whenever arr[j] <= pivot, extend the small zone
(i += 1) and swap arr[i] <-> arr[j]. Finish by swapping the
pivot into arr[i+1] — its final sorted position. O(hi - lo)
time, O(1) space. Quicksort = partition + recurse on each side.
"""
def lomuto_partition(arr: list, lo: int, hi: int) -> int:
    pivot = arr[hi]
    i = lo - 1                      # last index known to hold a <= pivot value
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1

if __name__ == "__main__":
    a = [4, 1, 3, 9, 7]
    p = lomuto_partition(a, 0, 4)
    assert p == 3 and a == [4, 1, 3, 7, 9]
    assert all(x <= 7 for x in a[:3]) and all(x >= 7 for x in a[4:])

    b = [3, 1, 2]
    assert lomuto_partition(b, 0, 2) == 1 and b == [1, 2, 3]

    c = [5]
    assert lomuto_partition(c, 0, 0) == 0

    d = [2, 8, 7, 1]
    assert lomuto_partition(d, 0, 3) == 0 and d[0] == 1

    e = [9, 7, 5, 3, 1, 8, 4, 6, 2]
    p = lomuto_partition(e, 2, 7)
    assert e[p] == 6
    assert all(x <= 6 for x in e[2:p]) and all(x >= 6 for x in e[p + 1:8])
    print("All tests passed!")
