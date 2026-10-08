# lesson-13-graphs-bfs-dfs — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: BFS vs DFS order
```
    0
   / \
  1   2
 /     \
3       4
adj = {0:[1,2], 1:[0,3], 2:[0,4], 3:[1], 4:[2]}
```
From `0`, which is BFS order and which is recursive DFS preorder?

- (A) `[0,1,3,2,4]` and `[0,1,2,3,4]`
- (B) `[0,1,2,3,4]` and `[0,1,3,2,4]`
- (C) identical — both give `[0,1,2,3,4]`

<details><summary>Answer</summary>
**(B)** — BFS does rings: level 1 is `{1,2}`, level 2 is `{3,4}` → `0,1,2,3,4`.
Recursive DFS dives `0→1→3`, hits a dead end, backtracks to `2→4` → `0,1,3,2,4`.
Same vertices, different story. If a test expects one and you wrote the
other, it's silently wrong.
</details>

---

## Check 02: Why a queue, not a stack?
```
queue:  append(right) — popleft(left)
stack:  append(right) — pop(right)
```
BFS pops the OLDEST pending vertex; a stack pops the NEWEST. What property
of "shortest path in unweighted graph" does the stack destroy?

<details><summary>Answer</summary>
**The level guarantee.** BFS only reaches distance d AFTER exhausting
distance d-1, because FIFO serves vertices in arrival order = distance
order. A stack (LIFO) jumps to the most recent discovery and dives —
you can reach the target via a 7-hop detour before ever checking the
2-hop direct route. You still visit everything; you just lose "first
reach = shortest reach."
</details>

---

## Check 03: The forgotten `seen`
```python
def dfs(adj, v, out):
    out.append(v)
    for nxt in adj[v]:
        dfs(adj, nxt, out)
```
On graph `0:[1], 1:[0]` — what happens?

<details><summary>Answer</summary>
**Infinite recursion.** `dfs(0)` calls `dfs(1)` calls `dfs(0)` calls
`dfs(1)`… until RecursionError (~1000 frames). On a cyclic graph, a
visited set isn't an optimization — it's the termination condition.
</details>

---

## Check 04: Enqueue-time vs pop-time marking
```python
adj = {0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]}
seen = {0}; q = deque([0])
# pop 0 → push 1, 2 (both marked NOW)
```
If marking happened at POP time instead of enqueue time, how many times
does vertex `3` get enqueued?

