"""
LESSON 14 — Graph Algorithms
MEDIUM P03 — Component Count via Union-Find
============================================

CONCEPT:
  Lesson 13 counted components by flooding; here edges ARRIVE as a
  list of unions — the streaming version. Union-Find shines: start at
  n sets, each successful union(a,b) merges two sets (count -= 1);
  a union between already-connected vertices is a no-op (that's how
  redundant edges are detected — see hard p03). Final count = answer.

PROBLEM:
  Write `components_after_unions(n, unions) -> int` — the number of
  disjoint sets remaining after applying every pair in `unions`, in
  order. Vertices are 0..n-1. Must use Union-Find (find with path
  compression + union by rank), not a re-flood per union.

TRY THIS INPUT:
  ```python
  print(components_after_unions(6, [(0,1),(1,2),(3,4)]))
  print(components_after_unions(5, []))
  print(components_after_unions(4, [(0,1),(2,3),(1,2)]))
  print(components_after_unions(3, [(0,1)]))
  print(components_after_unions(1, []))
  ```

EXPECTED OUTPUT:
  ```
  3
  5
  1
  2
  1
  ```

CHECK: python3 check.py medium/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
