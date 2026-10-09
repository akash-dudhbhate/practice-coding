# 03 — Greedy or DP? The one question to ask

> 4-minute read. The decision that decides everything else.

## The idea, plain words

Before coding a greedy, ask one question:

> **"Can a locally-best choice ever strand me — so I'd want to take it back?"**

- **No → greedy is legal.** Each commit is permanent and safe.
  Sort, sweep once, done.
- **Yes → it's DP territory** (lesson 15/16). A choice can look great now
  and ruin the endgame, so you must keep alternatives alive — exactly what
  DP's table of sub-answers does.

The `[1,3,4]` coin failure is the "yes" case made concrete: grabbing the 4
looked best at step 1, and you'd pay anything to undo it at step 3.
US coins never produce that regret; `[1,3,4]` can.

```python
def coin_change_dp(coins, amount):
    best = [float("inf")] * (amount + 1)
    best[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                best[a] = min(best[a], best[a - c] + 1)  # keep EVERY option alive
    return best[amount] if best[amount] != float("inf") else -1
```

`coin_change_dp([1,3,4], 6)` → **2** — the answer greedy missed. DP never
commits early; it asks every coin "what if I used you last?" That's why
it's slower (`O(amount × #coins)`) and why it can't lose.

## Why it exists

Picking the wrong family costs you the interview. Code greedy where DP
belongs → wrong answer. Code DP where greedy was legal → right answer but
you wrote 40 lines where 10 proved more insight. Stating "greedy works
here *because* no choice needs revising" is the senior answer.

## Where it's used

- Greedy wins: interval scheduling, jump/reach problems, matching
  smallest-need to smallest-resource — this whole lesson.
- DP required: arbitrary coin change, "minimum cost with carryover
  constraints", anything where a local pick can strand you later.

## Common mistake

Forcing greedy when it breaks. When your counterexample hunt (chapter 11)
finds one bad input, don't patch the rule — **pivot to DP** or
binary-search-the-answer (lesson 9). "My greedy is wrong, here's the DP"
beats a silently-wrong greedy every time.

## Your turn

Scheduling max meetings in one room: you pick the earliest-ending meeting,
cross off its conflicts, repeat. Does any pick ever need revising — greedy
or DP?

<details><summary>Answer</summary>
**Greedy.** Picking the earliest-ending meeting can only *free* time for
everything after — no choice strands you. That's why sort-by-end + one
sweep (chapter 6) is provably optimal, no DP table needed.
</details>

---

**← Prev** [02 — When Greedy FAILS](02-when-greedy-fails.md) ·
**Next →** [04 — Interval Words](04-interval-words.md)
