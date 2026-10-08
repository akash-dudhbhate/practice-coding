# Lesson 13 — Coding Check

Use this to verify your solutions before asking for a review.

## Easy

### p01-build-adjacency-list.py — Edge list → dict of lists
- [ ] `build_adjacency(4, [(0,1),(0,2),(1,3)])` → `{0:[1,2], 1:[0,3], 2:[0], 3:[1]}`
- [ ] EVERY vertex `0..n-1` is a key — `build_adjacency(3, [])` → `{0:[],1:[],2:[]}`
- [ ] Undirected edges added BOTH ways (`adj[a].append(b)` AND `adj[b].append(a)`)
- [ ] Neighbor order follows edge order — don't sort (the tests expect insertion order)

### p02-bfs-traversal-order.py — Queue BFS visit order
- [ ] `bfs_order(adj, 0)` on the lesson graph → `[0,1,2,3,4,5]`
- [ ] `bfs_order({0:[]}, 0)` → `[0]`; disconnected vertices are NOT visited
- [ ] Uses `collections.deque` + `popleft()` — `list.pop(0)` works but is O(n) per pop
- [ ] `seen.add(nxt)` happens at ENQUEUE time, not when popped (else duplicates pile up)

### p03-dfs-traversal-order.py — Recursive preorder
- [ ] `dfs_order(adj, 0)` on the lesson graph → `[0,1,3,2,4,5]` (dive, not rings!)
- [ ] Neighbors explored in stored list order; `seen` checked before recursing
- [ ] Disconnected graph returns only the start's component
- [ ] The output list is collected across calls (param or nonlocal) — not reset per call

## Medium

### p01-count-components.py — How many blobs?
- [ ] `count_components(5, [(0,1),(1,2),(3,4)])` → `2`
- [ ] `count_components(4, [])` → `4` — every isolated vertex is its own component
- [ ] Loop `for v in range(n)`, run DFS/BFS only when `v not in seen`
- [ ] `count += 1` happens ONCE per flood, not once per visited vertex

### p02-number-of-islands.py — Flood fill on a grid
- [ ] `num_islands([[1,1,0],[0,1,0],[0,0,1]])` → `2`
- [ ] All-water grid → `0`; `[[1]]` → `1`
- [ ] Neighbors = 4 directions `(±1,0),(0,±1)` — NOT diagonals
- [ ] Bounds check `0 <= nr < rows and 0 <= nc < cols` before touching the cell
- [ ] Cells marked visited when PUSHED (flip to 0 / add to set) — not when popped

### p03-shortest-path-unweighted.py — BFS distance
- [ ] Square graph `0→3` → `2`; `start == target` → `0`; unreachable → `-1`
- [ ] Distance stored per vertex (`dist` dict) or enqueued as `(v, d)` tuples
- [ ] It's a QUEUE (`popleft`) — a stack gives a wrong distance on cyclic graphs
- [ ] No re-visits: `seen`/`dist` doubles as the visited set

## Hard

### p01-word-ladder.py — BFS on an implicit graph
- [ ] `("hit","cog",["hot","dot","dog","lot","log","cog"])` → `5`
- [ ] `end` not in `word_list` → `0` (check early, before BFS)
- [ ] Neighbors found via wildcard patterns (`h*t`, `*ot`, `ho*`), not O(N²) pairwise diff
- [ ] Visited words removed/marked — a word can't be used twice in one ladder
- [ ] Answer counts WORDS including both endpoints (levels + 1), not edges

### p02-rotting-oranges.py — Multi-source BFS
- [ ] `[[2,1,1],[1,1,0],[0,1,1]]` → `4`; `[[2,1,1],[0,1,1],[1,0,1]]` → `-1`
- [ ] `[[0,2]]` → `0` (no fresh oranges); `[[1]]` → `-1`; `[[2]]` → `0`
- [ ] ALL initially-rotten cells enqueued BEFORE the loop starts (multi-source)
- [ ] Minutes = BFS levels — incremented once per round, not per cell
- [ ] After BFS, any `1` still left → return `-1` (it could never be reached)

### p03-clone-graph.py — Deep copy with a hashmap
- [ ] Clone of `[[2,4],[1,3],[2,4],[1,3]]` has identical shape, all NEW node objects
- [ ] `clone_graph(None)` → `None`
- [ ] `orig -> clone` dict maps each original to its copy BEFORE recursing into neighbors
- [ ] Neighbors of a clone are the CLONES of the neighbors — not the original objects
- [ ] Cyclic graphs terminate (the hashmap is your `seen` set)

## How to verify

```bash
python3 check.py easy/p01     # one problem
python3 check.py all          # everything
python3 check.py verify       # solutions pass + stubs rejected
```
