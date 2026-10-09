# 11 — The Pitfall Gallery: Five Ways 2D DP Goes Wrong

> 5-minute read. Every bug here is real — learn them on paper, not in prod.

## The idea, plain words

These aren't hypothetical bugs — they're the five that show up in every
2D DP code review. You don't debug them by staring at your code; you
recognize the *pattern* ("too-big answer → check the loop direction").
Learn the shapes once, spot them forever.

## The five classics

**1. Off-by-one between index and count.**
`dp[i]` means "first `i` items" → the item lives at `items[i-1]`.
`weights[i]` instead of `weights[i-1]` shifts every take/skip by one item.
The table fills fine. The answer is wrong. *Fix:* say the sentence
("first `i` items") before indexing.

**2. Forgetting the base row/column — or zeroing a min problem's borders.**
Row 0 / col 0 = "empty world". `0` is honest for counting (no items → 0
value) but a lie for min problems: `dp[0][j] = 0` claims empty→`b[:j]` is
free. *Fix:* min problems seed borders with real costs (`i`/`j` deletes/
inserts, accumulated tolls); count problems seed with `0`/`1`s.

**3. Fill order violating the arrows.**
`dp[i][j]` reads ↑, ←, ↖ — row-major top-left→bottom-right has them ready.
Fill column-major and you read unwritten cells. Interval DP needs
*by-length* order, not row-major. *Fix:* draw the arrows first, then pick
loops that respect them.

**4. Obstacle cells polluting borders.**
A wall at `dp[0][1]` must zero the *rest of that row* — paths can't hop
walls. Writing the whole border as `1`s leaks routes through walls.
*Fix:* seed borders as "copy previous cell unless I'm a wall".

**5. Iterating the 1-row knapsack upward.**
`range(wt, W+1)` lets each item be reused (chapter 6 showed `dp[4]=6` for a
single item!). 0/1 needs `range(W, wt-1, -1)`. *Fix:* `w` descends.

## Edge cases to always test

- **Empty inputs:** no items, empty string, 1×1 grid → answer often lives
  in the border (`dp[0][*]`).
- **Impossible targets:** nothing fits in the bag → `0`; no common chars →
  `0`; all walls → `0`.
- **Capacity/amount `0`:** honest `0` for knapsack; for coin-combination
  counting it's `1` (one way: choose nothing!) — check the problem.
- **Borders as the whole answer:** `edit_distance("", "abc")` = `dp[0][3]`.
- **Blocked start/end cells** in grid problems.

## A runnable self-check

```python
def knapsack(weights, values, W):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        wt, val = weights[i - 1], values[i - 1]
        for w in range(W + 1):
            dp[i][w] = dp[i - 1][w]
            if wt <= w:
                dp[i][w] = max(dp[i][w], val + dp[i - 1][w - wt])
    return dp[n][W]

print(knapsack([], [], 10))          # no items        → 0
print(knapsack([5], [10], 4))        # nothing fits    → 0
print(knapsack([5], [10], 0))        # zero capacity   → 0
print(knapsack([1], [1], 100))       # one tiny item   → 1
```

Output:

```
0
0
0
1
```

## Your turn

Spot the bug — run it. One item `(wt 2, val 3)`, bag `4`: correct is `3`:

```python
weights, values, W = [2], [3], 4           # one item, correct answer is 3

dp = [0] * (W + 1)
for wt, val in zip(weights, values):
    for w in range(wt, W + 1):              # ???
        dp[w] = max(dp[w], val + dp[w - wt])
print(dp[W])                                # prints 6 — WRONG, item reused
```

<details><summary>Answer</summary>
Pitfall #5 — `w` iterates *upward*, so `dp[w - wt]` is already updated this
pass → the item gets reused (prints `6`, i.e. two copies of one item).
For 0/1, use `range(W, wt - 1, -1)`. Same loop, wrong direction,
different problem.
</details>

---

**← Prev** [10 — Interval DP](10-interval-dp-burst-balloons.md) ·
**Next →** [12 — The "is it 2D?" checklist](12-the-2d-checklist.md)