<details><summary>Answer</summary>
**Twice.** When `1` is popped, `3` is unvisited → enqueued. When `2` is
popped next, `3` is STILL unvisited (it hasn't been popped yet) → enqueued
again. `3` then gets processed twice. Correctness survives (the `seen`
check still guards the pop), but the queue does redundant work — and on
denser graphs the duplicates multiply fast. Mark at enqueue.
</details>

---

## Check 05: Grid connectivity
```
1 1 0
0 1 0
1 0 1
```
4-directional islands vs 8-directional (diagonals count) — how many each?

<details><summary>Answer</summary>
**4-dir: 3 islands** — {(0,0),(0,1),(1,1)}, {(2,0)}, {(2,2)}.
**8-dir: 1 island** — (1,1) touches (2,0) diagonally and (2,0)... no wait:
(1,1)-(2,0) diagonal, and (2,2) touches (1,1) diagonal → all connected.
Reading "4-directional" as "8-directional" (or skipping the read) merges
regions that shouldn't merge — always confirm the connectivity rule.
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Adjacency list that loses vertices

```python
def build_adjacency(n, edges):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    return adj
```

**Hint:** `build_adjacency(4, [(0,1)])` returns `{0:[1], 1:[0]}` — where
did vertices 2 and 3 go?

<details><summary>Answer</summary>

**Bug:** vertices only appear if some edge mentions them — isolated
vertices are dropped entirely. Traversals then crash (`adj[v]` → KeyError)
or undercount components.
**Fix:** seed every vertex first, then add edges:
```python
adj = {v: [] for v in range(n)}
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)
return adj
```
</details>

---

## Debug 02 (Medium): BFS that pops the wrong end

```python
def shortest_distance(adj, start, target):
    dist = {start: 0}
    stack = [start]
    while stack:
        v = stack.pop()                     # <- the bug
        if v == target:
            return dist[v]
        for nxt in adj[v]:
            if nxt not in dist:
                dist[nxt] = dist[v] + 1
                stack.append(nxt)
    return -1
```

**Hint:** On `0:[1,2], 1:[0,3], 2:[0,3], 3:[1,2]` this returns 2 for
0→3 — lucky. On `0:[1,2], 1:[0], 2:[0,3], 3:[2]` it returns 2 as well…
but the real shortest is 2 via 0→2→3 while DFS luck varies. Find a case
where the stack overestimates.

<details><summary>Answer</summary>

**Bug:** `stack.pop()` makes it DFS — first-reach is no longer
shortest-reach. Example: `0:[1,3], 1:[0,2], 2:[1,3], 3:[0,2]`, target 3.
Stack pops 3's far neighbor first and dives `0→1→2→3` recording distance
**3**, when 0→3 directly is **1**.
**Fix:** `deque` + `popleft()`:
```python
q = deque([start])
while q:
    v = q.popleft()
    ...
```
</details>

---

## Debug 03 (Hard): Island counter that double-counts

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1
                stack = [(r, c)]
                while stack:
                    cr, cc = stack.pop()
                    grid[cr][cc] = 0              # <- marked at POP time
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = cr+dr, cc+dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            stack.append((nr, nc))
    return count
```

**Hint:** the count is right, but trace the stack on a 2×2 all-ones grid —
how big does it grow?

<details><summary>Answer</summary>

**Bug:** cells are flipped to 0 when POPPED, so the same cell gets pushed
many times before first pop (on a big blob the stack holds O(area)
duplicates and each pop re-scans it). Worse, a cell can be pushed after
it's already zeroed-and-popped → processed twice.
**Fix:** mark at PUSH time:
```python
grid[r][c] = 0
stack = [(r, c)]
while stack:
    cr, cc = stack.pop()
    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        nr, nc = cr+dr, cc+dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
            grid[nr][nc] = 0        # mark NOW
            stack.append((nr, nc))
```
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: One-way undirected edges
```python
# WRONG — you can reach B from A but never A from B
adj[a].append(b)

# CORRECT — undirected means BOTH directions
adj[a].append(b)
adj[b].append(a)
```

## Mistake 02: No `seen` on a cyclic graph
```python
# WRONG — 0→1→0→1→… RecursionError
for nxt in adj[v]:
    dfs(adj, nxt, out)

# CORRECT
for nxt in adj[v]:
    if nxt not in seen:
        dfs(adj, nxt, seen, out)
```

## Mistake 03: Stack where a queue belongs
```python
# WRONG for shortest path — this is DFS, distances lie
v = stack.pop()

# CORRECT — FIFO gives the level-order property
v = queue.popleft()
```

## Mistake 04: Single-source BFS for multi-source spread
```python
# WRONG — rotting from one orange at a time serializes the minutes;
# the answer becomes sum of distances instead of max
for src in rotten_cells:
    minutes += bfs_from(src)

# CORRECT — ALL rotten cells enter the queue at level 0 together;
# minutes = number of BFS levels
q = deque(all_initially_rotten)
```

## Mistake 05: `list.pop(0)` as a queue
```python
# WRONG — pop(0) shifts the whole list: O(n) per pop → O(n²) total
v = mylist.pop(0)

# CORRECT — deque.popleft() is O(1)
from collections import deque
v = q.popleft()
```

## Mistake 06: Clone graph without the orig→clone map
```python
# WRONG — infinite recursion on cycles; also clones shared neighbors
# twice (the copy isn't a faithful clone — diamond shapes get duplicated)
clone.neighbors = [clone_graph(n) for n in node.neighbors]

# CORRECT — memoize BEFORE recursing
mapping[node] = Node(node.val)
mapping[node].neighbors = [clone_graph(n) for n in node.neighbors]
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): DFS with a manual "visited" list
### Before
```python
def dfs_order(adj, start):
    out, visited = [], []
    def helper(v):
        visited.append(v)          # O(n) membership test per edge!
        out.append(v)
        for nxt in adj[v]:
            if nxt not in visited:
                helper(nxt)
    helper(start)
    return out
```
### Problems
1. `nxt not in visited` on a LIST is O(V) — turns O(V+E) into O(V·E)
2. `out` order is fine but `visited` duplicates its job — the set is enough

### After
```python
def dfs_order(adj, start):
    out, seen = [], set()
    def helper(v):
        seen.add(v)                # O(1) membership
        out.append(v)
        for nxt in adj[v]:
            if nxt not in seen:
                helper(nxt)
    helper(start)
    return out
```

