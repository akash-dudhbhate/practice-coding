# Lesson 14 — Coding Check

Use this to verify your solutions before asking for a review.

## Easy

### p01-detect-directed-cycle.py — Cycle in a directed graph
- [ ] `(3, [(0,1),(1,2),(2,0)])` → `True`; `(3, [(0,1),(1,2)])` → `False`
- [ ] `(1, [(0,0)])` → `True` (self-loop); `(4, [(0,1),(0,2),(1,3),(2,3)])` → `False` (diamond DAG)
- [ ] Kahn's version: `len(order) < n` means cycle — don't skip that check
- [ ] DFS version: needs THREE states (unseen/visiting/done) — a single `visited` set can't tell a back edge from a finished subtree

### p02-topo-sort-small-dag.py — Any valid order
- [ ] `(4, [(0,1),(1,2),(2,3)])` → `[0,1,2,3]`
- [ ] Output is a permutation of `range(n)` — every vertex exactly once
- [ ] For EVERY edge `(a,b)`, position of `a` < position of `b` in your output
- [ ] Cycle → `[]` (e.g., `(3, [(0,1),(1,0),(1,2)])`)

### p03-union-find-basics.py — The UnionFind class
- [ ] `UnionFind(5).count()` → `5` before any unions
- [ ] After `union(0,1)`: `same(0,1)` → `True`, `same(0,2)` → `False`, `count()` → `4`
- [ ] `union` returns `False` when endpoints already share a set
- [ ] Transitivity: after `union(0,1)` + `union(1,2)`, `same(0,2)` → `True`
- [ ] `find` compresses (`parent[v] = parent[parent[v]]` or recursion) and union attaches by rank — not strictly needed for these tests, needed for scale

## Medium

### p01-kahns-topo-order.py — Indegree BFS specifically
- [ ] `(4, [(0,1),(0,2),(1,3),(2,3)])` → a valid order with 0 first, 3 last
- [ ] `(2, [(0,1),(1,0)])` → `[]` (cycle → queue empties early)
- [ ] Queue seeded with ALL indegree-0 vertices at start, not just one
- [ ] `indeg[nxt] -= 1` happens per edge removal; enqueue exactly at `== 0`
- [ ] Return `[]` when `len(order) != n` — never a partial order

### p02-course-schedule.py — Can finish all courses?
- [ ] `(2, [(1,0)])` → `True`; `(2, [(1,0),(0,1)])` → `False`
- [ ] `(4, [(1,0),(2,1),(3,2)])` → `True`; `(1, [])` → `True`
- [ ] Edge direction: `(a,b)` means b→a — flipping it doesn't change the cycle answer but WILL break any order you derive from it
- [ ] It's the same cycle-detection as easy/p01 — reuse the idea

### p03-component-count-union-find.py — Sets after streaming unions
- [ ] `(6, [(0,1),(1,2),(3,4)])` → `3` — {0,1,2}, {3,4}, {5}
- [ ] `(5, [])` → `5`; `(4, [(0,1),(2,3),(1,2)])` → `1` (redundant union doesn't drop count)
- [ ] `count` decrements ONLY on a successful merge (`ra != rb`)
- [ ] Union-Find is required — a re-flood per union would be the lesson-13 answer, not this one's

## Hard

### p01-dijkstra-shortest-path.py — Weighted shortest paths
- [ ] `dijkstra(4, [(0,1,5),(0,2,1),(2,1,2),(1,3,1),(2,3,5)], 0)` → `[0, 3, 1, 4]`
- [ ] Unreachable vertices → `float("inf")`; `src`'s distance is `0`
- [ ] Heap tuples are `(distance, vertex)` — distance FIRST, that's what heapq sorts on
- [ ] Stale-entry guard `if d > dist[v]: continue` before relaxing
- [ ] Edges are DIRECTED here — `adj[a].append((b,w))` only

### p02-network-delay-time.py — Signal propagation
- [ ] `([(2,1,1),(2,3,1),(3,4,1)], 4, 2)` → `2`
- [ ] `([(1,2,1)], 2, 1)` → `1`; `([(1,2,1)], 2, 2)` → `-1`
- [ ] Vertices are 1-INDEXED — convert (e.g., offset by 1) or size arrays `n+1`
- [ ] Answer = MAX over shortest times, not the last-found
- [ ] Any unreachable node → `-1`, not the max of the reachable ones

### p03-redundant-connection.py — The edge that closes a cycle
- [ ] `[(1,2),(1,3),(2,3)]` → `[2,3]`; `[(1,2),(2,3),(3,4),(1,4),(1,5)]` → `[1,4]`
- [ ] `[(1,2),(2,3),(3,1)]` → `[3,1]` (wrap-around cycle)
- [ ] Return the LAST edge in input order where `find(a) == find(b)` — union returns False
- [ ] Vertices are 1-indexed — `UnionFind(n+1)` or shift ids
- [ ] Return the EDGE pair (e.g., `[2,3]`), not the vertices' roots

## How to verify

```bash
python3 check.py easy/p01     # one problem
python3 check.py all          # everything
python3 check.py verify       # solutions pass + stubs rejected
```
