# 05 — The Grid Is Secretly a Graph (the big unlock)

> 5-minute read. Once you see this, half of "matrix problems" become graph problems.

## The idea, plain words

Every 2-D grid is a graph in disguise:

- **Each cell is a node.**
- **Each cell has up to 4 edges** — to the cells up, down, left, right.

Nobody hands you an edge list. The edges are *computed on the fly*: from
cell `(r, c)` the neighbors are `(r-1, c)`, `(r+1, c)`, `(r, c-1)`,
`(r, c+1)` — as long as they're inside the grid.

```
GRID (1 = land, 0 = water)          THE SAME THING AS A GRAPH

1 1 0                                (0,0) —— (0,1)
0 1 0                                  |        |
0 0 1                                          (1,1)

                                     (2,2)   ← alone: its 4 neighbors
                                               are water or out of bounds
```

Look at that — the grid drew itself as a graph. The land cells form the
exact same shape as our friendship map (a chain of three, plus one lonely
node).

## Computing neighbors in code

```python
grid = [
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
]

def neighbors(r, c, rows, cols):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):   # down up right left
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:           # stay inside!
            yield nr, nc

rows, cols = len(grid), len(grid[0])
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == 1:
            print((r, c), "->", list(neighbors(r, c, rows, cols)))
# (0, 0) -> [(1, 0), (0, 1)]
# (0, 1) -> [(1, 1), (0, 2), (0, 0)]
# (1, 1) -> [(2, 1), (0, 1), (1, 2), (1, 0)]
# (2, 2) -> [(1, 2), (2, 1)]
```

`neighbors` returns every in-bounds candidate — some may be water
(e.g. `(1,0)` under `(0,0)`), which the walking code filters out. For
`(2,2)` ALL four candidates are water or off-grid → it's truly alone.

The bounds check `0 <= nr < rows and 0 <= nc < cols` is what stops you from
walking off the edge of the world.

## Why it exists

Because once a grid is a graph, **every graph tool transfers for free**:
- "Count the islands" = count connected components (ch.12).
- "Fill a region" (paint bucket) = DFS/BFS from a cell.
- "Shortest path through a maze" = BFS where edges are open cells.

No conversion step — you never build an adjacency dict. The `neighbors()`
function IS the adjacency list, computed per cell.

## Where it's used

Islands, flood fill, maze solving, "spread from a source" problems (rotting
oranges = BFS on a grid), board games, Minesweeper reveals, image
segmentation.

## Common mistake

- **Forgetting the bounds check** → `IndexError` (or silently wrapping to
  the wrong row).
- **Diagonal drift** — checking 8 neighbors when the problem says
  4-directional (or vice versa). Read the connectivity rule twice; it
  changes the answer.

## Your turn

In the grid above, how many neighbor *candidates* does cell `(0,0)` produce
before the bounds check, and how many survive it?

<details><summary>Answer</summary>
4 candidates — (1,0), (-1,0), (0,1), (0,-1) — and 2 survive: (-1,0) and
(0,-1) fall off the grid. Corner cells have 2 neighbors, edge cells have 3,
middle cells have 4.
</details>

---

**← Prev** [04 — Adjacency matrix](04-adjacency-matrix.md) ·
**Next →** [06 — BFS: ripples on a pond](06-bfs-ripples.md)
