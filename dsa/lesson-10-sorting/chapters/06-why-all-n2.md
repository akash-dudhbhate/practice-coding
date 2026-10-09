# 06 — Why the Simple Three Are All O(n²)

> 5-minute read. The payoff chapter for 03–05.

## The idea, plain words

Bubble, selection, and insertion look different, but they share one
structure: **an outer pass for each element, and inner work that scans or
shifts a big chunk of the array.**

Count the comparisons. For n items they all do roughly:

```
(n−1) + (n−2) + (n−3) + ... + 2 + 1  =  n(n−1)/2  ≈  n²/2
```

The "1+2+3+...+n" sum (you may know it as the triangle numbers) is about
n²/2 — and Big-O drops the /2. Quadratic.

## Watch it happen — count, don't guess

```python
def selection_comparisons(n):
    total = 0
    for i in range(n):
        for j in range(i + 1, n):     # the inner scan, literally counted
            total += 1
    return total

for n in [4, 8, 16, 32, 64]:
    print(n, "→", selection_comparisons(n))
```

Output:

```
4 → 6
8 → 28
16 → 120
32 → 496
64 → 2016
```

**Every time n doubles, the work quadruples** (6 → 28 → 120 → 496 → 2016).
That's the n² shape from lesson 01 — and it's why these sorts fall off a
cliff around n = 100,000 (→ ~5 billion comparisons ≈ seconds to minutes).

## Why it exists

These algorithms each "fix" one element per pass — and there are n passes.
The insight that unlocks the faster sorts: **compare elements that are far
apart**, so each comparison moves things a long distance (merge sort,
quicksort — next two chapters).

## Where it's used

Nowhere on purpose at large n — but knowing WHY they're quadratic is the
interview question: "walk me through why bubble sort is O(n²)."

## Common mistake

Thinking insertion sort's O(n) *best* case rescues it — it doesn't for
random data. Best case needs nearly-sorted input; average and worst stay
O(n²). Report the case that matches your actual input.

## Your turn

n = 10,000 items → how many comparisons for selection sort?

<details><summary>Answer</summary>
n(n−1)/2 = 10,000 × 9,999 / 2 ≈ **50 million**. That same job takes a
merge sort about n·log₂n ≈ 10,000 × 14 ≈ 140,000 — roughly 350× less work.
That's the whole point of the next chapters.
</details>

---

**← Prev** [05 — Insertion sort](05-insertion-sort.md) ·
**Next →** [07 — Merge sort](07-merge-sort.md)
