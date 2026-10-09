# 07 — Why push and pop are O(log n)

> 3-minute read. Where the guarantee comes from.

## The idea, plain words

Look back at chapters 05 and 06. Both operations do the same thing in
disguise: **walk one straight path through the tree** — leaf→root for
push, root→leaf for pop — one swap per level.

So the cost is just the **height of the tree**. And a complete binary
tree is as short as a tree can possibly be: every level *doubles* the
capacity, so height ≈ `log₂ n`.

```
  nodes n      levels (height)   worst-case swaps per push/pop
      8            3                  ≤ 3
  1,024           10                  ≤ 10
  1,000,000       ~20                 ≤ 20
  1,000,000,000   ~30                 ≤ 30
```

A **billion**-item heap: push and pop cost at most ~30 steps. That's
the "walk about 20" promise from chapter 02, kept.

Quick check you can run:

```python
import math

for n in [8, 1024, 1_000_000, 1_000_000_000]:
    height = math.floor(math.log2(n))
    print(f"n={n:>12,}  height={height}")
# n=         8  height=3
# n=     1,024  height=10
# n= 1,000,000  height=19
# n=1,000,000,000  height=29
```

And the cheapest operation of all: **peek** at the minimum is just
`h[0]` — **O(1)**, no walking at all.

## Why it exists

The O(log n) is *why the tree must be complete*. Completeness isn't a
stylistic choice — it's what pins the height at log₂n. A lopsided tree
can degenerate toward a stick (height n), and push/pop would be back
to O(n). Chapters 05–06's "append at the end / take from the end"
moves exist precisely to preserve completeness.

## Where it's used

This is the answer to "why a heap?" in every interview: both
operations O(log n), peek O(1), and it beats the sorted-list approach
(chapter 02) where one of the two was O(n).

## Common mistake

Two misrememberings: thinking **push always costs log n** — it's the
*worst* case; a large push often needs 0 swaps and stops immediately.
And thinking **peek costs log n** — the min is already at index 0,
it's O(1). The O(log n) is only for the two *mutating* operations.

## Your turn

A heap holds ~1,000,000 items. Worst case, how many swaps does one
`heappop` need? And how many does `h[0]` need?

<details><summary>Answer</summary>
Pop: ≤ ~20 swaps (height ≈ log₂(10⁶) ≈ 19.9). Peek `h[0]`: **zero**
work — O(1), the minimum is already sitting at index 0.
</details>

---

**← Prev** [06 — Pop: bubble down](06-pop-swap-and-bubble-down.md) ·
**Next →** [08 — heapq: min-heap only + the negation trick](08-heapq-min-heap-and-the-negation-trick.md)
