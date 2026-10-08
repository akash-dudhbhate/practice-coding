"""
SOLUTION: Merge Sort (Medium)
============================================
Split in half, sort each recursively, merge the sorted halves.
T(n) = 2T(n/2) + O(n)  ->  O(n log n) EVERY time — no worst-case
surprise like quicksort. Cost: O(n) extra space for the merged
output. It is also STABLE (equal elements keep input order)
because merge takes from the left on ties.
"""
def merge_sort(arr: list) -> list:
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge_two_sorted(left, right)


def merge_two_sorted(a, b):
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:        # <= on ties: left first -> stable
            merged.append(a[i]); i += 1
        else:
            merged.append(b[j]); j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

if __name__ == "__main__":
    assert merge_sort([5, 2, 4, 1, 3]) == [1, 2, 3, 4, 5]
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([3, -1, 0, -7]) == [-7, -1, 0, 3]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort([4, 4, 1, 4]) == [1, 4, 4, 4]
    print("All tests passed!")
