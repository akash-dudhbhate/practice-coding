# 13 — "Is This a DP Problem?" — the 10-second sniff test

> 5-minute read. The skill behind the skills: recognizing the shape.

## The idea, plain words

DP problems almost always arrive wearing one of **three phrases**:

| The problem says… | `dp[i]` means… | Recurrence uses… | You've seen it |
|---|---|---|---|
| "**count the number of ways** to…" | ways to reach `i` | `+` (sum over last moves) | stairs, tribonacci |
| "**min / max** cost, value, length…" | best achievable at `i` | `min` / `max` over choices | robber, coins, LIS |
| "**can you** reach / is it possible…" | True/False at `i` | `any(...)` | word break |

Plus one **structural tell** underneath all three:

> At each position you make a small choice among a few options, and the
> options only care about *which state you're in* — never about *how you
> got there*. History doesn't matter; position does.

If "how you got there" DOES matter (e.g., "you can't reuse an item"), it
has to be folded *into* the state — that's when `dp[i]` becomes
`dp[i][something]` and you've reached next lesson's 2D DP.

## The 10-second checklist

Run these in order:

1. **Phrase match?** count-ways / min-max / can-you-reach → DP candidate.
2. **Can I define `dp[i]` in one sentence?** → state exists.
3. **Does `dp[i]` depend only on earlier `dp[...]`?** → recurrence +
   fill order exist.
4. **Would naive recursion recompute?** (ch.03) → DP actually pays.
5. **Say the complexity:** O(#states × work-per-state) — e.g., coin
   change is O(amount × #coins).

## Greedy vs DP — the coin change lesson

"Just take the biggest coin" is *greedy* — fast but sometimes wrong
(`[1,3,4]`, amount 6 → greedy 3 coins, optimal 2). Rules of thumb:

- "count ways" → **never** greedy. It's DP.
- "min/max" → greedy ONLY with a proof of correctness. No proof? DP is
  the honest default.

## When it's NOT DP

- **No overlap** (merge sort, binary search) → divide & conquer, ch.03.
- **Subproblems share but depend on path history** — e.g., "longest path
  in a graph without revisiting nodes." Each subproblem would need to
  know every node you've used → state explodes, DP can't help (it's
  NP-hard).

## Mini-drill — classify before solving

1. "Number of ways to decode a digit string into letters"
2. "Sort an array by splitting it in half"
3. "Can you jump to the last index, jumping at most nums[i]?"
4. "Minimum number of perfect squares summing to n"

<details><summary>Answers</summary>
1. **DP** — count-ways phrasing; `dp[i]` = ways to decode s[:i], last
   move = 1 or 2 digits. 2. **Not DP** — no overlapping subproblems
   (that's merge sort). 3. **DP** — can-you-reach phrasing; `dp[i]` =
   reachable. 4. **DP** — min phrasing; it's coin change with coins
   {1,4,9,16,…}.
</details>

## Common mistake

Forcing DP onto a greedy-provable problem (leaves performance on the
table) — or worse, forcing *greedy* onto a DP problem (produces a
plausible wrong answer). The phrases above are your detector.

## Your turn

"Longest path through a graph visiting each node at most once" — DP?

<details><summary>Answer</summary>
No — this is the history-matters case. `best(node)` isn't enough; the
answer depends on *which nodes are already used*. You'd need a state
like `dp[node][visited_set]` → exponential states → effectively no
savings. (NP-hard; needs backtracking/heuristics.)
</details>

---

**← Prev** [12 — Space optimization](12-space-optimization.md) ·
**Next →** [14 — Pitfall gallery & recap](14-pitfall-gallery.md)
