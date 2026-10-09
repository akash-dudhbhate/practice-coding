# 09 — The O(n log n) Floor: why you can't compare-sort faster

> 5-minute read. The deepest idea in the lesson — kept simple.

## The idea, plain words

Here's a stunning fact: **no sort that works by comparing pairs of
elements can beat O(n log n) in the worst case.** Not "hasn't been
invented" — mathematically impossible.

Why? Think of sorting as a guessing game. n items can be arranged in
**n!** (n-factorial) different orders — for 3 items that's 3·2·1 = 6
orders. Your job: figure out which of the n! orders you're holding, using
only questions of the form "is a < b?" — each answer gives **1 bit** of
info (yes/no, like the halving game in lesson 01).

To tell apart n! possibilities you need at least **log₂(n!)** questions —
and log₂(n!) ≈ n log n. Merge sort hits that floor almost exactly.

## Watch it happen — the numbers

```python
import math

n = 1_000_000
need = sum(math.log2(k) for k in range(2, n + 1))   # log2(n!)
print(round(need))          # 18488885  comparisons, minimum worst case
print(round(n * math.log2(n)))   # 19931569  ← n·log n, same ballpark
```

Even for a million items, theory says ~18.5 million comparisons is the
best ANY comparison sort can guarantee — and n·log n ≈ 19.9M sits right on
top of it. Merge sort and (average) quicksort are literally as good as
comparison sorting gets.

Sanity check small: n=3 → n! = 6 orders → ⌈log₂6⌉ = 3 comparisons minimum.
Try sorting 3 items in fewer — you can't distinguish 6 cases with 2
yes/no answers (2²=4 < 6).

## Why it exists

It tells you when to stop optimizing — and flags the loophole: the bound
only applies to **comparison** sorts. Counting sort (next chapter) skips
comparisons entirely and legally beats the floor.

## Where it's used

Interview answer to "can we sort faster than n log n?" — "not with
comparisons, but yes with counting/radix/bucket when keys are special."

## Common mistake

Applying the floor to non-comparison sorts — counting sort is O(n + k),
fully legit, no paradox. The floor governs only "compare two elements"
algorithms.

## Your turn

Why does "sort 1000 items with at most ~10 questions" sound impossible?

<details><summary>Answer</summary>
log₂(1000!) ≈ 8,529 — you'd need thousands of comparisons, not ~10. The
10 halvings intuition is for SEARCH (narrowing 1 answer), but sorting must
distinguish n! different worlds — astronomically more. Two different games.
</details>

---

**← Prev** [08 — Quicksort](08-quicksort.md) ·
**Next →** [10 — Counting sort](10-counting-sort.md)
