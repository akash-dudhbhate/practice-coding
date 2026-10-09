# 02 — Graph Words, Made Friendly

> 6-minute read. Eight words, one tiny map.

## The words, in plain language

Interviewers and textbooks throw around scary labels. Each one maps to
something you already know. Same map as last chapter:

```
    A — B
    |   |
    C — D — E
```

| Word | Plain meaning | On the map |
|------|---------------|------------|
| **vertex / node** | a thing | A, B, C, D, E |
| **edge** | a connection | the 5 lines |
| **degree** | how many edges touch a node | D has degree 3, E has degree 1 |
| **path** | a walk along edges, no repeats | `A — C — D — E` is a path |
| **cycle** | a path that returns to its start | `A — B — D — C — A` |
| **connected** | every node can reach every other | yes here — E is far but reachable |
| **component** | a "blob" of connected nodes | this whole map is ONE component |
| **neighbor** | a node one edge away | D's neighbors: B, C, E |

## The two big labels: direction and weight

**Undirected vs directed** — is the edge a two-way street or a one-way arrow?

```
UNDIRECTED (friendship)        DIRECTED (Twitter follow / course prereq)

    A — B                          A → B
    "A and B know each other"      "A follows B; B may not follow back"
```

Two-way street: if A connects to B, B connects to A — same line. One-way
arrow: `A → B` lets you walk A→B but never B→A. Prerequisite courses are
directed (take Math → then Physics, not backwards). Friendships are
undirected.

**Unweighted vs weighted** — does the edge carry a cost?

```
UNWEIGHTED                     WEIGHTED
"connected" = 1 hop            "connected" = it costs something

    A — B                        A —4— B
    cost: count the hops         cost: add the numbers
    (fewest hops wins)           (cheapest total wins)
```

In an unweighted graph every hop costs the same, so "shortest" = fewest
edges. In a weighted graph (flight prices, road distances) a route with more
hops can be *cheaper* — that changes which algorithm you need (ch.07 and
lesson 14).

## Indegree — the directed-graph extra

On a directed graph, each node has an **indegree**: how many arrows point
INTO it. `A → B` gives B an indegree of 1. Used for "how many prerequisites
does this course still need?" — you'll see it again in topological sort
(lesson 14).

## Common mistake

**Confusing "connected" with "directly connected".** A and E are connected
(a path exists) but they are NOT neighbors. "Is there a path?" is a
traversal question — that's what BFS/DFS answer. "Are they neighbors?" is
a one-step lookup.

## Your turn

Add a lonely node `F` to our map — no edges at all.

```
    A — B
    |   |         F   ← nobody connects to F
    C — D — E
```

How many components does the graph have now?

<details><summary>Answer</summary>
2 components: {A, B, C, D, E} and {F} alone. An isolated node is still a
node — and it counts as its own component. (Remember this when we count
islands in ch.12.)
</details>

---

**← Prev** [01 — What is a graph?](01-what-is-a-graph.md) ·
**Next →** [03 — Storing a graph: the adjacency list](03-adjacency-list.md)
