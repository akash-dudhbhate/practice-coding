# 09 — Coin Change: min over choices, and why ∞ matters

> 7-minute read. The "minimum" version of counting — plus the greedy trap.

## The idea, plain words

> Coins `[1, 3, 4]`, target amount `6`. Fewest coins possible?

First, seductive wrong answer: **greedy** — grab the biggest coin that
fits. `4` + `1` + `1` → 3 coins. But `3 + 3` → **2 coins**. Greedy
failed; we'll come back to that.

DP thinking — last-move style: to make amount `a`, your last coin was
some `c`. Before it, you needed `a - c`, optimally. So:

```
dp[a] = 1 + min( dp[a-c] )   over all coins c ≤ a
```

## Watch the table fill — coins [1,3,4], amount 6

```
a:        0   1   2   3   4   5   6
          ─────────────────────────
init:     0   ∞   ∞   ∞   ∞   ∞   ∞     dp[0]=0: "no coins make 0"
a=1:      0   1   .   .   .   .   .     only coin 1 fits → 1+dp[0]=1
a=2:      0   1   2   .   .   .   .     1+dp[1]=2 (coins 3,4 too big)
a=3:      0   1   2   1   .   .   .     min(1+dp[2], 1+dp[0]) → 3 = 1
a=4:      0   1   2   1   1   .   .     min(1+dp[3],1+dp[1],1+dp[0]) → 4 = 1
a=5:      0   1   2   1   1   2   .     min(1+dp[4],1+dp[2],1+dp[1]) → 2 (4+1)
a=6:      0   1   2   1   1   2   2     min(1+dp[5],1+dp[3],1+dp[2]) → 2 (3+3)
Answer: dp[6] = 2   ← greedy said 3. DP found the better way.
```

## What's the ∞ doing there?

`∞` means "**can't make this amount yet.**" Two jobs:

- `1 + min(∞, ...)` stays `∞`-big → impossible routes lose the `min`
  naturally.
- At the end, `dp[amount] == ∞` → return `-1` ("impossible").

If you seeded unreachable cells with `0` instead, `min` would think
"impossible" is *free* — `dp[5]` would "cost" 1 coin via a route that
doesn't exist. Seed min-problems with something huge, count-problems
with `dp[0]=1`, and your table stays honest.

```python
def coin_change(coins, amount):
    INF = amount + 1                    # biggest real answer is `amount`
    dp = [INF] * (amount + 1)           # (all 1-coins) — so this is "∞"
    dp[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != INF else -1
```

Verified: `coin_change([1,3,4], 6)` → 2, `coin_change([1,2,5], 11)` → 3
(5+5+1), `coin_change([2], 3)` → -1.

## Why it exists

Some problems have no greedy shortcut — every locally-greedy move can be
globally wrong. DP tries *every* last coin and keeps the best, so it
never falls for the shiny big coin. When greedy lacks a proof, DP is the
honest answer.

## Where it's used

`medium/p03`. Also: min jumps to reach an index, fewest operations to
reduce a number, minimum perfect squares summing to n — same "min over
last move" shape.

## Common mistake

Two, related: (1) initializing unreachable states to `0` (see above —
garbage answers), and (2) forgetting the `-1` check, so `dp[amount]`
returns `INF` = a nonsense "12 coins" for an impossible target.

## Your turn

With coins `[2]` and amount `3`, what does the table look like, and what
is returned?

<details><summary>Answer</summary>
`dp = [0, ∞, 1, ∞]` — odd amounts are unreachable (only coin 2 exists),
`dp[3]` stays `INF` → return **-1**. The `∞` convention is what turns
"impossible" into a clean answer instead of a wrong number.
</details>

---

**← Prev** [08 — Min-cost stairs](08-min-cost-climbing-stairs.md) ·
**Next →** [10 — Longest increasing subsequence](10-longest-increasing-subsequence.md)
