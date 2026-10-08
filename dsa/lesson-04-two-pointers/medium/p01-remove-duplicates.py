"""
LESSON 04 — Two Pointers
MEDIUM P01 — Remove Duplicates from Sorted Array (in place)
============================================

CONCEPT:
  Fast/slow pointers moving the same direction: `fast` reads every
  element; `slow` marks where the next UNIQUE value goes. Since input
  is sorted, duplicates are adjacent — keep a value only when it
  differs from the last value written. Answer lives in nums[:slow];
  `slow` is the new length. O(n) time, O(1) space.

PROBLEM:
  Write a function `remove_duplicates(nums: list) -> int`. `nums` is
  sorted ascending. Remove duplicates IN PLACE so the first k elements
  hold the unique values in order, and return k. (Values beyond k are
  ignored.)

TRY THIS INPUT:
  ```python
  a = [1, 1, 2]
  k = remove_duplicates(a)
  print(k, a[:k])
  b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
  k = remove_duplicates(b)
  print(k, b[:k])
  ```

EXPECTED OUTPUT:
  ```
  2 [1, 2]
  5 [0, 1, 2, 3, 4]
  ```

CHECK: python3 check.py medium/p01
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
