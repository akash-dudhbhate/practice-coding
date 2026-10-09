# 12 — Space Optimization: keep only what the recurrence reads

> 5-minute read. O(n) memory → O(1) — the trick that makes interviewers nod.

## The idea, plain words

Look at `dp[i] = dp[i-1] + dp[i-2]` for a moment. To fill cell `i`, you
need… two cells. The other thousand cells you filled? Dead weight —
filled once, read once, never touched again.

Real-life version: keeping only *yesterday's and today's* weather note
on your desk instead of a folder of 365 old notes you'll never re-open.

So instead of an array, keep **two variables** and slide them forward:

```python
def fib(n):
    a, b = 0, 1                 # a = "dp[i-2]" role, b = "dp[i-1]" role
    for _ in range(n):
        a, b = b, a + b         # slide the 2-cell window one step right
    return a
```

Watch the window slide for `fib(7)`:

```
start:   a=0 (fib0)   b=1 (fib1)
step 1:  a=1  b=1      ← compute fib(1)'s next: a+b=1
step 2:  a=1  b=2
step 3:  a=2  b=3
step 4:  a=3  b=5
step 5:  a=5  b=8
step 6:  a=8  b=13
step 7:  a=13 b=21     → return a = 13 = fib(7)  ✓
```

Same answer, **O(1) space**. Verified: `fib(7)` → 13, `fib(10)` → 55.

The same move shrinks house robber — it also only reads `i-1`, `i-2`:

```python
def rob(nums):
    prev2, prev1 = 0, 0                    # dp[i-2], dp[i-1]
    for x in nums:
        prev2, prev1 = prev1, max(prev1, x + prev2)
    return prev1                           # 12 for [2,7,9,3,1] ✓
```

## Why it exists

"O(n) space" is fine; "O(1) space" is the flex that shows you understand
*why* each cell existed. More importantly, it trains the reflex: **the
table is just a convenience — the only memory you truly need is whatever
the recurrence reads.**

## Where it's used — and where it CAN'T be

- ✅ Stairs, tribonacci (needs 3 variables), house robber, min-cost
  stairs — anything reading a fixed few cells back.
- ❌ **LIS** — `dp[i]` reads *every* `dp[j]`, so you need the whole row.
- ❌ **Coin change** — `dp[a]` reads `dp[a-c]` for coins of any size; a
  coin of value 500 reaches back 500 cells. (Bounded tricks exist but
  the general answer is: keep the table.)

Rule of thumb: *how far back does the recurrence reach?* Fixed distance
→ roll it. All-history → keep it.

## Common mistake

Getting the slide backwards. `a, b = b, a + b` works because Python
evaluates the right side BEFORE assigning — `a+b` uses the *old* values.
Writing it as two lines (`a = b; b = a + b`) uses the NEW `a` — every
step is suddenly wrong. If you split it, use a temp variable.

## Your turn

Tribonacci reads `dp[i-1], dp[i-2], dp[i-3]`. How many rolling variables
do you need, and what's the update line?

<details><summary>Answer</summary>
Three: `a, b, c` for `dp[i-3], dp[i-2], dp[i-1]` roles, and
`a, b, c = b, c, a + b + c`. (Seed `a,b,c = 0,1,1` — this is `easy/p03`.)
</details>

---

**← Prev** [11 — Word break](11-word-break.md) ·
**Next →** [13 — Is this a DP problem?](13-is-this-a-dp-problem.md)
