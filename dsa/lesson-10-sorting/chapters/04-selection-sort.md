# 04 — Selection Sort: find the smallest, put it first

> 4-minute read.

## The idea, plain words

Real-life version: **lining up kids by height.** Scan the whole group,
pick the shortest, move them to position 1. Scan the rest, pick the
shortest of what's left, move them to position 2. Repeat.

Each round you *select* the minimum of the unsorted region and swap it into
place. After k rounds, the first k spots are final.

## Watch it happen — trace `[5, 2, 4, 1]`

```
[5, 2, 4, 1]  min of all = 1 (idx 3) → swap → [1, 2, 4, 5]
[1| 2, 4, 5]  min of rest = 2 (idx 1) → already there → [1, 2, 4, 5]
[1, 2| 4, 5]  min of rest = 4 (idx 2) → already there → [1, 2, 4, 5]
 last element is automatically right. Done.
```

(The `|` marks the wall: everything left of it is sorted forever.)

## The code

```python
def selection_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        m = i                              # index of smallest seen so far
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[m]:
                m = j
        arr[i], arr[m] = arr[m], arr[i]    # one swap per round
    return arr

print(selection_sort([5, 2, 4, 1]))        # [1, 2, 4, 5]
```

## Why it exists

One genuine superpower: **at most n−1 swaps, total.** Bubble sort can swap
on every comparison; selection sort compares a lot but only swaps once per
round. When *writing* is expensive — EEPROM, flash memory with limited
write cycles — minimum writes matter more than minimum comparisons.

## Where it's used

Memory-constrained embedded systems (cheap compares, expensive writes), and
as the "obvious" sort people invent on their own.

## Common mistake

- It's **not stable** — the big jump-swap can leap an element over an equal
  one and reorder ties.
- No early exit: even a sorted input still costs the full ~n²/2
  comparisons. Selection sort can't notice it's already done.

## Your turn

`[5, 2, 4, 1]` — how many SWAPS does selection sort do total?

<details><summary>Answer</summary>
2 real swaps: `5↔1` on round 1, then `2` and `4` were already minimal so
those swaps are self-swaps (no-ops). Contrast with bubble sort, which did
4 swaps on the same array.
</details>

---

**← Prev** [03 — Bubble sort](03-bubble-sort.md) ·
**Next →** [05 — Insertion sort](05-insertion-sort.md)
