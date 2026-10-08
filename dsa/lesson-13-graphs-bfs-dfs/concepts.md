# Lesson 13 — Concepts Explained (Graphs: BFS & DFS)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What a Graph Is — vertices, edges, directions, weights

**What:** A graph is a set of **vertices** (the "things") joined by **edges** (the "relationships"). That's the whole definition — a city map, a friend network, a dependency list, git history: all graphs.

Two labels matter:

- **Directed vs undirected.** An undirected edge `A—B` means "A and B are connected" — a two-way street. A directed edge `A → B` means "from A you can reach B, but not back" — a one-way street, a prerequisite, a Twitter follow.
- **Weighted vs unweighted.** Unweighted edges just say "connected" — every hop costs 1. Weighted edges carry a cost (distance, time, price) and "shortest" means *cheapest total*, not fewest hops.

```
UNDIRECTED, UNWEIGHTED         DIRECTED, UNWEIGHTED        DIRECTED, WEIGHTED
(friendship graph)             (course prerequisites)      (flight prices)

     A                              A                             A
   /   \                          /   \                         4|   |2
  B-----C                        v     v                         v   v
 "A knows B and C"              B     C                          B->C
 "B knows C too"              "A→B, A→C,                        (cost 1)
                              no way back"
```

More vocabulary you'll need:

- **Path:** a sequence of vertices joined by edges (`A→B→C` is a path).
- **Cycle:** a path that returns to its start (`A→B→C→A`).
- **Connected component:** a maximal blob of vertices that can all reach each other. A graph can have several — disconnected islands of vertices.
- **Degree / indegree:** how many edges touch a vertex / how many arrows point INTO it.

**Why it exists:** Because most real relationships aren't lines (arrays) or hierarchies (trees) — they're *networks*. Anywhere "things connect to things" without a clean parent-child shape, a graph is the honest model. Trees are just the special case: connected, no cycles, exactly one root-ish structure.

**Where it's used:** Social networks (friend suggestions = BFS 2 hops out), maps and routing, package/dependency managers (npm, apt), compilers (call graphs), web crawlers, recommendation systems, distributed systems (which services can reach which).

**What goes wrong without it:**
- Modeling a network as a list or tree forces fake structure onto it — e.g., storing friendships as "each person's friends list inside a tree" makes "are A and D connected through friends?" unanswerable without hacks.
- Treating an undirected edge as one-way (`adj[A].append(B)` but never `adj[B].append(A)`) silently breaks half your traversals — you can walk to B but never back, and components get miscounted.

**Worked example — describing a graph in words:**

```
    0 --- 1
    |     |
    2 --- 3      4

Edges (undirected): (0,1) (0,2) (1,3) (2,3)
Vertex 4 is ALONE — it's its own component.
Components: {0,1,2,3} and {4}  →  2 components.
Cycle: 0→1→3→2→0 exists (a square).
```

---

## Representations — adjacency list vs adjacency matrix

**What:** Two standard ways to store a graph in code:

```python
# Same graph:
#     0 --- 1
#     |     |
#     2 --- 3

# 1) ADJACENCY LIST — dict of lists (the default choice)
adj = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2],
}

# 2) ADJACENCY MATRIX — matrix[v][u] == 1 (or the weight) if edge exists
matrix = [
#    to: 0  1  2  3
        [0, 1, 1, 0],   # from 0
        [1, 0, 0, 1],   # from 1
        [1, 0, 0, 1],   # from 2
        [0, 1, 1, 0],   # from 3
]
```

| Question | Adjacency list | Adjacency matrix |
|----------|---------------|------------------|
| Space | O(V + E) | O(V²) — always |
| "Is u a neighbor of v?" | O(degree) scan | O(1) lookup |
| "List all neighbors of v" | O(degree) — instant | O(V) — scan a whole row |
| Memory at V=10⁵, sparse | fine | 10¹⁰ cells — dead |

