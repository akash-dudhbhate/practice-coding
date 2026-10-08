# Lesson 16 — Coding Check

Use this to verify your solutions before asking for review.

## Easy

### p01 — Unique paths
- [ ] `unique_paths(3, 2)` returns `3`
- [ ] `unique_paths(3, 7)` returns `28`
- [ ] `unique_paths(1, 1)` returns `1` and `unique_paths(1, 10)` returns `1` (degenerate grids)
- [ ] First row and first column are seeded to `1` — only one way to reach them

### p02 — Min path sum
- [ ] `min_path_sum([[1,3,1],[1,5,1],[4,2,1]])` returns `7`
- [ ] `min_path_sum([[1,2,3],[4,5,6]])` returns `12` (forced top row + right column)
- [ ] `min_path_sum([[1]])` returns `1`
- [ ] Border cells are PREFIX sums (top row = running sum leftward), not min-of-anything

### p03 — Count paths with obstacles
- [ ] `unique_paths_with_obstacles([[0,0,0],[0,1,0],[0,0,0]])` returns `2`
- [ ] `unique_paths_with_obstacles([[0,1],[0,0]])` returns `1`
- [ ] `unique_paths_with_obstacles([[1]])` returns `0` — start blocked → nothing
- [ ] A wall in the first row/column zeroes out the REST of that border, not just its own cell

## Medium

### p01 — 0/1 knapsack
- [ ] `knapsack([1,3,4,5], [1,4,5,7], 7)` returns `9`
- [ ] `knapsack([2,3,4,5], [3,4,5,6], 5)` returns `7`
- [ ] `knapsack([4,5,6], [1,2,3], 3)` returns `0` (nothing fits)
- [ ] `knapsack([1,2,3], [6,10,12], 5)` returns `22`
- [ ] Each item used AT MOST once — if you iterate the 1-row version, `w` goes DOWNWARD
- [ ] You can explain `dp[i][w]` in one sentence: "max value using items 0..i-1 with capacity w"

### p02 — Longest common subsequence
- [ ] `longest_common_subsequence("abcde", "ace")` returns `3`
- [ ] `longest_common_subsequence("abc", "def")` returns `0`
- [ ] `longest_common_subsequence("", "abc")` returns `0`
- [ ] `longest_common_subsequence("bsbininm", "jmjkbkjkv")` returns `1`
- [ ] Match → `dp[i-1][j-1] + 1`; mismatch → `max(dp[i-1][j], dp[i][j-1])`

### p03 — Coin change 2 (count combinations)
- [ ] `coin_change_count(5, [1,2,5])` returns `4`
- [ ] `coin_change_count(3, [2])` returns `0` (impossible)
- [ ] `coin_change_count(10, [10])` returns `1`
- [ ] `coin_change_count(0, [1,2])` returns `1` (one way: choose nothing)
- [ ] COINS are the outer loop, amount inner — swapping them counts permutations and returns 9 instead of 4 for `(5, [1,2,5])`

## Hard

### p01 — Edit distance
- [ ] `min_distance("horse", "ros")` returns `3`
- [ ] `min_distance("intention", "execution")` returns `5`
- [ ] `min_distance("", "")` returns `0`
- [ ] `min_distance("a", "ab")` returns `1` and `min_distance("abc", "")` returns `3`
- [ ] Base row/col seeded with `j`/`i` (insert/delete costs), NOT zeros

### p02 — Wildcard matching
- [ ] `is_match_wildcard("aa", "a")` returns `False`
- [ ] `is_match_wildcard("aa", "*")` returns `True`
- [ ] `is_match_wildcard("cb", "?a")` returns `False`
- [ ] `is_match_wildcard("adceb", "*a*b")` returns `True`
- [ ] `is_match_wildcard("acdcb", "a*c?b")` returns `False`
- [ ] `is_match_wildcard("", "*")` returns `True` — `*` matches empty
- [ ] `*` recurrence is `dp[i-1][j] or dp[i][j-1]` — consume a char OR let `*` keep expanding

### p03 — Burst balloons
- [ ] `max_coins([3, 1, 5, 8])` returns `167`
- [ ] `max_coins([1, 5])` returns `10`
- [ ] `max_coins([9])` returns `9` and `max_coins([])` returns `0`
- [ ] You chose the LAST balloon `k` in each interval, not the first — that's what decouples the halves
- [ ] Fill order is by increasing interval length, not plain row-by-row

## How to verify

```bash
python3 check.py all            # all nine of your files
python3 check.py hard/p01       # just one
python3 check.py solutions      # sanity-check the reference solutions
```
