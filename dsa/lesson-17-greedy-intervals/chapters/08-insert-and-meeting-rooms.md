# 08 — Insert Interval & Meeting Rooms

> 6-minute read. Merge's cousins — same skeleton, three phases.

## The idea, plain words

**Insert:** your calendar is *already sorted and disjoint*, and one new
meeting arrives. Slot it in, absorbing whatever it touches. The sweep has
three phases — **before** it, **overlapping** it (absorb & grow), **after** it.

Insert `[4,8]` into `[[1,2],[3,5],[6,7],[8,10],[12,16]]`:

```
[1,2]  ██
[3,5]    ███
[6,7]      ██          new → [4,8] █████
[8,10]       ███
[12,16]           █████
       ──────────────────────→ time
       1 2 3 4 5 6 7 8 ... 16
```

```
Phase 1 (before):  [1,2] ends 2 < 4  → output it
Phase 2 (overlap): [3,5],[6,7],[8,10] start <= 8 → absorb → new = [3,10]
                   [12,16] starts 12 > 10 → stop
Phase 3 (after):   [12,16] → output it
Result: [[1,2],[3,10],[12,16]]
```

```python
def insert(intervals, new):
    out, i, n = [], 0, len(intervals)
    while i < n and intervals[i][1] < new[0]:    # 1: ends before new
        out.append(intervals[i]); i += 1
    while i < n and intervals[i][0] <= new[1]:   # 2: overlaps → absorb
        new = [min(new[0], intervals[i][0]),
               max(new[1], intervals[i][1])]
        i += 1
    out.append(new)
    while i < n:                                 # 3: starts after new
        out.append(intervals[i]); i += 1
    return out
```

→ `[[1,2],[3,10],[12,16]]` ✓. No sort needed — input was already ordered.

**Meeting rooms** — the other sort-by-start job. "Can I attend all
meetings?" = sort by start, check each against the previous:

```python
def can_attend_all(intervals):
    ivs = sorted(intervals)
    return all(ivs[i][0] >= ivs[i-1][1] for i in range(1, len(ivs)))
```

`[[0,30],[5,10],[15,20]]` → `False` (0–30 swallows 5–10) ·
`[[7,10],[2,4]]` → `True`. And "**minimum rooms needed**" = the max number
of meetings alive at once — sorted starts walk a pointer through sorted
ends; a new room only when nothing freed up:

```python
def min_meeting_rooms(intervals):
    starts = sorted(iv[0] for iv in intervals)
    ends   = sorted(iv[1] for iv in intervals)
    rooms, e = 0, 0
    for s in starts:
        if s < ends[e]:      # earliest-ending room still busy → need one more
            rooms += 1
        else:
            e += 1           # a room freed → reuse it
    return rooms
```

`[[0,30],[5,10],[15,20]]` → **2** · `[[7,10],[2,4]]` → **1**.

## Why it exists

Insert appears whenever a sorted structure gets a new element (your sorted
calendar + one invite). Meeting-rooms is how you'd size real conference
floors or CPU cores. Both reuse the same sweep discipline.

## Common mistake

The classic insert bug: `iv.end < new.start` vs `<=` — decide if touching
merges (it does: overlap means `start <= new.end`). "Merge everything
anyway" also works for insert, just wasteful — three phases is the clean
version.

## Your turn

`insert([[1,5]], [6,8])` — what happens?

<details><summary>Answer</summary>
`[[1,5],[6,8]]`. Phase 1 outputs `[1,5]` because `5 < 6` — strictly
before. Phase 2 never runs, and the new interval lands cleanly in the
gap. (Try `[5,8]` instead: `5 < 5` fails phase 1, `1 <= 8` absorbs it in
phase 2 → `[[1,8]]` — touching DOES merge.)
</details>

---

**← Prev** [07 — Merge Intervals](07-merge-intervals.md) ·
**Next →** [09 — The Exchange Argument](09-exchange-argument.md)
