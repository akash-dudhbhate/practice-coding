# 14 — The Pitfall Gallery & 10-Second Recap

> 5-minute read. Five ways DP silently goes wrong — collect them all.

## Pitfall 1 — Wrong / missing base case

`dp[0] = 1` for count-ways ("one way to make nothing") vs `dp[0] = 0`
for min-cost ("nothing costs nothing"). Swap them and every answer is
off by exactly the seed. Ask: *what does the empty prefix mean in THIS
problem?*

## Pitfall 2 — Unreachable states seeded to 0

For min-problems, impossible cells must be `∞` (ch.09). Seeded to `0`,
`min` thinks "can't make this" is *free* — `dp[5]` "costs" 1 coin via a
route that doesn't exist. Min-problems → `inf` seeds. Count-problems →
`0` seeds with `dp[0] = 1`.

## Pitfall 3 — Wrong fill order

`dp[i]` reads `dp[i-1]`, but you loop `i` downward → every cell reads a
stale `0` (ch.04's "Your turn"). For 1D recurrences that look backward:
loop ascending. If a recurrence ever needs `i-1` **and** `i+1`, that's a
signal to reformulate the state — DP needs a one-directional dependency
flow.

## Pitfall 4 — Answering from the wrong cell

- Climbing stairs → `dp[n]` ✓
- Min-cost stairs → `min(dp[-1], dp[-2])` — the top is PAST the array
- LIS → `max(dp)` — the winner can end anywhere
- Coin change → `dp[amount]` — and check for `∞` → `-1`

Recipe step 5 is the most-skipped step. Always ask where the answer
*lives* before returning `dp[-1]` on autopilot.

## Pitfall 5 — Greedy temptation

"Biggest coin first" fails `[1,3,4]` amount 6 (ch.09). Greedy is
tempting because it's short; DP is honest because it tries every last
move. When greedy has a counterexample and no proof — DP.

## Edge cases to always test

- `n = 0` / empty input — decide the convention (`0`? `1`? `-1`?)
- `n = 1`, single-element arrays
- Impossible inputs — return `-1`/`False`, don't crash
- Answers at extremes — use ALL elements, or NONE

## The whole lesson, 10 seconds

```
1. Phrase?        count-ways / min-max / can-you-reach → DP candidate
2. State?         dp[i] defined in one sentence
3. Recurrence?    dp[i] ← earlier cells only  (think: last move)
4. Base + order?  seeds first, fill in dependency direction
5. Answer cell?   dp[n]? max(dp)? dp[amount]?  — check twice
```

**DP = recursion that remembers.** Top-down when it's easier to think
recursively (ch.02); bottom-up when you want control (ch.04); roll the
variables when only a few cells are read (ch.12). That's all of it —
the fear was bigger than the technique.

## Your turn (final check)

Coin change returns `4` for `coin_change([2], 3)`. Walk the pitfalls:
which one fired, and what's the fix?

<details><summary>Answer</summary>
Pitfall 2 + 4 together: `dp[3]` should be `∞` (unreachable — only coin
2 exists), meaning either the seeds were `0` instead of `INF`, or the
final `dp[amount] == INF → return -1` check was skipped. Fix: seed with
`INF`, return `-1` when `dp[amount]` is still `INF`. Verified correct
answer: **-1**.
</details>

---

**← Prev** [13 — Is this a DP problem?](13-is-this-a-dp-problem.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/p01` next.
