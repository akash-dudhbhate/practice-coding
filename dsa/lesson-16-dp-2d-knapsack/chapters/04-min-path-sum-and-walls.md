# 04 — Same Grid, New Rules: Costs and Walls

> 6-minute read. Two small twists on chapter 2 — same skeleton, new choice.

## The idea, plain words

Unique paths asked "how many ways?". Two follow-ups appear constantly:

- **Min path sum:** every cell has a toll. Get to the bottom-right paying
  the *least*. Now `dp[r][c]` stores a **cost**, not a count.
- **Paths with obstacles:** some cells are walls. Now `dp[r][c]` is `0` on
  walls — no path can pass through.

The skeleton doesn't move: borders first, each cell reads ↑ and ←.

## Twist 1 — min path sum, traced

Grid (the tolls):

```
 1  3  1
 1  5  1
 4  2  1
```

`dp[r][c]` = cheapest toll total to *reach* `(r,c)`, including its own toll:

```
dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
           this toll   + cheaper of (above, left)
```

**Borders are running totals** — the first row can only arrive from the
left, so it accumulates:

```
row 0:  dp[0][1] = 3 + 1 = 4     dp[0][2] = 1 + 4 = 5
col 0:  dp[1][0] = 1 + 1 = 2     dp[2][0] = 4 + 2 = 6
```

Inside, cell by cell:

```
dp[1][1] = 5 + min(↑4, ←2) = 7       dp[1][2] = 1 + min(↑5, ←7) = 6
dp[2][1] = 2 + min(↑7, ←6) = 8       dp[2][2] = 1 + min(↑6, ←8) = 7
```

```
tolls:           dp (cheapest cost to reach):
 1  3  1          1   4   5
 1  5  1    →     2   7   6
 4  2  1          6   8   7  ← answer: 7
```

The winning route: right, right, down, down → `1+3+1+1+1 = 7`.

## Twist 2 — walls

`1` = wall. A wall cell contributes **nothing** — set `dp[r][c] = 0` and
move on:

```
grid:  0 0 0        dp:    1 1 1
       0 1 0   →           1 0 1    center wall: 0 paths through it
       0 0 0               1 1 2    bottom-right: 2 paths squeeze around
```

Watch out — a wall **on the border** poisons the rest of that border.
`dp[0][2]` after a wall at `dp[0][1]` is `0`: you can't hop over. Seed
borders with "copy the previous cell unless I'm a wall", not plain `1`s.

## The code

```python
def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for c in range(1, n):                        # first row: from the left
        dp[0][c] = dp[0][c - 1] + grid[0][c]
    for r in range(1, m):
        dp[r][0] = dp[r - 1][0] + grid[r][0]     # first col: from above
        for c in range(1, n):
            dp[r][c] = grid[r][c] + min(dp[r - 1][c], dp[r][c - 1])
    return dp[m - 1][n - 1]
```

Verified: `min_path_sum([[1,3,1],[1,5,1],[4,2,1]])` → `7`.

```python
def paths_with_obstacles(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1 if grid[0][0] == 0 else 0
    for c in range(1, n):
        dp[0][c] = dp[0][c - 1] if grid[0][c] == 0 else 0
    for r in range(1, m):
        dp[r][0] = dp[r - 1][0] if grid[r][0] == 0 else 0
        for c in range(1, n):
            dp[r][c] = 0 if grid[r][c] == 1 else dp[r - 1][c] + dp[r][c - 1]
    return dp[m - 1][n - 1]
```

Verified: `paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]])` → `2`.

## Why it exists

Same reason as chapter 2: the route count / cost explodes if you enumerate
paths. The table compresses "all routes" into "best cost so far" per cell.

## Common mistake

Seeding a **min** problem's borders with `0`. A `0` border reads as "free to
enter" — `min(0, real_cost)` picks the fake free path. Counting problems get
`1`-ish borders, min problems get **accumulated real costs**.

## Your turn

In the toll grid, why is `dp[2][2] = 7` and not `6` — which path does it
actually represent?

<details><summary>Answer</summary>
`dp[2][2] = 1 + min(dp[1][2]=6, dp[2][1]=8) = 7`, coming via `dp[1][2]`.
That path is right→right→down→down: `1+3+1+1+1 = 7`. The `8` from the left
would mean paying `4` at the bottom-left — pricier.
</details>

---

**← Prev** [03 — Reading a 2D table](03-reading-a-2d-table.md) ·
**Next →** [05 — Knapsack: take it or leave it](05-knapsack-take-or-skip.md)
