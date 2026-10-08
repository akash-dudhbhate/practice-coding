# lesson-08-recursion-backtracking — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Where does the answer live?
```python
def countdown(n):
    if n == 0:
        return []
    return [n] + countdown(n - 1)

print(countdown(3))
```
Trace the return values — what does `countdown(0)` give `countdown(1)`, and
what bubbles up?

<details><summary>Answer</summary>
`countdown(0)` → `[]`. Then `countdown(1)` → `[1] + []` = `[1]`;
`countdown(2)` → `[2] + [1]` = `[2,1]`; `countdown(3)` → `[3] + [2,1]` =
`[3,2,1]`. The empty list IS the base case's answer — every level
concatenates onto the deeper result.
</details>

---

## Check 02: Mutated path vs copied path
```python
out = []
path = []
for x in [1, 2]:
    path.append(x)
    out.append(path)
path.pop()
print(out)
```
What prints?
- (A) `[[1], [1, 2]]`
- (B) `[[1], [1]]`
- (C) `[[1, 2], [1, 2]]`

<details><summary>Answer</summary>
**(B) `[[1], [1]]`** — every entry is the SAME list object; `pop()` after
both appends shrinks what both entries point at. This is why backtracking
records `path.copy()` (or builds `path + [x]`): you want a snapshot, not a
live view.
</details>

---

## Check 03: How many subset leaves?
```
subsets([1,2,3,4]): at index i you branch include / skip
```
How many leaf nodes (complete paths) in the decision tree — and what does
that tell you about the algorithm's minimum cost?

- (A) 4
- (B) 8
- (C) 16

<details><summary>Answer</summary>
**(C) 16 = 2^4** — one binary choice per element. The OUTPUT is exponential,
so the algorithm can't possibly be faster than O(2^n): backtracking isn't
"slow", the answer itself is big. That's the difference vs DP, where the
answer is one number and the tree is only big because of redundant revisits.
</details>

---

## Check 04: Recursion vs loop cost
```python
def power_loop(b, e):
    r = 1
    for _ in range(e):
        r *= b
    return r

def power_rec(b, e):
    if e == 0: return 1
    return b * power_rec(b, e - 1)
```
For `power_rec(2, 900)` vs `power_loop(2, 900)` — which is closer to dying,
and on `power_rec(2, 2000)`?

<details><summary>Answer</summary>
At 900 both work, but `power_rec` is at ~900 stack frames — near the ~1000
default cap. `power_rec(2, 2000)` raises `RecursionError` while the loop is
fine. Recursion spends a frame per depth level; depth should be problem-
shaped (log n, branching small-n), not proportional to a huge input.
</details>

---

## Check 05: Diagonal ID in N-Queens
```
board cell (r, c): which formula is constant along a down-right diagonal?
```
- (A) r + c
- (B) r - c
- (C) r * c

<details><summary>Answer</summary>
**(B) `r - c`** — down-right adds 1 to BOTH r and c, so the difference is
constant along each \-diagonal. Its mirror image, **`r + c`**, is constant
along each /-diagonal (down-left adds 1 to r, subtracts 1 from c). Track
`cols`, `d1` (r-c), and `d2` (r+c) sets for O(1) conflict checks.
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Countdown that returns None

```python
def countdown(n):
    if n == 0:
        return []
    countdown(n - 1).append(n)      # <- returns a list... then what?
```

**Hint:** `countdown(3)` gives `None` — trace what each call returns.

<details><summary>Answer</summary>

**Bug:** `.append()` returns `None`, and the function never `return`s the
result — the contract ("returns a list") is honored at depth 0 then broken
everywhere else.
**Fix:** honor the contract at every level:
```python
return [n] + countdown(n - 1)      # or build then return:
# rest = countdown(n - 1); return [n] + rest
```
If you want countdown order `[n..1]`, prepend; for `[1..n]` append-after.
</details>

