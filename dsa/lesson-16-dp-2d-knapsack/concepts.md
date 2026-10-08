# Lesson 16 — Concepts Explained (2D DP & Knapsack)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Why Two Dimensions — the state needs two variables

**What:** In lesson 15, `dp[i]` captured everything that mattered about a prefix. Here one index isn't enough — the subproblem is defined by a *pair*:

- **Knapsack:** `dp[i][w]` = best value using items `0..i` with capacity `w`. Two knobs: which items, how much room left.
- **Grid:** `dp[r][c]` = best answer for reaching cell `(r, c)`. Two coordinates.
- **Two sequences:** `dp[i][j]` = best answer for prefix `a[:i]` vs prefix `b[:j]`. One pointer per sequence.

**Why it exists:** The subproblem has two independent things that vary, and the recurrence chooses based on both. If you collapsed to 1D you'd lose information — e.g., in knapsack, "best value so far" means nothing without knowing the remaining capacity.

**Where it's used:** Resource allocation (budget × items), pathfinding on grids (games, robotics, image processing), string comparison (diff tools, DNA alignment, spell checkers — edit distance is everywhere), regex/wildcard matching.

**What goes wrong without it:** Trying to flatten a genuinely-2D state into 1D produces wrong answers — the classic bug is a knapsack where the "remaining capacity" dimension is dropped, so items get silently reused or skipped.

**The same five-step recipe applies** — state, recurrence, base cases, fill order, answer location — but the table is now a grid and the fill order is usually row-by-row (or diagonal).

---

## 0/1 Knapsack — the canonical 2D DP

**What:** `n` items, each with `weight[i]` and `value[i]`; a bag holding `W` total weight. Each item is taken **at most once** (0/1 — no fractions, no repeats). Maximize value.

- **State:** `dp[i][w]` = max value using items `0..i-1` with capacity `w`. (Table is `(n+1) × (W+1)`; row 0 = "no items".)
- **Recurrence (take-or-skip):**
  ```
  dp[i][w] = dp[i-1][w]                          skip item i
           = max(dp[i-1][w], value[i-1] + dp[i-1][w - wt[i-1]])   take it, if it fits
  ```
- **Base:** row 0 and column 0 are all 0 (no items or no capacity → 0 value).
- **Order:** row by row — `dp[i][*]` reads only `dp[i-1][*]`.
- **Answer:** `dp[n][W]` (bottom-right).

**Full table trace — `weights = [1,3,4,5]`, `values = [1,4,5,7]`, `W = 7`:**

```
               capacity w →
        0    1    2    3    4    5    6    7
i=0  [  0    0    0    0    0    0    0    0  ]   no items → all 0
i=1  [  0    1    1    1    1    1    1    1  ]   item (w1,v1): fits at w>=1
i=2  [  0    1    1    4    5    5    5    5  ]   item (w3,v4)
i=3  [  0    1    1    4    5    6    6    9  ]   item (w4,v5)
i=4  [  0    1    1    4    5    7    8    9  ]   item (w5,v7)
```

Row-by-row, cell-by-cell:

```
i=1, item (wt=1, val=1):
  w=1: max(dp[0][1]=0, 1+dp[0][0]=1) = 1 ... every w>=1 gets 1

i=2, item (wt=3, val=4):
  w=2: doesn't fit → dp[1][2] = 1
  w=3: max(dp[1][3]=1, 4+dp[1][0]=4) = 4     ← take it
  w=4: max(dp[1][4]=1, 4+dp[1][1]=5) = 5     ← item1 + item2
  w=7: max(dp[1][7]=1, 4+dp[1][4]=5) = 5

i=3, item (wt=4, val=5):
  w=5: max(dp[2][5]=5, 5+dp[2][1]=6) = 6
  w=7: max(dp[2][7]=5, 5+dp[2][3]=9) = 9     ← items 1+2+3 (w 1+3+4=8? no —
       wait: w - wt = 7-4 = 3, dp[2][3] = 4; 5+4 = 9; items (3,4)+(4,5) weigh 7)

i=4, item (wt=5, val=7):
  w=7: max(dp[3][7]=9, 7+dp[3][2]=7+1=8) = 9 ← SKIP wins
Answer: dp[4][7] = 9   (items of weight 3 and 4 → value 4+5 = 9)
```

