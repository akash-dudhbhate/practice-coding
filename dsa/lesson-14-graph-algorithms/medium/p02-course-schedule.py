"""
LESSON 14 — Graph Algorithms
MEDIUM P02 — Course Schedule (Is the Prereq Graph a DAG?)
============================================

CONCEPT:
  Prerequisites form a directed graph; "can I take all courses?" IS
  "is this graph acyclic?" — a cycle of prerequisites (a needs b,
  b needs a) makes both impossible. Pair (a, b) reads "to take a you
  need b first" — edge b -> a. Then run either cycle detector from
  easy/p01: Kahn's leftover check or 3-color DFS.

PROBLEM:
  Write `can_finish(num_courses, prereqs) -> bool`. prereqs hold pairs
  (a, b) = "course a requires course b". True iff every course can
  eventually be taken (the graph is a DAG).

TRY THIS INPUT:
  ```python
  print(can_finish(2, [(1,0)]))
  print(can_finish(2, [(1,0),(0,1)]))
  print(can_finish(4, [(1,0),(2,1),(3,2)]))
  print(can_finish(1, []))
  print(can_finish(3, [(0,1),(1,2),(2,0)]))
  ```

EXPECTED OUTPUT:
  ```
  True
  False
  True
  True
  False
  ```

CHECK: python3 check.py medium/p02
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
