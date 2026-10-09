# 13 — The pitfall gallery: five ways these go wrong

> 5-minute read. Review chapter — every bug in one place.

## 1. Kahn's: returning a partial order on a cyclic graph

```python
# WRONG — silently returns an incomplete "order"
return order
# CORRECT — leftover vertices mean a cycle; there IS no valid order
return order if len(order) == n else []
```

## 2. DFS cycle check without three colors

A single `visited` set can't distinguish a back edge (cycle!) from an
edge to a finished vertex (legal — see the diamond in ch.05). Use
`state[v] ∈ {unseen, visiting, done}`; only `visiting` means cycle.

## 3. Union-Find: skipping `if ra == rb`

Merging a root into itself creates a self-loop at the root and decrements
`count` spuriously. The early return is load-bearing — it's also how you
detect redundant edges.

## 4. Dijkstra: no stale-entry guard

```python
# WRONG — processes outdated (dist, v) pairs; may relax with stale d
d, v = heapq.heappop(heap)
for nxt, w in adj[v]: ...
# CORRECT
d, v = heapq.heappop(heap)
if d > dist[v]:
    continue
for nxt, w in adj[v]: ...
```

## 5. Dijkstra on negative edges

Greedy finalization assumes costs only grow. A `−5` edge can invalidate
an already-"final" distance (ch.10). Negatives → Bellman-Ford — or state
the assumption out loud.

## Edge cases to always test

- **Empty edge list** — topo = any order; union-find = n separate sets.
- **Self-loop** `(a,a)` — instant cycle.
- **Unreachable vertex in Dijkstra** — `dist` stays `inf`; that's a
  correct answer, not a bug.
- **Single vertex, no edges.**
- **"Already connected" union** — must return `False`, `count` unchanged.

## What you now know

You can: spot when BFS/DFS isn't enough · produce a topo order two ways
(Kahn's by indegree, DFS postorder-reversed) · detect directed cycles
with three colors · merge-and-query groups in ~O(1) with Union-Find ·
trace Dijkstra's heap and distance table · explain exactly why negative
edges break it · build an MST with Kruskal · and pick the right tool from
the question's *shape*.

**That's the whole lesson.** The problems in `easy/` → `medium/` →
`hard/` now drill exactly this — and `concepts-reference.md` keeps the
full write-up as a lookup doc.

## Your turn

Without looking back: what are the *two* lines of defense that keep a
lazy-heap Dijkstra correct on non-negative weights?

<details><summary>Answer</summary>
1. The heap always pops the cheapest known distance first, so a vertex's
distance is final at pop time. 2. `if d > dist[v]: continue` discards
stale entries left behind by later improvements. Drop either and the
invariant dies.
</details>

---

**← Prev** [12 — Picking the right tool](12-picking-the-tool.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/` next.
