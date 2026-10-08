# Lesson 12 — Coding Check

Use this to verify your solutions before asking for review.

## Easy

### p01 — Heap ops basics
- [ ] `run_heap_ops([5,1,3], [("push",0), ("pop",), ("peek",), ("pop",)])` returns `[0, 1, 1]`
- [ ] `run_heap_ops([4,2,7], [("pop",),("pop",),("peek",)])` returns `[2, 4, 7]` (pops come out ascending)
- [ ] `run_heap_ops([], [("push",3),("push",1),("pop",)])` returns `[1]`
- [ ] You `heapify` first — a raw list is not a heap until you heapify it
- [ ] `peek` reads `h[0]` and does NOT remove it

### p02 — Kth largest
- [ ] `kth_largest([3,2,1,5,6,4], 2)` returns `5`
- [ ] `kth_largest([3,2,3,1,2,4,5,5,6], 4)` returns `4` (duplicates count)
- [ ] `kth_largest([1], 1)` returns `1`
- [ ] `kth_largest([7,7,7], 2)` returns `7`
- [ ] You keep a MIN-heap of size k — `h[0]` is the worst of the kept best; newcomers must beat it

### p03 — Top-k frequent words
- [ ] `top_k_frequent_words(["i","love","leetcode","i","love","coding"], 2)` returns `["i","love"]`
- [ ] Same input, `k=3` → `["i","love","coding"]` — freq tie between `"coding"`/`"leetcode"` breaks alphabetically
- [ ] `top_k_frequent_words(["the","day","is","sunny","the","the","the","sunny","is","is"], 4)` returns `["the","is","sunny","day"]`
- [ ] Higher frequency first; alphabetical SECOND — `(-freq, word)` heap entries or equivalent

## Medium

### p01 — K closest points
- [ ] `k_closest([[1,3],[-2,2]], 1)` returns `[[-2,2]]`
- [ ] `k_closest([[3,3],[5,-1],[-2,4]], 2)` returns `[[3,3],[-2,4]]`
- [ ] Result is sorted by distance — and ties break deterministically (by `x`, then `y`)
- [ ] You compare distance² (no `sqrt` needed — same ordering)

### p02 — Merge k sorted lists
- [ ] `merge_k_sorted([[1,4,5],[1,3,4],[2,6]])` returns `[1,1,2,3,4,4,5,6]`
- [ ] `merge_k_sorted([])` returns `[]`; `merge_k_sorted([[],[],[1]])` returns `[1]`
- [ ] Heap entries are `(value, list_idx, elem_idx)` — the indices prevent comparing payloads and let you push each list's NEXT element on pop
- [ ] `heapq.merge(*lists)` is the one-liner version — do you know why it works?

### p03 — Last stone weight
- [ ] `last_stone_weight([2,7,4,1,8,1])` returns `1`
- [ ] `last_stone_weight([1])` returns `1`; `last_stone_weight([1,1])` returns `0`
- [ ] `last_stone_weight([10,4,2,10])` returns `2`
- [ ] You used a MAX-heap via negation — every pop is `-heappop(h)`, every push is `heappush(h, -x)`
- [ ] Loop continues while `len(h) >= 2`; leftover single stone = its weight, empty = 0

## Hard

### p01 — Median of stream
- [ ] `running_medians([1,2,3])` returns `[1.0, 1.5, 2.0]`
- [ ] `running_medians([5,1,4,2,3])` returns `[5.0, 3.0, 4.0, 3.0, 3.0]`
- [ ] `running_medians([])` returns `[]`; `running_medians([2])` returns `[2.0]`
- [ ] Two heaps: `lo` = max-heap of lower half (NEGATED), `hi` = min-heap of upper half; sizes differ by at most 1
- [ ] After every insert you rebalance: max of `lo` ≤ min of `hi`, and `-lo[0]` is the median when sizes are equal-or-one-apart

### p02 — Task scheduler
- [ ] `least_interval(['A','A','A','B','B','B'], 2)` returns `8`
- [ ] `least_interval(['A','A','A','B','B','B'], 0)` returns `6` (no cooldown → just len)
- [ ] `least_interval(['A','A','A','B','B','B','C','C','C'], 2)` returns `9`
- [ ] `least_interval(['A','A','A','A','A','A','B','C','D','E','F','G'], 2)` returns `16`
- [ ] Each slot runs the most-frequent available task (max-heap on counts); tasks on cooldown wait in a separate list until the cooldown expires

### p03 — Reorganize string
- [ ] `reorganize_string("aab")` returns a valid arrangement (`"aba"` or equivalent — no adjacent equal, same letters)
- [ ] `reorganize_string("aaab")` returns `""` (impossible: `freq('a')=3 > (4+1)//2 = 2`)
- [ ] `reorganize_string("aaabbc")` returns a valid arrangement
- [ ] Algorithm: always place the most frequent remaining char (max-heap on `-freq`), but never twice in a row — hold back the just-used char for one step

## How to verify

```bash
python3 check.py all            # all nine of your files
python3 check.py hard/p01       # just one
python3 check.py solutions      # sanity-check the reference solutions
```
