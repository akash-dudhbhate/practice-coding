# lesson-15-dp-1d — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Is it DP?

For each problem, say whether DP applies and why:

1. Binary search on a sorted array (find target's index).
2. Number of distinct ways to tile a 2×n board with dominoes.
3. Shortest path in an unweighted graph (BFS).
4. Min coins to make an amount.
5. Sort an array faster than O(n²).

<details><summary>Answer</summary>
1. NO — each comparison halves the range; subproblems never repeat (divide & conquer).
2. YES — `ways(n) = ways(n-1) + ways(n-2)`, identical to climbing stairs.
3. YES-ish — BFS IS the DP for unweighted shortest path (`dist[v] = dist[u]+1`); but you'd implement it as BFS, not a table.
4. YES — "min cost" phrasing + overlapping subproblems.
5. NO — sorting has no subproblem reuse; it's a comparison problem.

Rule: ask "would naive recursion recompute the same call?" Yes → DP. No → something else.
</details>

---

## Check 02: Which of the three phrasings?

Label each as COUNT-WAYS, MIN-MAX, or CAN-REACH:

1. House robber.
2. Word break.
3. Tribonacci.
4. Coin change (fewest coins).
5. Partition equal subset sum.

<details><summary>Answer</summary>
1. MIN-MAX (max money) · 2. CAN-REACH (boolean: segmentable?) · 3. COUNT-WAYS-ish (it's actually a pure recurrence — same shape as count-ways: sum over predecessors) · 4. MIN-MAX · 5. CAN-REACH (does a subset summing to total/2 exist?).

The phrasing tells you the *combining operator*: `sum` for count, `min`/`max` for optimize, `any`/`or` for reachability.
</details>

---

## Check 03: What does this print?

```python
def mystery(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        if i >= 2:
            dp[i] += dp[i - 2]
    return dp[n]

print(mystery(5))
```

<details><summary>Answer</summary>
**8** — it's climbing stairs (`dp[i] = dp[i-1] + dp[i-2]`, seeded `dp[0]=1`). The table: `1,1,2,3,5,8`.
</details>

---

## Check 04: Spot the wrong base case

```python
def climb_stairs(n):
    dp = [0] * (n + 1)
    dp[0] = 0                 # ← seeded 0
    if n >= 1:
        dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

What does `climb_stairs(5)` return, and what's the fix?

<details><summary>Answer</summary>
Returns **5** instead of 8. Table: `0,1,1,2,3,5` — every cell is the correct value minus what the missing `dp[0]=1` would have propagated. Base cases encode the *meaning* of the empty state: "one way to be standing at the bottom" requires `dp[0] = 1`. (Or return `dp[n]` from a table starting `dp[1]=1, dp[2]=2` with `n<=2` handled — equally valid.)
</details>

---

## Check 05: Answer location

For LIS, `dp[i]` = "length of longest increasing subsequence ENDING at index `i`". For `nums = [10,9,2,5,3,7,101,18]`, the table is:

```
nums:  10   9   2   5   3   7   101  18
dp:    1   1   1   2   2   3   4    4
```

Why is `dp[-1]` (4) the wrong thing to return in general, even though it happens to be right here?

<details><summary>Answer</summary>
`dp[-1]` only counts subsequences that END at the last element. For `nums = [1,2,8,3,4]` the LIS is `[1,2,3,4]` ending at index 4 anyway — but try `nums = [1,2,8,3]`: LIS is `[1,2,3]` (len 3) ending at index 3, while `dp[-1] = 2` (subsequences ending at 3 are `[1,3]`/`[2,3]`). Always return `max(dp)`.
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Fibonacci — off-by-one base

```python
def fib(n):
    dp = [0] * (n + 1)
    dp[0] = 1                # BUG
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

**Hint:** Check `fib(0)` and `fib(2)`.

<details><summary>Answer</summary>

**Bug:** `dp[0] = 1` shifts everything: `fib(2)` returns 2 instead of 1, `fib(0)` returns 1 instead of 0. Also crashes on `fib(0)` with IndexError on `dp[1]`.
**Fix:** `dp[0] = 0`, and guard `if n <= 1: return n` before allocating (or handle `n == 0` first).
</details>

---

## Debug 02 (Medium): House robber — skipping the wrong house

```python
def rob(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])   # BUG
    return dp[-1]
```

**Hint:** What happens at `i = 1`? And on `nums = [5]`?

<details><summary>Answer</summary>

**Bugs:** (1) At `i=1`, `dp[i-2]` is `dp[-1]` — Python's negative indexing reads the *last* element (which is 0, luckily — but the logic is still wrong-by-accident, and if `len(nums)==2`, `dp[-1]` is that last cell = 0, so `rob([1,5])` returns max(1, 5+0)=5 by luck). (2) `nums=[5]` → `dp[0]=nums[0]` then loop doesn't run → returns 5, ok; but `nums=[]` → IndexError.
**Fix:** guard `n <= 2` cases, or use the rolling form:
```python
prev2 = prev1 = 0
for x in nums:
    prev2, prev1 = prev1, max(prev1, x + prev2)
return prev1
```
The rolling form has no negative-index landmine.
</details>

---

## Debug 03 (Medium): Coin change — unreachable cells seeded with 0

```python
def coin_change(coins, amount):
    dp = [0] * (amount + 1)              # BUG: all zeros
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])   # min with 0 → always 0?
    return dp[amount]
```

**Hint:** What is `min(0, anything)`?

<details><summary>Answer</summary>

**Bug:** `dp` starts at 0, so `min(dp[a], 1 + dp[a-c])` is `min(0, positive)` = 0 forever — every answer is 0. Also `dp[a-c]` for an *unreachable* `a-c` is 0, so even fixing the seed naively is dangerous.
**Fix:**
```python
INF = amount + 1
dp = [INF] * (amount + 1)
dp[0] = 0
...
return dp[amount] if dp[amount] != INF else -1
```
Only `dp[0]` is reachable at the start; `inf` cells stay `inf` because `1 + inf` never wins a `min`.
</details>

---

## Debug 04 (Hard): Word break — no memoization

```python
def word_break(s, wordDict):
    def helper(i):
        if i == len(s):
            return True
        return any(s.startswith(w, i) and helper(i + len(w))
                   for w in wordDict)          # BUG: recomputes
    return helper(0)
```

**Hint:** Try `s = "a" * 30`, `wordDict = ["a", "aa"]`. Count the calls.

<details><summary>Answer</summary>

**Bug:** Correct but exponential — `helper(i)` recomputes for every path that reaches `i`, and with `["a","aa"]` nearly every index is reachable two ways → ~2ⁿ calls. On `s = "aaaa...aab"` (all reachable, all fail at the end) it hangs.
**Fix:** memoize on `i`:
```python
from functools import lru_cache
@lru_cache(maxsize=None)
def helper(i): ...
```
or convert to bottom-up: `dp[i]` = "`s[:i]` segmentable", `dp[i] = any(dp[j] and s[j:i] in words)`.
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: Answer read from the wrong cell
```python
# WRONG for LIS — LIS can end before the last element
return dp[-1]

# CORRECT
return max(dp)          # or track best during the fill
```
Also: min-cost-stairs returns `min(dp[-1], dp[-2])`, not `dp[-1]` — the top is past the end.

## Mistake 02: Unreachable states = 0
```python
# WRONG — min() treats unreachable as free
dp = [0] * (amount + 1)

# CORRECT — inf never wins a min; check at the end
INF = amount + 1
dp = [INF] * (amount + 1)
dp[0] = 0
return dp[amount] if dp[amount] != INF else -1
```

## Mistake 03: Negative index reads in early cells
```python
# WRONG — at i=1, dp[i-2] is dp[-1] (the LAST cell), silently wrong
for i in range(1, n):
    dp[i] = max(dp[i-1], nums[i] + dp[i-2])

# CORRECT — seed dp[0] and dp[1] before the loop, or roll two variables
dp[1] = max(nums[0], nums[1])
for i in range(2, n):
    ...
```

## Mistake 04: Greedy where DP belongs
```python
# WRONG — biggest-coin-first fails [1,3,4] amount 6 (greedy: 4+1+1; optimal: 3+3)
# CORRECT — dp[a] = 1 + min(dp[a-c]) over all c <= a
```
Rule: greedy needs a proof; DP needs a recurrence. When in doubt, DP.

## Mistake 05: Memoizing a key that loses state
```python
# WRONG — two different remaining-suffix problems collide if you key by len(i)
# or forget part of the state (e.g., index AND something else the problem needs)

# CORRECT — key = everything that distinguishes one subproblem from another
@lru_cache(None)
def solve(i):        # i fully determines s[i:]
    ...
```

## Mistake 06: Confusing `dp[0]` conventions
- Count-ways: `dp[0] = 1` ("one way to choose nothing")
- Min-cost: `dp[0] = 0` ("zero cost to reach the start")
- Can-reach: `dp[0] = True`

Pick the wrong convention and every downstream cell inherits the error.

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Full table → rolling variables
### Before
```python
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```
### Problems
1. O(n) space for a recurrence that only reads two cells back.

### After
```python
def climb_stairs(n):
    a, b = 1, 2                     # ways(1), ways(2)
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b if n >= 2 else n       # n in {0? ,1,2}: handle small n
```
(or keep the `if n <= 2: return n` guard for clarity — the lesson is the two rolling variables.)

---

## Refactor 02 (Medium): Manual memo dict → `@lru_cache`
### Before
```python
memo = {}
def fib(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```
### Problems
1. Boilerplate hides the recurrence; easy to forget the store line.

### After
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    return n if n <= 1 else fib(n - 1) + fib(n - 2)
```

---

## Refactor 03 (Hard): Inner `any` with slicing → explicit loop (word break)
### Before
```python
return any(s.startswith(w, i) and helper(i + len(w)) for w in wordDict)
```
### Problems
1. Works, but `any` short-circuits invisibly — harder to debug which word succeeded when tracing.
2. If `wordDict` is large and `s` long, iterating all words per index is wasteful; iterate word-lengths instead.

### After
```python
maxlen = max(map(len, words)) if words else 0
for L in range(1, maxlen + 1):
    if i + L <= len(s) and s[i:i+L] in words and helper(i + L):
        return True
return False
```
Same answer; now the matching candidates are bounded by word length, not dictionary size — and you can print/trace each candidate.

---

## Approach Comparison — different ways to solve it

## Problem: Coin change (fewest coins)

### Approach 1: top-down memoized recursion
```python
@lru_cache(None)
def min_coins(a):
    if a == 0: return 0
    if a < 0: return INF
    return 1 + min(min_coins(a - c) for c in coins)
```
**Pros:** recurrence falls straight out of the problem statement. **Cons:** recursion depth = amount (limit risk at amount ~10⁴+); computes unreachable-state checks as exceptions.

### Approach 2: bottom-up table (this lesson)
```python
dp = [INF] * (amount + 1); dp[0] = 0
for a in range(1, amount + 1):
    for c in coins:
        if c <= a:
            dp[a] = min(dp[a], 1 + dp[a - c])
```
**Pros:** O(amount × #coins), no recursion limit, iteration order explicit. **Cons:** computes every amount 0..amount even if only a few are reachable.

### Approach 3: BFS over amounts
```python
# level-order from 0; first time we hit `amount`, depth = min coins
```
**Pros:** stops at the exact answer depth; elegant for small amounts. **Cons:** visited-set bookkeeping ≈ the dp table anyway; not obviously faster.

**Winner:** Approach 2 for interviews — predictable, bounded, easy to explain. Mention Approach 1 as "the same recurrence, top-down" to show you see both directions.

---

## Problem: Longest increasing subsequence

### Approach 1: O(n²) DP (this lesson)
```python
dp = [1] * n          # dp[i] = LIS ending at i
for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
return max(dp)
```
**Pros:** recipe-shaped; easy to write under pressure. **Cons:** O(n²), ~10⁴ element limit.

### Approach 2: O(n log n) patience sorting
```python
import bisect
tails = []                     # tails[k] = smallest tail of an LIS of length k+1
for x in nums:
    i = bisect.bisect_left(tails, x)
    if i == len(tails): tails.append(x)
    else: tails[i] = x
return len(tails)
```
**Pros:** O(n log n) — interview gold if you can explain `tails` is NOT the LIS itself but a proxy for its length. **Cons:** doesn't reconstruct the subsequence; trickier to justify on a whiteboard.

**Winner:** write Approach 1 first, then say "this can be O(n log n) with binary search on tails" — shows range without gambling on the harder implementation.
