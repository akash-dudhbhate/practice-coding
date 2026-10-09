# Lesson 15 — 1D Dynamic Programming

## How to read this lesson — small chapters, NOT one big file

Don't read this page top-to-bottom. It's an index. The real lesson lives
in `chapters/` — **14 tiny files, ~5 minutes each**. Read one, try the
mini-practice at the bottom, take a breath, come back. That's the design.

DP is the topic everyone fears — so this lesson goes extra slowly. The
whole thing is ONE idea repeated 14 ways: **recursion that remembers.**

## Reading order

| # | Chapter | You'll be able to answer after |
|---|---------|-------------------------------|
| 01 | [Fib revisited](chapters/01-fib-revisited.md) | why naive recursion explodes — the call tree, circled |
| 02 | [Memoization (top-down)](chapters/02-memoization-top-down.md) | the notebook trick: 2.7M calls → 59 |
| 03 | [When does DP apply?](chapters/03-when-does-dp-apply.md) | overlapping subproblems + optimal substructure |
| 04 | [Bottom-up tabulation](chapters/04-bottom-up-tabulation.md) | fill a table left→right, no recursion |
| 05 | [Climbing stairs](chapters/05-climbing-stairs.md) | derive your first recurrence ("last-move thinking") |
| 06 | [The 5-step recipe](chapters/06-the-five-step-recipe.md) | state → recurrence → base → order → answer cell |
| 07 | [House robber](chapters/07-house-robber.md) | the take-it-or-skip-it `max` choice |
| 08 | [Min-cost stairs](chapters/08-min-cost-climbing-stairs.md) | when the answer ISN'T `dp[n-1]` |
| 09 | [Coin change](chapters/09-coin-change.md) | min-over-choices + why `∞` seeds matter |
| 10 | [Longest increasing subsequence](chapters/10-longest-increasing-subsequence.md) | `dp[i]` reads ALL previous cells; answer is `max(dp)` |
| 11 | [Word break](chapters/11-word-break.md) | the "can you reach?" boolean shape |
| 12 | [Space optimization](chapters/12-space-optimization.md) | O(n) → O(1) when only last few cells are read |
| 13 | [Is this a DP problem?](chapters/13-is-this-a-dp-problem.md) | the 3 tell-tale phrases + 10-second checklist |
| 14 | [Pitfall gallery & recap](chapters/14-pitfall-gallery.md) | the 5 silent ways DP goes wrong |

**Rule:** stop when a chapter clicks — don't binge-read. Understanding one
beats skimming five.

## The one-paragraph answer (bookmark this)

> DP = recursion that remembers. If a problem asks "count ways" /
> "min-max" / "can you reach", define `dp[i]` in one sentence, write how
> it reads earlier cells (think about the *last move*), seed the base
> cases, fill left→right, and return the right cell — `dp[n]`, `max(dp)`,
> or `dp[amount]`. Memoize top-down (`@lru_cache`) or fill a table
> bottom-up; keep only the last few variables when the recurrence only
> reads a few cells back.

## Then do this

1. `task-explanation.md` — what to build, in plain words.
2. `easy/` → `medium/` → `hard/` — solve in order, run `check.py` after each.
3. `coding-check.md` — oral-interview drills (say answers aloud).
4. `EXTRA-PRACTICE.md` — real interview questions on this topic.

## Full reference

Want it all in one page later? → `concepts-reference.md` (the old
monolithic file, kept as a lookup doc — not required reading).
