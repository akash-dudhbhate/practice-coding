# 03 — When Does the Notebook Trick Work? (the two requirements)

> 5-minute read. This saves you from memoizing the wrong problem.

## The idea, plain words

Memoization pays off only when the recursion **asks the same question
twice**. A problem qualifies for DP when it has BOTH of these:

1. **Overlapping subproblems** — solving the big problem forces you to
   re-solve the same small problems again and again. (`fib(30)` needs
   `fib(28)` a ridiculous number of times.)
2. **Optimal substructure** — the big answer is *built from* the small
   answers. `fib(n)` literally IS `fib(n-1) + fib(n-2)`. The sub-answers
   combine cleanly into the final answer.

Real-life version of rule 1: if nobody ever re-asks a question, a
notebook is wasted paper.

## A problem where the notebook is USELESS

Binary search / merge sort split a list into two halves — but each half
is processed **once**. No question repeats:

```
merge_sort([8,1,4,7])
   ├─ sort([8,1])     ← each piece appears exactly ONCE
   │   ├─ [8]  [1]       in the whole tree
   └─ sort([4,7])
       ├─ [4]  [7]
```

Memoizing `sort([8,1])` saves nothing — it's never asked twice. That's
**divide & conquer**, not DP. Different technique for a different shape.

## How to check in 10 seconds

Ask two questions:

- **"Does the recursion recompute?"** Sketch the call tree (like ch.01).
  See the same call twice? → overlap ✓
- **"Does the answer combine sub-answers?"** Can you write
  `answer(n) = f(answer(smaller))`? → optimal substructure ✓

Both yes → DP will help. Overlap without combination, or combination
without overlap → DP won't help.

| Problem | Overlap? | Combines? | DP? |
|---------|----------|-----------|-----|
| `fib(n)` | yes (huge) | yes, sums | ✅ |
| merge sort | no | yes (merge) | ❌ divide & conquer |
| binary search | no | n/a | ❌ |
| climbing stairs | yes | yes, sums | ✅ |

## Why it exists

Because the fix costs memory — you're trading space for time. If nothing
repeats, you pay the memory and get nothing back. Knowing the two
requirements keeps DP a *tool you choose*, not a hammer for every nail.

## Where it's used

Interview triage: the moment you suspect DP, draw the mini call tree for
a small input. If subtrees repeat, say "overlapping subproblems" out
loud — that's the phrase interviewers listen for.

## Common mistake

Memoizing a recursion where the subproblems are all distinct. You get a
big dict full of entries each read exactly once — all the memory cost,
zero speedup. The tell: your cache hit rate is 0%.

## Your turn

`def total(nums, i): return 0 if i == len(nums) else nums[i] + total(nums, i+1)`
— recursive array sum. Does DP help here?

<details><summary>Answer</summary>
No. Each `total(i)` is called exactly once — the "tree" is a straight
line, no repeated subproblems. There IS optimal substructure (sum =
head + sum of rest) but no overlap → nothing to memoize.
</details>

---

**← Prev** [02 — Memoization](02-memoization-top-down.md) ·
**Next →** [04 — Bottom-up: fill a table](04-bottom-up-tabulation.md)
