# Lesson 13 — Graphs: BFS & DFS

## What you'll learn
- What a graph is: vertices/edges, directed vs undirected, weighted vs unweighted
- Building an adjacency list (dict of lists) from an edge list — and why it beats a matrix
- BFS with a `deque`: level-by-level order, shortest path in UNWEIGHTED graphs
- DFS recursive + iterative, and why `seen` is the difference between done and infinite
- The grid-as-graph trick: islands/flood-fill are components in disguise

## Lesson

A graph is vertices + edges. Interview input is usually `n` vertices plus an
edge list `[(0,1), (0,2), ...]` — the first move is building the adjacency dict:

```python
adj = {v: [] for v in range(n)}     # isolated vertices exist too!
for a, b in edges:
    adj[a].append(b)                # undirected: append BOTH ways
    adj[b].append(a)                # directed: skip this line
```

### BFS — rings from the source (queue)

```python
from collections import deque

def bfs(adj, start):
    seen = {start}                  # mark at ENQUEUE time
    q = deque([start])
    while q:
        v = q.popleft()             # oldest first = closest first
        for nxt in adj[v]:
            if nxt not in seen:
                seen.add(nxt)
                q.append(nxt)
```

Level 0 = the source, level 1 = everything 1 hop away... so the first time
BFS reaches the target, that level IS the shortest distance (unweighted only!).

### DFS — dive deep, then backtrack (stack)

```python
def dfs(adj, v, seen, out):         # recursive: call stack = the stack
    seen.add(v)
    out.append(v)
    for nxt in adj[v]:
        if nxt not in seen:
            dfs(adj, nxt, seen, out)

def dfs_iter(adj, start):           # iterative: explicit stack
    seen, stack, out = {start}, [start], []
    while stack:
        v = stack.pop()
        out.append(v)
        for nxt in adj[v]:
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return out
```

### Grids are graphs

Each cell is a vertex; neighbors are `(r±1, c)` and `(r, c±1)` inside bounds.
Islands = connected components. Flood = DFS/BFS marking visited by flipping 1→0.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.
Unless stated otherwise, graphs are given as adjacency dicts or `n` + edge
lists of undirected edges, and traversal order follows stored neighbor order.

### Easy (start here)
1. `easy/p01-build-adjacency-list.py` — Write `build_adjacency(n, edges)` returning a dict `vertex -> [neighbors]` for an UNDIRECTED graph. `build_adjacency(4, [(0,1),(0,2),(1,3)])` → `{0:[1,2], 1:[0,3], 2:[0], 3:[1]}`; every vertex in `range(n)` must appear, even with no edges.
2. `easy/p02-bfs-traversal-order.py` — Write `bfs_order(adj, start)` returning the visit order of a queue-based BFS: `{0:[1,2],1:[0,3],2:[0,4,5],3:[1],4:[2],5:[2]}` from `0` → `[0,1,2,3,4,5]`; on a disconnected graph only the start's component is listed.
3. `easy/p03-dfs-traversal-order.py` — Write `dfs_order(adj, start)` returning RECURSIVE preorder (visit, then recurse into neighbors in stored order): the same graph from `0` → `[0,1,3,2,4,5]`.

### Medium
4. `medium/p01-count-components.py` — Write `count_components(n, edges)` counting connected components: `count_components(5, [(0,1),(1,2),(3,4)])` → `2`; `count_components(4, [])` → `4` (isolated vertices count!).
5. `medium/p02-number-of-islands.py` — Write `num_islands(grid)` counting islands of `1`s connected 4-directionally: `[[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]` → `3`; all water → `0`. You may mutate the grid to mark visited.
6. `medium/p03-shortest-path-unweighted.py` — Write `shortest_distance(adj, start, target)` returning the fewest hops via BFS: square graph `0:[1,2],1:[0,3],2:[0,3],3:[1,2]` from `0` to `3` → `2`; unreachable → `-1`; `start == target` → `0`.

### Hard
7. `hard/p01-word-ladder.py` — Write `ladder_length(begin, end, word_list)`: words are vertices; two words are neighbors if they differ by exactly one letter. BFS the implicit graph: `("hit","cog",["hot","dot","dog","lot","log","cog"])` → `5` (`hit→hot→dot→dog→cog`); `end` absent from the list → `0`. Trick: `hot` matches patterns `*ot`, `h*t`, `ho*` — group words by patterns instead of comparing all pairs.
8. `hard/p02-rotting-oranges.py` — Write `oranges_rotting(grid)` where `2`=rotten, `1`=fresh, `0`=empty; every minute rot spreads 4-directionally from ALL rotten cells at once (multi-source BFS). `[[2,1,1],[1,1,0],[0,1,1]]` → `4`; a fresh cell that can never rot → `-1`; no fresh cells → `0`.
9. `hard/p03-clone-graph.py` — Write `clone_graph(node)` deep-copying a graph of `Node(val, neighbors)` objects: every cloned node must be a NEW object (no shared identity) with the same shape. Use DFS/BFS plus a `orig -> clone` hashmap so cycles don't recurse forever. `None` → `None`.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python3 check.py <level>/<pNN>` to test one problem, `python3 check.py all` for everything.
- `python3 check.py solutions` runs the reference solutions; `verify` checks both.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has drills.
- Solutions live in `<level>/solutions/` — look only AFTER trying.
