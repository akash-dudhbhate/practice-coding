# 03 — Reading a 2D Table: What `dp[i][j]` Actually Means

> 5-minute read. The sentence template that unlocks every 2D DP.

## The idea, plain words

In 1D you wrote the sentence "`dp[i]` = best answer for the first `i`
items". In 2D the sentence just gets a second half:

> **`dp[i][j]` = the best answer using the first `i` of X and the first `j` of Y**

Fill in X and Y per problem:

| Problem | `dp[i][j]` means |
|---------|------------------|
| Unique paths | ways to reach **row `i`, column `j`** |
| Knapsack | best value using **first `i` items** and **capacity `j`** |
| LCS | longest common subsequence of **first `i` chars of A** and **first `j` chars of B** |

If you can't say the sentence out loud, the state is wrong. Say it *before*
writing the loop — it's the unit test for your design.

## The arrows picture — where every cell looks

Almost every 2D DP cell reads some of these three neighbors:

```
        dp[i-1][j-1]  ←  dp[i-1][j]
              ↖            ↑
                 dp[i][j]  ←  dp[i][j-1]
```

- **Unique paths:** reads ↑ and ← (add them).
- **Knapsack:** reads ↑ (skip) and ↑-shifted-left (take).
- **LCS:** reads ↖ (match) or ↑ and ← (skip a char).

Different problems, same neighborhood. If you fill **top-left →
bottom-right**, all three are always ready when you need them. That's why
"row by row" is the default fill order — it's not a rule, it's just the
order that respects the arrows.

## Borders are not zeros — they're the base case

Row 0 and column 0 always mean "**the empty version**":

- Unique paths: first row/col = `1` (one forced way to get there).
- Knapsack: row 0 = `0` (no items → no value), col 0 = `0` (no room → no
  value).
- LCS: row 0/col 0 = `0` (an empty prefix shares nothing with anything).
- Min-cost problems: borders hold **real running costs**, not `0` — a fake
  `0` looks like a free path (chapter 4 shows this bite).

A tiny runnable demo — watch the borders get seeded before the inside loop:

```python
R, C = 3, 3
dp = [[0] * C for _ in range(R)]
dp[0] = [1, 1, 1]                    # first row: reachable only from the left
for r in range(R):
    dp[r][0] = 1                     # first col: reachable only from above
for r in range(1, R):
    for c in range(1, C):
        dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
for row in dp:
    print(row)
```

Output:

```
[1, 1, 1]
[1, 2, 3]
[1, 3, 6]
```

## Why it exists

The sentence is how you check yourself mid-problem. When `dp[2][3]` looks
weird, ask: "best answer using first 2 of X and first 3 of Y — is that
plausible?" If the sentence doesn't parse, you stored the wrong thing, not
the wrong number.

## Common mistake

Off-by-one between index and count. `dp[i]` often means "first `i` items",
so item `i` lives at `items[i-1]` in the list. Writing `weights[i]` when the
row means `weights[i-1]` shifts every take/skip by one item — the table
still fills, the answer is just wrong. The sentence catches this: "first `i`
items" vs "item index `i`" are different sentences.

## Your turn

In the unique-paths table above, say in words what `dp[2][1] = 3` means —
and which two cells fed it.

<details><summary>Answer</summary>
"Three different right/down routes reach row 2, column 1." It was fed by
`dp[1][1] = 2` (above) + `dp[2][0] = 1` (left).
</details>

---

**← Prev** [02 — Unique paths](02-unique-paths-your-first-grid.md) ·
**Next →** [04 — Min path sum & walls](04-min-path-sum-and-walls.md)
