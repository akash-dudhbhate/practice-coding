# Lesson 14 — Graph Algorithms

## What you'll learn
- Topological sort on a DAG: Kahn's BFS (indegree) and DFS postorder
- Cycle detection in directed graphs — Kahn's leftover vertices ARE the cycle
- Union-Find: `find`/`union`, path compression, union by rank, `count`
- Dijkstra: min-heap relaxation, why greedy works, why negatives break it
- Which tool when: BFS (unweighted) vs Dijkstra (weighted ≥0) vs Union-Find
  (connectivity queries) vs topo sort (dependency ordering)

## Lesson

Lesson 13 gave you traversal. This lesson gives you the three algorithms
built ON TOP of it.

### Topological sort — DAG → legal order (Kahn's)

```python
from collections import deque

adj = {v: [] for v in range(n)}
indeg = [0] * n
for a, b in edges:                    # edge a -> b (a must come first)
    adj[a].append(b); indeg[b] += 1
q = deque(v for v in range(n) if indeg[v] == 0)   # no prereqs = emit now
order = []
while q:
    v = q.popleft(); order.append(v)
    for nxt in adj[v]:
        indeg[nxt] -= 1
        if indeg[nxt] == 0: q.append(nxt)
# len(order) < n  ->  cycle! the leftovers are stuck waiting on each other
```

### Union-Find — connectivity as a structure

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n)); self.rank = [0]*n; self.count = n
    def find(self, v):
        while self.parent[v] != v:
            self.parent[v] = self.parent[self.parent[v]]  # compression
            v = self.parent[v]
        return v
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return False        # same set already
        if self.rank[ra] < self.rank[rb]: ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]: self.rank[ra] += 1
        self.count -= 1
        return True
```

### Dijkstra — weighted shortest path

```python
import heapq
dist = [float("inf")] * n; dist[src] = 0
heap = [(0, src)]
while heap:
    d, v = heapq.heappop(heap)
    if d > dist[v]: continue             # stale entry — skip it
    for nxt, w in adj[v]:
        if d + w < dist[nxt]:
            dist[nxt] = d + w
            heapq.heappush(heap, (d + w, nxt))
```

The heap serves vertices in cheapest-known-first order; once popped, that
distance is final — valid ONLY because all weights are non-negative.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.
Edge lists use pairs `(a, b)` — in topo problems `a → b` means "a before b",
in union-find problems they're undirected connections.

### Easy (start here)
1. `easy/p01-detect-directed-cycle.py` — Write `has_directed_cycle(n, edges)` returning True iff the directed graph has a cycle. `(3, [(0,1),(1,2),(2,0)])` → `True`; `(3, [(0,1),(1,2)])` → `False`; self-loop `(1, [(0,0)])` → `True`. Kahn's leftover check or 3-color DFS — your pick.
2. `easy/p02-topo-sort-small-dag.py` — Write `topo_order(n, edges)` returning ANY valid topological order (every edge points earlier→later in the output). `(4, [(0,1),(1,2),(2,3)])` → `[0,1,2,3]`; `(3, [(0,1),(0,2)])` → 0 first, then 1,2 in either order. Cycle → `[]`.
3. `easy/p03-union-find-basics.py` — Write a `UnionFind` class: `UnionFind(n)` makes n singleton sets; `union(a,b)` merges (returns False if already same set); `find(a)` returns the root; `same(a,b)` returns whether they share a set; `count()` returns the number of sets. After `union(0,1)` on n=5, `same(0,1)` is True and `count()` is 4.

### Medium
4. `medium/p01-kahns-topo-order.py` — Write `kahn_order(n, edges)` implementing Kahn's algorithm specifically: compute indegrees, seed the queue with indegree-0 vertices, decrement on emit. Return the order, or `[]` if a cycle prevents a full ordering: `(4, [(0,1),(0,2),(1,3),(2,3)])` → `[0,1,2,3]` or `[0,2,1,3]`; `(2, [(0,1),(1,0)])` → `[]`.
5. `medium/p02-course-schedule.py` — Write `can_finish(num_courses, prereqs)` where `(a, b)` means "course a needs b first" (edge b→a): `(2, [(1,0)])` → `True`; `(2, [(1,0),(0,1)])` → `False`. This is just "is the prereq graph acyclic?" in disguise.
6. `medium/p03-component-count-union-find.py` — Write `components_after_unions(n, unions)` returning the number of sets after processing each union in order: `(6, [(0,1),(1,2),(3,4)])` → `3`; `(5, [])` → `5`. Must use Union-Find — that's the lesson.

### Hard
7. `hard/p01-dijkstra-shortest-path.py` — Write `dijkstra(n, edges, src)` for DIRECTED weighted edges `(a, b, w)`, returning a list `dist[0..n-1]` (float('inf') for unreachable). `(4, [(0,1,5),(0,2,1),(2,1,2),(1,3,1),(2,3,5)], 0)` → `[0, 3, 1, 4]` — the 0→2→1 detour (3) beats the direct edge (5).
8. `hard/p02-network-delay-time.py` — Write `network_delay_time(times, n, k)`: `times` holds directed edges `(u, v, w)` (u,v are 1-indexed!), a signal leaves node k, and the answer is the time until ALL nodes receive it — the max of shortest times — or -1 if some node is unreachable. `([(2,1,1),(2,3,1),(3,4,1)], 4, 2)` → `2`.
9. `hard/p03-redundant-connection.py` — Write `find_redundant_connection(edges)`: an undirected graph on vertices 1..n with exactly n edges (one too many — it's a tree + 1 edge). Return the LAST edge in input order whose endpoints are already connected. `[(1,2),(1,3),(2,3)]` → `[2,3]`; `[(1,2),(2,3),(3,4),(1,4),(1,5)]` → `[1,4]`. Union-Find: the edge where `union` first fails is the answer.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python3 check.py <level>/<pNN>` to test one problem, `python3 check.py all` for everything.
- `python3 check.py solutions` runs the reference solutions; `verify` checks both.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has drills.
- Solutions live in `<level>/solutions/` — look only AFTER trying.
