# 12 — Counting Islands = Counting Connected Components

> 6-minute read. The pattern that unlocks a hundred problems.

## The idea, plain words

Put ch.05 and ch.09 together: a grid is a graph, and an **island** is just
a **connected component** — a blob of nodes that can all reach each other.

"Number of islands" = "how many separate blobs of land exist?"

```
grid (1 = land, 0 = water)          the graph hiding inside:

1 1 0                                (0,0) —— (0,1)
0 1 0                       =                 |
0 0 1                                        (1,1)

                                     (2,2)   ← a second component
```

Two blobs → **2 islands.**

## The pattern: scan + flood

```
for every cell:
    if it's unvisited land:
        count += 1                  # found a NEW blob
        flood it (DFS/BFS)          # visit & mark its WHOLE blob
```

The flood touches every cell of one island exactly once; when the scan next
finds land, it must be a different island.

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:          # unvisited land → new island
                count += 1
                stack = [(r, c)]         # flood it: iterative DFS
                grid[r][c] = 0           # mark visited (sink the land)
                while stack:
                    cr, cc = stack.pop()
                    for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                        nr, nc = cr + dr, cc + dc
                        if (0 <= nr < rows and 0 <= nc < cols
                                and grid[nr][nc] == 1):
                            grid[nr][nc] = 0      # mark at PUSH time
                            stack.append((nr, nc))
    return count

grid = [[1, 1, 0],
        [0, 1, 0],
        [0, 0, 1]]
print(num_islands(grid))    # 2
```

## Hand-trace the scan + flood

```
scan (0,0)=1 → ISLAND #1. flood:
    stack=[(0,0)]  sink (0,0)
    pop (0,0): push (0,1)   [(1,0) is water, edges off-grid]
    pop (0,1): push (1,1)   [(0,0) already 0, (0,2) water]
    pop (1,1): all 4 neighbors water or sunk → done
scan continues: every cell is 0 or water...
scan (2,2)=1 → ISLAND #2. flood: just (2,2).
Answer: 2
```

## Two ways to mark "visited" in a grid

1. **Mutate the cell** — write `0` over the `1`. Free memory, the flood
   literally erases the island. Use it when the input is yours to destroy.
2. **A `seen` set of `(r, c)` tuples** — when the input must survive.
   Same idea as ch.08, stored in a set instead of the grid.

## Why it exists

This one pattern — "outer scan, inner flood" — counts components on ANY
graph, not just grids. Given an adjacency dict instead of a grid, the
identical shape works: loop over all nodes, flood from each unvisited one.

## Where it's used

Islands, provinces ("friend circles"), connected regions in images,
counting separate networks/clusters, flood fill tools, Minesweeper reveals.

## Common mistake

- **Marking at pop time** → the same cell gets pushed repeatedly; queues
  balloon (ch.08's rule applies on grids too).
- **Forgetting components can be a single cell** — `(2,2)` above floods
  itself and counts. Never assume a component has 2+ nodes.

## Your turn

`grid = [[1,0,1],[0,1,0],[1,0,1]]` — five isolated land cells, touching
only diagonally. How many islands (4-directional)?

<details><summary>Answer</summary>
5 islands. Diagonals don't connect in 4-directional problems — every 1 is
its own component. (If the problem said 8-directional, it would be 1.)
</details>

---

**← Prev** [11 — BFS vs DFS](11-bfs-vs-dfs.md) ·
**Next →** [13 — The 10-second recipe](13-the-recipe.md)
