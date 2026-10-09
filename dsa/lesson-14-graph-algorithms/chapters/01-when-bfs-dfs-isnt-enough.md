# 01 — When plain BFS/DFS isn't enough

> 4-minute read. Sets up the whole lesson.

## The idea, plain words

In lesson 13 you learned **BFS** (explore layer by layer) and **DFS**
(go deep, backtrack). They answer exactly two questions:

- "Is there a path from A to B?"
- "How many **hops** is the shortest path?"

But real problems ask four other questions BFS/DFS can't answer:

| Question | Why BFS/DFS fails | The tool |
|----------|-------------------|----------|
| "In what ORDER should I do tasks with dependencies?" | They visit nodes, they don't produce a legal schedule | **Topological sort** |
| "Is there a cycle in this dependency web?" | Plain `visited` can't tell "back edge" from "already done" | **3-color DFS** / Kahn's leftover check |
| "Are A and B in the same group? Ask me 1000 times while edges arrive" | Re-running BFS per query is way too slow | **Union-Find** |
| "What's the CHEAPEST path when edges have different costs?" | BFS counts hops, not cost | **Dijkstra** |

That's the whole lesson: **four questions, four named algorithms.** Each
one is just BFS/DFS with one extra idea bolted on.

## See BFS give the wrong answer — 30 seconds

```
    0 --5--> 1        BFS says "0→1 is 1 hop — shortest!"
    |        ^
  1 |        | 1      But cost(0→1) = 5, while cost(0→2→1) = 2.
    v        |        Hops ≠ cost.
    2 -------+
```

```python
from collections import deque

def bfs_hops(adj, src, dst):          # lesson-13 BFS, counts HOPS
    dist = {src: 0}
    q = deque([src])
    while q:
        v = q.popleft()
        if v == dst:
            return dist[v]
        for nxt in adj[v]:
            if nxt not in dist:
                dist[nxt] = dist[v] + 1
                q.append(nxt)
    return -1

adj = {0: [1, 2], 1: [], 2: [1]}      # the graph above, weights ignored
print(bfs_hops(adj, 0, 1))            # → 1 hop ... but that hop costs 5!
```

BFS is honest — it truly counts hops. It's just answering a different
question than "cheapest." Chapter 08–09 fix this with a heap.

## Why this framing matters

Every "graph algorithm" in interviews is secretly "BFS/DFS + one trick."
Learn the trick, not a brand-new algorithm, and the names stop being scary.

## Your turn

"Minimum number of flights between two cities, any airline" — BFS or
Dijkstra?

<details><summary>Answer</summary>
BFS. "Number of flights" = hop count, every edge costs the same (1).
Dijkstra would work but wastes a heap where a deque sufficed.
</details>

---

**Next →** [02 — DAGs and topological order](02-dags-and-topo-order.md)
