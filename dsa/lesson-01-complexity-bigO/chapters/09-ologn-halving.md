# 09 — O(log n): Logarithmic Time — halving

> 5-minute read.

## The idea, plain words

`O(log n)` means: **every step throws away half the remaining work.**

Real-life version — the number game: "I'm thinking of a number 1–100."

- You guess 50. I say "higher." → 50 numbers eliminated in ONE guess.
- You guess 75. "Lower." → eliminated 25 more.
- 88 → 94 → 97… each guess halves what's left.

1,000,000 items → only ~20 steps. That's `log n` — it counts **how many
halvings until 1 remains**.

| n | log₂ n (halvings) |
|---|-------------------|
| 8 | 3 |
| 1,024 | 10 |
| 1,000,000 | ~20 |
| 1,000,000,000 | ~30 |

A billion items, ~30 steps. That's why log n is nearly free.

## In code — binary search (sorted list only!)

```python
def binary_search(nums, target):       # nums must be SORTED
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2           # check the middle
        if nums[mid] == target:
            return mid                 # found it
        elif nums[mid] < target:
            lo = mid + 1               # target must be right half
        else:
            hi = mid - 1               # target must be left half
    return -1
```

Hand trace: `nums = [1,3,5,7,9,11,13]`, target = `11`:

```
range [0..6] → mid=3 → nums[3]=7 < 11 → search right: [4..6]
range [4..6] → mid=5 → nums[5]=11 → FOUND at index 5
```

7 items, 2 steps — because each step halved the search space.

## Why it exists

Halving works because sorted order lets you *reason about* the half you
throw away ("everything left of mid is too small"). Random data gives you
no such guarantee — which is why "sorted" is the magic requirement.
(Lesson 09 builds this skill fully.)

## Where it's used

Binary search on sorted arrays, balanced BSTs, `bisect` module,
divide-and-conquer steps inside bigger algorithms.

## Your turn

How many steps to find a target in a sorted list of 1,000 items?

<details><summary>Answer</summary>
~10. log₂(1000) ≈ 9.97 → at most 10 halvings: 1000→500→250→125→62→31→
15→7→3→1. Done.
</details>

---

**← Prev** [08 — O(n²): quadratic](08-on2-quadratic.md) ·
**Next →** [10 — O(n log n) and O(2ⁿ)](10-onlogn-and-2n.md)
