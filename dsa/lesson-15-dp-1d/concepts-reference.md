# Lesson 15 — Concepts Explained (1D Dynamic Programming)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## What DP Actually Is — the two requirements

**What:** Dynamic programming = *recursion with a memory*. A problem qualifies for DP when it has BOTH of these properties:

1. **Overlapping subproblems** — solving the big problem forces you to solve the same small problems over and over. (If the subproblems never repeat, you want divide & conquer like binary search or merge sort, not DP.)
2. **Optimal substructure** — the optimal answer is built from optimal answers to subproblems. `best(n)` is a function of `best(something smaller)`. (If a sub-solution can't be combined cleanly — e.g., "longest path without revisiting nodes" — DP alone won't save you.)

**Why it exists:** Plain recursion recomputes identical subproblems exponentially many times. DP says: *solve each subproblem once, store the answer, look it up next time.* You trade memory for time — usually turning O(2ⁿ) into O(n).

**Where it's used:** Counting paths/ways, min/max cost problems, sequence problems (subsequence, substring, edit distance), resource allocation (knapsack), string segmentation (word break), bioinformatics (gene alignment IS edit distance), compilers, route planning.

**What goes wrong without it:** `fib(50)` by naive recursion does ~2⁵⁰ ≈ 10¹⁵ calls — your laptop needs days. With DP it's 50 additions.

---

## Fibonacci — the gateway drug

**What:** `fib(n) = fib(n-1) + fib(n-2)`, with `fib(0) = 0`, `fib(1) = 1`. The naive recursive version is the poster child for overlapping subproblems.

**The explosion — trace `fib(5)`:**

```
                    fib(5)
                   /      \
              fib(4)        fib(3)          ← fib(3) computed 2nd time...
             /     \        /    \
        fib(3)   fib(2)  fib(2) fib(1)      ← fib(2) appears 3× total
        /   \     /  \    /  \
     fib(2) f(1) f(1) f(0) f(1) f(0)
     /  \
   fib(1) fib(0)

  Recompute count for fib(5):
    fib(3) → 2 times      fib(2) → 3 times      fib(1) → 5 times
  For fib(n), fib(1) is computed ~fib(n) times. Total calls ≈ 2^n.
```

Every repeated subtree is *wasted work* — the answer for `fib(3)` can't change, so computing it twice is pure loss.

**Fix 1 — memoization (top-down):** keep the recursion, add a dict/cache. Before computing, check the cache; after computing, store.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

Now each `fib(k)` runs its body once — ~2n calls total. `fib(50)` → instant.

**Fix 2 — tabulation (bottom-up):** flip the direction. Fill a table from the smallest subproblem up.

```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

**The table filling step by step — `fib(7)`:**

```
i:      0   1   2   3   4   5   6   7
        ─────────────────────────────
init:   0   1   _   _   _   _   _   _      base cases
i=2:    0   1   1   _   _   _   _   _      dp[2] = dp[1]+dp[0] = 1+0
i=3:    0   1   1   2   _   _   _   _      dp[3] = dp[2]+dp[1] = 1+1
i=4:    0   1   1   2   3   _   _   _      dp[4] = dp[3]+dp[2] = 2+1
i=5:    0   1   1   2   3   5   _   _      dp[5] = 3+2
i=6:    0   1   1   2   3   5   8   _      dp[6] = 5+3
i=7:    0   1   1   2   3   5   8   13     dp[7] = 8+5  ← answer sits at dp[n]
```

Read it left to right: **each cell only reads cells to its left**, so a single forward `for` loop is a valid order of computation.

Expected output for `fib(7)`: **13** · `fib(10)`: **55**

---

## Top-Down vs Bottom-Up — same answer, different direction

**What:** Two ways to write the same DP:

| | Top-down (memoization) | Bottom-up (tabulation) |
|---|---|---|
| Direction | Start at the answer, recurse down to base cases | Start at base cases, loop up to the answer |
| Storage | dict or `@lru_cache` | array/list `dp` |
| Stack | uses recursion stack (depth n → recursion limit risk) | no recursion |
| Computes | only reachable states | every state, reachable or not |
| Order of code | recurrence falls out of the recursion | you must figure out a valid fill order |

**Why it exists:** Some problems are easier to *think* top-down (just write the recursion, add `@lru_cache`), and some need the explicit control of bottom-up (space optimization, iteration order). Interviews: top-down is acceptable; bottom-up signals mastery.

**Where it's used:** Memoization shines when only a fraction of states are reachable (sparse state space, e.g., word break with long strings). Tabulation shines when you'll touch every state anyway and want O(1)-ish overhead per cell.

**What goes wrong without it:**
- Memoizing with a dict keyed wrong (forgetting part of the state) → collisions return wrong answers.
- `@lru_cache` on a method/function with unhashable args (list) → TypeError. Convert to tuple or indices.
- Bottom-up fill order wrong: if `dp[i]` reads `dp[i-1]` but you loop `i` downward, every cell reads a stale zero.

**Space optimization — the last trick:** if `dp[i]` only reads `dp[i-1]` and `dp[i-2]`, you never need the whole table — keep the last two values:

```python
def fib(n):
    a, b = 0, 1           # a = fib(i-2) role, b = fib(i-1) role
    for _ in range(n):
        a, b = b, a + b   # slide the two-variable window forward
    return a
