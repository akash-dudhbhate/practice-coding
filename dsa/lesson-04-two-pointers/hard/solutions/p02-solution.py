"""
SOLUTION: Merge Two Sorted Arrays In Place (Hard)
=================================================
Fill nums1's buffer from the back. i reads nums1's real tail, j reads
nums2's tail, w writes at the buffer's end. Larger value goes to w.
Backward writing never overwrites unread data. Leftover nums2 items
(if any) copy over; leftover nums1 items are already in place.
"""
def merge_sorted(nums1: list, m: int, nums2: list, n: int) -> None:
    i, j, w = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[w] = nums1[i]
            i -= 1
        else:
            nums1[w] = nums2[j]
            j -= 1
        w -= 1

if __name__ == "__main__":
    a = [1, 2, 3, 0, 0, 0]
    merge_sorted(a, 3, [2, 5, 6], 3)
    assert a == [1, 2, 2, 3, 5, 6]
    b = [1]
    merge_sorted(b, 1, [], 0)
    assert b == [1]
    c = [0]
    merge_sorted(c, 0, [1], 1)
    assert c == [1]
    d = [4, 5, 6, 0, 0, 0]
    merge_sorted(d, 3, [1, 2, 3], 3)
    assert d == [1, 2, 3, 4, 5, 6]
    print("All tests passed!")
