# 12 — The "Is It 2D?" Checklist: Recognize the Shape in 15 Seconds

> 5-minute read. Ties the whole lesson together — keep this page open.

## The recognition checklist

Staring at a new problem? Ask these in order:

1. **Does the subproblem need the word "and"?** "Best value using first `i`
   items **and** `w` room left" → 2D. One quantity → it's probably 1D
   (lesson 15's `dp[i]`).
2. **What are the TWO things that vary?** The usual suspects:
   - items × capacity → **knapsack**
   - row × column → **grid**
   - prefix of A × prefix of B → **two-sequence** (LCS / edit / wildcard)
   - left wall × right wall → **interval**
3. **Say the `dp[i][j]` sentence.** Can't? The state is wrong — go back.
4. **What's the choice?** take/skip · up/left · match/skip · delete/insert/
   substitute · last-pick `k`. The recurrence is always "compare the
   options, keep the best".
5. **Seed borders with real values.** Zeros for counts; accumulated costs
   for min problems; honest propagation for booleans.
6. **Match fill order to the arrows.** Row-major for prefix problems;
   by-length for interval; descending `w` for 1-row knapsack.
7. **Where's the answer?** Usually `dp[m][n]` — but interval DP wants
   `dp[0][n-1]`, and some knapsack variants want `max(dp[n])`.

## The whole lesson on one screen

| Pattern | `dp[i][j]` means | Recurrence is a choice between |
|---------|------------------|-------------------------------|
| Unique paths | ways to reach (i,j) | ↑ + ← (sum) |
| Min path sum | cheapest cost to (i,j) | min(↑, ←) + toll |
| 0/1 knapsack | best value, i items, capacity j | skip vs take |
| LCS | shared subseq, a[:i] vs b[:j] | diag+1 vs max(↑,←) |
| Edit distance | min edits, a[:i] → b[:j] | free diag vs 1+min(↑,←,↖) |
| Wildcard | does p[:j] match s[:i] | `*`: `dp[i-1][j] or dp[i][j-1]` |
| Interval | best inside walls (i,j) | max over last-pick `k` |

## Complexity out loud

Say it as **states × work per state**:

- Knapsack: `n·W` cells, O(1) each → **O(n·W)** time; O(W) with the 1-row
  trick.
- LCS / edit / wildcard: `m·n` cells, O(1) each → **O(m·n)**.
- Grid: `m·n` cells → **O(m·n)**.
- Interval: `n²` cells × O(n) inner `k`-loop → **O(n³)**.

If you can't say the complexity, you can't defend the solution in an
interview — it's part of the answer, not a bonus.

## Your turn

Run the checklist on these — 1D or 2D, and what's the state sentence?

1. "Best score picking levels, but each level costs stamina from a pool."
2. "How similar are two DNA strands?"
3. "Longest run of increasing prices in a stock list."

<details><summary>Answer</summary>
1. 2D — items × stamina: `dp[i][s]` = best score from first `i` levels with
   `s` stamina left. 2. 2D — prefix × prefix (that's LCS/edit distance).
3. 1D — only one thing varies (position): `dp[i]` = longest run ending at
   `i`. Lesson 15's shape; not everything needs the grid.
</details>

## What you now know

- One index fails when the question needs **two** variables — and the fix
  is a table, not cleverness.
- `dp[i][j]` is a *sentence*: say it before you code it.
- Borders are base cases with real values — the #1 silent bug farm.
- Fill order follows the arrows; the backwards `w` is why 1-row 0/1
  knapsack works.
- LCS, edit distance, and wildcard are **one skeleton with three
  recurrences** — learn one, get three.

## Then do this

The concepts are done. Now make them yours:

1. `task-explanation.md` — the 9 problems, in order.
2. `easy/` is all grid DP — you've literally traced these tables.
3. `medium/` is the classic trio — knapsack, LCS, and a take-or-skip
   counting variant.
4. `hard/` — edit distance and wildcard will feel familiar; burst balloons
   is the interval finale.
5. `coding-check.md` — oral drills; `EXTRA-PRACTICE.md` — debug exercises.

**Rule from lesson 01 still holds:** stop when it clicks. One chapter
understood beats five skimmed.

---

**← Prev** [11 — The pitfall gallery](11-the-pitfall-gallery.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/p01` next.