```

O(n) time, **O(1) space**. This "keep only what the recurrence reads" move generalizes to almost every DP in this lesson.

---

## The DP Recipe — five steps, every time

1. **Define the state.** "What is `dp[i]`?" — one sentence. E.g., "*`dp[i]` = max money robbing houses `0..i`*". If you can't say it in one sentence, you don't have a state yet.
2. **Write the recurrence.** How does `dp[i]` come from earlier states? Usually it's a choice: take-it-or-skip-it, minimum over predecessors, etc.
3. **Base cases.** The cells that don't need a recurrence: `dp[0]`, `dp[1]`, empty-input answer.
4. **Order of computation.** Which direction fills the table so every cell's dependencies are ready? (For 1D with backward-looking recurrences: left → right.)
5. **Answer location.** Where does the final answer live? Usually `dp[n-1]` — but sometimes `max(dp)`, `dp[amount]`, or a derived value. **Check this — it's the most-forgotten step.**

**Worked example — House Robber, the recipe applied:**

Houses `[2, 7, 9, 3, 1]`, can't rob two adjacent houses, maximize loot.

- **State:** `dp[i]` = max money robbing houses `0..i`.
- **Recurrence:** at house `i` either rob it → `nums[i] + dp[i-2]` (skip `i-1`), or skip it → `dp[i-1]`. Take the max.
- **Base:** `dp[0] = nums[0]`; `dp[1] = max(nums[0], nums[1])`.
- **Order:** left → right (reads `i-1`, `i-2`).
- **Answer:** `dp[n-1]`.

**Table trace:**

```
nums:   [2,  7,  9,  3,  1]
i:       0   1   2   3   4
─────────────────────────────
dp[0] = 2                       (only choice: rob house 0)
dp[1] = max(2, 7) = 7           (rob the richer of the two)
dp[2] = max(dp[1], 9+dp[0])
      = max(7, 9+2) = 11        (rob houses 0,2)
dp[3] = max(dp[2], 3+dp[1])
      = max(11, 3+7) = 11       (skip house 3)
dp[4] = max(dp[3], 1+dp[2])
      = max(11, 1+11) = 12      (rob houses 0,2,4)
Answer: dp[4] = 12
```

```python
def rob(nums):
    if not nums:
        return 0
    prev2, prev1 = 0, 0              # dp[i-2], dp[i-1] — space-optimized
    for x in nums:
        prev2, prev1 = prev1, max(prev1, x + prev2)
    return prev1
```

Expected output for `rob([2,7,9,3,1])`: **12**

---

## Recognizing DP — the three tell-tale phrases

**What:** DP problems almost always phrase as one of:

- **"Count the number of ways…"** → `dp[i]` = number of ways to reach `i`; recurrence sums over last-moves. (Climbing stairs, tribonacci, coin change-2.)
- **"Min/max cost, value, length…"** → `dp[i]` = best achievable at `i`; recurrence takes `min`/`max` over predecessors. (House robber, min-cost stairs, coin change min-coins, LIS.)
- **"Can you reach / is it possible…"** → `dp[i]` = True/False; recurrence is `any(...)` over ways to arrive. (Word break, partition subset sum.)

Plus the structural tell: **at each position you make a small choice among options, and the options only care about *which state you're in*, not *how you got there*.** If history matters (e.g., "can't reuse an element"), that must be folded into the state — that's lesson 16's 2D states.

**What goes wrong without it (trying DP on a non-DP problem):**
- "Longest *path* in a graph with no revisits" — subproblems share nodes but the no-revisit constraint makes each subproblem depend on history → DP fails (it's NP-hard).
- Greedy-vs-DP confusion: "count ways" is never greedy; "min cost" is greedy ONLY if a greedy-choice proof exists — when in doubt, DP is the safe default.

**Worked example — Climbing Stairs, count-ways shape:**

`n` stairs, you step 1 or 2 at a time. `ways(i) = ways(i-1) + ways(i-2)` — to arrive at step `i`, your last step was 1 (from `i-1`) or 2 (from `i-2`).

```
n:      0   1   2   3   4   5
        ─────────────────────
