# 06 — The Backwards Loop Trick: One Row Instead of n

> 6-minute read. The single most-asked knapsack trick. Watch the bug first.

## The idea, plain words

Look at the knapsack code again: row `i` only ever reads row `i-1`. The
whole `(n+1) × (W+1)` table exists mostly to be thrown away — you only need
the **previous row** while filling the current one.

So: keep two rows (`prev`, `cur`). Space drops from O(n·W) to O(W).

Then the famous move: you don't even need two rows. **One** row works — if
you fill it in the right direction.

## Why direction matters — the bug, demonstrated

With one row `dp[w]`, the "take" branch reads `dp[w - wt]`. For that to mean
"*previous* row's value" — i.e. item not yet taken — `dp[w - wt]` must not
have been overwritten this pass. Since `w - wt < w`, overwriting **from
small to large** destroys it. Go **large to small** and it survives.

One item `(wt 2, val 3)`, bag `W = 4`. Correct answer: `3` (take it once —
0/1!). Watch both directions:

```python
W, wt, val = 4, 2, 3

# FORWARDS — the bug
dp = [0] * (W + 1)
for w in range(wt, W + 1):
    dp[w] = max(dp[w], val + dp[w - wt])
print("forwards :", dp)
# forwards : [0, 0, 3, 3, 6]   ← dp[4]=6 says "two copies" — impossible!

# BACKWARDS — correct 0/1
dp = [0] * (W + 1)
for w in range(W, wt - 1, -1):
    dp[w] = max(dp[w], val + dp[w - wt])
print("backwards:", dp)
# backwards: [0, 0, 3, 3, 3]   ← dp[4]=3 — taken exactly once
```

Read the forwards pass like a story:

```
w=2: dp[2] = 3 + dp[0] = 3        took the item  → dp[2]=3
w=4: dp[4] = 3 + dp[2] = 3 + 3    read dp[2] AFTER it was overwritten
                                  → took the SAME item twice → 6
```

Forwards, `dp[w - wt]` is already "this item included". Backwards, it still
holds last row's answer. Same loop — direction is the difference between
0/1 knapsack and **unbounded** knapsack (items reusable).

## The full 1-row knapsack

```python
def knapsack_1row(weights, values, W):
    dp = [0] * (W + 1)
    for i in range(len(weights)):
        wt, val = weights[i], values[i]
        for w in range(W, wt - 1, -1):     # DOWN — don't reuse the item
            dp[w] = max(dp[w], val + dp[w - wt])
    return dp[W]
```

Verified: `knapsack_1row([1,3,4,5],[1,4,5,7], 7)` → `9` — same answer as the
full table from chapter 5, with one row.

## Why it exists

`n = 10⁴` items × `W = 10⁵` capacity is a **billion-cell** table — gigabytes.
One row of `W+1` ints is ~megabytes. Interviewers ask for this optimization
by name.

## Where it's used

- **Knapsack family:** 1 row + backwards `w`.
- **LCS / edit distance:** 2 rolling rows (`prev`, `cur`) — they read the
  diagonal too, so a single row needs an extra saved variable.
- **Grid DP:** 1 row — or even zero extra space by overwriting `grid`
  itself (only if mutating the input is allowed!).

## Common mistake

- Rolling rows when the recurrence reads `dp[i-2]` — you deleted a row you
  still need. Check which rows the recurrence touches FIRST.
- `range(wt, W+1)` (ascending) → silently becomes unbounded knapsack;
  answers come out *too big* and it's maddening to spot.
- In-place grid DP that destroys input the caller still needed — copy first.

## Your turn

Why does the backwards loop start at `W` and stop at `wt` (not `0`)?

<details><summary>Answer</summary>
`w` is the capacity; below `wt` the item can't fit, so those cells keep the
skip answer — no work needed. Below `wt`, `w - wt` would also go negative.
Stopping early is both correct and free speed.
</details>

---

**← Prev** [05 — Knapsack](05-knapsack-take-or-skip.md) ·
**Next →** [07 — LCS: comparing two strings](07-lcs-two-strings.md)
