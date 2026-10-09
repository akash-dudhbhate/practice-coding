# 02 — DAGs and topological order

> 4-minute read. The "course schedule" idea.

## The idea, plain words

A **DAG** is a **D**irected **A**cyclic **G**raph — arrows, no cycles.

Think **course prerequisites**: "before Lab you need Lecture, before
Lecture you need Intro." Draw each rule as an arrow:

```
   Intro ──► Lecture ──► Lab
     │                    ▲
     └──► Reading ────────┘        "Lab needs Lecture AND Reading first"
```

A **topological sort** answers: *give me an order of the vertices where
every arrow points forward* — every prerequisite comes before the thing
that needs it.

```
One valid order:  Intro  Lecture  Reading  Lab
Also valid:       Intro  Reading  Lecture  Lab     ← order is NOT unique
```

**Not a DAG:**

```
A ──► B ──► C ──► A      ← a cycle: A needs C, C needs B, B needs A.
                           No legal order exists. Impossible schedule.
```

A cycle in a dependency graph means "impossible requirements" — that's
why topo sort doubles as a **cycle detector** (chapter 05).

## In code — first just *check* an order

Before producing an order, here's a tiny verifier — it's the whole
definition in one line:

```python
def is_topo_order(order, edges):
    pos = {v: i for i, v in enumerate(order)}   # where does each v sit?
    return all(pos[a] < pos[b] for a, b in edges)  # every edge points forward?

edges = [(0,1), (0,2), (1,3), (2,3)]     # 0→1, 0→2, 1→3, 2→3
print(is_topo_order([0,1,2,3], edges))   # → True
print(is_topo_order([0,2,1,3], edges))   # → True  (order isn't unique!)
print(is_topo_order([3,0,1,2], edges))   # → False — 3 came before its deps
```

## Why it exists

Real work has prerequisites — you can't compile a module before its
imports, can't take the lab before the lecture, can't run a pipeline step
before its inputs. Topo sort turns "a web of constraints" into "a legal
schedule."

## Where it's used

Build systems (Make, Bazel), course scheduling, package managers picking
install order, spreadsheet recalculation, task pipelines, `git` commit
ordering.

## Common mistake

Trying to topo-sort an **undirected** graph. Every undirected edge means
"a before b AND b before a" — instantly a cycle, instantly meaningless.
Topo sort is for **directed** graphs only.

## Your turn

Graph: `0→2, 1→2, 2→3`. Is `[1, 0, 2, 3]` a valid topo order?

<details><summary>Answer</summary>
Yes. Check every edge points forward: 0@1 < 2@2 ✓, 1@0 < 2@2 ✓,
2@2 < 3@3 ✓. Two sources (0 and 1) can go in either order.
</details>

---

**← Prev** [01 — When BFS/DFS isn't enough](01-when-bfs-dfs-isnt-enough.md) ·
**Next →** [03 — Kahn's algorithm](03-kahns-algorithm.md)
