# 12 — Two heaps (streaming median) + the recipe

> 6-minute read. Ties the lesson together.

## The idea, plain words — the median of a stream

"What's the median of everything seen so far?" after *every* new
number. Keep the stream **split in two heaps** with the median living
on the boundary:

```
lo = max-heap of the LOWER half   (Python: store negated)
hi = min-heap of the UPPER half

         lo                hi
        max↑              min↑
      [1, 2, 4]   |   [5, 8, 9]
                  ^
         the median lives HERE — between the two roots
```

Two invariants do all the work:

- `max(lo) <= min(hi)` — every lower-half element ≤ every upper-half one
- sizes differ by at most 1

Then the median is `-lo[0]` (odd count) or `(-lo[0] + hi[0]) / 2`
(even) — both O(1) reads off the roots. Each insert is O(log n).

## An insert, step by step

Push into `lo`, hand `lo`'s max to `hi` (fixes ordering), then if `hi`
outgrew `lo`, give `lo` back `hi`'s min (fixes sizes):

```python
from heapq import heappush, heappop

lo, hi = [], []
def add(x):
    heappush(lo, -x)
    heappush(hi, -heappop(lo))        # lo hands its biggest to hi
    if len(hi) > len(lo):             # hi too big -> give lo its smallest
        heappush(lo, -heappop(hi))
```

Stream `[5, 1, 4, 2, 3]`:

```
x=5: lo=[-5]        hi=[]            median 5.0
x=1: lo=[-1]        hi=[5]           median (1+5)/2 = 3.0
x=4: lo=[-4,-1]     hi=[5]           median 4.0
x=2: lo=[-2,-1]     hi=[4,5]         median (2+4)/2 = 3.0
x=3: lo=[-3,-1,-2]  hi=[4,5]         median 3.0
```

## Why it exists

Re-sorting the window per step is O(n log n) *per insert* → O(n² log n)
for a stream. But the median only depends on the two middle values —
exactly the two heap roots. Two heaps give you just that, nothing more.

## The recipe — recognize a heap problem in 10 seconds

1. **"kth largest / smallest / most frequent / closest"?** → heap of
   size k. Largest → min-heap of the k best; smallest → max-heap
   (negate).
2. **"Repeatedly take min/max while inserting"?** → plain heap. Need
   max → negate; need payloads → `(priority, counter, item)`.
3. **"Median (or two-sided stat) of a stream"?** → TWO heaps, sizes
   within 1.
4. **"Merge k sorted streams"?** → heap holding one `(value, source_i,
   elem_i)` per source.
5. Say it out loud: push/pop **O(log n)**, peek **O(1)**, heapify
   **O(n)**, top-k **O(n log k)**.

## The five-ways-it-goes-wrong gallery

1. Heap array ≠ sorted — `heap[1]` is not the 2nd smallest. Pop for that.
2. Wrong direction for top-k — k largest wants a *min*-heap of size k.
3. Tuple tie-break crash — add a unique counter.
4. `list.sort()` or `pop(0)` inside a loop — that's a slow heap by hand.
5. `heappop` when you meant `h[0]` — pop removes; peek is free. And
   `heappop([])` → `IndexError`.

## Common mistake (this chapter's own)

Forgetting the **rebalance-back** step in two heaps — `hi` can outgrow
`lo` by 2+, and your "median" silently reads a value that isn't the
middle.

## Your turn

For the stream `[8, 2, 9]`, what's the median after all three inserts?

<details><summary>Answer</summary>
**8.** Trace the `add` function: x=8 → lo=[-8], hi=[] → median 8.
x=2 → push -2 to lo, route lo's max (8) to hi → lo=[-2], hi=[8] →
median (2+8)/2 = 5. x=9 → push -9, route lo's max (9) to hi →
lo=[-2], hi=[8,9] — now hi is bigger, so hi hands its min (8) back:
lo=[-8,-2], hi=[9] → median = -lo[0] = **8**. Sorted view [2,8,9] →
middle is 8. ✔
</details>
