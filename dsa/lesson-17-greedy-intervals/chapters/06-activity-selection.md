# 06 — Activity Selection: sort by END, keep what fits

> 6-minute read. The first greedy interval algorithm — traced fully.

## The idea, plain words

One meeting room, many requests. "Remove the fewest meetings so nothing
overlaps" is the same question as "**keep the MOST non-overlapping
meetings**." The famous greedy:

> **Sort by end time. Repeatedly take the meeting that ends earliest and
> doesn't clash with what you kept.**

Earliest-ending first leaves the most room for everything after — that's
the provable part (chapter 9 proves it).

```
[0,2]   ██
[1,3]    ██
[2,4]     ██
[3,5]      ██
[4,6]       ██
        ──────────→ time
        0 1 2 3 4 5 6
```

Already sorted by end — convenient. Sweep once, tracking `last_end`:

```
Keep [0,2]                    last_end = 2
[1,3]: starts 1 < 2  → DROP   (clashes with kept)
[2,4]: starts 2 >= 2 → KEEP   last_end = 4   (touching is OK!)
[3,5]: starts 3 < 4  → DROP
[4,6]: starts 4 >= 4 → KEEP   last_end = 6
Kept: 3 → answer = 5 − 3 = 2 removals
```

```python
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda iv: iv[1])   # earliest END first — the trick
    kept, last_end = 0, float("-inf")
    for s, e in intervals:
        if s >= last_end:        # no clash with last kept → keep it
            kept += 1
            last_end = e
    return len(intervals) - kept
```

`erase_overlap_intervals([[0,2],[1,3],[2,4],[3,5],[4,6]])` → **2** ·
`erase_overlap_intervals([[1,10],[2,3],[3,4]])` → **1** (drop the big one,
keep the two small — sorting by start would wrongly return 2).

## Why it exists

This is the cleanest greedy on intervals: one sort, one running variable,
provably optimal. Internalize it and "minimum deletions", "max bookings",
and "how many events can I attend" all become the same transcription.

## Where it's used

- Booking maximum meetings in one room
- Minimum deletions to de-conflict a calendar
- Max non-overlapping jobs on a single machine

## Common mistake

`if s < last_end` vs `if s >= last_end` direction confusion — remember
**`>=` keeps** (starts at/after last end → no clash). Also: sorting by
start or by length both fail (the 9-hour-meeting trap from chapter 5).

## Your turn

`[[1,2],[2,3],[3,4]]` — meetings touch but never truly overlap. How many
removals?

<details><summary>Answer</summary>
**0.** Sort by end (already sorted): keep `[1,2]` (last_end=2), `[2,3]`
starts `2 >= 2` keep, `[3,4]` starts `3 >= 3` keep → kept 3, removed 0.
Touching endpoints don't clash — that's why `>=` is the right comparison.
</details>

---

**← Prev** [05 — Sort by Start or by End?](05-sort-by-key.md) ·
**Next →** [07 — Merge Intervals](07-merge-intervals.md)
