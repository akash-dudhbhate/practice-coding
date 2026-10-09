# 13 — The Recipe: Recognize a Graph Problem in 10 Seconds

> 4-minute read. Ties every chapter together.

## The 5 steps

When a problem lands in front of you:

1. **"Connected things" mentioned at all?** → it's a graph — even if
   disguised as a grid, a word list, a course catalog, or a dependency
   list. Friendships, roads, prerequisites, adjacency: all edges.
2. **"Shortest / fewest / minimum steps" on UNWEIGHTED edges?** → **BFS**.
   Levels = distance (ch.07). Weighted? → Dijkstra, lesson 14.
3. **"Any path? / reachable? / count groups? / enumerate all?"** → **DFS**.
   Recursion or stack (ch.09–10).
4. **Grid input with "count regions / spread / fill"?** → grid-as-graph
   (ch.05), flood with DFS or BFS (ch.12).
5. **Say the invariant out loud:** "every vertex processed once, `seen`
   marked at enqueue/push time, O(V + E) time, O(V) space."

## Play it through — three disguised problems

**A.** "Courses have prerequisites; can you finish them all?"
→ Step 1: prerequisites = directed edges. Step 3: "can you?" = cycle
detection = DFS. (This is topological sort — lesson 14.)

**B.** "A fire starts in several cells of a grid and spreads to neighbors
each minute. When is the last cell burned?"
→ Step 4: grid-as-graph. Step 2: "when" = distance = multi-source BFS.

**C.** "How many separate friend groups exist in a class?"
→ Step 1: friendships = undirected edges. Step 3: "count groups" =
components = outer loop + flood, either traversal (ch.12).

## The code skeletons, side by side

```python
from collections import deque
adj = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"],
       "D": ["B", "C", "E"], "E": ["D"]}

# BFS — for "shortest / fewest / minimum steps"
q, seen = deque(["A"]), {"A"}
while q:
    v = q.popleft()                    # oldest first → rings
    for nxt in adj[v]:
        if nxt not in seen:
            seen.add(nxt); q.append(nxt)
print("BFS reached", len(seen), "nodes")          # 5

# DFS — for "any path / all / count / detect" — SAME skeleton, stack
st, seen = ["A"], {"A"}
while st:
    v = st.pop()                       # newest first → dive
    for nxt in adj[v]:
        if nxt not in seen:
            seen.add(nxt); st.append(nxt)
print("DFS reached", len(seen), "nodes")          # 5
```

One data-structure swap separates them — the frontier order IS the
algorithm (ch.11).

## What you now know

You can: draw any "connected things" problem as nodes+edges, store it as a
dict-of-lists, see grids as graphs, ripple out with BFS (and trust it for
shortest paths), dive with DFS recursively or iteratively, keep `seen`
honest, and count components with scan+flood. **That's the lesson.** The
problems in `easy/`→`medium/`→`hard/` drill exactly this.

## Your turn

"Given a list of word pairs `[(w1, w2)]` where w2 can be formed from w1 by
changing one letter, find the fewest changes to turn 'hit' into 'cog'."
Recipe step?

<details><summary>Answer</summary>
Step 1: words are nodes, "one letter apart" is an edge (the classic
word-ladder graph — you don't even need the pairs; generate neighbors by
trying 26 letters per position). Step 2: "fewest changes" on unweighted
edges → **BFS**, dist = number of changes.
</details>

---

**← Prev** [12 — Counting islands](12-counting-islands.md) ·
**Next →** [14 — The pitfall gallery](14-pitfall-gallery.md)
