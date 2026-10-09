# 06 — Union-Find: "same group?" in nearly O(1)

> 6-minute read. New topic — connectivity that updates as edges arrive.

## The idea, plain words

Friend groups at a party: two groups merge whenever a friendship links
them. Union-Find tracks "who's in whose group" under repeated merging,
with two operations:

- `find(v)` → the **root** (a representative id) of v's group.
  `find(a) == find(b)` means same group.
- `union(a, b)` → merge a's group and b's group.

The data structure is almost absurdly simple: **`parent[v]` = who v
points to.** A group is a little tree where everyone eventually points
at the root.

```
union(0,1):  0         union(2,3):  0     2      union(1,3):    0
             ^                        ^    ^                    / \
             1                        1    3                   1   2
                                                                ^
                                             find(3): 3→2→0     3
```

## The code

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))     # everyone their own parent
        self.rank = [0] * n              # tree-height estimate (ch.07)
        self.count = n                   # how many groups

    def find(self, v):
        while self.parent[v] != v:
            self.parent[v] = self.parent[self.parent[v]]  # hop 2 levels
            v = self.parent[v]
        return v

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False                 # already same group — redundant!
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra              # shorter tree under taller
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True
```

## Hand trace — n=5, unions `(0,1) (2,3) (1,3)`

```
start:        {0} {1} {2} {3} {4}    count=5
union(0,1):   {0,1} {2} {3} {4}      count=4
union(2,3):   {0,1} {2,3} {4}        count=3
union(1,3):   {0,1,2,3} {4}          count=2     (1's root 0, 3's root 2,
                                                2 joins under 0)
find(0)=0, find(2)=0 → same group ✓
find(4)=4           → different   ✗
```

```python
uf = UnionFind(5)
for a, b in [(0,1), (2,3), (1,3)]:
    uf.union(a, b)
print(uf.count)                # → 2
print(uf.find(0) == uf.find(2))  # → True
print(uf.find(0) == uf.find(4))  # → False
```

## Why it exists

The alternative — "to answer 'are a and b connected?', run BFS" — costs
O(V + E) **per query**. A thousand queries = a thousand BFS runs.
Union-Find preprocesses connectivity as edges arrive, then answers in
nearly O(1). Streaming edges are exactly where BFS dies.

## Where it's used

"Are these already connected?" checks, redundant-edge detection, counting
components as edges stream in, friend-circle queries, Kruskal's MST
(chapter 11), image connected-regions.

## Common mistake

**Skipping `if ra == rb`.** Merging a root into itself creates a self-loop
and decrements `count` spuriously. That early `return False` is
load-bearing — it's also how you detect that an edge would close a cycle.

## Your turn

After unions `(0,1), (1,2)` on n=4: is `union(0,2)` True or False? What
does that tell you about edge `0–2`?

<details><summary>Answer</summary>
False — both already have root 0. The edge is redundant: adding it would
close a cycle in the group. Union-Find doubles as an undirected cycle
detector.
</details>

---

**← Prev** [05 — Detecting cycles](05-cycle-detection.md) ·
**Next →** [07 — Why Union-Find is fast](07-why-union-find-is-fast.md)