---

## Refactor 02 (Medium): Components with a rebuilt-every-time flood
### Before
```python
def count_components(n, edges):
    adj = {v: [] for v in range(n)}
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    count = 0
    visited_all = []
    for v in range(n):
        if v not in visited_all:
            comp = []
            stack = [v]
            while stack:
                x = stack.pop()
                if x not in comp:
                    comp.append(x)
                    stack += adj[x]
            visited_all += comp
            count += 1
    return count
```
### Problems
1. Two linear-scan membership structures (`visited_all`, `comp`) — quadratic
2. Collecting the component's members when only the COUNT is needed
3. `x not in comp` checked at pop instead of marking at push → duplicates

### After
```python
def count_components(n, edges):
    adj = {v: [] for v in range(n)}
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    seen, count = set(), 0
    for v in range(n):
        if v not in seen:
            count += 1
            seen.add(v)
            stack = [v]
            while stack:
                for nxt in adj[stack.pop()]:
                    if nxt not in seen:
                        seen.add(nxt)
                        stack.append(nxt)
    return count
```
One `seen` set, marked at push, no per-component bookkeeping.

---

## Refactor 03 (Hard): Word ladder with O(N²·L) neighbor checks
### Before
```python
def neighbors(word, word_list):
    out = []
    for w in word_list:
        diff = sum(1 for a, b in zip(word, w) if a != b)
        if diff == 1:
            out.append(w)
    return out            # called at EVERY pop: O(N·L) each, O(N²·L) total
```
### Problems
1. Comparing the current word against ALL N words, for every vertex popped
2. The same comparisons repeat across BFS — nothing is shared

### After
```python
from collections import defaultdict, deque

def ladder_length(begin, end, word_list):
    if end not in word_list:
        return 0
    patterns = defaultdict(list)          # "h*t" -> [hit, hot, hat...]
    for w in word_list + [begin]:
        for i in range(len(w)):
            patterns[w[:i] + "*" + w[i+1:]].append(w)
    seen, q = {begin}, deque([(begin, 1)])
    while q:
        w, d = q.popleft()
        if w == end:
            return d
        for i in range(len(w)):
            for nxt in patterns[w[:i] + "*" + w[i+1:]]:
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, d + 1))
    return 0
```
Pattern buckets find all 1-letter neighbors in O(L) lookups per word
instead of O(N·L) comparisons — the difference between ~5k and ~25M ops
on the classic word lists.

---

## Approach Comparison — different ways to solve it

## Problem: Count connected components

### Approach 1: DFS/BFS flood — O(V + E)
```python
seen = set(); count = 0
for v in range(n):
    if v not in seen:
        count += 1
        stack = [v]; seen.add(v)
        while stack:
            for w in adj[stack.pop()]:
                if w not in seen:
                    seen.add(w); stack.append(w)
```
**Pros:** The universal answer — works on any graph, any representation.
**Cons:** O(V+E) space for adjacency + seen.

### Approach 2: Union-Find — O(E·α(V)) (lesson 14 preview!)
```python
uf = UnionFind(n)
for a, b in edges:
    uf.union(a, b)
return uf.count
```
**Pros:** Handles edges arriving ONE AT A TIME (streaming/incremental —
"add edge, recount") where flood would rescan the whole graph per edge.
**Cons:** Can't enumerate paths or orderings; slightly more code.

**Winner:** Flood for "here's the whole graph, count once" (this lesson).
Union-Find when edges arrive incrementally or queries repeat — that's
why lesson 14 exists.

---

## Problem: Shortest path, `start` → `target`

### Approach 1: DFS + track minimum — O(V + E) visits, wrong answer risk
```python
# explore every path, keep min depth — exponential paths on cyclic graphs,
# and "first found" tells you nothing about "shortest"
```
**Pros:** None for this problem. **Cons:** Finds A path, not THE shortest;
must explore everything to be sure. Wrong tool.

### Approach 2: BFS — O(V + E), first-reach = shortest-reach
```python
dist = {start: 0}; q = deque([start])
while q:
    v = q.popleft()
    if v == target: return dist[v]
    ...
```
**Pros:** Optimal AND early-exits the moment target pops. **Cons:** Only
valid when every edge costs the same — weights break it.

**Winner:** Approach 2. "Shortest" + "unweighted" is BFS's entire job
description. Weighted → Dijkstra (lesson 14). All-pairs or negative
edges → different algorithms entirely.
