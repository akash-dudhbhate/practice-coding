# 09 — `heapify` is faster than n pushes

> 4-minute read.

## The idea, plain words

Given a scrambled list, there are two ways to turn it into a heap:

```python
import heapq

nums = [5, 3, 8, 1, 9, 2]

# Way 1: heapify the whole thing at once — O(n)
a = nums[:]
heapq.heapify(a)                    # rearranges IN PLACE
print(a)                            # [1, 3, 2, 5, 9, 8]  (a valid heap)

# Way 2: push items one at a time — O(n log n)
b = []
for x in nums:
    heapq.heappush(b, x)
print(b)                            # [1, 3, 2, 5, 9, 8]  (same here)
```

Both produce valid heaps (the internal order can differ — either is
legal, since only the heap *rule* matters). But way 1 is O(n) while way
2 costs O(log n) **per push** → O(n log n) total.

## Why is `heapify` cheaper?

`heapify` runs **bubble-down from the bottom up** on every non-leaf
node — and here's the cute part, most nodes are near the bottom where
they can only fall a tiny distance:

```
level from bottom    how many nodes    work each (max swaps)
0  (the leaves)      ~ n/2             0 — nothing to do
1                    ~ n/4             ≤ 1
2                    ~ n/8             ≤ 2
3                    ~ n/16            ≤ 3
                   ...                 adds up to < n total swaps
```

Half the nodes do *zero* work, a quarter do at most one swap, an eighth
at most two... the sum stays under `n`. Contrast with pushing: every
one of n items can climb the full height → n × log n.

## When to use which

- **All data upfront?** → `heapify`. One O(n) pass, done.
- **Data arrives as a stream?** → `heappush` each item as it comes.
  You can't heapify what hasn't arrived yet.

## Where it's used

Kick-starting top-K solutions (chapter 10 heaps first `nums[:k]`),
heapsort's build phase, any "I have a list, make it a heap" moment.

## Common mistake

Two traps: **`heapify` returns `None`** — it modifies in place, so
`h = heapq.heapify(h)` sets `h` to `None` and everything after crashes.
And **reaching for pushes out of habit** when the whole list is already
sitting there — an easy O(n log n) → O(n) win.

## Your turn

You have a list of 1,000,000 items already in memory. `heapify` or a
million `heappush` calls — and roughly how much work does each do?

<details><summary>Answer</summary>
`heapify` — ≈ 1,000,000 units of work (O(n), most nodes barely move).
A million pushes ≈ 1,000,000 × ~20 = ~20,000,000 (each item may climb
the full height). Heapify wins by ~20×.
</details>

---

**← Prev** [08 — heapq + negation](08-heapq-min-heap-and-the-negation-trick.md) ·
**Next →** [10 — The top-k pattern](10-the-top-k-pattern.md)