**Why it exists:** Real graphs are usually **sparse** — each vertex touches few others (a person has ~hundreds of friends, not billions). A matrix pays V² memory to store mostly zeros. The list pays only for edges that exist.

**Where it's used:** Interview problems hand you an **edge list** like `[(0,1),(0,2),(1,3)]` and `n` vertices — your first move is almost always building the adjacency dict. Matrices appear for dense graphs, tiny graphs, or grid-shaped input where the matrix IS the input already.

**What goes wrong without it:**
- Forgetting isolated vertices: building the dict only from edges that exist drops vertices with no edges → `KeyError` on traversal, or undercounted components. Always seed `adj = {v: [] for v in range(n)}` first.
- One-directional edges on an undirected graph (see above).
- Using a matrix on a sparse million-node graph → memory blows up before the algorithm even starts.

**Worked example — build the list from edges:**

`n = 4`, `edges = [(0,1), (0,2), (1,3)]`, undirected.

```python
def build_adjacency(n, edges):
    adj = {v: [] for v in range(n)}     # every vertex exists, even lonely ones
    for a, b in edges:
        adj[a].append(b)                # a — b is two directed edges:
        adj[b].append(a)                # a→b AND b→a
    return adj
```

Expected output for `build_adjacency(4, [(0,1),(0,2),(1,3)])`:
**`{0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}`**

(Directed graph? Drop the `adj[b].append(a)` line — the only difference.)

---

## BFS — level-by-level with a queue

**What:** Breadth-First Search explores in **rings**: start at a vertex, visit everything 1 hop away, then everything 2 hops away, then 3... It uses a **`deque`** (a queue): pop from the left, append new discoveries on the right.

```
Graph:              BFS from 0 (neighbors in stored order):

    0               Level 0: 0
   / \              Level 1: 1  2
  1   2             Level 2: 3  4
  |   |\
  3   4 5           Visit order: 0, 1, 2, 3, 4, 5
      ^--- (2's neighbors: 4 then 5)
```

```python
from collections import deque

def bfs_order(adj, start):
    seen = {start}                  # mark at ENQUEUE time — see below
    queue = deque([start])
    order = []
    while queue:
        v = queue.popleft()         # left end = oldest = closest
        order.append(v)
        for nxt in adj[v]:
            if nxt not in seen:
                seen.add(nxt)       # mark NOW, not when popped
                queue.append(nxt)
    return order
```

Expected output for `bfs_order(adj, 0)` on the diagram above: **`[0, 1, 2, 3, 4, 5]`**

**Why it exists:** Because the ring-by-ring property gives you something DFS cannot: **the shortest path in an unweighted graph.** The first time BFS pops the target, the number of rings you've expanded IS the distance — there is no shorter route left undiscovered, because everything closer was already explored.

To get distances instead of just order, enqueue `(vertex, dist)` or process the queue level-by-level:

```python
dist = {start: 0}
queue = deque([start])
while queue:
    v = queue.popleft()
    for nxt in adj[v]:
        if nxt not in dist:
            dist[nxt] = dist[v] + 1     # parent's distance + 1 hop
            queue.append(nxt)
```

**Where it's used:** Shortest path on unweighted graphs (fewest hops between people, fewest moves in a puzzle, minimum mutations in word-ladder), "all nodes within k hops" (friend suggestions, network broadcast radius), level-order anything, multi-source spread (rotting oranges — start BFS from ALL sources at once).

**What goes wrong without it:**
- **Using a stack instead of a queue** — `queue.pop()` instead of `popleft()` turns BFS into DFS. You still visit everything, but the "shortest path" guarantee is gone and distances are wrong.
- **Marking `seen` at pop time instead of enqueue time** — a vertex gets enqueued many times before it's popped, so the queue balloons and vertices get processed multiple times (still correct, but wasteful; on cyclic graphs it can explode).
- **Using BFS on a weighted graph** — BFS counts *hops*, not *cost*. A 3-hop route of weight 1+1+1 beats a 1-hop route of weight 100 in BFS's eyes, even though it's cheaper. Weighted shortest paths need Dijkstra (lesson 14).

