"""
LESSON 17 — Greedy & Intervals
EASY P02 — Meeting Rooms: Can Attend All?
============================================

CONCEPT:
  Overlap detection is the simplest use of the sort+sweep pattern.
  After sorting by start, each meeting only needs comparing to the
  PREVIOUS one — if it starts before the previous ends, they clash.
  Touching endpoints ([1,5] then [5,8]) do NOT clash.

PROBLEM:
  Write a function `can_attend_all(intervals: list[list[int]]) -> bool`
  that returns True if a person could attend every meeting (no two
  overlap), False otherwise. Input may be unsorted; an empty or
  single-meeting schedule is always attendable.

TRY THIS INPUT:
  ```python
  print(can_attend_all([[0,30],[5,10],[15,20]]))
  print(can_attend_all([[7,10],[2,4]]))
  print(can_attend_all([[1,5],[5,8],[8,10]]))
  print(can_attend_all([]))
  ```

EXPECTED OUTPUT:
  ```
  False
  True
  True
  True
  ```

CHECK: python3 check.py easy/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
