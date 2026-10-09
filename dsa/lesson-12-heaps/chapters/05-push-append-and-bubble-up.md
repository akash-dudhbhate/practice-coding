# 05 — Push: append, then bubble up

> 5-minute read. First of the two heap operations.

## The idea, plain words

Pushing a new item into a heap is two steps:

1. **Append** it at the end of the array — that's the next free slot in
   the complete tree (bottom level, left-to-right).
2. **Bubble up** (a.k.a. *sift-up*): while the new item is smaller than
   its parent, swap them.

That's it. Append keeps the *shape* rule; bubbling up repairs the
*order* rule along the single path from the new leaf to the root.

## Hand-trace: push `0` into `[1, 3, 5, 7, 4]`

```
step 0  append:   [1, 3, 5, 7, 4, 0]
             1
            / \
           3   5        0 sits under 5 — and 0 < 5, violation!
          / \ /
         7  4 0

step 1  swap 0↔5: [1, 3, 0, 7, 4, 5]
             1
            / \
           3   0        now 0 < 1, still violating
          / \ /
         7  4 5

step 2  swap 0↔1: [0, 3, 1, 7, 4, 5]
             0
            / \
           3   1        0 reached the root — done
          / \ /
         7  4 5
```

Two swaps, fixed. Only ONE path up the tree was ever touched — every
other node already obeyed the rule.

## In real code — `heapq` does it for you

```python
import heapq

h = [1, 3, 5, 7, 4]          # already a valid min-heap
heapq.heappush(h, 0)
print(h)                     # [0, 3, 1, 7, 4, 5]
```

And here's what `heappush` is doing inside — pure index math from
chapter 04:

```python
def my_push(h, x):
    h.append(x)                    # next free slot
    i = len(h) - 1
    while i > 0:
        p = (i - 1) // 2           # parent index
        if h[p] <= h[i]:
            break                  # rule satisfied — stop early!
        h[p], h[i] = h[i], h[p]    # swap with parent
        i = p

h = [1, 3, 5, 7, 4]
my_push(h, 0)
print(h)                           # [0, 3, 1, 7, 4, 5] — same as heapq
```

## Why it exists

The new item can only break the rule on its *own ancestor path* — every
other parent-child pair is untouched by an append. So one upward walk
repairs everything. No global re-sort needed.

## Where it's used

`heapq.heappush` is exactly this. You'll also hand-write it in
interviews ("implement a heap") — it's ~10 lines.

## Common mistake

Thinking you must compare the new item against **siblings** or the
whole subtree. You only ever compare `child vs parent`, walking up.
Also: the `while` can stop early — pushing a big value often needs
**zero** swaps, so push is *at most* O(log n), frequently O(1).

## Your turn

Push `2` into `[1, 4, 3, 8, 5]`. What's the final array?

<details><summary>Answer</summary>
Append → `[1, 4, 3, 8, 5, 2]`. The 2's parent is index 2 → `3`, and
`2 < 3` → swap → `[1, 4, 2, 8, 5, 3]`. New parent is index 0 → `1`,
and `2 > 1` → stop. Final: `[1, 4, 2, 8, 5, 3]`. One swap.
</details>

---

**← Prev** [04 — The array trick](04-the-array-trick.md) ·
**Next →** [06 — Pop: swap and bubble down](06-pop-swap-and-bubble-down.md)
