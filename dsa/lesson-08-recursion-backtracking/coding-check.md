# Lesson 08 — Coding Check

Use this to verify your solutions before asking for a review.

## Easy

### p01-sum-digits.py — Sum of digits, recursively
- [ ] `sum_digits(1234)` returns `10`
- [ ] `sum_digits(0)` returns `0`
- [ ] `sum_digits(999)` returns `27`
- [ ] Recursive — no loop, no `str(n)` digit-splitting
- [ ] Base case `n == 0` (or `n < 10 -> n`); shrink via `n // 10`

### p02-countdown.py — Build [n..1] recursively
- [ ] `countdown(5)` returns `[5,4,3,2,1]`
- [ ] `countdown(1)` returns `[1]`
- [ ] `countdown(0)` returns `[]`
- [ ] Returns a LIST at every depth — same contract all the way down

### p03-power.py — Recursive power
- [ ] `power(2, 10)` returns `1024`
- [ ] `power(2, 0)` returns `1` (base case — anything^0)
- [ ] `power(3, 3)` returns `27`; `power(5, 1)` returns `5`
- [ ] Recursive — no `**`, `pow()`, or loops

## Medium

### p01-subsets.py — All 2^n subsets
- [ ] `subsets([1,2])` returns 4 lists containing `[]`, `[1]`, `[2]`, `[1,2]`
- [ ] `subsets([1,2,3])` returns exactly 8 subsets, none duplicated
- [ ] `subsets([])` returns `[[]]`
- [ ] You append `path.copy()` (or build `path + [x]`) — not raw `path`

### p02-permutations.py — All orderings
- [ ] `permutations([1,2,3])` returns all 6 orderings
- [ ] `permutations([1])` returns `[[1]]`
- [ ] No permutation is missing or duplicated
- [ ] Each element is used exactly once per path (`used[]` flags or a shrinking pool)

### p03-letter-case-permutation.py — Flip each letter's case
- [ ] `letter_case_permutation("a1b2")` = `{"a1b2","a1B2","A1b2","A1B2"}` (4 items)
- [ ] `letter_case_permutation("3z4")` = `{"3z4","3Z4"}`
- [ ] `letter_case_permutation("123")` = `{"123"}` (digits make one branch, not two)
- [ ] Branch only on `isalpha()` chars — digits recurse straight through

## Hard

### p01-n-queens.py — All n×n boards
- [ ] `solve_n_queens(4)` returns exactly 2 boards
- [ ] `solve_n_queens(1)` returns `[["Q"]]`
- [ ] `solve_n_queens(2)` returns `[]` (impossible)
- [ ] Conflict pruning uses column + 2 diagonal sets (r-c and r+c are constant on diagonals)
- [ ] Boards are lists of strings, `"Q"`/`"."`, each row fully built

### p02-combination-sum.py — Combos summing to target
- [ ] `combination_sum([2,3,6,7], 7)` returns `[[2,2,3],[7]]` (any order)
- [ ] `combination_sum([2], 1)` returns `[]`
- [ ] `combination_sum([2,3,5], 8)` returns `[[2,2,2,2],[2,3,3],[3,5]]`
- [ ] Recursion passes `i` (not `i+1`) to allow reuse — but never goes BACK to lower i, or permutations sneak in as duplicates

### p03-word-search.py — Word in a 2D grid
- [ ] `"ABCCED"` → `True`, `"SEE"` → `True`, `"ABCB"` → `False` on the standard board
- [ ] `[["a"]]` with `"a"` → `True`, `"b"` → `False`
- [ ] A cell can't be reused within one path — mark visited, then UNMARK (restore) when the recursive call returns
- [ ] All 4 neighbors explored; bounds-checked

## How to verify

```bash
python3 check.py easy/p01     # one problem
python3 check.py all          # everything
```
