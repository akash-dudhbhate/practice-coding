# 05 — Sort by Start or by End? The key IS the algorithm

> 5-minute read. The single most important insight in the lesson.

## The idea, plain words

Unsorted intervals are a tangle — `[8,10]` might secretly overlap `[1,3]`
through a chain of intermediates. Sorting puts them in a line so that
overlap becomes a **local** question: only check each interval against its
neighbor. That turns `O(n²)` pairwise checks into one sweep.

But *which* key? Watch the SAME three meetings sorted both ways:

```
        [1,10]  ██████████
        [2,3]    ██
        [4,5]        ██
        ──────────────────→ time
        1 2 3 4 5 6 7 8 9 10
```

```python
intervals = [[1,10], [2,3], [4,5]]

sorted(intervals, key=lambda iv: iv[0])  # by START → [[1,10],[2,3],[4,5]]
sorted(intervals, key=lambda iv: iv[1])  # by END   → [[2,3],[4,5],[1,10]]
```

Same input, different first element — and the first element is what a
greedy grabs. That changes the whole answer:

| Sort by | First thing you see | Question it answers | Used in |
|---------|--------------------|---------------------|---------|
| `iv[0]` start | the 9-hour meeting `[1,10]` | "what comes next in time order?" | merge, insert, meeting rooms |
| `iv[1]` end | the tiny `[2,3]` | "what frees up soonest?" | max non-overlapping, min removals |

## Trace the difference — "keep max meetings"

```
Sort by START: pick [1,10] → [2,3] and [4,5] both clash → keep 1
Sort by END:   pick [2,3] → [4,5] fits → [1,10] clashes → keep 2  ✓ optimal
```

The sort key decided the winner **before the loop even ran.**

## Why it exists

"Which key" is really asking *what resource am I optimizing*: order of
processing (start) vs. freeing the resource earliest (end). Once you feel
that, every interval problem reduces to picking a sort column.

## Where it's used

- **By end:** activity selection, erase-min-overlaps (chapter 6)
- **By start:** merge intervals, insert interval, meeting-room checks
  (chapters 7–8)

## Common mistake

Sort-by-start on an activity-selection problem is **the #1 greedy bug** —
see the trace above: it kept the 9-hour meeting and lost two small ones.
Ask first: does my decision depend on when things *begin* or when they
*free up*?

## Your turn

To merge busy-time into free/busy blocks (`[[1,3],[2,6],[8,10]]` →
`[[1,6],[8,10]]`), which key — and why does the other fail?

<details><summary>Answer</summary>
**By start.** Merging walks time in order: each new interval either
touches the last block or doesn't. Sorted by end, `[1,3]` could come
*after* `[2,6]` even though it starts first — the sweep order would be
scrambled and overlaps missed.
</details>

---

**← Prev** [04 — Interval Words](04-interval-words.md) ·
**Next →** [06 — Activity Selection](06-activity-selection.md)
