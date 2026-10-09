# 07 — Why Union-Find is nearly O(1)

> 5-minute read. The two tricks inside `find`/`union`.

## The idea, plain words

`find(v)` walks parent pointers up to the root — so cost = **tree
height**. Two tricks keep that height microscopic:

**Union by rank** — attach the *shorter* tree under the *taller* one.
Without it, unions build a linked list:

```
NAIVE — always attach a's root under b's root, union(i, i+1):

  5       parent chain: 0→1→2→3→4→5
  ^
  4       find(0) walks 5 hops = O(n)
  ^
  ...
  ^
  0

SMART — union by rank, same unions:

     0            everyone points at the root
   / | \ \        find(anything) ≤ ~2 hops
  1  2 3 4 5
```

**Path compression** — every `find` re-points nodes straight at the root,
so the tree *flattens itself while you use it*:

```python
self.parent[v] = self.parent[self.parent[v]]   # hop 2 levels per step
```

Each find makes the next find shorter. First `find(3)` in a deep tree
hops a few times; it leaves every node it passed pointing near the root.

## Verified — same unions, both versions

```python
class NaiveUF:                     # NO rank, NO compression
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, v):
        hops = 0
        while self.parent[v] != v:
            v = self.parent[v]; hops += 1
        return v, hops
    def union(self, a, b):
        ra, _ = self.find(a); rb, _ = self.find(b)
        self.parent[ra] = rb       # a's root always under b's root

nuf = NaiveUF(6)
for i in range(5):
    nuf.union(i, i + 1)
print(nuf.parent)        # [1, 2, 3, 4, 5, 5]  — a 5-deep chain!
print(nuf.find(0))       # (5, 5)  — find(0) costs 5 hops
```

The smart version from chapter 06 on the same unions:
`parent = [0,0,0,0,0,0]` — a flat star, every find ~1 hop. Same
operations, wildly different shape.

## How fast is "nearly O(1)"?

Rank + compression together give amortized **O(α(n))** per operation,
where α is the inverse Ackermann function — α(n) ≤ 5 for any n smaller
than the number of atoms in the universe. For every practical purpose:
**constant time.**

## Why it exists

Without rank: chains → O(n) finds. Without compression: trees stay tall
forever. Either alone leaves you with "a linked list with extra steps."
Together: effectively free.

## Where it's used

The optimizations are why Union-Find beats BFS-per-query at scale —
network connectivity, Kruskal's MST (ch.11), percolation simulations.

## Common mistake

Implementing `find` recursively *without* compression and `union`
*without* rank because "it's simpler." It works on n=10 and silently
degrades to O(n) per op on n=100,000 — the classic TLE (time limit
exceeded) surprise.

## Your turn

Why does `union` compare `rank` (height estimate) instead of set *size*?

<details><summary>Answer</summary>
Either works (union-by-size is equally valid!). What matters is
"shorter/smaller goes under taller/bigger" so height grows slowly.
Rank is just the cheapest approximation — no need to maintain exact
sizes.
</details>

---

**← Prev** [06 — Union-Find](06-union-find.md) ·
**Next →** [08 — Dijkstra: the idea](08-dijkstra-idea.md)
