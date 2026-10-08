# Lesson 12 — Heaps

## What you'll learn
- A heap = complete binary tree + heap property, stored as a flat array
  (`parent=(i-1)//2`, children `2i+1` / `2i+2`)
- Why push/pop are O(log n): sift-up and sift-down walk one root-to-leaf path
- `heapq` is a MIN-heap; max-heap via negation; payloads via tuples
- The top-K pattern: a heap of size k beats sorting — O(n log k) vs O(n log n)
- `heapq.merge` / `nlargest` / `nsmallest`, and the heap as a priority queue

## Lesson

`import heapq` — a heap is just a Python **list** with the invariant
`heap[i] <= heap[2i+1]` and `heap[i] <= heap[2i+2]` maintained by the
`heapq` functions. `heap[0]` is always the minimum (peek in O(1)).

```python
heapq.heapify(h)          # rearrange a list in place — O(n)
heapq.heappush(h, x)      # insert — O(log n)  (append + sift-up)
heapq.heappop(h)          # remove & return min — O(log n) (sift-down)
heapq.heappush(h, -x)     # max-heap: store negated values
heapq.heappush(h, (pri, i, item))   # priority queue: tuples order lexically
```

**Top-K pattern:** keep a heap of size k holding "the best k so far"; its
root is the worst of the best — the bar newcomers must beat.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels.

### Easy (start here) — the basic moves
1. `easy/p01-heap-ops-basics.py` — `run_heap_ops(nums, ops)`: heapify `nums`, then apply ops — `("push", x)`, `("pop",)`, `("peek",)` — collecting what pop/peek return.
   `[5,1,3]` + `push 0, pop, peek, pop` → `[0, 1, 1]`. Teaches heapify/push/pop/peek and that `heap[0]` is the min.
2. `easy/p02-kth-largest.py` — `kth_largest(nums, k)` → the kth largest element (duplicates count).
   `[3,2,1,5,6,4], k=2 → 5`. Do it with a heap of size k — O(n log k), not a full sort.
3. `easy/p03-top-k-frequent-words.py` — `top_k_frequent_words(words, k)` → k most frequent words, ties broken **alphabetically**.
   `["i","love","leetcode","i","love","coding"], k=3 → ["i","love","coding"]` (freq ties: `"coding" < "leetcode"` alphabetically).

### Medium — the top-K family
4. `medium/p01-k-closest-points.py` — `k_closest(points, k)` → k points closest to the origin, returned sorted by `(distance², x, y)` ascending.
   `[[3,3],[5,-1],[-2,4]], k=2 → [[3,3],[-2,4]]` (dist² 18 and 20).
5. `medium/p02-merge-k-sorted.py` — `merge_k_sorted(lists)` → one sorted list merging k sorted lists (plain lists, no linked list).
   `[[1,4,5],[1,3,4],[2,6]] → [1,1,2,3,4,4,5,6]`. Heap entries: `(value, list_idx, elem_idx)`.
6. `medium/p03-last-stone-weight.py` — `last_stone_weight(stones)`: repeatedly smash the two heaviest (`x==y` → both gone, else `|x-y|` remains); return the last weight, `0` if none.
   `[2,7,4,1,8,1] → 1`. The "always grab the max" loop = max-heap via negation.

### Hard — heaps as machinery
7. `hard/p01-median-of-stream.py` — `running_medians(nums)` → list where `out[i]` is the median of `nums[:i+1]` (floats).
   `[5,1,4,2,3] → [5.0, 3.0, 4.0, 3.0, 3.0]`. TWO heaps: max-heap for lower half (negated), min-heap for upper half, sizes within 1.
8. `hard/p02-task-scheduler.py` — `least_interval(tasks, n)` → minimum time slots to finish all tasks; same task needs `n` slots between runs (idle `_` allowed).
   `['A','A','A','B','B','B'], n=2 → 8` (e.g. `A B _ A B _ A B`). Greedily run the most-frequent available task — a max-heap on frequencies.
9. `hard/p03-reorganize-string.py` — `reorganize_string(s)` → any rearrangement with no two equal adjacent chars, or `""` if impossible.
   `"aab" → "aba"`; `"aaab" → ""`. Impossible iff `max_freq > (len(s)+1)//2`. Max-heap on `(freq, char)`.

### How to work
- Read `concepts.md` first — the recipe section maps each problem to a heap move.
- Open a problem file, read the header, write your code under the TODO marker.
- Run `python3 check.py easy/p01` for one problem, `python3 check.py all` for all nine.
- `coding-check.md` is your manual checklist; `EXTRA-PRACTICE.md` has debug drills after you finish.
- Peek at `solutions/` only after a real attempt — then close it and redo from memory.