Notice the last cell is a SKIP — the optimal set `{w3,w4}` was already found by row 3. That happens: the table's job is to have *considered* taking item 4, not to force it.

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wt, val = weights[i - 1], values[i - 1]
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]                  # skip
            if wt <= w:
                dp[i][w] = max(dp[i][w], val + dp[i - 1][w - wt])  # take
    return dp[n][W]
```

Expected output for `knapsack([1,3,4,5], [1,4,5,7], 7)`: **9**

---

## Grid DP — `dp[r][c] = f(top, left)`

**What:** A `m × n` grid; you move only RIGHT or DOWN. `dp[r][c]` = best answer for reaching cell `(r, c)`.

- Unique paths: `dp[r][c] = dp[r-1][c] + dp[r][c-1]` — ways from top + ways from left.
- Min path sum: `dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])`.

**Borders are the base case:** the first row can only be reached from the left; the first column only from above. Fill them before the inner loop (or guard with `if r>0 / c>0`).

**Table fill — unique paths on a `3 × 4` grid:**

```
        c=0  c=1  c=2  c=3
r=0  [  1    1    1    1  ]    first row: only reachable from the left
r=1  [  1    2    3    4  ]    each cell = top + left
r=2  [  1    3    6   10  ]    dp[2][3] = dp[1][3] + dp[2][2] = 4 + 6
Answer: 10 paths
```

It's Pascal's triangle tilted — `dp[r][c] = C(r+c, r)` mathematically, but the DP works even when math formulas can't (obstacles, weights).

**Table fill — min path sum on `[[1,3,1],[1,5,1],[4,2,1]]`:**

Each cell: `grid[r][c] + min(top, left)` — you arrived from whichever neighbor was cheaper.

```
grid:              dp (running cost):
 1  3  1            1   4   5          row 0: accumulate left (only entry path)
 1  5  1    →       2   7   6          dp[1][1] = 5 + min(4, 2)
 4  2  1            6   8   7          dp[2][3]… wait, dp[2][2] = 1 + min(6, 8)

step-by-step:
  dp[0][0]=1
  row 0:  dp[0][1]=3+1=4,   dp[0][2]=1+4=5
  col 0:  dp[1][0]=1+1=2,   dp[2][0]=4+2=6
  dp[1][1] = 5 + min(dp[0][1]=4, dp[1][0]=2) = 7
  dp[1][2] = 1 + min(dp[0][2]=5, dp[1][1]=7) = 6
  dp[2][1] = 2 + min(dp[1][1]=7, dp[2][0]=6) = 8
  dp[2][2] = 1 + min(dp[1][2]=6, dp[2][1]=8) = 7
Answer: 7   (path 1→1→4→2… actually 1→1(down)→4(down)→2(right)→1(right) = 9?
  recheck: path [1,3,1,1,1] = 1+3+1+1+1 = 7 — right,right,down,down)
```

**Obstacle handling:** if `grid[r][c]` is blocked, `dp[r][c] = 0` — no paths pass through. *And* a blocked cell in row 0 / column 0 zeros out everything after it in that border (a wall in the first row blocks the rest of that row).

```
grid:  0 0 0       dp:   1 1 1
       0 1 0  →         1 0 1     blocked center zeros the cell;
       0 0 0            1 1 2     bottom-right keeps 2 paths around it
```

```python
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]        # first row/col seeded to 1
    for r in range(1, m):
        for c in range(1, n):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[m - 1][n - 1]
