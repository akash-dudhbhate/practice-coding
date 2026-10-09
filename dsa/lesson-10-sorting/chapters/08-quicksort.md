# 08 — Quicksort: pick a pivot, split the room

> 6-minute read. The other famous one.

## The idea, plain words

Real-life version: **lining up a class by height, fast.** Grab one kid —
the *pivot* — and tell everyone shorter to stand left, taller to stand
right. The pivot lands in their **final** spot instantly. Then repeat the
trick on each side.

That reorder step is called **partition**. Lomuto's version: pivot = last
element; keep a wall `i` marking where "small" elements end; scan with `j`,
and every time `arr[j] ≤ pivot`, extend the wall and swap `arr[j]` inside.

## Watch it happen — partition `[4, 1, 3, 9, 7]`, pivot = 7

```
i starts at -1 (wall before index 0)
j=0: 4 ≤ 7 → i=0, swap a[0]↔a[0]   [4,1,3,9,7]
j=1: 1 ≤ 7 → i=1, swap a[1]↔a[1]   [4,1,3,9,7]
j=2: 3 ≤ 7 → i=2, swap a[2]↔a[2]   [4,1,3,9,7]
j=3: 9 > 7 → skip
final: swap pivot into i+1         [4,1,3,7,9]   ← 7 is DONE at index 3
```

Everything ≤7 is left of index 3, everything bigger is right — the pivot
never moves again. Recurse on `[0..2]` and `[4..4]` and it's sorted.

## The code

```python
def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1                          # wall: everything ≤ pivot ends here
    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
    return i + 1                        # pivot's final index

def quicksort(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    if lo < hi:
        p = partition(arr, lo, hi)
        quicksort(arr, lo, p - 1)       # pivot at p is DONE — exclude it
        quicksort(arr, p + 1, hi)
    return arr

print(quicksort([4, 1, 3, 9, 7]))       # [1, 3, 4, 7, 9]
```

## Why it exists

Average **O(n log n) with tiny constants** — the inner loop is a
cache-friendly linear scan, and it sorts in place (O(log n) stack vs merge
sort's O(n) buffer). That's why most language runtimes use a quicksort
variant for primitive arrays.

**The catch:** worst case O(n²) — when every pivot is the min or max, the
"splits" are 0 vs n−1, no real divide. Sorted input + last-element pivot
is the classic killer. Fix: pick the pivot **at random** (or
median-of-three) — bad luck becomes essentially impossible.

## Where it's used

C's `qsort`, most languages' primitive sorts, and **quickselect** —
partition once, recurse only into the side containing the k-th element →
"k-th smallest" in average O(n).

## Common mistake

- `i` starts at `lo − 1`, not `lo` — starting at `lo` pretends `arr[lo]`
  is already placed.
- Recursing on `[lo, p]` — that re-includes the finished pivot → infinite
  recursion. It's `[lo, p−1]` and `[p+1, hi]`.
- Last-element pivot on **already-sorted** big input → O(n²) AND stack
  overflow.

## Your turn

If the pivot always splits the array in half, how many partition levels
for n=8?

<details><summary>Answer</summary>
3 — 8 → 4 → 2 → 1. Each level does ~n partition work → n·log₂n total.
Perfect balance is what makes it fast; lopsided splits are the enemy.
</details>

---

**← Prev** [07 — Merge sort](07-merge-sort.md) ·
**Next →** [09 — The O(n log n) floor](09-the-nlogn-floor.md)
