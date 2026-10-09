# 08 — Dijkstra: expand the cheapest frontier

> 6-minute read. BFS with a heap instead of a queue.

## The idea, plain words

BFS asks "whoever arrived first goes next." Dijkstra asks "**whoever is
currently cheapest goes next.**" Swap the deque for a **min-heap** ordered
by distance, and "fewest hops" becomes "lowest total cost."

Think of it like flood-filling a map where roads have tolls: at every
moment you expand the frontier at the *cheapest known* point — because no
undiscovered route can undercut it (all tolls ≥ 0, so detours only add
cost).

```
    0 --5--> 1        BFS hops:  0→1 (1 hop) "wins" — wrong, costs 5.
    |        ^
  1 |        | 1      Dijkstra:  pops 0 → dist 1:5, 2:1
    v        |        pops (1,2) → dist 1 = min(5, 1+1) = 2
    2 -------+        pops (2,1) → dist[1] final = 2
```

The key move is **relaxing** an edge: offer each neighbor
`dist[v] + w` — keep it only if it beats the best we've recorded.

## The code

```python
import heapq

def dijkstra(n, edges, src):
    adj = {v: [] for v in range(n)}
    for a, b, w in edges:                 # directed edge a -w-> b
        adj[a].append((b, w))
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    heap = [(0, src)]                     # (best-known dist, vertex)
    while heap:
        d, v = heapq.heappop(heap)
        if d > dist[v]:
            continue                      # stale entry — skip (ch.09!)
        for nxt, w in adj[v]:
            nd = d + w
            if nd < dist[nxt]:            # RELAX: cheaper route found
                dist[nxt] = nd
                heapq.heappush(heap, (nd, nxt))
    return dist

print(dijkstra(4, [(0,1,5),(0,2,1),(2,1,2),(1,3,1),(2,3,5)], 0))
# → [0, 3, 1, 4]   note dist[1]=3 via 0→2→1, beating the direct 5
```

## Why the greedy choice works

When the heap pops `(d, v)`, `d` is *final*: every other route to v still
in the heap already costs ≥ d, and any undiscovered route would have to
pass through one of those. Non-negative weights mean detours never get
cheaper — so "popped = settled." That's the whole correctness argument.

Complexity: **O((V + E) log V)** time (each push costs log-heap-size),
**O(V + E)** space. Unreachable vertices stay `inf` — a feature, not a bug.

## Where it's used

GPS routing, network latency ("signal propagates at edge-weight speed" —
that's the classic *network delay time* problem), flight itineraries,
game pathfinding (A* is Dijkstra + a heuristic).

## Common mistake

Pushing `(vertex, dist)` instead of `(dist, vertex)`. `heapq` orders by
the **first** tuple element — distance must come first, or your "cheapest
frontier" is sorted by vertex number and returns garbage.

## Your turn

Why does BFS's deque give wrong answers here, exactly?

<details><summary>Answer</summary>
A deque orders by *arrival time* = hop count. A 1-hop edge of weight 100
arrives before a 3-hop path of weight 3. When cost ≠ hop count, queue
order must be by total cost — that's precisely what the heap provides.
</details>

---

**← Prev** [07 — Why Union-Find is fast](07-why-union-find-is-fast.md) ·
**Next →** [09 — Dijkstra: full trace](09-dijkstra-trace.md)
