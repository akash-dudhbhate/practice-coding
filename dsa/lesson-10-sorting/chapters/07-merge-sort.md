# 07 — Merge Sort: divide, conquer, zip

> 6-minute read. Take this one slowly.

## The idea, plain words

Real-life version: **two people each sort half a deck of cards**, then you
merge the two sorted stacks — look at the two top cards, take the smaller,
repeat. Merging two already-sorted stacks is easy and fast.

So: split the array in half, sort each half (same recipe, recursively —
halves of halves, down to single elements which are trivially sorted), then
merge pairs of sorted halves on the way back up.

## Watch it happen — trace `[5, 2, 4, 1]`

```
            [5, 2, 4, 1]
           /            \
      [5, 2]            [4, 1]        ← split
      /    \            /    \
    [5]    [2]        [4]    [1]      ← size 1: already sorted
      \    /            \    /
      [2, 5]            [1, 4]        ← merge pairs
           \            /
      merge [2,5] & [1,4]:
      compare 2 vs 1 → take 1   out=[1]
      compare 2 vs 4 → take 2   out=[1,2]
      compare 5 vs 4 → take 4   out=[1,2,4]
      right exhausted → append left's tail → [1,2,4,5]
```

## The code

```python
def merge(left, right):
    out = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:           # <= keeps equal-left first: stable!
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:])                  # whichever side has leftovers
    out.extend(right[j:])
    return out

def merge_sort(arr):
    if len(arr) <= 1:                     # base case — sorted already
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

print(merge_sort([5, 2, 4, 1]))           # [1, 2, 4, 5]
```

## Why it exists — guaranteed O(n log n)

Each merge level touches all n elements once (O(n) per level). Halving n
elements can only happen log n times (lesson 01, halving). n × log n, and
crucially: **ALWAYS** — no bad input can make it worse. When a guaranteed
bound matters, this is the sort you reach for.

## Where it's used

Linked lists (merging needs only pointer rewiring → O(1) extra space),
external sorting of files too big for RAM, counting inversions, Java's
`Arrays.sort` for objects, git's internals.

## Common mistake

- Forgetting the **O(n) extra space** — merging needs an output buffer;
  it's not in-place.
- Missing base case `len(arr) <= 1` → infinite recursion.
- Using `<` instead of `<=` in the merge — taking the right element on
  ties silently **breaks stability** (chapter 02).

## Your turn

Merging `[1, 3, 5]` and `[2, 4]` — what's the first element taken, and
from which side?

<details><summary>Answer</summary>
`1`, from the left — compare fronts: 1 < 2. Then 2, then 3, then 4, then
5. Six comparisons-free steps of "take the smaller front."
</details>

---

**← Prev** [06 — Why all O(n²)](06-why-all-n2.md) ·
**Next →** [08 — Quicksort](08-quicksort.md)
