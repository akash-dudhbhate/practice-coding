# lesson-16-dp-2d-knapsack — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: What are the two state variables?

For each problem, name the two things `dp[i][j]` (or equivalent) indexes:

1. 0/1 knapsack.
2. Longest common subsequence.
3. Unique paths on a grid.
4. Edit distance.
5. Burst balloons.

<details><summary>Answer</summary>
1. items considered × remaining capacity · 2. prefix length of a × prefix length of b · 3. row × column · 4. prefix length of word1 × prefix length of word2 · 5. left wall × right wall (interval endpoints).

If you can't name two independent variables, either the problem is 1D or the state is wrong.
</details>

---

## Check 02: Combination vs permutation

Coin change counting: `amount = 3`, `coins = [1, 2]`.

1. How many COMBINATIONS? 2. How many ORDERED sequences (permutations)?

<details><summary>Answer</summary>
Combinations: **2** — {1,1,1} and {1,2}. Permutations: **3** — [1,1,1], [1,2], [2,1].

The loop structure decides: coins-outer/amount-inner dedupes by processing coins in a fixed order → combinations. Amount-outer/coins-inner → permutations (every amount can append any coin, so [1,2] and [2,1] both count).
</details>

---

## Check 03: Trace one cell

Knapsack `weights=[2,3], values=[4,5], W=5`. After filling all rows, what is `dp[2][5]`, and which items produce it?

<details><summary>Answer</summary>
`dp[2][5] = 9` — take BOTH items (weight 2+3 = 5 exactly, value 4+5 = 9).
- `dp[1][5] = 4` (only item 1)
- `dp[2][5] = max(dp[1][5]=4, 5 + dp[1][2]=4) = 9` — take item 2, use dp[1][2] for the remaining capacity.
</details>

---

## Check 04: What does this print?

```python
def f(a, b):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

print(f("abc", "acb"))
```

<details><summary>Answer</summary>
**2** — LCS of "abc" and "acb" is "ab" or "ac" (either works, length 2). Table:

```
      ""  a  c  b
  ""   0  0  0  0
  a    0  1  1  1
  b    0  1  1  2
  c    0  1  2  2
```
</details>

---

## Check 05: 1-row knapsack — which direction?

```python
dp = [0] * (W + 1)
for i in range(n):
    for w in range(wt[i], W + 1):        # ascending!
        dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
```

Same loop, `w` ascending instead of descending. What problem does this now solve instead?

<details><summary>Answer</summary>
**UNBOUNDED knapsack** — items reusable. Ascending `w` means `dp[w - wt[i]]` may already include item `i` from THIS iteration, so an item can be picked repeatedly. For 0/1 you must iterate `w` downward so `dp[w - wt[i]]` still holds the previous row's value.
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Unique paths with obstacles — border leak

```python
def unique_paths_with_obstacles(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    for c in range(n):
        dp[0][c] = 1                     # BUG: ignores walls in row 0
    for r in range(m):
        dp[r][0] = 1                     # BUG: ignores walls in col 0
    for r in range(1, m):
        for c in range(1, n):
            if grid[r][c] == 0:
                dp[r][c] = dp[r-1][c] + dp[r][c-1]
    return dp[m-1][n-1]
```

**Hint:** `grid = [[0, 1, 0]]` — can you reach the last cell?

<details><summary>Answer</summary>

**Bug:** Border cells are set to 1 unconditionally, so a wall at `grid[0][1]` doesn't stop "paths" from flowing past it — `[[0,1,0]]` returns 1 instead of 0.
**Fix:** seed borders cumulatively —
```python
for c in range(n):
    if grid[0][c] == 1: break_after_zero = ... 
```
Cleaner: `dp[0][c] = dp[0][c-1] if c > 0 else 1`, then `dp[0][c] = 0 if grid[0][c] else dp[0][c]` — equivalently:
```python
dp[0][0] = 1 if grid[0][0] == 0 else 0
for c in range(1, n): dp[0][c] = dp[0][c-1] if grid[0][c] == 0 else 0
for r in range(1, m): dp[r][0] = dp[r-1][0] if grid[r][0] == 0 else 0
```
A wall on a border zeroes itself AND everything downstream.
</details>

---

## Debug 02 (Medium): LCS — wrong off-diagonal read

```python
def lcs(a, b):
    m, n = len(a), len(b)
    dp = [[0] * n for _ in range(m)]      # BUG: no base row/col
    for i in range(m):
        for j in range(n):
            if a[i] == b[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m-1][n-1]
```

