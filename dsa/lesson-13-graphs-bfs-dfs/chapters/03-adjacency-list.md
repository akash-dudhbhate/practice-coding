# 03 — Storing a Graph: the Adjacency List (the one to master)

> 6-minute read. This is THE data structure of the lesson.

## The idea, plain words

An **adjacency list** is a dict: `node -> list of its neighbors`. That's it.
It's a phone contact list — each person's name maps to the people they can
call.

```
    A — B                       {
    |   |              ──►        "A": ["B", "C"],
    C — D — E                     "B": ["A", "D"],
                                  "C": ["A", "D"],
                                  "D": ["B", "C", "E"],
                                  "E": ["D"],
                              }
```

## Building it from an edge list

Interview problems hand you edges like `[(0,1), (0,2), (1,3)]` plus `n`
nodes. Your first move is almost always this function:

```python
def build_adjacency(n, edges):
    adj = {v: [] for v in range(n)}   # seed EVERY node, even lonely ones
    for a, b in edges:
        adj[a].append(b)              # a — b is TWO arrows:
        adj[b].append(a)              # a→b AND b→a
    return adj

print(build_adjacency(5, [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]))
# {0: [1, 2], 1: [0, 3], 2: [0, 3], 3: [1, 2, 4], 4: [3]}
```

Those five edges draw exactly our map (0=A, 1=B, 2=C, 3=D, 4=E). Run it —
every node appears, and each undirected edge was stored twice, once per
direction.

**Directed graph?** Drop the `adj[b].append(a)` line. That's the only
difference.

## Hand-trace the loop

`edges = [(0,1), (0,2)]`, `n = 3`:

```
adj starts:  {0: [], 1: [], 2: []}
edge (0,1):  adj[0] += 1 → [1];  adj[1] += 0 → [0]
edge (0,2):  adj[0] += 2 → [1,2]; adj[2] += 0 → [0]
result:      {0: [1,2], 1: [0], 2: [0]}
```

## Why it exists

Real graphs are **sparse** — each node touches few others (a person has
~hundreds of friends, not billions of possible ones). The adjacency list
pays memory only for edges that actually exist: **O(V + E)** space. And
"give me all neighbors of v" is instant — it's literally `adj[v]`, which is
the single operation every traversal does constantly.

## Where it's used

- The default representation for BFS, DFS, components — basically every
  graph algorithm in this course.
- `collections.defaultdict(list)` is the shortcut when you don't know `n`
  up front.

## Common mistake

**Two silent killers:**

1. *One-directional edges on an undirected graph* — `adj[a].append(b)` but
   never `adj[b].append(a)`. Now you can walk to B but never back, and
   component counts come out wrong. Undirected = append BOTH ways.
2. *Dropping isolated nodes* — building the dict only from edges skips
   nodes with no edges → `KeyError` mid-traversal, or undercounted
   components. Seed `adj = {v: [] for v in range(n)}` FIRST, then fill.

## Your turn

`build_adjacency(3, [(0,1), (1,2), (0,2)])` — write out the result by hand
before running it.

<details><summary>Answer</summary>
`{0: [1, 2], 1: [0, 2], 2: [1, 0]}` — a triangle. Every node lists the
other two because every edge got stored in both directions.
</details>

---

**← Prev** [02 — Graph words](02-graph-words-made-friendly.md) ·
**Next →** [04 — The adjacency matrix](04-adjacency-matrix.md)
