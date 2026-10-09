# 03 — Kahn's algorithm: topo sort by indegree

> 6-minute read. BFS with one extra idea.

## The idea, plain words

A vertex's **indegree** = how many arrows point **into** it = how many
prerequisites it still needs.

Kahn's trick: **a vertex with indegree 0 needs nothing — emit it now.**
Then delete its outgoing edges (each neighbor owes one less prerequisite),
and any neighbor that drops to 0 joins the queue.

It's literally lesson-13 BFS — except you enter the queue when your
indegree hits 0, not when you're first seen.

```
   0 ──► 1 ──► 3        indegree: 0:0  1:1  2:1  3:2
   │           ▲        "0 owes nothing. 3 owes two things."
   └──► 2 ─────┘
```

## The code

```python
from collections import deque

def kahn_order(n, edges):
    adj = {v: [] for v in range(n)}
    indeg = [0] * n
    for a, b in edges:                        # edge a -> b
        adj[a].append(b)
        indeg[b] += 1
    q = deque(v for v in range(n) if indeg[v] == 0)   # free vertices
    order = []
    while q:
        v = q.popleft()
        order.append(v)
        for nxt in adj[v]:
            indeg[nxt] -= 1                   # "delete" edge v->nxt
            if indeg[nxt] == 0:
                q.append(nxt)                 # nxt's deps all emitted
    return order if len(order) == n else []   # leftovers = cycle!
```

## Hand trace — edges `0→1, 0→2, 1→3, 2→3`

```
indeg:   0:0   1:1   2:1   3:2

q=[0]    pop 0 → order=[0];       1:1→0 ✓, 2:1→0 ✓   q=[1,2]
q=[1,2]  pop 1 → order=[0,1];     3:2→1              q=[2]
q=[2]    pop 2 → order=[0,1,2];   3:1→0 ✓            q=[3]
q=[3]    pop 3 → order=[0,1,2,3]                     q=[]
```

Output: **`[0, 1, 2, 3]`** — `[0, 2, 1, 3]` would be equally legal.
(Run it: `kahn_order(4, [(0,1),(0,2),(1,3),(2,3)])` → `[0, 1, 2, 3]`.)

## The free bonus: cycle detection

If the graph has a cycle, the cyclic vertices **never reach indegree 0**
— each is always waiting on another. The queue empties early and
`len(order) < n`. That's why the last line returns `[]` instead of a
broken partial order.

`kahn_order(3, [(0,1),(1,2),(2,0)])` → `[]`. Nobody can start.

## Why it exists

"Emit whoever is currently unblocked" is exactly how a build system or a
student picking courses actually works — greedy, local, and provably
correct on any DAG. O(V + E): each vertex queued once, each edge deleted once.

## Where it's used

Task schedulers, course planners, anything that repeatedly asks "what can
I do *right now*?"

## Common mistake

**Returning the partial order on a cyclic graph.** If you drop the
`len(order) == n` check, you silently return an incomplete "order" and
the leftover vertices — exactly the ones stuck in cycles — vanish. Always
check.

## Your turn

Edges `0→1, 1→2, 0→2` (n=3). What does Kahn's produce?

<details><summary>Answer</summary>
`[0, 1, 2]`. indeg: 0:0, 1:1, 2:2. Pop 0 → 1:0, 2:1. Pop 1 → 2:0.
Pop 2. Done.
</details>

---

**← Prev** [02 — DAGs and topological order](02-dags-and-topo-order.md) ·
**Next →** [04 — Topo sort via DFS](04-topo-sort-dfs.md)