**Hint:** What does `dp[-1]` mean in Python? Try `lcs("ab", "ba")`.

<details><summary>Answer</summary>

**Bugs:** (1) No padding row/col: at `i=0` or `j=0`, `dp[i-1]` / `dp[j-1]` wrap to the LAST row/col via negative indexing — `lcs("ab","ba")` reads stale cells. (2) Even when it "works," the semantics are subtly wrong: `dp[i-1][j]` at `i=0` reads the bottom row which is unwritten anyway (=0, harmless here — but the wrap is a landmine).
**Fix:** allocate `(m+1) × (n+1)`, loop `i`/`j` from 1, index strings with `a[i-1]`, `b[j-1]`.
</details>

---

## Debug 03 (Medium): Knapsack — item index off by one

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wt, val = weights[i], values[i]      # BUG: should be i-1
        for w in range(W + 1):
            dp[i][w] = dp[i-1][w]
            if wt <= w:
                dp[i][w] = max(dp[i][w], val + dp[i-1][w - wt])
    return dp[n][W]
```

**Hint:** Trace `i = 1`: which item does `weights[1]` point at?

<details><summary>Answer</summary>

**Bug:** `weights[i]` at `i=1` is the SECOND item — you skipped item 0 entirely, and at `i=n` you get an IndexError. The table row `i` represents "items 0..i-1", so the item being decided is index `i-1`.
**Fix:** `wt, val = weights[i-1], values[i-1]`.
</details>

---

## Debug 04 (Hard): Edit distance — zeroed borders

```python
def min_distance(w1, w2):
    m, n = len(w1), len(w2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]   # BUG: borders = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if w1[i-1] == w2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[m][n]
```

**Hint:** `min_distance("abc", "")` should return 3. What does this return?

<details><summary>Answer</summary>

**Bug:** `dp[i][0] = 0` claims turning `"abc"` into `""` costs nothing — deleting a char is an OPERATION, not free. `("abc","")` returns 0 instead of 3, and every interior cell undercounts because it can "route through" fake-free borders.
**Fix:**
```python
for i in range(m + 1): dp[i][0] = i      # delete i chars
for j in range(n + 1): dp[0][j] = j      # insert j chars
```
</details>

---

## Debug 05 (Hard): Wildcard — `*` can't match empty

```python
# inside the table fill, p[j-1] == '*':
dp[i][j] = dp[i-1][j]        # BUG: only "consume a char" case
```

**Hint:** `is_match("", "*")` — can `*` match zero characters?

<details><summary>Answer</summary>

**Bug:** `*` matches EMPTY too — handled by `dp[i][j-1]` (pattern's `*` simply doesn't cover this char position). With only `dp[i-1][j]`, `is_match("", "*")` and `is_match("a", "a*")` wrongly return False.
**Fix:** `dp[i][j] = dp[i-1][j] or dp[i][j-1]` — `*` consumes the current char of s (if nonempty) OR stands for empty.
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: Off-by-one between table index and item/char index
```python
# WRONG — row i decides item i-1, not i
wt, val = weights[i], values[i]
a[i], b[j]

# CORRECT
wt, val = weights[i-1], values[i-1]
a[i-1], b[j-1]
```

## Mistake 02: Base row/col seeded with the wrong value
```python
# WRONG for min-problems — borders aren't free
dp = [[0] * (n+1) for _ in range(m+1)]

# CORRECT — real costs (edit distance) / prefix sums (min path) / 1s (count paths)
dp[i][0] = i ; dp[0][j] = j        # edit distance
dp[0][c] = dp[0][c-1] + grid[0][c] # min path sum
```

## Mistake 03: 1-row knapsack iterating upward (0/1 → unbounded)
```python
# WRONG for 0/1 — dp[w-wt] already includes item i
for w in range(wt, W + 1):

# CORRECT for 0/1 — preserve previous row's values
for w in range(W, wt - 1, -1):
```

## Mistake 04: Combinations vs permutations — loop order
```python
# COMBINATIONS (coin-change-2): coin outer, amount inner
for c in coins:
    for a in range(c, amount + 1):
        dp[a] += dp[a - c]

# PERMUTATIONS: amount outer, coin inner
for a in range(1, amount + 1):
    for c in coins:
        if c <= a: dp[a] += dp[a - c]
