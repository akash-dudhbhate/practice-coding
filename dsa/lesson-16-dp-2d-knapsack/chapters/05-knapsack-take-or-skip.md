# 05 — 0/1 Knapsack: Take It or Leave It

> 7-minute read. THE canonical 2D DP. Go slow — it's worth it.

## The idea, plain words

You're packing a bag that holds `W` kilograms. Each item has a weight and a
value. Each item is **take it or leave it** — no halves, no repeats (that's
the "0/1"). Maximize the value inside.

Real-life version: **packing a suitcase for a flight.** Weight limit is
real; every item is a yes/no decision.

The sentence (chapter 3): **`dp[i][w]` = best value using the first `i`
items with a bag of capacity `w`.**

For each item, exactly two moves exist:

```
dp[i][w] = max(
    dp[i-1][w],                          # SKIP item i — keep the old answer
    value[i-1] + dp[i-1][w - wt[i-1]]    # TAKE it — its value + best with the room left
)
```

Take it **only if it fits** (`wt[i-1] <= w`). "Take" asks the *previous row*
what's achievable with `w - wt` room left — that's the genius: the item's
weight is spent inside the lookup.

## The trace — 3 items, bag of 4

Items: `(wt 1, val 2)`, `(wt 3, val 4)`, `(wt 2, val 3)`. `W = 4`.

```
              capacity w →
        0    1    2    3    4
i=0  [  0    0    0    0    0  ]   no items → all 0
i=1  [  0    2    2    2    2  ]   item (1,2): fits whenever w ≥ 1
i=2  [  0    2    2    4    6  ]   item (3,4)
i=3  [  0    2    3    5    6  ]   item (2,3)
```

Cell by cell for row 2 — item `(wt 3, val 4)`:

```
w=2: 3 > 2, doesn't fit → dp[2][2] = dp[1][2] = 2          ← SKIP (forced)
w=3: max(skip: dp[1][3]=2,  take: 4 + dp[1][0]=4) = 4      ← TAKE it alone
w=4: max(skip: dp[1][4]=2,  take: 4 + dp[1][1]=6) = 6      ← TAKE both items!
```

Row 3 — item `(wt 2, val 3)`:

```
w=2: max(skip: 2, take: 3 + dp[2][0]=3) = 3                ← TAKE
w=3: max(skip: 4, take: 3 + dp[2][1]=5) = 5                ← TAKE (items 1+3)
w=4: max(skip: 6, take: 3 + dp[2][2]=5) = 6                ← SKIP wins!
```

Answer: `dp[3][4] = 6` — items 1+2 (weight `1+3=4`, value `2+4=6`).

Notice the last cell is a **skip**. The table's job is to have *considered*
item 3, not to force it in. The best set was already found one row earlier.

## The code

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wt, val = weights[i - 1], values[i - 1]   # row i means item i-1!
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]                                # skip
            if wt <= w:
                dp[i][w] = max(dp[i][w], val + dp[i - 1][w - wt])  # take
    return dp[n][W]
```

Verified: `knapsack([1,3,2],[2,4,3], 4)` → `6` ·
`knapsack([1,3,4,5],[1,4,5,7], 7)` → `9`.

## Why it exists

Trying all subsets is `2ⁿ` — 30 items is a billion sets. The table notices
that "best with capacity `w`" is the same question no matter which items got
you there, so `n × W` cells replace the exponential search.

## Where it's used

Budget allocation, cargo loading, picking tasks for limited time — any
"choose a subset under a hard limit" problem. It's also the pattern behind
coin-counting and subset-sum problems (see `medium/p03`).

## Common mistake

The `i-1` shift. Row `i` means "first `i` items", so its weight lives at
`weights[i-1]`. Write `weights[i]` and every row quietly uses the wrong
item — the table fills fine and the answer is wrong. Say the sentence out
loud: "*first* `i` items" → index `i-1`.

## Your turn

In the table above, what does `dp[2][4] = 6` say in the sentence template,
and which items produce it?

<details><summary>Answer</summary>
"Best value using the first 2 items with capacity 4 is 6" — items
`(wt1,val2)` + `(wt3,val4)` exactly fill the bag: weight 4, value 2+4=6.
</details>

---

**← Prev** [04 — Min path sum & walls](04-min-path-sum-and-walls.md) ·
**Next →** [06 — The backwards loop trick](06-the-backwards-loop-trick.md)
