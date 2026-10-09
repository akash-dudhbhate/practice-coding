# 08 — Min-Cost Stairs: when the answer ISN'T dp[n-1]

> 6-minute read. Same stairs as ch.05, but now they charge a toll — and recipe step 5 bites.

## The idea, plain words

> Each stair `i` charges a toll `cost[i]` the moment you step on it.
> You may **start at stair 0 or stair 1 for free**, climb 1 or 2 at a
> time. Cheapest way to reach the *top* — which is one step PAST the
> last stair?

Real-life version: a toll-bridge staircase. You can hop on at the first
or second step free; every step after costs. The exit is *beyond* the
top step.

Last-move thinking again: to stand on stair `i` you paid `cost[i]`, and
you arrived either from `i-1` or `i-2` — whichever route was cheaper:

```
dp[i] = cost[i] + min( dp[i-1], dp[i-2] )
```

## Watch the table fill — cost = [10, 15, 20]

```
i:        0    1    2
          ──────────────
init:    10   15    _        base cases: starting there is free → pay toll only
i=2:     10   15   30        dp[2] = 20 + min(15, 10) = 30
```

Now the trap — what's the answer? **Not `dp[2]`.** The top is PAST the
last stair, and you can exit by stepping off from stair 2 (cost 30) OR
jumping over it from stair 1 (cost 15):

```
Answer: min(dp[2], dp[1]) = min(30, 15) = 15
  → start at stair 1 (free), pay 15, leap clean over stair 2 to the top.
```

A bigger trace — cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]:

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
  → route 0→2→4→6→(7)→9 then off the top — we hopped over both 100-tolls.
```

```python
def min_cost(cost):
    n = len(cost)
    dp = cost[:]                    # dp[i] = min cost to STAND on stair i
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    return min(dp[n - 1], dp[n - 2])
```

Verified: `min_cost([10,15,20])` → 15,
`min_cost([1,100,1,1,1,100,1,1,100,1])` → 6.

## Why it exists

It's recipe **step 5 made flesh**: same stairs as ch.05, nearly the same
recurrence — but "the top" isn't a stair, so `dp[n-1]` alone is wrong.
Whenever the goal sits *beyond* the array, expect a `min(dp[-1], dp[-2])`
or similar finishing move.

## Where it's used

`medium/p02`. The general lesson: always re-read the problem asking
*where does the answer live* — `dp[n-1]`, `dp[amount]`, `max(dp)`, or a
`min` over the last few cells.

## Common mistake

Returning `dp[n-1]` = 30 instead of 15 in the first trace. It *runs*,
it's plausible — and it's wrong. Also: seeding `dp[0] = 0` ("starting is
free") — free means you skip the *approach* cost, not the toll. Standing
on stair 0 still costs `cost[0]`.

## Your turn

`min_cost([1, 2, 3])` — table and answer?

<details><summary>Answer</summary>
`dp = [1, 2, 4]` (dp[2] = 3 + min(2,1) = 4). Answer =
`min(dp[2], dp[1]) = min(4, 2) = 2` — start at stair 1, pay 2, jump
over stair 3 to the top.
</details>

---

**← Prev** [07 — House robber](07-house-robber.md) ·
**Next →** [09 — Coin change](09-coin-change.md)
