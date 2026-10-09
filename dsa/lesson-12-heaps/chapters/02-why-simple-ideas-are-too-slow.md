# 02 — Why the simple ideas are too slow

> 4-minute read.

## The idea, plain words

You already know two ways to build `add` + `take_best` with a plain
Python list. Both have one fast side and one slow side:

**Idea A — keep the list sorted.** Taking the best is instant (it's at
the end). But *adding* means finding the right slot and shifting
everything over → **O(n) per add**.

**Idea B — don't bother sorting.** Adding is instant (`append` → O(1)).
But *taking* the best means scanning the whole list → **O(n) per take**.

```python
# Idea A: sorted list — slow ADD, fast TAKE
waiting = []
waiting.append(8); waiting.sort()      # insert + re-sort: O(n) shifting

# Idea B: unsorted list — fast ADD, slow TAKE
waiting = []
waiting.append(8)                       # O(1) — but...
best = max(waiting)                     # O(n) — scan everything
waiting.remove(best)
```

Either way, **one of the two operations costs O(n)**. Do a million
adds and a million takes and you've done ~a trillion little steps.

```
                    add          take best      million ops each
unsorted list       O(1)         O(n)  scan     ~10^12 steps  💀
sorted list         O(n) shift   O(1)           ~10^12 steps  💀
heap (coming soon)  O(log n)     O(log n)       ~2×10^7 steps ✅
```

`log₂(1,000,000)` is about **20**. That's the entire magic trick of
this lesson: turn *every* operation from "walk a million" into "walk
about 20".

## Hand-trace the pain

Idea B on `waiting = [5, 2, 9, 1]`:

```
take_best: scan 5,2,9,1  -> find 9 (4 compares)
take_best: scan 5,2,1    -> find 5 (3 compares)
add(7):    append        -> [5,2,1,7] (1 step — nice)
take_best: scan again    -> find 7 (4 compares)
```

Every take re-scans *everything*, even though almost nothing changed.
That's the waste.

## Why it exists

You don't actually *need* the whole list sorted — you only need to know
**the single most extreme element**. Sorting maintains full order, which
is way more order than the question asks for. The heap's insight:
**pay for just enough order to find the extreme fast** — nothing more.

## Where it's used

This trade-off table *is* the interview answer. "Why a heap?" —
"because sorted lists make insert O(n), unsorted makes query O(n),
and a heap makes both O(log n)."

## Common mistake

Sorting inside a loop: `for x in stream: lst.append(x); lst.sort()` —
that's O(n log n) *per item*, O(n² log n) total. If you catch yourself
re-sorting every step, a heap is what you wanted. Same for `pop(0)`,
which is secretly O(n).

## Your turn

One million items, and you alternate `add`/`take_best` a million times
each using idea B (unsorted). Roughly how much work?

<details><summary>Answer</summary>
Each take scans up to ~1,000,000 items → ~10⁶ × 10⁶ = ~10¹² compares.
A heap does the same job in ~10⁶ × 20 = ~2×10⁷ steps — about 50,000×
less work.
</details>

---

**← Prev** [01 — The problem](01-the-problem-grab-the-extreme-fast.md) ·
**Next →** [03 — What a heap is](03-what-a-heap-is.md)
