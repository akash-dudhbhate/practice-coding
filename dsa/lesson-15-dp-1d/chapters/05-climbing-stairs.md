# 05 — Climbing Stairs: your first *new* recurrence

> 6-minute read. Fibonacci in disguise — and your first real DP problem.

## The idea, plain words

> You're climbing `n` stairs. Each move is a step of **1 or 2** stairs.
> How many different ways can you reach the top?

The beginner-fear here is "how do I even START?" The trick is to think
about the **last step only**. You're standing ON stair `n`. How did you
arrive? Exactly two possibilities:

- your last step was a **1-step** from stair `n-1`, or
- your last step was a **2-step** from stair `n-2`.

Every complete path ends one of those two ways, and no path ends both
ways. So:

```
ways(n) = ways(n-1) + ways(n-2)
```

Sound familiar? **It's Fibonacci.** You just derived your first
recurrence without being handed one — by asking "what are the possible
last moves?"

```python
def climb_stairs(n):
    if n <= 1:
        return 1               # 1 way to stand at the bottom
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1          # dp[i] = ways to reach stair i
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

## Watch the table fill — n = 5

```
i:      0   1   2   3   4   5
        ─────────────────────
init:   1   1   _   _   _   _    dp[0]=1 (stand still), dp[1]=1 ({1})
i=2:    1   1   2   _   _   _    dp[2] = 1+1  → {1+1, 2}
i=3:    1   1   2   3   _   _    dp[3] = 2+1  → {1+1+1, 2+1, 1+2}
i=4:    1   1   2   3   5   _    dp[4] = 3+2
i=5:    1   1   2   3   5   8    dp[5] = 5+3
Answer: dp[5] = 8 ways
```

Sanity check by hand for `n=3`: {1+1+1, 1+2, 2+1} — 3 ways ✓. Verified:
`climb_stairs(5)` → 8, `climb_stairs(45)` → 1836311903.

## Why it exists

This is the template for every "count the number of ways" problem:
find the possible **last moves**, sum the ways to reach each
starting point of that last move. Coin change (count-ways version),
decode ways, tribonacci — same skeleton, different move set.

## Where it's used

Literally `easy/p02` in this lesson. More broadly: the
"last-move thinking" habit — *don't think about building the whole path,
think about the final choice* — is THE mental move that unlocks 1D DP.

## Common mistake

`dp[0]`: "zero ways to reach stair 0" feels right but is wrong — there's
exactly **one** way to stand at the bottom (do nothing). Seed `dp[0] = 1`
for count-ways problems, or every cell downstream stays 0. Ask yourself:
*what does the empty starting position mean in THIS problem?*

## Your turn

Same problem, but now steps of **1, 2, or 3** are allowed. What's the
recurrence? (Just the formula — code comes in the next chapter.)

<details><summary>Answer</summary>
`ways(n) = ways(n-1) + ways(n-2) + ways(n-3)` — your last step was a
1, a 2, or a 3. Three last-move options → three terms. (This is
tribonacci, `easy/p03` — and it's the worked example in ch.06.)
</details>

---

**← Prev** [04 — Bottom-up tabulation](04-bottom-up-tabulation.md) ·
**Next →** [06 — The 5-step recipe](06-the-five-step-recipe.md)
