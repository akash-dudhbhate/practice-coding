"""
LESSON 10 — Sorting
MEDIUM P02 — Lomuto Partition (Quicksort's Engine)
============================================

CONCEPT:
  Partition: pick a pivot value, rearrange so everything left of
  it is <= pivot and everything right is >= pivot — the pivot
  lands in its FINAL sorted position. Lomuto's scheme: pivot =
  arr[hi]; keep a boundary i where all arr[lo..i] <= pivot; scan
  j, extend the boundary on each small element; finally swap the
  pivot into place. Quicksort = partition + recurse on both sides.

PROBLEM:
  Write `lomuto_partition(arr: list, lo: int, hi: int) -> int`:
  partition arr[lo..hi] IN PLACE using arr[hi] as pivot, and
  return the pivot's final index. After your call, every element
  in arr[lo..p-1] <= arr[p] <= every element in arr[p+1..hi].

TRY THIS INPUT:
  ```python
  a = [4, 1, 3, 9, 7]
  p = lomuto_partition(a, 0, 4)
  print(p, a)          # a[p] == 7, left <= 7 <= right

  b = [3, 1, 2]
  print(lomuto_partition(b, 0, 2), b)
  ```

EXPECTED OUTPUT:
  ```
  3 [4, 1, 3, 7, 9]
  1 [1, 2, 3]
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
