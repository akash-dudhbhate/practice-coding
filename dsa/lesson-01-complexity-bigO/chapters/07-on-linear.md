# 07 — O(n): Linear Time

> 4-minute read.

## The idea, plain words

`O(n)` means: **touch each item once.** Double the input, double the work.
The graph is a straight line — hence "linear."

Real-life version: **reading every page of a book.** 100 pages = 100 reads.
There's no shortcut — every page needs eyes on it.

## In code

```python
def total(nums):
    s = 0
    for x in nums:          # n rounds
        s += x
    return s                # work = n → O(n)

def find(nums, target):
    for x in nums:          # worst case: checks all n
        if x == target:
            return True
    return False            # → O(n)
```

Two loops *in a row* are still O(n):

```python
def two_passes(nums):
    for x in nums: print(x)        # n steps
    for x in nums: print(x * 2)    # n more steps
# total = 2n → drop the 2 → O(n)
```

Side-by-side loops **add** (n + n = 2n → O(n)). Nested loops **multiply**
(next chapter — that's where the danger is).

## Why it exists

If your algorithm must look at every input element at least once, O(n) is
the floor — you literally cannot do better. Finding the max of an unsorted
list MUST look at everything (any skipped element could secretly be the max).

## Where it's used

Single passes: sum, max/min, count, filter, transform, linear search.
`O(n)` is *good* — most interview answers aim for it when the input is
unsorted.

## Your turn

```python
def has_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
```

O(n) or not?

<details><summary>Answer</summary>
**Not linear — it's O(n²).** Nested loops: for each i, inner runs
n-i times → n-1 + n-2 + ... + 1 ≈ n²/2 steps → O(n²). "Almost all pairs."
(You'll learn to fix this with a set — O(n) — in lesson 03.)
</details>

---

**← Prev** [06 — O(1): constant](06-o1-constant.md) ·
**Next →** [08 — O(n²): quadratic time](08-on2-quadratic.md)
