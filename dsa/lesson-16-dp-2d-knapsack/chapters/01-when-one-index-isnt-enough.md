# 01 — When One Index Isn't Enough

> 4-minute read. Why this lesson needs a GRID, not a row.

## The idea, plain words

In lesson 15 every subproblem was `dp[i]` — one number describing "the best
answer for the first `i` items". One dial told the whole story.

2D DP is for problems where **the subproblem has TWO things that vary**, and
you can't answer the question without knowing both.

Real-life version: **"What's the best deal I can get?"**

You can't answer that with only "which shop am I in". You also need "how much
money do I have left". Same shop + different budget = different answer. The
question needs TWO numbers: `(shop, money left)`.

Here are the three pairs you'll meet in this lesson:

- **Knapsack:** `dp[i][w]` = best value using the first `i` items, with `w`
  room left in the bag. Two knobs: *which items* × *how much room*.
- **Grid:** `dp[r][c]` = best answer for reaching cell `(r, c)`. Two
  coordinates: *which row* × *which column*.
- **Two strings:** `dp[i][j]` = best answer comparing the first `i` chars of
  string A with the first `j` chars of string B. *One pointer per string*.

## Watch 1D actually fail

Try to do the shopping problem with one index — "best value considering the
first `i` items":

```python
values  = [4, 5, 7]
weights = [3, 4, 5]
bag_capacity = 7
```

`dp[2]` = best value from items 1–2? It's `5` — *if* you have room for the
weight-4 item. But if the bag only has `3` room left, the answer is `0` —
item 2 doesn't fit. **Same `i`, different answers.** The remaining capacity
is missing, so the state is incomplete. That's the signal: go 2D.

## Why it exists

If you flatten a genuinely-2D problem into 1D, you silently lose information.
The classic bug: a knapsack that forgets "room left" ends up taking the same
item twice, or skipping items that would have fit. Two variables in the
question → two dimensions in the table. That's the whole rule.

## Where it's used

- **Grid paths** — games, robots, image processing: position = (row, col).
- **Resource packing** — budget × items, time × tasks.
- **String comparison** — diff tools, spell checkers, DNA alignment
  (comparing two sequences always needs a pointer into each).
- **Pattern matching** — text × pattern (wildcards, regex).

## Common mistake

Looking for "the one clever index". If describing the subproblem needs the
word "**and**" — "first `i` items **and** `w` room left" — the table needs
two dimensions. Fighting it just produces a harder-to-debug wrong answer.

## Your turn

For each, say the TWO things that vary:

1. Best score reaching level `r` having spent `c` coins.
2. Comparing the first `i` letters of two passwords.
3. Longest increasing subsequence ending at index `i` (lesson 15!).

<details><summary>Answer</summary>
1. level × coins → `dp[r][c]`. 2. prefix of A × prefix of B → `dp[i][j]`.
3. Trick question — only ONE thing varies (`i`), so it's 1D `dp[i]`.
Not everything is 2D!
</details>

---

**Next →** [02 — Unique Paths: your first 2D table](02-unique-paths-your-first-grid.md)
