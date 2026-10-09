# 02 — Unique Paths: Your First 2D Table

> 6-minute read. The gentlest 2D DP there is — trace it with me.

## The idea, plain words

A robot sits on the **top-left** corner of a grid. It can only move **right**
or **down**. How many different routes reach the **bottom-right** corner?

Real-life version: **walking city blocks.** If you can only walk east or
south, how many ways to cross a neighborhood?

Here's the one insight that solves the whole problem:

> To arrive at a cell, you must have come from the cell **above** it
> or the cell **left** of it. Those are the only two last steps possible.

So: `paths(cell) = paths(above) + paths(left)`.

## Fill the 3×3 by hand — slow motion

`dp[r][c]` = number of ways to reach cell `(r, c)`.

**Borders first.** First row can only be reached by walking right — one way
each. First column, only by walking down — one way each:

```
        c=0  c=1  c=2
r=0   [  1    1    1  ]   ← all 1s: only one way to get here
r=1   [  1    ?    ?  ]
r=2   [  1    ?    ?  ]
```

Now fill inside, top-left → bottom-right. Each cell asks its two neighbors:

```
dp[1][1]:        dp[1][2]:
  ↓ 1              ↓ 1
  1 → [2]          2 → [3]
  = 1 + 1          = 1 + 2
                     (above=1, left=2)
```

```
        c=0  c=1  c=2
r=0   [  1    1    1  ]
r=1   [  1    2    3  ]   dp[1][2] = 1 (above) + 2 (left) = 3
r=2   [  1    ?    ?  ]
```

Bottom row, same move:

```
dp[2][1] = 1 + 2 = 3       dp[2][2] = 3 + 3 = 6
        ↓ 1                    ↓ 3
        2 → 3                  3 → 6
```

```
final table:                Answer: dp[2][2] = 6 paths
 1   1   1
 1   2   3
 1   3   6  ← bottom-right
```

You just filled your first 2D DP table. Notice: every cell only ever reads
**up** and **left** — cells that are already done. That's the whole pattern.

## The code — shorter than the trace

```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]     # borders seeded: first row/col = 1
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]   # up + left
    return dp[m - 1][n - 1]
```

Verified outputs: `unique_paths(3, 3)` → `6` · `unique_paths(3, 7)` → `28` ·
`unique_paths(1, 1)` → `1`.

Fun fact: this table is Pascal's triangle tilted. You don't need the math —
the DP already knows it.

## Why it exists

Counting paths by brute force means listing every right/down sequence —
that's an exponential number of routes on big grids. The table reuses each
cell's answer: a 30×30 grid takes 900 cell-fills instead of millions of
route-listings.

## Where it's used

- Robot/game movement on grids.
- The skeleton for **everything else in this lesson** — `dp[r][c]` reading
  `dp[r-1][c]` and `dp[r][c-1]` is THE shape. Later chapters just swap what
  the cell stores (cost, boolean, length) and what the choice is.

## Common mistake

Forgetting that the first row and column are **all 1s** — one forced path.
If you leave them `0`, the whole inside sums to `0`. Borders aren't
decoration; they're the base case doing real work.

## Your turn

Hand-fill a 4×4 grid (first row/col all 1s, then up+left). What's
`unique_paths(4, 4)`?

<details><summary>Answer</summary>
```
1  1  1  1
1  2  3  4
1  3  6 10
1  4 10 20
```
**20.** Check with code if you like — `unique_paths(4, 4)` returns 20.
</details>

---

**← Prev** [01 — When one index isn't enough](01-when-one-index-isnt-enough.md) ·
**Next →** [03 — Reading a 2D table](03-reading-a-2d-table.md)
