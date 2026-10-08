"""
LESSON 10 — Sorting
MEDIUM P03 — Sort By Multiple Keys (Mixed Directions)
============================================

CONCEPT:
  Sorting by several criteria with DIFFERENT directions can't be
  one ascending tuple. Two tricks: (1) negate numeric keys —
  key=(-score, name) sorts score descending, name ascending;
  (2) exploit STABILITY — sort by the secondary key first, then
  by the primary; Python's sort keeps the existing order of ties.

PROBLEM:
  Write `sort_students(records: list) -> list` where each record
  is a (name, score) tuple. Return a NEW list sorted by score
  DESCENDING; students with equal scores ordered by name
  ASCENDING.

TRY THIS INPUT:
  ```python
  print(sort_students([("bob", 75), ("amy", 90), ("cal", 90), ("dan", 60)]))
  print(sort_students([("zed", 50), ("ann", 50)]))
  ```

EXPECTED OUTPUT:
  ```
  [('amy', 90), ('cal', 90), ('bob', 75), ('dan', 60)]
  [('ann', 50), ('zed', 50)]
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