init:   1   1   _   _   _   _    dp[0]=1 (one way to stand at bottom)
i=2:    1   1   2   _   _   _    1+1
i=3:    1   1   2   3   _   _    2+1
i=4:    1   1   2   3   5   _    3+2
i=5:    1   1   2   3   5   8    5+3
Answer: dp[5] = 8
```

It's Fibonacci shifted by one. That recognition — *this problem is secretly the same recurrence* — is the skill this lesson trains.

Expected output for `climb_stairs(5)`: **8**

---

## Min-Cost Climbing Stairs — "start or step" base cases, full trace

**What:** `cost[i]` is the toll for stepping on stair `i`. From a stair you may climb 1 or 2. You may START at stair 0 or stair 1 for free. Find the min cost to reach the top (past the last stair).

- **State:** `dp[i]` = min cost to *stand on* stair `i` (paying `cost[i]`).
- **Recurrence:** `dp[i] = cost[i] + min(dp[i-1], dp[i-2])` — you arrived from one of the two previous stairs.
- **Base:** `dp[0] = cost[0]`, `dp[1] = cost[1]` — starting there is free, you just pay the toll.
- **Answer:** NOT `dp[n-1]` — the top is *past* the last stair, so `min(dp[n-1], dp[n-2])`. This is the "answer location" step biting you.

**Table fill — `cost = [10, 15, 20]`:**

```
i:        0    1    2
          ──────────────
init:    10   15    _        base cases: pay the toll of the start
i=2:     10   15   30        dp[2] = 20 + min(15, 10) = 30
Answer: min(dp[2], dp[1]) = min(30, 15) = 15
  → start at stair 1, jump straight over the top. Never pay 10 or 20.
```

**Second trace — `cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]`:**

```
i:        0   1    2   3   4   5    6   7   8    9
init:     1   100  _   _   _   _    _   _   _    _
i=2:      1   100  2   _   _   _    _   _   _    _    1 + min(100,1)
i=3:      1   100  2   3   _   _    _   _   _    _    1 + min(2,100)
i=4:      1   100  2   3   3   _    _   _   _    _    1 + min(3,2)
i=5:      1   100  2   3   3   103  _   _   _    _    100 + min(3,3)
i=6:      1   100  2   3   3   103  4   _   _    _    1 + min(103,3)
i=7:      1   100  2   3   3   103  4   5   _    _    1 + min(4,103)
i=8:      1   100  2   3   3   103  4   5   104  _    100 + min(5,4)
i=9:      1   100  2   3   3   103  4   5   104  6    1 + min(104,5)
Answer: min(dp[9], dp[8]) = min(6, 104) = 6
  → path 0→2→4→6→9→top. Notice we STEPPED OVER both 100s.
```

```python
def min_cost(cost):
    n = len(cost)
    prev2, prev1 = cost[0], cost[1]        # dp[i-2], dp[i-1]
    for i in range(2, n):
        prev2, prev1 = prev1, cost[i] + min(prev1, prev2)
    return min(prev1, prev2)               # top is past the last stair
```

Expected output for `min_cost([10,15,20])`: **15** · `[1,100,1,1,1,100,1,1,100,1]`: **6**

---

## Memoization on strings — a top-down trace

**What:** Word break: can `"leetcode"` be segmented into `{"leet", "code"}`? Top-down: `can_break(i)` = "can `s[i:]` be segmented?" Try every word matching at position `i`, recurse on the rest, memoize on `i`.

```
can_break(0)  "leetcode"
  ├─ "leet" matches → can_break(4)
  │     ├─ "code" matches → can_break(8) = True (empty suffix!)
  │     └─ "leet"? "code"... doesn't match "code" → dead
  └─ "code" doesn't match at 0 → dead
Answer: True
```

The memo key is just the index `i` — `can_break(4)` computed once, reused forever. Without it, strings like `"aaaa...a"` with `["a","aa"]` blow up exponentially (every prefix admits two branches).

```python
from functools import lru_cache

def word_break(s, wordDict):
    words = set(wordDict)
    @lru_cache(maxsize=None)
    def can_break(i):
        if i == len(s):
            return True
        return any(s.startswith(w, i) and can_break(i + len(w))
                   for w in words)
    return can_break(0)
