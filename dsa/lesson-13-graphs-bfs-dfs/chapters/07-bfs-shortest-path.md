# 07 — Why BFS Gives the Shortest Path (level = distance)

> 5-minute read. The reason BFS is famous.

## The idea, plain words

In an **unweighted** graph, every hop costs the same. So "shortest path"
just means "fewest hops." And BFS visits nodes in order of hop count —
that's literally what the rings ARE.

**The rule: the ring number where BFS first touches a node IS its distance
from the start.** When the ripple first reaches E, no shorter path to E can
still be hiding — everything closer was already explored.

```
    A — B              distance from A:
    |   |              A=0   B=1  C=1
    C — D — E          D=2   E=3
```

## Code: track distance instead of just order

Same BFS, but store `dist[node]` = parent's distance + 1:

```python
from collections import deque

def distances(adj, start):
    dist = {start: 0}              # dist doubles as the "seen" set
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for nxt in adj[v]:
            if nxt not in dist:
                dist[nxt] = dist[v] + 1    # parent's dist + one hop
                queue.append(nxt)
    return dist

adj = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"],
       "D": ["B", "C", "E"], "E": ["D"]}
print(distances(adj, "A"))
# {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 3}
```

## Watch the guarantee work — trace to E

```
queue=[A]   dist={A:0}
pop A:  B,C get dist 1              queue=[B,C]    dist={A:0,B:1,C:1}
pop B:  D gets dist 2               queue=[C,D]    dist+=D:2
pop C:  A,D already have dist       queue=[D]
pop D:  E gets dist 3               queue=[E]      dist+=E:3
pop E:  nothing new → done
```

E was first written with distance 3 — could there be a 2-hop path? Only if
some ring-1 node touched E. B and C's neighbors are {A,D} — no E. So 3 is
provably minimal. **BFS checked every shorter path before any longer one.**

## Why it exists (the fine print)

The guarantee is rock-solid — *for unweighted graphs only.* The moment
edges carry costs, hop count ≠ cost: a 3-hop route of 1+1+1 can beat a
1-hop route costing 100. BFS would still crown the 1-hop path "shortest."
Weighted shortest paths need a different algorithm (Dijkstra, lesson 14).

## Where it's used

- Fewest hops between people in a network.
- Fewest moves in a puzzle (sliding tiles, Rubik's-like states).
- Word ladders: minimum mutations between two words.
- Multi-source spread: enqueue ALL sources at once → each cell's dist =
  distance to the NEAREST source (fires, rot, infection).

## Common mistake

Applying BFS-shortest-path to a weighted graph. Read the problem: if edges
have different costs, "shortest" means cheapest *total*, not fewest *hops*.

## Your turn

`distances(adj, "E")` — predict the result dict before running it.

<details><summary>Answer</summary>
`{'E': 0, 'D': 1, 'B': 2, 'C': 2, 'A': 3}` — distances are symmetric in an
undirected graph: E is 3 from A, so A is 3 from E. Same map, opposite end.
</details>

---

**← Prev** [06 — BFS ripples](06-bfs-ripples.md) ·
**Next →** [08 — The visited set](08-the-visited-set.md)