**Worked example — shortest distance, queue trace:**

Graph `0:[1,2] 1:[0,3] 2:[0,3] 3:[1,2]`, find distance 0 → 3.

```
queue=[(0,0)]  pop (0,0):  enqueue (1,1),(2,1)
queue=[(1,1),(2,1)]  pop (1,1):  0 seen, enqueue (3,2)
queue=[(2,1),(3,2)]  pop (2,1):  0 seen, 3 seen (already enqueued!)
queue=[(3,2)]  pop (3,2):  TARGET at distance 2.
```

Every shortest path (0→1→3 and 0→2→3) has length 2 — BFS finds 2, guaranteed, because it checked ALL length-1 paths before any length-2 path.

---

## DFS — depth-first, recursive and iterative

**What:** Depth-First Search picks one direction and **dives as far as it can** before backtracking — like exploring a maze by always following a corridor to its end, then retracing to the last junction and trying the next corridor. Two equivalent implementations:

```python
# RECURSIVE — the call stack IS the stack
def dfs(adj, v, seen, out):
    seen.add(v)
    out.append(v)
    for nxt in adj[v]:
        if nxt not in seen:
            dfs(adj, nxt, seen, out)

# ITERATIVE — explicit stack, no recursion limit worries
def dfs_iter(adj, start):
    seen = {start}
    stack = [start]
    out = []
    while stack:
        v = stack.pop()             # right end = most recent = dive deeper
        out.append(v)
        for nxt in adj[v]:
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return out
```

Same graph as before (`0:[1,2] 1:[0,3] 2:[0,4,5] 3:[1] 4:[2] 5:[2]`):

```
Recursive preorder from 0:  0, 1, 3, 2, 4, 5
(dive 0→1→3, dead end, back up, 0→2→4, dead end, →5)
```

**Why it exists:** DFS answers different questions than BFS: "is there ANY path?", "what's reachable?", "does a cycle exist?", "enumerate all of X". It's also the natural fit when the answer lives at the *deepest* point (backtracking problems, tree traversals). Recursive DFS is often 5 lines — the shortest correct graph code you'll write.

**Where it's used:** Reachability and component counting, cycle detection, topological sort (lesson 14), maze/puzzle solving, backtracking (every "try all combinations" problem is DFS on an implicit graph), flood fill.

**What goes wrong without it:**
- **Forgetting the `seen` set → infinite loop.** Cyclic graph, no `seen`: `0→1→0→1→0→1…` until RecursionError or a hang. This is THE graph bug. Every vertex must be processed exactly once; `seen` is how you enforce that.
- **Recursion depth:** Python's default limit is ~1000 frames. A path graph of 2000 vertices crashes recursive DFS — convert to the iterative stack version.
- **Expecting DFS order to match BFS order** — they're both "traverse everything" but produce different sequences; tests that assume one and run the other are silently wrong.

**Worked example — iterative stack trace** on `0:[1,2] 1:[0,3] 2:[0,4] 3:[1] 4:[2]`:

```
stack=[0]  pop 0 → seen={0}, push 1,2        stack=[1,2]
pop 2 → seen={0,2}, push 4                   stack=[1,4]
pop 4 → seen={0,2,4} (2 seen)                stack=[1]
pop 1 → seen={0,1,2,4}, push 3               stack=[3]
pop 3 → seen={0,1,2,3,4} (1 seen)            stack=[]
out = [0, 2, 4, 1, 3]
```

Note the iterative order differs from recursive (stack pops the LAST pushed neighbor first). Both are valid DFS — just don't expect identical orderings.

---

## The Grid-as-Graph Trick — islands are graphs in disguise

**What:** A 2-D grid is secretly a graph. Each cell is a vertex; each cell has up to 4 edges (up/down/left/right) to its in-bounds neighbors. "Count the islands" IS "count connected components." "Flood fill" IS "DFS/BFS from a cell."