---

## Debug 02 (Medium): Subsets where every answer is []

```python
def subsets(nums):
    out = []
    def dfs(i, path):
        if i == len(nums):
            out.append(path)          # <- the bug
            return
        path.append(nums[i]); dfs(i + 1, path); path.pop()
        dfs(i + 1, path)
    dfs(0, [])
    return out
```

**Hint:** `subsets([1,2])` returns `[[],[],[],[]]` — four identical empties.

<details><summary>Answer</summary>

**Bug:** `out.append(path)` stores a reference to the SAME list — after all
the pops, it ends as `[]`, so all four entries read `[]`.
**Fix:** record a snapshot: `out.append(path.copy())` (or use the
non-mutating `dfs(i+1, path + [nums[i]])` style — no pop needed then).
</details>

---

## Debug 03 (Hard): Combination-sum with permutation duplicates

```python
def combination_sum(cands, target):
    out = []
    def dfs(start_target, path):      # start_target = remaining
        if start_target == 0:
            out.append(path.copy()); return
        if start_target < 0:
            return
        for c in cands:               # <- the bug: restarts from scratch
            path.append(c)
            dfs(start_target - c, path)
            path.pop()
    dfs(target, [])
    return out
```

**Hint:** `combination_sum([2,3], 5)` returns `[[2,3],[3,2]]` — those are
the same combination.

<details><summary>Answer</summary>

**Bug:** Every branch tries EVERY candidate — so `[2,3]` and `[3,2]` both
appear. Combinations need a "never look back" rule: pass an index `i` and
loop `for j in range(i, len(cands))`, recursing with `dfs(j, ...)` (same j
= reuse allowed, never earlier = no permutations).
**Fix:** signature `dfs(i, remaining, path)`; loop `j` from `i`; recurse
`dfs(j, remaining - cands[j], path)`.
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: No base case / input doesn't shrink
```python
# WRONG — infinite recursion -> RecursionError
def f(n): return n + f(n)

# CORRECT — base + strictly shrinking input
def f(n):
    if n <= 0: return 0
    return n + f(n - 1)
```

## Mistake 02: Appending the live path instead of a copy
```python
# WRONG — all entries alias the same list
out.append(path)

# CORRECT — snapshot at this moment
out.append(path.copy())      # or list(path), or path[:]
```

## Mistake 03: Forgetting to unchoose
```python
# WRONG — sibling branches inherit leftover state
path.append(c)
dfs(rest, path)
# next sibling sees c still in path!

# CORRECT — symmetric choose/unchoose
path.append(c)
dfs(rest, path)
path.pop()
```

## Mistake 04: Slicing inputs every call (hidden O(n) per level)
```python
# WRONG-ish — nums[1:] copies the list: O(n^2) total work
dfs(nums[1:])

# CORRECT — pass an index; the list is shared read-only
dfs(i + 1)
```

## Mistake 05: Recursing on deep linear input
```python
# WRONG for big n — ~1000-frame limit
def walk(n): return 0 if n == 0 else 1 + walk(n - 1)

# CORRECT — a loop carries no frame cost
def walk(n): return n
```

## Mistake 06: Returning early INSIDE the choice loop
```python
# WRONG — first choice found? fine for "any solution", wrong for "all"
for choice in choices:
    backtrack(...)
    return            # kills the siblings!

# CORRECT — let the loop finish so every branch gets explored
for choice in choices:
    backtrack(...)
# return AFTER the loop (or on the done-condition only)
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): sum_digits with flag-style base
### Before
```python
def sum_digits(n):
    if n < 10 and n >= 0:
        return n
    s = 0
    while False:       # vestigial loop the author gave up on
        pass
    return n % 10 + sum_digits(n // 10)
```
### Problems
1. Dead code left in; `n < 10 and n >= 0` re-verifies what `n == 0` says
   more clearly (either base is fine, pick the simple one)

### After
```python
def sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)
```

---

## Refactor 02 (Medium): subsets without backtracking hygiene
### Before
```python
def subsets(nums):
    out = []
    for i in range(len(nums) + 1):
        import itertools
        for combo in itertools.combinations(nums, i):
            out.append(list(combo))
    return out
