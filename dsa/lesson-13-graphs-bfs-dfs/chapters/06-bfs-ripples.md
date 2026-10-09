# 06 — BFS: Ripples on a Pond (layer by layer)

> 6-minute read. The traversal that visits by distance.

## The idea, plain words

Drop a stone in a pond: the ripple hits the nearest water first, then the
next ring out, then the next. **BFS (Breadth-First Search) is that ripple.**

Start at one node. First visit everything **1 hop away**, then everything
**2 hops away**, then 3... Nodes are visited in order of *distance from the
start*.

```
    A — B              ripple from A:
    |   |              ring 0:  A
    C — D — E          ring 1:  B, C     (1 hop away)
                       ring 2:  D        (2 hops)
                       ring 3:  E        (3 hops)
```

## The tool: a queue

The trick that makes rings work is a **queue** — a line at the coffee shop.
First in line, first served. New discoveries join the BACK; we serve from
the FRONT. In Python that's `collections.deque` with `popleft()`.

```python
from collections import deque

def bfs_order(adj, start):
    seen = {start}                # mark when it JOINS the queue (ch.08!)
    queue = deque([start])
    order = []
    while queue:
        v = queue.popleft()       # front of line = oldest = closest
        order.append(v)
        for nxt in adj[v]:
            if nxt not in seen:
                seen.add(nxt)     # mark NOW — not when popped
                queue.append(nxt)
    return order

adj = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"],
       "D": ["B", "C", "E"], "E": ["D"]}
print(bfs_order(adj, "A"))        # ['A', 'B', 'C', 'D', 'E']
```

## Watch it happen — queue trace

Adjacency lists are alphabetical, so each node discovers neighbors in the
order shown above.

```
queue=[A]      pop A → visit A.  new: B, C        queue=[B, C]
queue=[B,C]    pop B → visit B.  A seen; new: D   queue=[C, D]
queue=[C,D]    pop C → visit C.  A, D both seen   queue=[D]
queue=[D]      pop D → visit D.  B, C seen; new E queue=[E]
queue=[E]      pop E → visit E.  D seen           queue=[]  done

visit order: A, B, C, D, E
```

Feel the rule: **whoever entered the queue earliest gets served first** —
so all of ring 1 is emptied before ring 2 is touched. That's what makes it
layer-by-layer and not random wandering.

## Why it exists

Ring order = distance order. BFS is the only traversal where "when I first
see a node" tells you "how far it is." That property is the entire point of
the next chapter.

## Where it's used

Shortest path on unweighted graphs (fewest hops between people, fewest
moves in a puzzle), "everything within k hops" (friend suggestions,
broadcast radius), level-order processing, spreading processes (rotting
oranges — start BFS from ALL sources at once).

## Common mistake

**Using `.pop()` instead of `.popleft()`** — a one-character-class bug that
turns your queue into a stack: now it dives deep instead of rippling out.
You still visit everything, but ring order is destroyed and any "shortest
path" answer is wrong. Queue = `popleft()`. Always.

## Your turn

On our map, run BFS starting at **E** instead of A. What are the rings?

<details><summary>Answer</summary>
Ring 0: E. Ring 1: D (E's only neighbor). Ring 2: B, C. Ring 3: A.
Visit order: E, D, B, C, A — the ripple just starts from the other end.
</details>

---

**← Prev** [05 — Grid as graph](05-grid-as-graph.md) ·
**Next →** [07 — Why BFS = shortest path](07-bfs-shortest-path.md)
