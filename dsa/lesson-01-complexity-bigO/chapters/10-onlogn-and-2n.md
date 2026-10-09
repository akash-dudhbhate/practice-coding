# 10 — O(n log n) and O(2ⁿ): sorting speed & the brick wall

> 5-minute read.

## O(n log n) — "linearithmic", the sorting zone

**What:** `n × log n` — do the halving trick, but *per element*. It sits
between O(n) and O(n²): much slower than linear, much faster than quadratic.

Real-life version: **sorting a pile of exam papers by splitting.** Split the
pile in half repeatedly until piles have 1 paper (log n splits), then merge
pairs back together in order (n work per merge level × log n levels).

| n | n | n log n | n² |
|---|---|---------|-----|
| 1,000 | 1,000 | ~10,000 | 1,000,000 |
| 1,000,000 | 1M | ~20M | 1,000,000,000,000 |

**Why it exists:** comparison-based sorting literally cannot do better than
n log n (that's a proven floor). Merge sort and good quicksort live here.
You'll meet them properly in lesson 10.

**Where it's used:** `sorted()`, `list.sort()`, `heapq` — the workhorses.

## O(2ⁿ) — exponential, the brick wall

**What:** work *doubles* with each added item. n=10 → ~1,000 steps.
n=20 → ~1,000,000. n=30 → ~1 billion. n=64 → more steps than atoms on Earth.

Real-life version: **trying every combination on a lock.** Each extra digit
multiplies the possibilities by 10. Add digits and it becomes hopeless fast.

The classic source — recursion that recomputes:

```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)     # each call spawns TWO more
```

```
fib(5) → 15 calls    fib(10) → 177 calls    fib(30) → ~2.7 million
fib(50) → ~1 trillion calls — do NOT run this and wait
```

Every level doubles: 1 → 2 → 4 → 8 → 16... that's where the 2ⁿ comes from.
(Lesson 15, dynamic programming, is literally the fix for this exact trap.)

## When it's unavoidable

"Try every subset/permutation" problems are *inherently* 2ⁿ or worse —
the output itself is that big (all subsets of 5 items = 32). Fine for
small n (≤ ~20). For big n you need pruning (backtracking, lesson 08) or
memoization (lesson 15).

## Your turn

`sorted(nums)` on a million items — which class does it land in, and roughly
how many steps?

<details><summary>Answer</summary>
O(n log n) — about 20 million steps. Compare: a quadratic sort would do
a trillion. That's why we never hand-roll a slow sort.
</details>

---

**← Prev** [09 — O(log n)](09-ologn-halving.md) ·
**Next →** [11 — Nested vs side-by-side loops](11-nested-vs-sequential.md)