```
### Problems
1. `itertools` hides the skill — interviews want the recursion written
2. Generates each SIZE separately instead of one include/skip tree

### After
```python
def subsets(nums):
    out = []
    def dfs(i, path):
        if i == len(nums):
            out.append(path.copy())
            return
        path.append(nums[i]); dfs(i + 1, path); path.pop()
        dfs(i + 1, path)
    dfs(0, [])
    return out
```

---

## Refactor 03 (Hard): n_queens with O(n) conflict scan
### Before
```python
def solve_n_queens(n):
    out = []
    def dfs(row, queens):           # queens: list of (r, c)
        if row == n:
            out.append(build(queens)); return
        for col in range(n):
            ok = True
            for qr, qc in queens:   # scan every placed queen
                if qc == col or abs(qr - row) == abs(qc - col):
                    ok = False; break
            if ok:
                dfs(row + 1, queens + [(row, col)])
    dfs(0, [])
    return out
```
### Problems
1. Conflict check is O(row) per cell — set lookups are O(1)
2. `queens + [(r,c)]` copies the list each call — mutate + pop instead

### After
```python
def solve_n_queens(n):
    out, cols, d1, d2 = [], set(), set(), set()
    board = [["." for _ in range(n)] for _ in range(n)]
    def dfs(r):
        if r == n:
            out.append(["".join(row) for row in board]); return
        for c in range(n):
            if c in cols or (r - c) in d1 or (r + c) in d2:
                continue
            board[r][c] = "Q"; cols.add(c); d1.add(r - c); d2.add(r + c)
            dfs(r + 1)
            board[r][c] = "."; cols.discard(c); d1.discard(r - c); d2.discard(r + c)
    dfs(0)
    return out
```

---

## Approach Comparison — different ways to solve it

## Problem: All subsets

### Approach 1: Include/skip backtracking — O(n·2^n)
```python
def dfs(i, path):
    if i == len(nums):
        out.append(path.copy()); return
    dfs(i + 1, path + [nums[i]])   # include
    dfs(i + 1, path)               # skip
```
**Pros:** Mirrors the decision tree; trivially adaptable (skip duplicates,
size caps). **Cons:** Builds the path per call if using `path + [x]`.

### Approach 2: Iterative doubling — O(n·2^n)
```python
out = [[]]
for x in nums:
    out += [s + [x] for s in out]
```
**Pros:** Beautifully short; same output. **Cons:** Hides the recursion
thinking the lesson teaches; harder to extend with pruning.

**Winner:** Approach 1 for learning and interviews — it's the template that
also solves permutations, combinations, and letter-case by changing what's
a valid "choice". Approach 2 is the pythonic one-liner worth knowing exists.

---

## Problem: power(base, exp)

### Approach 1: Naive recursion — O(exp)
```python
if exp == 0: return 1
return base * power(base, exp - 1)
```
**Pros:** Dead simple. **Cons:** exp frames — dies around exp ≈ 1000.

### Approach 2: Fast power — O(log exp)
```python
if exp == 0: return 1
half = power(base, exp // 2)
if exp % 2 == 0: return half * half
return half * half * base
```
**Pros:** Logarithmic depth — `power(2, 1000000)` in ~20 calls. **Cons:**
Slightly trickier; easy to write as `power(b, e//2) * power(b, e//2)` which
throws away the whole speedup (TWO recursive calls → back to O(e)).

**Winner:** Approach 2 — and it's the classic "halve the input" recursion
that previews binary search (lesson 09). The trap version above is exactly
the overlapping-subproblem smell lesson 15 teaches you to cache.