```

Expected output for `unique_paths(3, 4)`: **10** · `unique_paths(3, 7)`: **28**

---

## Two-Sequence DP — LCS: `dp[i][j]` over prefixes

**What:** Longest Common Subsequence of strings `a`, `b`. `dp[i][j]` = LCS length of `a[:i]` and `b[:j]`. Two pointers, one per sequence — that's the second dimension.

- **Recurrence:**
  ```
  if a[i-1] == b[j-1]:   dp[i][j] = dp[i-1][j-1] + 1     ← chars match: extend
  else:                  dp[i][j] = max(dp[i-1][j], dp[i][j-1])  ← skip one char
  ```
- **Base:** row 0 / col 0 = 0 (a prefix vs empty string shares nothing).
- **Answer:** `dp[len(a)][len(b)]` — bottom-right.

**Full table — `a = "abcde"`, `b = "ace"`:**

```
          ""   a   c   e
        ┌───┬───┬───┬───┐
   ""   │ 0 │ 0 │ 0 │ 0 │
    a   │ 0 │ 1 │ 1 │ 1 │   a==a at (1,1): diag+1; rest = max(up,left)
    b   │ 0 │ 1 │ 1 │ 1 │   no new matches; inherit best
    c   │ 0 │ 1 │ 2 │ 2 │   c==c at (3,2): dp[2][1]+1 = 2
    d   │ 0 │ 1 │ 2 │ 2 │
    e   │ 0 │ 1 │ 2 │ 3 │   e==e at (5,3): dp[4][2]+1 = 3
        └───┴───┴───┴───┘
Answer: dp[5][3] = 3   ("ace")
```

Cell example `dp[5][3]` (a[4]='e' vs b[2]='e'): match → `dp[4][2] + 1 = 2 + 1 = 3`.
Cell example `dp[2][1]` (a[1]='b' vs b[0]='a'): no match → `max(dp[1][1], dp[2][0]) = max(1, 0) = 1`.

```python
def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1        # match: extend diagonal
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # skip from either side
    return dp[m][n]
```

Expected output for `lcs("abcde", "ace")`: **3**

The same prefix-pair state powers edit distance (hard/p01) and wildcard matching (hard/p02) — only the recurrence changes.

**Edit distance preview — the recurrence, same shape as LCS:**

`dp[i][j]` = min operations to turn `a[:i]` into `b[:j]`:

```
a[i-1] == b[j-1]:  dp[i][j] = dp[i-1][j-1]               free match
else:              dp[i][j] = 1 + min(dp[i-1][j],        delete a's char
                                      dp[i][j-1],        insert b's char
                                      dp[i-1][j-1])      substitute
```

Table for `a = "horse"`, `b = "ros"` (answer 3: horse → rorse → rose → ros):

```
        ""  r  o  s
    ""   0  1  2  3     base: insert j chars
    h    1  1  2  3
    o    2  2  1  2     o==o at (2,2): dp[1][1] = 1
    r    3  2  2  2     r==r at (3,1): dp[2][0] = 2
    s    4  3  3  2     s==s at (4,3): dp[3][2] = 2
    e    5  4  3  3     e vs s: 1 + min(3, 2, 2)... dp[4][3]=2? check:
                        dp[5][3] = 1 + min(dp[4][3], dp[5][2], dp[4][2])
                                 = 1 + min(2, 3, 3) = 3
Answer: dp[5][3] = 3
```

The base row/column for edit distance is `j` / `i` — turning an empty string into `b[:j]` costs `j` inserts. **Min-problems seed borders with real costs, not zeros.**

---

## Rolling Rows — when 2D collapses to 2×W (and when it doesn't)

**What:** If `dp[i][*]` reads ONLY `dp[i-1][*]`, keep two rows (`prev`, `cur`) instead of the whole table. If it reads only `prev[j]` and `prev[j-k]` — same. Space drops from O(n·W) to O(W).

**Why it exists:** Knapsack with W = 10⁵ and n = 10⁴ is a 10⁹-cell table — too much memory. Two rows = 2·10⁵ cells.

**The 1-row trick for knapsack:** iterate `w` **downward** (W → wt) and reuse a single array:
```python
dp = [0] * (W + 1)
for i in range(n):
    for w in range(W, wt - 1, -1):        # DOWNWARD — preserves "not yet taken" values
        dp[w] = max(dp[w], val + dp[w - wt])