```

## Mistake 05: Forgetting `*` matches empty (wildcard)
```python
# WRONG — '*' only consumes
dp[i][j] = dp[i-1][j]
# CORRECT — consume OR stand for empty
dp[i][j] = dp[i-1][j] or dp[i][j-1]
```

## Mistake 06: Interval DP filled row-major
```python
# WRONG — dp[i][k] and dp[k][j] may not be filled yet
for i in range(n):
    for j in range(n): ...

# CORRECT — fill by increasing interval length
for length in range(1, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Unique paths — full grid → one row
### Before
```python
dp = [[1] * n for _ in range(m)]
for r in range(1, m):
    for c in range(1, n):
        dp[r][c] = dp[r-1][c] + dp[r][c-1]
return dp[m-1][n-1]
```
### Problems
1. O(m·n) space when only the previous row is read.

### After
```python
row = [1] * n
for _ in range(1, m):
    for c in range(1, n):
        row[c] += row[c - 1]     # row[c] is "top", row[c-1] is "left"
return row[-1]
```
Same O(m·n) time, O(n) space — and it reads as "each row accumulates on the previous."

---

## Refactor 02 (Medium): Knapsack 2D → 1 row
### Before
```python
dp = [[0] * (W + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    wt, val = weights[i-1], values[i-1]
    for w in range(W + 1):
        dp[i][w] = dp[i-1][w]
        if wt <= w:
            dp[i][w] = max(dp[i][w], val + dp[i-1][w - wt])
return dp[n][W]
```
### Problems
1. O(n·W) space; the skip case is a no-op when rolling in place.

### After
```python
dp = [0] * (W + 1)
for i in range(n):
    for w in range(W, weights[i] - 1, -1):   # DOWNWARD — 0/1!
        dp[w] = max(dp[w], values[i] + dp[w - weights[i]])
return dp[W]
```
The downward scan is load-bearing: `dp[w - wt]` must still hold the previous iteration's value.

---

## Refactor 03 (Hard): LCS 2D → two rows
### Before
```python
dp = [[0] * (n + 1) for _ in range(m + 1)]
# ... fill ... return dp[m][n]
```
### Problems
1. O(m·n) memory for a recurrence reading only rows i-1 and i.

### After
```python
prev = [0] * (n + 1)
for i in range(1, m + 1):
    cur = [0] * (n + 1)
    for j in range(1, n + 1):
        if a[i-1] == b[j-1]:
            cur[j] = prev[j-1] + 1
        else:
            cur[j] = max(prev[j], cur[j-1])
    prev = cur
return prev[n]
```
Safe because the recurrence reads `prev` and `cur` only — never `i-2`.

---

## Approach Comparison — different ways to solve it

## Problem: 0/1 knapsack

### Approach 1: top-down memoized recursion
```python
@lru_cache(None)
def best(i, w):
    if i == 0 or w == 0: return 0
    skip = best(i-1, w)
    take = values[i-1] + best(i-1, w - weights[i-1]) if weights[i-1] <= w else 0
    return max(skip, take)
```
**Pros:** recurrence is the problem statement; computes only reachable states. **Cons:** recursion depth = n; cache overhead per call.

### Approach 2: bottom-up table (this lesson)
**Pros:** O(n·W) predictable, no stack risk, teachable fill order. **Cons:** fills every cell even unreachable ones.

### Approach 3: 1-row array, downward w
**Pros:** O(W) space — the interview upgrade. **Cons:** direction must be exactly right; harder to explain under pressure.

**Winner:** Approach 2 first, then say "and I can compress to one row by iterating w downward." Shows both the model and the optimization.

---

## Problem: Longest common subsequence

### Approach 1: prefix-pair table (this lesson)
```python
dp[i][j] = dp[i-1][j-1] + 1            if match
           max(dp[i-1][j], dp[i][j-1]) otherwise
```
O(m·n) time and space; recoverable string by backtracking the table.

### Approach 2: memoized recursion
```python
@lru_cache(None)
def lcs(i, j):
    if i == 0 or j == 0: return 0
    if a[i-1] == b[j-1]: return lcs(i-1, j-1) + 1
    return max(lcs(i-1, j), lcs(i, j-1))
```
Same states, top-down. Fine, but the table version also supports reconstruction.

### Approach 3: Hunt–Szymanski / binary-search LCS
O(r log n) where r = matching position pairs — much faster on long strings with few matches. Overkill for interviews; exists for bioinformatics scale.

**Winner:** Approach 1 — and if asked to also RETURN the subsequence, walk the table backward from `dp[m][n]`: at each cell, match → emit char and move diagonal; else move toward the larger neighbor.
