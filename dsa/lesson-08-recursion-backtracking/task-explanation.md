# Lesson 08 — Recursion & Backtracking

## What you'll learn
- The three questions: contract · base case · shrinking input
- Trusting the recursive call instead of simulating it
- Recursion vs iteration; the ~1000-frame depth cap
- Backtracking as choose → explore → unchoose
- When to enumerate (backtracking) vs cache overlapping subproblems (DP preview)

## Lesson

Recursion = a function that calls itself on a smaller input until a base
case answers directly. Three questions to answer before coding:

1. **What does it return?** (same contract at every depth)
2. **What's the base case?**
3. **How does the input shrink toward the base?**

```python
def sum_digits(n):                    # contract: sum of n's digits
    if n == 0:                        # base
        return 0
    return n % 10 + sum_digits(n // 10)   # shrink: drop last digit
```

Backtracking adds state you mutate and restore:

```python
def dfs(i, path):
    if i == len(nums):
        out.append(path.copy())       # COPY — path is reused!
        return
    path.append(nums[i])              # choose
    dfs(i + 1, path)                  # explore
    path.pop()                        # unchoose
    dfs(i + 1, path)                  # sibling branch: skip
```

Depth warning: Python caps the call stack near ~1000 frames. Recursion is
for branching/log-depth shapes; long linear work belongs in a loop.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here)
1. `easy/p01-sum-digits.py` — Write `sum_digits(n)` recursively (no loop, no `str()`): `1234` → `10`, `0` → `0`. Base: `n == 0`. Shrink: `n // 10`.
2. `easy/p02-countdown.py` — Write `countdown(n)` returning `[n, n-1, ..., 1]` recursively: `5` → `[5,4,3,2,1]`; `0` → `[]`.
3. `easy/p03-power.py` — Write `power(base, exp)` recursively for non-negative int `exp`: `(2,10)` → `1024`, `(2,0)` → `1`. No `**`, no loops.

### Medium
4. `medium/p01-subsets.py` — Write `subsets(nums)` returning all `2^n` subsets: `[1,2]` → `[[], [1], [2], [1,2]]` (any order). Include/exclude recursion; `copy()` when you record a path.
5. `medium/p02-permutations.py` — Write `permutations(nums)` returning all orderings: `[1,2,3]` → 6 permutations (any order). Choose-any-unused with a `used` array or shrinking pool.
6. `medium/p03-letter-case-permutation.py` — Write `letter_case_permutation(s)` returning every string where each LETTER appears lower or upper: `"a1b2"` → `{"a1b2","a1B2","A1b2","A1B2"}` (digits stay put; `"123"` → just `{"123"}`).

### Hard
7. `hard/p01-n-queens.py` — Write `solve_n_queens(n)` returning all boards for n queens on an n×n board (each board = list of n strings, `"Q"`/`"."`): `n=4` → 2 boards; `n=1` → `[["Q"]]`; `n=2` → `[]`. Place one queen per row; prune with column/diagonal conflict sets.
8. `hard/p02-combination-sum.py` — Write `combination_sum(candidates, target)` returning all combos (reuse allowed, order within combo irrelevant) that sum to target: `([2,3,6,7], 7)` → `[[2,2,3],[7]]` in any order. Recurse on index + remaining target; don't revisit earlier indices or you get `[2,2,3]` AND `[3,2,2]` duplicates.
9. `hard/p03-word-search.py` — Write `exist(board, word)` checking whether `word` is spelled by adjacent (up/down/left/right) cells in the 2D char grid, no cell reused per path: `"ABCCED"`/`"SEE"` → `True`, `"ABCB"` → `False` on the classic board. Mark visited by mutating the cell, unmark on the way out — the purest choose/explore/unchoose.

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete solution from scratch** below the TODO marker.
- Remove the TODO line when done.
- Run `python3 check.py <level>/<pNN>` to test one problem, `python3 check.py all` for everything.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has drills.
- Solutions live in `<level>/solutions/` — look only AFTER trying.
