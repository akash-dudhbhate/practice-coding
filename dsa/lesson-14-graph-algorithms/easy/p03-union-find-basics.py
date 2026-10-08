"""
LESSON 14 — Graph Algorithms
EASY P03 — Union-Find Basics
============================================

CONCEPT:
  Union-Find tracks which vertices share a set while sets keep merging.
  `parent[v]` points toward a set's ROOT; `find(v)` walks to the root
  (with path compression — re-point nodes at the root as you go);
  `union(a,b)` merges two sets by attaching one root under the other
  (by rank: shorter tree under taller). Two vertices are connected iff
  find(a) == find(b). Each successful merge drops the set count by 1.

PROBLEM:
  Write a `UnionFind` class:
    - UnionFind(n): n singleton sets {0}, {1}, ..., {n-1}
    - find(a) -> root of a's set (with path compression)
    - union(a, b) -> merge; return False if already same set, else True
    - same(a, b) -> bool: do a and b share a set?
    - count() -> number of sets currently

TRY THIS INPUT:
  ```python
  uf = UnionFind(5)
  print(uf.same(0, 1))
  print(uf.union(0, 1))
  print(uf.same(0, 1), uf.count())
  print(uf.union(2, 3), uf.union(1, 3))
  print(uf.same(0, 2), uf.count())
  ```

EXPECTED OUTPUT:
  ```
  False
  True
  True 4
  True True
  True 2
  ```

CHECK: python3 check.py easy/p03
"""

# === WRITE YOUR CODE BELOW ===
# TODO: Write your solution from scratch.
