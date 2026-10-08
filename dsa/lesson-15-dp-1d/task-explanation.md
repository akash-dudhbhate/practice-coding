# Lesson 15 — 1D Dynamic Programming

## What you'll learn
- The two requirements for DP: overlapping subproblems + optimal substructure
- Top-down (memoization) vs bottom-up (tabulation) — and space optimization
- The five-step recipe: state → recurrence → base cases → fill order → answer location
- The three tell-tale phrasings: "count ways", "min/max cost", "can you reach"

## Lesson

DP = recursion that remembers. Define `dp[i]` in one sentence, write how it
depends on earlier cells, seed the base cases, fill in dependency order, and
return the answer from the right cell.

### The skeleton
```python
dp = [BASE] * (n + 1)            # or {} / @lru_cache for top-down
dp[0] = ...                      # base cases
for i in range(1, n + 1):
    dp[i] = f(dp[<earlier>])     # recurrence: max / min / sum / any
return dp[n]                     # ...or max(dp), or min(dp[-1], dp[-2])
```

Space optimization: when `dp[i]` only reads `dp[i-1]`, `dp[i-2]`, keep just
those in rolling variables — O(n) → O(1) space.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here) — the Fibonacci family
1. `easy/p01-fib-memoized.py` — `fib(n)` → nth Fibonacci number, `fib(0)=0, fib(1)=1`.
   `fib(10) → 55`, `fib(50) → 12586269025` — must be memoized/tabulated, naive recursion times out.
2. `easy/p02-climbing-stairs.py` — `climb_stairs(n)` → number of ways to climb `n` stairs stepping 1 or 2 at a time.
   `climb_stairs(2) → 2`, `climb_stairs(5) → 8`, `climb_stairs(45) → 1836311903`.
3. `easy/p03-tribonacci.py` — `tribonacci(n)` → `T(0)=0, T(1)=1, T(2)=1, T(n)=T(n-1)+T(n-2)+T(n-3)`.
   `tribonacci(4) → 4`, `tribonacci(25) → 1389537`, `tribonacci(37) → 2082876103`.

### Medium — real 1D DP recurrences
4. `medium/p01-house-robber.py` — `rob(nums)` → max money robbing houses with no two adjacent.
   `[1,2,3,1] → 4` (houses 0,2), `[2,7,9,3,1] → 12`, `[2,1,1,2] → 4` (ends win), `[] → 0`.
5. `medium/p02-min-cost-climbing-stairs.py` — `min_cost(cost)` → min toll to reach the top; may start at index 0 or 1; top is *past* the last stair.
   `[10,15,20] → 15`, `[1,100,1,1,1,100,1,1,100,1] → 6`. Answer is `min(dp[n-1], dp[n-2])`, not `dp[n-1]`.
6. `medium/p03-coin-change-min-coins.py` — `coin_change(coins, amount)` → fewest coins to make `amount`; `-1` if impossible.
   `[1,2,5], 11 → 3` (5+5+1), `[2], 3 → -1`, `[1], 0 → 0`. Seed unreachable cells with `inf`, not 0.

### Hard — DP on sequences
7. `hard/p01-word-break.py` — `word_break(s, wordDict)` → can `s` be segmented into dictionary words? (Reuse allowed.)
   `"leetcode", ["leet","code"] → True`; `"catsandog", ["cats","dog","sand","and","cat"] → False`;
   `"aaaaaaa", ["aaaa","aaa"] → True` (the memoization stress case).
8. `hard/p02-longest-increasing-subsequence.py` — `length_of_lis(nums)` → length of the longest strictly increasing subsequence (not necessarily contiguous).
   `[10,9,2,5,3,7,101,18] → 4` (`[2,3,7,101]` or `[2,5,7,18]`), `[7,7,7] → 1`, `[] → 0`.
   O(n²) is expected — note the O(n log n) patience-sorting variant exists. Answer is `max(dp)`, not `dp[-1]`.
9. `hard/p03-partition-equal-subset-sum.py` — `can_partition(nums)` → can the array split into two subsets with equal sum?
   `[1,5,11,5] → True` (`[1,5,5]` vs `[11]`), `[1,2,3,5] → False`. Trick: it's subset-sum targeting `total // 2` — a "can you reach" DP over achievable sums.

### How to work
- Read `concepts.md` first — every problem maps to one of the three phrasings.
- For each problem, write the five recipe steps in comments BEFORE coding: state / recurrence / base / order / answer.
- Run `python3 check.py easy/p01` for one problem, `python3 check.py all` for all nine.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has debug drills after you finish.
- Peek at `solutions/` only after a real attempt — then close it and redo from memory.
