# 10 — The top-k pattern: a heap of size k

> 6-minute read. The #1 interview pattern from this lesson.

## The idea, plain words

"Give me the **kth largest** / top k" does NOT need the whole input
sorted. It needs a **min-heap of size k** holding *the best k seen so
far* — where the root is the **worst of the best**, the bar a newcomer
must beat.

The direction feels backwards at first, so say it slowly: for the k
**largest**, keep a **min**-heap. Why? When a new item beats the worst
one you're keeping, you want to *evict the weakest* — and the weakest
kept item is exactly what a min-heap puts on top.

```python
import heapq

def kth_largest(nums, k):
    h = nums[:k]
    heapq.heapify(h)                  # min-heap of the first k
    for x in nums[k:]:
        if x > h[0]:                  # only bother if it beats the worst kept
            heapq.heapreplace(h, x)   # pop min + push, in one step
    return h[0]                       # the k-th largest overall

print(kth_largest([3, 2, 1, 5, 6, 4], 2))   # 5
```

## Hand-trace: `kth_largest([3, 2, 1, 5, 6, 4], k=2)`

```
h = [2, 3]        heapified first k=2        (min on top = the bar)
x=1:  1 < h[0]=2  -> skip                    (can't crack top 2)
x=5:  5 > 2       -> heapreplace -> [3, 5]   (bar rises to 3)
x=6:  6 > 3       -> heapreplace -> [5, 6]   (bar rises to 5)
x=4:  4 < 5       -> skip
answer: h[0] = 5   -> the 2nd largest ✅
```

## Why it exists

Sorting costs **O(n log n)** and stores all n. This pattern is
**O(n log k)** time, **O(k) memory** — and for *streaming* input it's
the only option, since you never hold more than k items. "Top 10 of 10
million" barely notices the data.

Flip it for "**k smallest**" → keep a **max-heap** of size k (negated
values, chapter 08). The rule never changes: *the heap holds the k best
so far; its root is the one you'd evict.*

And the cheat code — Python ships it:

```python
print(heapq.nlargest(2, [3, 2, 1, 5, 6, 4]))   # [6, 5]
print(heapq.nsmallest(2, [3, 2, 1, 5, 6, 4]))  # [1, 2]
```

…but interviews want the manual pattern, because `nlargest` can't
express "size-k heap with a custom rule."

## Where it's used

Top-K frequent words, k closest points, kth largest in a stream,
merge-k-sorted-lists (the heap holds one frontier element per list —
also a size-k heap!).

## Common mistake

**Keeping the wrong direction.** "We want largest, so max-heap" — a
max-heap of size k keeps evicting your *best* item and answers garbage.
You want the min-heap so the evictable one is on top. Second trap:
**pushing all n then popping k** — works, but it's O(n log n) and O(n)
space, which defeats the whole point; `heapreplace` gated by `x > h[0]`
keeps it at size k.

## Your turn

`kth_largest([7, 10, 4, 3, 20, 15], 3)` — trace it, then answer.

<details><summary>Answer</summary>
Heapify first 3 → [4, 10, 7]. x=3 < 4 skip. x=20 > 4 → replace →
[7, 10, 20]. x=15 > 7 → replace → [10, 20, 15]. Answer: **10**.
Check: sorted descending [20, 15, 10, 7, 4, 3] → 3rd largest is 10. ✔
</details>

---

**← Prev** [09 — heapify vs n pushes](09-heapify-faster-than-n-pushes.md) ·
**Next →** [11 — Tuples, priorities, and the priority queue](11-tuples-priorities-and-the-priority-queue.md)