```
Iterating downward means `dp[w - wt]` still holds the *previous row's* value (it hasn't been overwritten this pass) — so each item is used at most once. **Iterate upward and you get UNBOUNDED knapsack** (item reusable) — same loop, different direction, different problem. This direction detail is the single most-asked knapsack trick.

**Where it's used:** Knapsack (1 row), LCS/edit distance (2 rows), grid problems (1 row, in-place even — overwrite `grid` itself if mutation is allowed).

**What goes wrong:**
- Rolling rows in a recurrence that reads `dp[i-2]` — you threw away the row you still need. Check which rows the recurrence touches *first*.
- Knapsack 1-row with `w` ascending → silently becomes unbounded knapsack; answers come out too big.
- In-place grid DP that mutates the input when the caller still needs it — copy if mutation isn't allowed.

---

## The Pitfall Gallery — five ways 2D DP goes wrong

**1. Off-by-one between index and count.** `dp[i]` refers to item `i-1` when the table is 1-indexed over "items considered". `weights[i]` where you meant `weights[i-1]` shifts every take/skip by an item.

**2. Forgetting the base row/column.** Row 0 = "no items" / "empty prefix" / "off the grid edge". Skipping it leaves `0`s that happen to be right for knapsack/LCS but wrong for min-problems (min path sum needs `inf` borders, not `0` — a zero border would look like a free path).

**3. Fill order violating dependencies.** `dp[i][j]` reads `dp[i-1][j]`, `dp[i][j-1]`, `dp[i-1][j-1]` — all *already-filled* if you go top-left → bottom-right in row-major order. Filling column-major reads unwritten cells.

**4. Obstacle cells polluting borders.** In unique-paths-with-obstacles, an obstacle at row 0 must zero out every cell *after* it in that row — `dp[0][c] = 0 if blocked else dp[0][c-1]`. Writing plain `1`s for the whole border leaks paths through walls.

**5. Iterating the 1-row knapsack upward.** `for w in range(wt, W+1)` → each item may be taken repeatedly (unbounded). 0/1 requires `range(W, wt-1, -1)`.

**Edge cases to always test:** empty items/empty string/1×1 grid; capacity 0 / empty pattern; all-obstacle borders; impossible targets (knapsack with nothing fitting → 0; LCS with no common char → 0); and inputs where the answer lives in the base row (`dp[0][*]`).

---

## Interval DP — when the answer is built from the inside out

**What:** Some problems can't be solved by "extend a prefix" — the smart move is choosing the *last* operation and recursing into the interior. Burst balloons is the classic: `dp[i][j]` = max coins from bursting balloons strictly between walls `i` and `j`; try each `k` in between as the LAST balloon to burst:

```
dp[i][j] = max over k in (i..j):  nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j]
```

Choosing `k` LAST is the trick — its neighbors are fixed walls `i` and `j`, so the two halves `dp[i][k]` and `dp[k][j]` are independent subproblems.

**Why it exists:** choosing `k` first entangles the two halves (bursting order changes neighbors). Choosing it last decouples them — that's what makes it a valid DP instead of an exponential mess.

**Fill order for interval DP:** by increasing interval LENGTH (`for length in 2..n`), not row-by-row — a cell reads *smaller* intervals on both sides.

**Where it's used:** burst balloons, palindrome partitioning, matrix-chain multiplication, optimal BST, "remove boxes"-style games.

---

## Recipe recap — recognize the 2D shape in 15 seconds

1. One index can't describe the subproblem → go 2D. Ask: "what are the TWO things that vary?" (items×capacity, row×col, prefix×prefix, left-wall×right-wall).
2. Write `dp[i][j]` in one sentence. If you can't, the state is wrong.
3. Recurrence = a choice: take/skip (knapsack), top+left (grid), match/skip (LCS), last-pick (interval).
4. Borders first — row 0 and col 0 are your base cases; give them REAL values (0 for counts, costs for min-problems).
5. Fill order must respect dependencies: row-major for prefix problems, by-length for interval problems, downward `w` for 1-row knapsack.
6. Answer location: usually bottom-right `dp[m][n]` — but knapsack variants may want `max(dp[n])`, and interval DP wants `dp[0][n-1]`.
7. Complexity out loud: **states × work per state** — knapsack is O(n·W), LCS is O(m·n), each O(1) per cell.
