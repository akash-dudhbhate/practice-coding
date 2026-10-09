# 11 — Tuples: priorities with payloads, and the real priority queue

> 6-minute read. How heaps carry actual data.

## The idea, plain words

So far our heap held bare numbers. Real problems attach a **payload** to
a **priority** — `(distance, node)`, `(frequency, word)`. Python makes
this free: push a **tuple**, and tuples compare element-by-element,
left to right — so the heap orders by priority first, then breaks ties
on the second element.

```python
import heapq

h = []
heapq.heappush(h, (2, "wake up"))
heapq.heappush(h, (1, "fix prod"))
heapq.heappush(h, (1, "answer pager"))
print(heapq.heappop(h))     # (1, 'answer pager') — tie broke on the string
```

## The tie-break crash — and the counter fix

Here's the trap: on a **tie**, Python compares the *second* element —
and if your payloads can't be compared, it explodes:

```python
h = []
heapq.heappush(h, (1, {"task": "a"}))
heapq.heappush(h, (1, {"task": "b"}))   # tie on 1 -> compares dicts -> TypeError!
```

The standard fix: insert a **unique counter** so items are never
compared:

```python
import itertools

h = []
counter = itertools.count()             # 0, 1, 2, ... forever unique
heapq.heappush(h, (1, next(counter), {"task": "a"}))
heapq.heappush(h, (1, next(counter), {"task": "b"}))
print(heapq.heappop(h))                 # (1, 0, {'task': 'a'}) — first in, first out
```

And for a **max-heap with a payload**, negate just the priority —
`(-dist, counter, node)`. (Negating the whole tuple doesn't work;
strings and dicts can't be negated.)

## A heap IS a priority queue — preview of lesson 14

Dijkstra's shortest path is literally this loop — the frontier always
expands the *closest known* node:

```python
heap = [(0, start)]                       # (distance, node)
while heap:
    dist, node = heapq.heappop(heap)      # grab the closest frontier
    if dist > best[node]:                 # stale entry? skip (lazy deletion)
        continue
    for nxt, w in graph[node]:
        heapq.heappush(heap, (dist + w, nxt))
```

Two idioms to notice: **lazy deletion** (push a better entry; skip
outdated pops instead of removing them) and **`(priority, item)`
tuples** carrying payloads. Event simulators, schedulers, Huffman
coding — all the same shape.

## The remaining `heapq` utilities

```python
heapq.heappushpop(h, x)    # push THEN pop — x can pop right back out
heapq.heapreplace(h, x)    # pop THEN push — always pops the old min
list(heapq.merge([1, 4], [2, 3]))   # -> [1, 2, 3, 4] — inputs MUST be sorted!
```

## Why it exists

Tuples + negation mean Python's single min-heap implementation covers
every real case — priorities, payloads, max-ordering — without new
machinery.

## Common mistake

The trio: **tie-break crash** (add a counter), **`heapq.merge` on
unsorted input** (it *merges*, it doesn't sort — silently produces
garbage), and **heapreplace vs pushpop order** — `heapreplace` pops
first, so top-k filtering wants it gated by `x > h[0]` (chapter 10).

## Your turn

After pushes `(1, "b")` then `(1, "a")`, what does `heappop` return?

<details><summary>Answer</summary>
`(1, "a")` — priorities tie at 1, so the second element breaks it, and
`"a" < "b"`. String tie-breaks work; uncomparable payloads need a
counter.
</details>

---

**← Prev** [10 — The top-k pattern](10-the-top-k-pattern.md) ·
**Next →** [12 — Two heaps + the recipe](12-two-heaps-and-the-recipe.md)
