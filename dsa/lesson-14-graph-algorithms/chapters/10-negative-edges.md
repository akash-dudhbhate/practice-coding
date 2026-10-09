# 10 — Why negative edges break Dijkstra

> 4-minute read. One concrete counterexample.

## The idea, plain words

Dijkstra's guarantee rests on one promise: **"popped means final."** It
works because every route not yet explored costs *at least* what's in the
heap — non-negative edges can only add.

A negative edge breaks that promise: a route you haven't processed yet
can come back and **undercut** a vertex you already declared final.

## The counterexample

```
   0 ──4──► 1
   │
 5 │            edges: (0,1,4) (0,2,5) (2,1,-3)
   ▼
   2 ──(-3)──► 1

True shortest to 1:  0→2→1 = 5 + (−3) = 2
```

Watch the promise die:

```
heap=[(0,0)]
  pop (0,0) → relax: 1:4, 2:5          heap=[(4,1),(5,2)]
  pop (4,1) → "1 is DONE at cost 4"    ← THE LIE: 1 gets finalized
  pop (5,2) → relax 1: 5 + (−3) = 2    too late — 1 was already declared
```

Any implementation that treats a popped vertex as settled keeps
`dist[1] = 4` — **wrong answer, no crash, no warning.**

```python
import heapq

def dijkstra_settled(n, edges, src):
    adj = {v: [] for v in range(n)}
    for a, b, w in edges:
        adj[a].append((b, w))
    dist = [float("inf")] * n
    dist[src] = 0
    done = set()
    heap = [(0, src)]
    while heap:
        d, v = heapq.heappop(heap)
        if v in done:
            continue
        done.add(v)                     # final — never reconsidered
        for nxt, w in adj[v]:
            if nxt not in done and d + w < dist[nxt]:
                dist[nxt] = d + w
                heapq.heappush(heap, (d + w, nxt))
    return dist

print(dijkstra_settled(3, [(0,1,4),(0,2,5),(2,1,-3)], 0))
# → [0, 4, 5]   WRONG — true answer is [0, 2, 5]
```

## So what *does* handle negative edges?

**Bellman-Ford**: instead of greedily finalizing, it relaxes **every
edge, V−1 times** — improvements ripple outward no matter the order.
Slower: O(V·E) instead of O(E log V) — but correct with negatives, and a
V-th round that still improves anything means a **negative cycle**
(shortest path = −∞, which is its own answer).

Rule of thumb: **non-negative weights → Dijkstra. Any negatives →
Bellman-Ford** (or call out the assumption explicitly).

## Why it exists

The counterexample isn't trivia — it's the exact moment the greedy
invariant ("finalized stays final") provably fails. Knowing *why* tells
you when you can trust Dijkstra: only when edge weights ≥ 0.

## Where it's used

Currency arbitrage, graphs with rebates/penalties, reweighting schemes —
anywhere negative weights are meaningful, Dijkstra is off the table.

## Common mistake

Testing Dijkstra on a negative-edge graph, getting a right-looking answer
(it can self-correct in some cases — our lazy version did!), and
concluding it's safe. It's not a guarantee, it's luck. The promise is
structurally broken; don't rely on it.

## Your turn

`dist[1]` was "final" at 4. What single property of edge `2→1` made that
finalization invalid?

<details><summary>Answer</summary>
Its weight is negative (−3). A vertex (2) popped *after* 1 could still
offer 1 a cheaper route — impossible when all weights ≥ 0, possible the
moment any weight is negative.
</details>

---

**← Prev** [09 — Dijkstra: full trace](09-dijkstra-trace.md) ·
**Next →** [11 — Kruskal's MST](11-kruskal-mst.md)
