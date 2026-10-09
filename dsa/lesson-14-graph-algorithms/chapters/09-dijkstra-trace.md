# 09 — Dijkstra by hand: the heap trace

> 6-minute read. One careful pass over the whole algorithm.

## The setup

Graph (all directed): `n=4`, source = `0`.

```
        5
   0 ──────► 1          edges: (0,1,5) (0,2,1) (2,1,2)
   │         ▲                    (1,3,1) (2,3,5)
 1 │         │ 2
   ▼         │
   2 ────────┘
   │         5
   └────────► 3 ◄── (also 1→3 weight 1)
```

Goal: fill the distance table. Every entry starts at ∞, `dist[0]=0`.

## Step-by-step — heap on the left, table on the right

```
heap=[(0,0)]
  pop (0,0)      → relax 1: 0+5=5,  2: 0+1=1
                   heap=[(1,2),(5,1)]       dist: [0, 5, 1, ∞]

  pop (1,2)      → 2 final=1. relax 1: 1+2=3 < 5 → update!
                   relax 3: 1+5=6
                   heap=[(3,1),(5,1),(6,3)] dist: [0, 3, 1, 6]

  pop (3,1)      → 1 final=3. relax 3: 3+1=4 < 6 → update!
                   heap=[(4,3),(5,1),(6,3)] dist: [0, 3, 1, 4]

  pop (4,3)      → 3 final=4. no relaxations.
                   heap=[(5,1),(6,3)]

  pop (5,1)      → STALE! dist[1] is 3, not 5 → skip
  pop (6,3)      → STALE! dist[3] is 4, not 6 → skip
                   heap empty. dist = [0, 3, 1, 4]
```

Run it — `dijkstra(4, [(0,1,5),(0,2,1),(2,1,2),(1,3,1),(2,3,5)], 0)`
returns `[0, 3, 1, 4]`. Same table.

## The stale-entry detail — the most-missed line

Vertices get pushed **multiple times** as better distances appear (1 was
pushed at 5, then at 3; 3 at 6, then at 4). The old entries stay in the
heap — they're garbage now. The guard:

```python
if d > dist[v]:
    continue          # this (d, v) pair is outdated — ignore it
```

is what throws them away. Without it you'd relax edges *from a stale
distance* — wrong answers and wasted work.

## Why tracing matters

Every interview "walk me through it" wants exactly this table: pop order,
when each `dist` was updated, and *why* `dist[1]` ended at 3 instead of 5
— because relaxing `2→1` found `1+2` < `5`. The heap makes cheapest-first
automatic; the trace is just bookkeeping.

## Where it's used

Anytime you'd dry-run Dijkstra in a problem: network delay, min-cost
paths. The stale-skip pattern also appears in lazy-deletion heaps
generally.

## Common mistake

Assuming each vertex is popped once. With lazy deletion (pushing instead
of updating in-place), pops can exceed V — that's fine, that's the
design. Don't "optimize" by removing the guard.

## Your turn

In the trace, could `dist[1]` ever have been finalized at 5?

<details><summary>Answer</summary>
Only if (5,1) popped before (1,2) improved it. Heaps pop smallest first,
so (1,2) — cost 1 — always pops first and fixes dist[1] to 3 before the
stale 5 is ever processed. Cheapest-first ordering IS the safety.
</details>

---

**← Prev** [08 — Dijkstra: the idea](08-dijkstra-idea.md) ·
**Next →** [10 — Negative edges break Dijkstra](10-negative-edges.md)
