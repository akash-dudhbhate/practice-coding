"""
SOLUTION: Count Inversions via Merge Sort (Hard)
============================================
When the merge step picks an element from the RIGHT half while i
elements remain unpicked in the LEFT, that right element is
smaller than ALL of them — every remaining left element is an
inversion with it. Add (len(left) - i) each time that happens.
Same recursion as merge sort, O(n log n).
"""
def count_inversions(arr: list) -> int:
    def sort_and_count(a):
        if len(a) <= 1:
            return a, 0
        mid = len(a) // 2
        left, inv_l = sort_and_count(a[:mid])
        right, inv_r = sort_and_count(a[mid:])
        merged, inv_cross = merge_and_count(left, right)
        return merged, inv_l + inv_r + inv_cross

    def merge_and_count(left, right):
        merged = []
        i = j = inv = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i]); i += 1
            else:
                merged.append(right[j]); j += 1
                inv += len(left) - i   # right[j] < all remaining left[i:]
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv

    _, total = sort_and_count(arr)
    return total

if __name__ == "__main__":
    assert count_inversions([2, 4, 1, 3, 5]) == 3
    assert count_inversions([1, 2, 3]) == 0
    assert count_inversions([3, 2, 1]) == 3
    assert count_inversions([]) == 0
    assert count_inversions([5, 4, 3, 2, 1]) == 10
    assert count_inversions([1, 1, 1]) == 0
    assert count_inversions([8, 4, 2, 1]) == 6
    print("All tests passed!")
