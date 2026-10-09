# 11 — Kruskal's MST: cheapest edges first, skip cycles

> 5-minute read. Union-Find pays off immediately.

## The idea, plain words

A **minimum spanning tree (MST)**: connect all n vertices with the
cheapest possible set of edges — n−1 edges, no cycles, minimum total
weight. Like laying pipes to connect every house for the least money.

Kruskal's greedy plan, in two lines:

1. **Sort all edges cheapest-first.**
2. Take each edge **unless both ends are already connected** (adding it
   would close a cycle).

And "already connected" is *exactly* what Union-Find answers in ~O(1).
Chapters 06–07 were building to this.

```
edges: 0–1 (1), 1–2 (2), 2–3 (3), 0–3 (4), 1–3 (5)

   0 ──1── 1
   │       │
   4       2
   │       │
   3 ──3── 2      wait — 2–3 weight 3, 1–3 weight 5

take 1 ✓   {0,1}
take 2 ✓   {0,1,2}
take 3 ✓   {0,1,2,3}
skip 4 ✗   0 and 3 already same group — cycle!
skip 5 ✗   same
total = 6, picked = [(0,1,1),(1,2,2),(2,3,3)]
```

## The code — Union-Find from ch.06, reused verbatim

```python
def kruskal(n, edges):
    edges = sorted(edges, key=lambda e: e[2])   # cheapest first
    uf = UnionFind(n)                            # from chapter 06
    total, picked = 0, []
    for a, b, w in edges:
        if uf.union(a, b):          # False = same group = would cycle
            picked.append((a, b, w))
            total += w
    return total, picked

print(kruskal(4, [(0,1,1),(1,2,2),(2,3,3),(0,3,4),(1,3,5)]))
# → (6, [(0, 1, 1), (1, 2, 2), (2, 3, 3)])
```

Sort dominates the cost: **O(E log E)**. The union-find part is
practically free.

## Why it exists

Greedy works because of the **cut property**: the cheapest edge crossing
any "already-built / not-yet-built" split is always safe to include. And
cycle-checking each candidate is what Union-Find does natively —
`union()` returning `False` *is* the cycle test.

## Where it's used

Network design (cables, pipes, roads), cluster analysis, approximation
inside other algorithms, anywhere "connect everything for minimum cost."

## Common mistake

Checking connectivity with BFS inside the loop — O(V+E) per edge →
O(E·(V+E)) total. The whole point of Kruskal's is that Union-Find makes
each check ~O(1). This is the callback: right tool, right question.

## Your turn

Why exactly n−1 edges in the answer, always?

<details><summary>Answer</summary>
A tree on n vertices has exactly n−1 edges: each union merges two groups
into one, and going from n groups to 1 group takes exactly n−1 merges.
`uf.count` literally counts down to 1.
</details>

---

**← Prev** [10 — Negative edges break Dijkstra](10-negative-edges.md) ·
**Next →** [12 — Picking the right tool](12-picking-the-tool.md)
