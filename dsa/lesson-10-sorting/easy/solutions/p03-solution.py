"""
SOLUTION: Merge Two Sorted Arrays (Easy)
============================================
Two pointers, one output. Always take the smaller front element;
when one list is exhausted, the other tail appends as-is.
O(n + m) — this single subroutine powers merge sort.
"""
def merge_two_sorted(a: list, b: list) -> list:
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])   # at most one of these is non-empty
    merged.extend(b[j:])
    return merged

if __name__ == "__main__":
    assert merge_two_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_two_sorted([], [1]) == [1]
    assert merge_two_sorted([1, 2], []) == [1, 2]
    assert merge_two_sorted([1, 4], [2, 3]) == [1, 2, 3, 4]
    assert merge_two_sorted([1, 1], [1]) == [1, 1, 1]
    assert merge_two_sorted([], []) == []
    print("All tests passed!")
