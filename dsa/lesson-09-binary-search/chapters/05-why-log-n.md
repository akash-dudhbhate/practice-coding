# 05 — Why O(log n)

> 4-minute read. This connects back to lesson 01 chapter 09 — same math, now with the code in front of you.

## The idea, plain words

Every probe **halves** the live range. So the question "how many steps?"
is really "how many times can you halve `n` before only 1 remains?" —
and that's exactly what `log₂ n` counts.

| n (sorted elements) | worst-case probes | log₂ n |
|--------------------:|------------------:|-------:|
| 8 | ~4 | 3 |
| 1,024 | ~11 | 10 |
| 1,000,000 | ~20 | ~20 |
| 1,000,000,000 | ~31 | ~30 |

A billion elements → ~30 comparisons. Linear scan would do a billion.
That's not an optimization, it's a different universe.

## Feel it in code

```python
def count_probes(n):
    """How many halvings until a range of n elements is down to 1?"""
    probes, size = 0, n
    while size > 1:
        size = (size + 1) // 2     # ceil halving — worst case
        probes += 1
    return probes

for n in [8, 1024, 10**6, 10**9]:
    print(n, "elements →", count_probes(n), "probes max")
```

```
8 elements → 3 probes max
1024 elements → 10 probes max
1000000 elements → 20 probes max
1000000000 elements → 30 probes max
```

Each line IS the loop doing halving — same `while` shape as the search.

## Why it exists

Halving works because each comparison gives you a *directional* fact, not
just a yes/no. One look at `nums[mid]` rules out half the array — the
information gain per step is enormous, and it compounds: kill half, then
half of that half, then half of THAT.

## Where it's used

Anywhere a check splits the space in two: sorted arrays, balanced trees,
`git bisect`, number-range narrowing. When you see O(log n) in the wild,
something is halving.

## Common mistake

Thinking "log n is basically O(1), so skip it." It's not free — 30 probes
on a billion rows still happen. But the bigger mistake is the reverse:
using O(n) scan "because the array is small today" and shipping a
time-bomb for when it isn't.

## Your turn

A sorted array has 4,000,000 elements. Roughly how many probes, worst case?

<details><summary>Answer</summary>
~22. log₂(4,000,000) ≈ 21.9 → at most 22 halvings. Doubling the data
only costs ONE extra probe — that's why log n scales so gently.
</details>

---

**← Prev** [04 — Hand trace, start to finish](04-hand-trace.md) ·
**Next →** [06 — The infinite-loop bug](06-infinite-loop-bug.md)