```

Expected output for `word_break("leetcode", ["leet","code"])`: **True**

---

## Coin Change — the "min over choices" shape, full trace

**What:** `coins = [1, 2, 5]`, `amount = 11`. Fewest coins summing to `amount`; `-1` if impossible.

- **State:** `dp[a]` = fewest coins to make `a`.
- **Recurrence:** `dp[a] = 1 + min(dp[a - c])` over coins `c ≤ a`.
- **Base:** `dp[0] = 0`; everything else starts at `inf` (unreachable).
- **Order:** `a` from 1 → 11 (each `dp[a]` reads strictly smaller indices).
- **Answer:** `dp[11]` — `-1` if still `inf`.

**Table fill for `dp[0..11]`, coins [1,2,5]:**

```
a:        0   1   2   3   4   5   6   7   8   9   10  11
          ───────────────────────────────────────────────
init:     0   ∞   ∞   ∞   ∞   ∞   ∞   ∞   ∞   ∞   ∞   ∞
a=1:      0   1   .   .   .   .   .   .   .   .   .   .   1+dp[0]
a=2:      0   1   1   .   .   .   .   .   .   .   .   .   min(1+dp[1], 1+dp[0])
a=3:      0   1   1   2   .   .   .   .   .   .   .   .   min(1+dp[2],1+dp[1])
a=4:      0   1   1   2   2   .   .   .   .   .   .   .   min(1+dp[3],1+dp[2])
a=5:      0   1   1   2   2   1   .   .   .   .   .   .   1+dp[0]=1 (single 5!)
a=6:      0   1   1   2   2   1   2   .   .   .   .   .   min(1+dp[5],1+dp[4],1+dp[1])
a=7:      0   1   1   2   2   1   2   2   .   .   .   .   min(1+dp[6],1+dp[5],1+dp[2])
a=8:      0   1   1   2   2   1   2   2   3   .   .   .   min over dp[7],dp[6],dp[3]
a=9:      0   1   1   2   2   1   2   2   3   3   .   .   min over dp[8],dp[7],dp[4]
a=10:     0   1   1   2   2   1   2   2   3   3   2   .   1+dp[5] (a 5 + a 5)
a=11:     0   1   1   2   2   1   2   2   3   3   2   3   min(1+dp[10],1+dp[9],1+dp[6])
Answer: dp[11] = 3   (5 + 5 + 1)
```

Note the `∞` convention: unreachable states stay `inf` and `min` ignores them naturally — but you must initialize to `inf`, not `0`, or `min` thinks impossible amounts are free.

```python
def coin_change(coins, amount):
    INF = amount + 1                    # "infinity" that fits in an int
    dp = [INF] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != INF else -1
```

Expected output for `coin_change([1,2,5], 11)`: **3**

---

## The Pitfall Gallery — five ways DP goes wrong

**1. Wrong/missing base case.** `dp[0] = 1` for counting ("one way to make nothing") vs `dp[0] = 0` for min-cost. Swap them and every answer is off by exactly the seed. Ask: *what does the empty prefix mean in THIS problem?*

**2. Unreachable states seeded to 0.** For min-problems, impossible cells must be `inf`. `dp[a] = 1 + min(...)` over `inf`s yields `inf` — correct. If they're `0`, impossible looks free → garbage answers.

**3. Wrong fill order.** If `dp[i]` reads `dp[i-1]`, looping `i` from high→low reads uninitialized cells. For 1D backward-looking recurrences: loop ascending. If a recurrence reads `i-1` AND `i+1` (rare), that's a signal the problem needs a different formulation — DP requires a DAG of dependencies.

**4. Answering from the wrong cell.** `dp[n-1]` vs `max(dp)` vs `dp[target]` vs `sum(dp)`. In LIS the answer is `max(dp)`, not `dp[n-1]` — the longest increasing subsequence can end anywhere.

**5. Greedy temptation.** "Use the biggest coin" fails coin change: `[1, 3, 4]` amount `6` — greedy takes 4+1+1 (3 coins), DP finds 3+3 (2). Whenever greedy has a counterexample, DP is the honest answer.

**Edge cases to always test:** `n = 0` / empty input (decide the convention), `n = 1`, impossible inputs (return `-1`/`False`, don't crash), single-element arrays, and inputs where the answer equals an extreme (all elements, none).

---

## Recipe recap — recognize DP in 10 seconds

1. Does it ask "count ways", "min/max", or "can you reach"? → DP candidate.
2. Can you define `dp[i]` in one sentence? → you have a state.
3. Does `dp[i]` depend only on earlier `dp[...]` cells? → recurrence + order exist.
4. Overlapping subproblems confirmed? (Would naive recursion recompute?) → DP pays off.
5. Say complexity out loud: **O(n) states × O(choices) work** — e.g., coin change is O(amount × #coins).
