# 12 — Picking the Right Sort (or skipping the sort)

> 5-minute read. Ties the lesson together.

## The idea, plain words

Sorting is a means, not an end. The pro move is asking: **"do I need the
full order, or just one answer?"** Full order → sort. Just the k smallest
→ a heap or quickselect can beat sorting. Just "have I seen this" → a
hash set makes sorting pointless.

## Watch it happen — same answer, less work

```python
import heapq

nums = [7, 2, 9, 4, 5]
print(sorted(nums)[2])                 # 5  — k-th smallest via FULL sort
print(heapq.nsmallest(3, nums)[-1])    # 5  — same answer, no full sort
```

Both give `5`. The first costs O(n log n); `nsmallest` costs O(n log k) —
and quickselect averages O(n). When k is small and n is huge, that gap is
the whole game.

## The cheat sheet

| Situation | Winner | Why |
|---|---|---|
| general purpose, Python | `sorted()` / `.sort()` | Timsort: stable, adaptive, tuned |
| guaranteed O(n log n) | merge sort | no bad-pivot surprise |
| guaranteed O(n log n), no extra memory | heapsort (rare in Python) | merge sort needs O(n) space |
| linked list | merge sort | pointer rewiring, O(1) extra |
| small int keys, small range | counting / radix | O(n + k) beats the floor |
| nearly sorted / tiny arrays | insertion sort | ~O(n) adaptive, zero overhead |
| k-th smallest, not full sort | quickselect / heap | ~O(n) beats sorting |
| elements near sorted spots | heap of size k+1 | O(n log k) |
| writes expensive (flash) | selection sort | ≤ n−1 swaps |
| just need membership | hash set | O(1) lookup — sorting is overkill |

## Quick reference — the numbers

| Sort | Best | Average | Worst | Space | Stable |
|---|---|---|---|---|---|
| bubble | O(n)\* | O(n²) | O(n²) | O(1) | yes |
| selection | O(n²) | O(n²) | O(n²) | O(1) | no |
| insertion | O(n) | O(n²) | O(n²) | O(1) | yes |
| merge | O(n log n) | O(n log n) | O(n log n) | O(n) | yes |
| quick (random pivot) | O(n log n) | O(n log n) | O(n²) | O(log n) | no |
| counting | O(n + k) | O(n + k) | O(n + k) | O(k) | output rebuild |
| Timsort (Python) | O(n) | O(n log n) | O(n log n) | O(n) | yes |

\*bubble's O(n) best case needs the swapped-flag early exit.

## Why it exists

Interviews (and real systems) don't ask "sort this" — they ask "find the
top k / dedupe / which is closest." Each answer has a cheapest tool; this
chapter is the menu.

## Common mistake

Sorting when you need ONE thing. `sorted(arr)[0]` is O(n log n) when
`min(arr)` is O(n). `sorted(arr)[:k]` when `heapq.nsmallest(k, arr)` is
O(n log k). Full sort buys you full order — don't pay for it if you won't
use it.

## Your turn

n = 10⁶ items, and you need the single biggest. Sort or scan?

<details><summary>Answer</summary>
Scan — `max(nums)` is O(n), one pass, no extra memory. Sorting is
O(n log n) and builds the whole order you'll never look at. Sort only
when you'll ask MANY order questions.
</details>

---

**← Prev** [11 — Python's sorted()](11-python-sorted-sort.md) ·
Done with concepts? → Open `task-explanation.md` and solve `easy/p01` next.
