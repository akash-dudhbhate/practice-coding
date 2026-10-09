# 11 — BFS or DFS? The Decision Table

> 4-minute read. You've built both tools — now choose.

## The idea, plain words

BFS and DFS both visit every reachable node exactly once — **O(V + E)**,
same cost, same `seen` set, same code skeleton. The only difference is the
order. So the choice is never "which works?" but **"which order answers the
question?"**

```
    A — B              BFS from A:  A, B, C, D, E   (by distance)
    |   |              DFS from A:  A, B, D, C, E   (by diving)
    C — D — E
    (recursive order)
```

## The decision table

| The problem asks... | Use | Why |
|--------------------|-----|-----|
| "shortest path", "fewest hops", "minimum moves" (unweighted) | **BFS** | rings = distance; first touch IS the answer |
| "everything within k steps" | **BFS** | stop after k rings |
| "spread from many sources at once" | **multi-source BFS** | enqueue all sources; dist = nearest source |
| "is there ANY path?" / "what's reachable?" | **either — DFS is shorter** | order doesn't matter; 5 lines of recursion |
| "count the groups / islands / components" | **either** | outer loop + flood; both flood the same blob |
| "does a cycle exist?" | **DFS** | a dive that meets a "seen but still on the current path" node = cycle |
| "enumerate all paths / all arrangements" | **DFS (backtracking)** | dive, record, undo, try next |
| answer lives at the DEEPEST point | **DFS** | depth is where it searches first anyway |

Rule of thumb: **"shortest/minimum" → BFS. "Any/all/count/detect" → DFS.**
When in doubt on a plain traversal, DFS is fewer lines.

## Same skeleton, one-word difference

```python
from collections import deque
adj = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"],
       "D": ["B", "C", "E"], "E": ["D"]}

def bfs(adj, start):
    seen = {start}; q = deque([start]); out = []
    while q:
        v = q.popleft()              # front = OLDEST → ripple outward
        out.append(v)
        for nxt in adj[v]:
            if nxt not in seen:
                seen.add(nxt); q.append(nxt)
    return out

def dfs(adj, start):                 # identical skeleton...
    seen = {start}; st = [start]; out = []
    while st:
        v = st.pop()                 # ...except end = NEWEST → dive
        out.append(v)
        for nxt in adj[v]:
            if nxt not in seen:
                seen.add(nxt); st.append(nxt)
    return out

print(bfs(adj, "A"))   # ['A', 'B', 'C', 'D', 'E']
print(dfs(adj, "A"))   # ['A', 'C', 'D', 'E', 'B']
```

Everything else — the `seen` set, the neighbor loop, marking at push time —
is identical. The frontier data structure IS the algorithm.

## Why it exists

Because interviews don't ask "run BFS." They ask "fewest moves to unlock
the vault" (BFS) or "print all valid combinations" (DFS/backtracking).
Recognizing which is being asked for is most of the problem.

## Common mistake

Using BFS "because it's the safe one" for an enumerate-all-paths problem.
BFS stores whole layers of the frontier — on "all paths" problems the queue
explodes and you still need backtracking logic anyway. Match the tool to
the question, not to comfort.

## Your turn

Problem: "A zombie infects adjacent cells each turn. After how many turns
is the whole grid infected?" — BFS or DFS?

<details><summary>Answer</summary>
BFS — specifically multi-source BFS. Enqueue every zombie cell at once;
the ring number when the last healthy cell turns is the answer. Rings =
turns, exactly like dist = hops in ch.07.
</details>

---

**← Prev** [10 — Iterative DFS](10-iterative-dfs.md) ·
**Next →** [12 — Counting islands](12-counting-islands.md)
