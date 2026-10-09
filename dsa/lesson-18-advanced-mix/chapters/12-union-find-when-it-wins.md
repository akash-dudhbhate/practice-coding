# 12 — Union-Find: When It Beats DFS

> 4-minute read. A 60-second recap of lesson 14 — then the real point.

## The idea, plain words

Union-find tracks **which things are in the same group** as groups
merge. Two operations, both near-O(1):

- `find(x)` → which set is x in? (with *path compression*: everyone on
  the path gets re-pointed straight at the root)
- `union(a,b)` → merge a's and b's sets

```python
n = 6
parent = list(range(n))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]   # path halving — hop by two
        x = parent[x]
    return x

def union(a, b):
    parent[find(a)] = find(b)

edges = [[1, 2], [1, 3], [2, 3]]
for a, b in edges:
    if find(a) == find(b):
        print(f"edge {a}-{b} is redundant — it makes a cycle!")
    else:
        union(a, b)
```

```
edge 2-3 is redundant — it makes a cycle!
```

## Hand-trace

```
union(1,2): {1,2}           union(1,3): {1,2,3}
edge (2,3): find(2)→3, find(3)→3 — SAME root → already connected.
            Adding this edge would make a cycle → it's redundant.
```

Three near-O(1) queries — no graph traversal at all.

## Why it exists — the "when," not the "how"

The decision is about **dynamic connectivity**: edges/groups *arrive
over time*, and you keep answering "are a and b in the same set?" or
"did this edge create a cycle?"

- **Union-find wins** — each new edge/query updates the structure
  incrementally, near-O(1) per op.
- **DFS/BFS wins** — on a *static* graph with a one-shot question
  ("count islands in this fixed grid"). Re-running DFS per streaming
  edge is O(V+E) every time → too slow.

## Where it's used

Redundant-connection detection, provinces-on-a-stream, accounts-merge,
Kruskal's MST — the signature is always "connectivity that keeps
*changing*."

## Common mistake

Reaching for union-find on a fixed grid problem ("count islands") —
DFS is simpler and equally fast there. Conversely, re-running DFS per
streaming edge is the classic TLE trap union-find exists to prevent.

## Your turn

Edges `[[1,2],[2,3],[3,1]]` on nodes 1–3. Which edge is redundant, and
how does union-find know?

<details><summary>Answer</summary>
**`[3,1]`.** After two unions, `find(3)` and `find(1)` share a root —
they're already connected through node 2. Equal roots ⇒ the edge would
close a cycle ⇒ redundant.
</details>

---

**← Prev** [11 — Largest rectangle + circular arrays](11-rectangle-and-circular.md) ·
**Next →** [13 — The clue table + what's next](13-the-clue-table.md)
