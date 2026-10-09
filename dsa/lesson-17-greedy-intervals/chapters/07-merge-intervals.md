# 07 — Merge Intervals: sort by START, grow one blob

> 5-minute read. The other canonical interval algorithm.

## The idea, plain words

Merge takes messy overlapping intervals and returns the minimal clean
cover — like collapsing all your "busy" blocks into one free/busy calendar.

The recipe: **sort by start, sweep once, keep ONE running blob.** Each new
interval either overlaps the blob (extend it) or doesn't (seal it, start a
new blob).

```
before:  [1,3]   ███
         [2,6]    █████
         [8,10]          ███
         [15,18]                 ████
                  ────────────────────────→ time
                  1   5   10   15   18

after:   [1,6]   ██████
         [8,10]          ███
         [15,18]                 ████
```

## Hand trace — `[[1,3],[2,6],[8,10],[15,18]]` (sorted by start)

```
merged = []
[1,3]   → blob: merged = [[1,3]]
[2,6]   → 2 <= 3 overlap → extend top → [[1,6]]
[8,10]  → 8 > 6 disjoint → new blob  → [[1,6],[8,10]]
[15,18] → 15 > 10 new    → [[1,6],[8,10],[15,18]]
```

3 neighbor checks, not 6 pairwise — sorting made overlap *local*.

```python
def merge(intervals):
    intervals = sorted(intervals)        # by start
    merged = []
    for s, e in intervals:
        if merged and s <= merged[-1][1]:      # overlaps the last blob?
            merged[-1][1] = max(merged[-1][1], e)   # extend, don't append
        else:
            merged.append([s, e])              # seal old, start new blob
    return merged
```

`merge([[1,3],[2,6],[8,10],[15,18]])` → `[[1,6],[8,10],[15,18]]` ·
`merge([[8,10],[1,3],[2,6],[15,18]])` → same (sorting rescues scrambled
input) · `merge([[1,10],[2,3],[4,5]])` → `[[1,10]]` (the contained
intervals get swallowed — note `max` keeps the outer end, that's why it
must be `max`, not just `e`).

## Why it exists

This is THE "sort + sweep + one running variable" skeleton. If you
internalize it, half of all interval interview questions are transcription:
the variable is the merged-so-far blob here, `last_end` in chapter 6,
`reach` in chapter 10.

## Where it's used

- Calendar free/busy computation
- Union of IP ranges or version ranges
- Merging overlapping gene ranges in genomics

## Common mistake

- **Merging without sorting first:** `[[2,6],[1,3]]` emits `[2,6]` then
  can't merge `[1,3]` backwards. Sort always.
- **Appending instead of extending** on overlap → double-counts. If it
  overlaps, grow `merged[-1][1]`; never add a new blob.
- **`s < merged[-1][1]` instead of `<=`:** touching intervals `[1,3]` +
  `[3,5]` SHOULD merge into `[1,5]` here (opposite convention from
  scheduling!).

## Your turn

`merge([[1,4],[0,2],[3,5]])` — what's the output?

<details><summary>Answer</summary>
`[[0,5]]`. Sorted: `[[0,2],[1,3],[3,5]]`. Blob `[0,2]`; `[1,3]` overlaps
(1 <= 2) → `[0,3]`; `[3,5]` touches (3 <= 3) → `[0,5]`. One blob
swallowed everything — the "all-overlapping chain" edge case.
</details>

---

**← Prev** [06 — Activity Selection](06-activity-selection.md) ·
**Next →** [08 — Insert & Meeting Rooms](08-insert-and-meeting-rooms.md)
