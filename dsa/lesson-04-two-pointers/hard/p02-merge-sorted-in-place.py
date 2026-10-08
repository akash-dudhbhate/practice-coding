"""
LESSON 04 — Two Pointers
HARD P02 — Merge Two Sorted Arrays In Place
============================================

CONCEPT:
  nums1 has room at the back (m + n slots, first m filled). Fill from
  the BACK: three pointers — read end of nums1's real data (i = m-1),
  read end of nums2 (j = n-1), write at the buffer's end (w = m+n-1).
  Place the bigger of nums1[i], nums2[j] at w and step left. Writing
  backward never clobbers a value you haven't read yet. O(m+n), O(1)
  space.

PROBLEM:
  Write `merge_sorted(nums1: list, m: int, nums2: list, n: int) -> None`.
  nums1 has length m + n: first m entries are sorted values, the rest
  are 0 placeholders. nums2 has n sorted values. Merge into nums1
  ascending, in place. Return None (mutate nums1).

TRY THIS INPUT:
  ```python
  a = [1, 2, 3, 0, 0, 0]
  merge_sorted(a, 3, [2, 5, 6], 3)
  print(a)
  b = [0]
  merge_sorted(b, 0, [1], 1)
  print(b)
  ```

EXPECTED OUTPUT:
  ```
  [1, 2, 2, 3, 5, 6]
  [1]
  ```

CHECK: python3 check.py hard/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
