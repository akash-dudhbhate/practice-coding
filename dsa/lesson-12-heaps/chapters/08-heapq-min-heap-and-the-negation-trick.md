# 08 — `heapq`: min-heap only, and the negation trick

> 5-minute read.

## The idea, plain words

Python's `heapq` is a **min-heap** operating on a plain list — the list
IS the heap, no wrapper class. Four functions do everything:

```python
import heapq

h = [5, 1, 3, 8, 4]
heapq.heapify(h)          # rearrange h into a valid heap (in place)
print(h)                  # [1, 4, 3, 8, 5]

heapq.heappush(h, 0)      # append + bubble-up
print(h)                  # [0, 4, 1, 8, 5, 3]

print(heapq.heappop(h))   # 0  -> remove min + bubble-down
print(h)                  # [1, 4, 3, 8, 5]

print(h[0])               # 1  -> peek the min, O(1), doesn't remove
```

## "But I need the BIGGEST" — the negation trick

`heapq` has **no max-heap mode**. The classic workaround: store every
value negated. The smallest `-x` sits at the root ⇔ the biggest `x`
does. Negate again on the way out.

```python
max_heap = []
for x in [3, 1, 4]:
    heapq.heappush(max_heap, -x)    # store -x, not x

print(max_heap)                     # [-4, -1, -3] — most negative on top
print(-heapq.heappop(max_heap))     # 4  <- negate back: the real max!
```

It feels backwards at first — "to get the biggest out, put the most
negative in" — but ordering under negation is just flipped, so the
min-heap machinery works unchanged.

## Why it exists

One implementation serving both directions is simpler than two. And the
trick generalizes: any time you want "largest first" from a min-first
structure — heap, sort key, bisect — negation is the move.

## Where it's used

Everywhere a max-heap shows up: `last_stone_weight` (smash the two
heaviest), task schedulers (highest priority first), "k smallest"
pattern in chapter 10.

## Common mistake

**Forgetting to negate on the way back out.** You push `-x`, then read
`heappop(h)` directly and get `-4` instead of `4` — a silent wrong
answer, not a crash. Also: `heappop([])` raises `IndexError` — guard
empty heaps with `if h:`. And no, there's no `heapq.maxheap` flag;
the underscore functions (`_heapify_max`) are private — don't touch
them in real code.

## Your turn

You push `-7`, `-2`, `-9` into a heap (the negation trick). What does
`-heapq.heappop(h)` return?

<details><summary>Answer</summary>
9. Inside the heap, `-9` is the smallest, so it pops first; negating
back gives `9` — the maximum of the original values {7, 2, 9}. ✔
</details>

---

**← Prev** [07 — Why push/pop are O(log n)](07-why-push-and-pop-are-ologn.md) ·
**Next →** [09 — heapify: faster than n pushes](09-heapify-faster-than-n-pushes.md)
