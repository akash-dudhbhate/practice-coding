# Lesson 16 — 2D DP & Knapsack

## What you'll learn
- When one index isn't enough: two-variable states (items×capacity, row×col, prefix×prefix)
- 0/1 knapsack take-or-skip, filling the table row by row
- Grid DP: `dp[r][c] = f(top, left)` + obstacle handling
- Two-sequence DP: LCS/edit distance over prefixes
- Space optimization: rolling rows and the downward-iterate 1-row knapsack trick

## Lesson

Same recipe as lesson 15, bigger table: state is now `dp[i][j]`.
The recurrence is always a *choice* — take-or-skip, top-or-left,
match-or-skip. Borders (row 0 / col 0) are your base cases; fill in
dependency order; answer usually sits bottom-right.

### The skeleton
```python
dp = [[BASE] * (n + 1) for _ in range(m + 1)]
# seed row 0 and col 0 with real base values
for i in range(1, m + 1):
    for j in range(1, n + 1):
        dp[i][j] = f(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
return dp[m][n]
```

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here) — grid DP
1. `easy/p01-unique-paths.py` — `unique_paths(m, n)` → paths from top-left to bottom-right moving only right/down.
   `(3, 2) → 3`, `(3, 7) → 28`, `(1, 1) → 1`.
2. `easy/p02-min-path-sum.py` — `min_path_sum(grid)` → min sum along a right/down path.
   `[[1,3,1],[1,5,1],[4,2,1]] → 7`. First row/column are forced-prefix sums.
3. `easy/p03-count-paths-with-obstacles.py` — `unique_paths_with_obstacles(grid)` → paths where `1` cells are walls.
   `[[0,0,0],[0,1,0],[0,0,0]] → 2`. A wall in row 0/col 0 zeroes the rest of that border.

### Medium — the classic 2D trio
4. `medium/p01-knapsack-01.py` — `knapsack(weights, values, capacity)` → max value, each item used at most once.
   `([1,3,4,5], [1,4,5,7], 7) → 9` (weights 3+4 → values 4+5). Trace the table row by row before coding.
5. `medium/p02-longest-common-subsequence.py` — `longest_common_subsequence(a, b)` → LCS length.
   `("abcde", "ace") → 3`, `("abc", "def") → 0`. Match → `diag+1`; else `max(up, left)`.
6. `medium/p03-coin-change-2.py` — `coin_change_count(amount, coins)` → number of COMBINATIONS (order doesn't matter) making `amount`.
   `(5, [1,2,5]) → 4`. Loop coins in the OUTER loop, amounts inner — that's what makes combinations not permutations.

### Hard — two-sequence and interval DP
7. `hard/p01-edit-distance.py` — `min_distance(word1, word2)` → min insert/delete/substitute ops to convert word1 → word2.
   `("horse", "ros") → 3`, `("intention", "execution") → 5`. Base row/col = insert/delete counts, not zeros.
8. `hard/p02-wildcard-matching.py` — `is_match_wildcard(s, p)` → does pattern `p` match all of `s`? `?` = any single char, `*` = any sequence (incl. empty).
   `("aa", "*") → True`, `("adceb", "*a*b") → True`, `("acdcb", "a*c?b") → False`. The `*` case: `dp[i][j] = dp[i-1][j] or dp[i][j-1]` (consume a char OR expand the match).
9. `hard/p03-burst-balloons.py` — `max_coins(nums)` → max coins bursting balloons; bursting `i` pays `nums[i-1]*nums[i]*nums[i+1]` (out-of-range = 1).
   `[3,1,5,8] → 167`. Interval DP: choose the LAST balloon `k` between walls `i,j` — that decouples the two sides.

### How to work
- Read `concepts.md` first — the knapsack and LCS tables are filled there cell by cell.
- For each problem, write the five recipe steps in comments BEFORE coding: state / recurrence / base / order / answer.
- Run `python3 check.py easy/p01` for one problem, `python3 check.py all` for all nine.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has debug drills after you finish.
- Peek at `solutions/` only after a real attempt — then close it and redo from memory.