```python
grid = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
]
# cells holding 1: (0,0), (0,1), (1,1), (2,2)
# edges: (0,0)-(0,1), (0,1)-(1,1)   — no explicit edge list needed!
# components: {(0,0),(0,1),(1,1)} and {(2,2)}  →  2 islands
```

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:           # found an unvisited island
                count += 1
                stack = [(r, c)]          # sink it: DFS flood
                grid[r][c] = 0            # mark visited in place
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            stack.append((nr, nc))
    return count
```

Expected output for the grid above: **`2`**

**Why it exists:** Because once you see the grid IS a graph, every traversal tool transfers for free — no conversion needed. The neighbors aren't stored anywhere; they're *computed* on the fly from `r±1, c±1` with a bounds check. That's the trick: **implicit edges.**

**Where it's used:** Islands, flood fill (paint-bucket tool), maze solving, "spread from a source" problems (rotting oranges = BFS on a grid), board games, image segmentation, minesweeper-style reveals.

**What goes wrong without it:**
- Forgetting the bounds check → `IndexError` or silently wrapping onto the wrong row.
- Not marking visited → the flood revisits (0,0)→(0,1)→(0,0)→… forever. Mutating the cell to 0 is a cheap visited set (saves memory); if the input can't be mutated, use a `seen` set of `(r,c)` tuples.
- Marking a cell visited when it's POPPED instead of when it's PUSHED → the same cell gets pushed many times (queues balloon).
- Diagonal drift: checking 8 neighbors when the problem says 4-directional (or vice versa) — read the problem's connectivity rule twice.

**Worked example — island count walkthrough** on the grid above:

```
scan (0,0)=1: island #1. flood: (0,0)→(0,1)→(1,1). all become 0.
scan (0,1),(0,2),(1,0),(1,1),(1,2): all 0 or water — nothing.
scan (2,2)=1: island #2. flood: just (2,2).
Answer: 2.
```

---

## The Recipe — recognize it in 10 seconds

1. **"Connected things" mentioned at all?** → it's a graph, even if disguised as a grid, a word list, or a dependency list.
2. **"Shortest/fewest/minimum steps" on UNWEIGHTED edges?** → BFS. Levels = distance.
3. **"Any path? / reachable? / count groups? / enumerate all?"** → DFS. Recursion or stack.
4. **Grid input with "count regions/spread/fill"?** → grid-as-graph, flood with DFS or BFS.
5. **Say the invariant out loud:** "Every vertex processed once, `seen` marked at enqueue/push time, O(V + E) time, O(V) space."

---

## The Pitfall Gallery — five ways graph code goes wrong

**1. No `seen` set → infinite recursion.**
```python
# WRONG — cycles forever on any cyclic graph
def dfs(adj, v, out):
    out.append(v)
    for nxt in adj[v]:
        dfs(adj, nxt, out)
# CORRECT — guard at entry
def dfs(adj, v, seen, out):
    seen.add(v)
    out.append(v)
    for nxt in adj[v]:
        if nxt not in seen:
            dfs(adj, nxt, seen, out)
```

**2. Marking `seen` at pop time (BFS).**
Enqueue-time marking means each vertex enters the queue ONCE. Pop-time marking lets duplicates pile up — correctness survives, complexity doesn't.

**3. One-directional edges on an undirected graph.**
`adj[a].append(b)` without `adj[b].append(a)` — your traversal can go but never return, and component counts come out wrong.

**4. Dropping isolated vertices.**
Build `adj` from `range(n)` FIRST, then fill from edges. Vertices with no edges are still vertices — they count as components and can still be DFS starts.

**5. Asking BFS for weighted shortest paths.**
BFS minimizes *hop count*, not *cost*. The moment edges have weights, the queue-by-levels argument breaks — that's lesson 14 (Dijkstra).

**Edge cases to always test:** empty graph / empty edge list, single vertex, disconnected graph (components!), self-loops `(a,a)`, a vertex pointing at itself in a grid flood, start == target in shortest path (answer: 0).
