# 10 — Counting Sort: beating the floor (legally)

> 5-minute read. The loophole chapter.

## The idea, plain words

Last chapter's floor only applies to *comparison* sorts. So... don't
compare.

Real-life version: **grading exams scored 0–100.** Don't compare tests to
each other — make 101 piles (one per score), toss each test into its pile,
then stack the piles in order. Linear time, no comparisons.

If keys are integers in a small range [min, max]: count how many times
each value occurs, then emit each value `count[v]` times in order.
**O(n + k)** where k = max − min + 1 — the range size.

## Watch it happen — trace `[−3, 1, −1, 2]`, min=−3, max=2

```
counts index:   0   1   2   3   4   5      (represents value −3..2)
counts       : [1,  0,  1,  0,  1,  1]     ← −3,−1,1,2 each seen once
emit: −3(×1)  −1(×1)  1(×1)  2(×1)  →  [−3,−1,1,2]
```

Note the **offset**: value −3 lives at index `−3 − (−3) = 0`. You never
index by the raw value.

## The code

```python
def counting_sort(arr):
    lo, hi = min(arr), max(arr)
    counts = [0] * (hi - lo + 1)      # index = value - lo   <- THE OFFSET
    for v in arr:
        counts[v - lo] += 1
    out = []
    for offset, c in enumerate(counts):
        out.extend([offset + lo] * c)  # emit each value c times
    return out

print(counting_sort([-3, 1, -1, 2]))   # [-3, -1, 1, 2]
```

## Why it exists

Linear time! When k ≈ n (exam scores 0–100, ages, byte values 0–255), it
crushes every comparison sort — the n log n floor doesn't apply because
there are no comparisons. Radix sort extends the trick digit-by-digit for
big keys; bucket sort handles floats.

## Where it's used

Radix sort's inner pass, histogram problems, sorting by small integer keys
(exam scores, ages, ASCII chars).

## Common mistake

- **Negatives**: `counts[-3]` is NOT index −3 — always shift by `value − min`.
  (Python's negative indexing makes this a *silent* wrong answer, not a
  crash — worse.)
- **Huge range**: 3 elements spread across 10⁹ → the counts array eats
  gigabytes. O(n + k) is only good when k is small.
- Non-integer keys (strings, floats) can't be array indices — you need
  comparisons or buckets for those.

## Your turn

`[90, 95, 91]` — is counting sort a good idea here?

<details><summary>Answer</summary>
Yes — k = 95−90+1 = 6, tiny vs. n. Three counts, emit in order → O(n + k).
Contrast: `[1, 500_000_000, 7]` → k ≈ 500 million → terrible. Small RANGE
is the requirement, not small n.
</details>

---

**← Prev** [09 — The O(n log n) floor](09-the-nlogn-floor.md) ·
**Next →** [11 — Python's sorted() / .sort()](11-python-sorted-sort.md)
