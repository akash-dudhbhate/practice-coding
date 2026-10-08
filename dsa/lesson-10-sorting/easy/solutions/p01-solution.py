"""
SOLUTION: Insertion Sort (Easy)
============================================
arr[0..i-1] is always sorted. Take arr[i], shift every bigger
element one slot right, insert into the gap. Worst case O(n^2),
but on nearly-sorted input the inner loop exits almost
immediately -> near O(n). That's why Timsort uses it on runs.
"""
def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]    # shift right
            j -= 1
        arr[j + 1] = key           # drop into the gap
    return arr

if __name__ == "__main__":
    a = [5, 2, 4, 1, 3]
    assert insertion_sort(a) == [1, 2, 3, 4, 5]
    assert a == [1, 2, 3, 4, 5]
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]
    assert insertion_sort([3, -1, 0]) == [-1, 0, 3]
    assert insertion_sort([3, 3, 1]) == [1, 3, 3]
    print("All tests passed!")
