# 01 — Why Sorting Matters at All

> 4-minute read. One idea only.

## The idea, plain words

**Sorting means putting things in a defined order** — usually smallest to
biggest. That's it. The interesting part isn't *how* to sort; it's *why
sorted data is a superpower.*

Real-life version: a pile of 500 business cards vs a **Rolodex**. Same
cards. But in the pile, finding "Priya" means flipping through all 500. In
the Rolodex, you flip to "P" — done in seconds. Sorted order turns "search
everything" into "jump to the right spot."

## Watch it happen

```python
nums = [4, 2, 4, 1, 2]
print(sorted(nums))          # [1, 2, 2, 4, 4]
```

Look at that output. Three problems just became easy:

- **Search?** Sorted → binary search (lesson 09) → ~3 checks instead of 5.
- **Duplicates?** They're *neighbors* now: `2, 2` and `4, 4` sit together.
  One pass removes them.
- **"3rd smallest"?** On `[1, 2, 2, 4, 4]` it's just index 2 → `2`.
  Unsorted, you'd have to hunt for it.

## Why it exists

Sorting is a **force multiplier**: you pay a cost ONCE to sort, then every
future question — search, dedup, k-th smallest, merging two datasets —
becomes cheap forever. Databases sort your query results, search engines
sort rankings, and inside interview problems "sort first" is often the
hidden step that unlocks everything else.

## Where it's used

Databases (`ORDER BY`, indexes), scheduling (earliest deadline first),
leaderboards, and as the secret preprocessing step inside tons of
two-pointer and greedy solutions.

## Common mistake

Sorting inside a hot loop — `for q in queries: arr.sort()` re-sorts n items
m times. Sort once outside the loop. Also: sorting isn't free (O(n log n)),
so don't sort if you only need ONE answer like the max — `max(arr)` is O(n).

## Your turn

`[5, 2, 4, 1]` sorted is `[1, 2, 4, 5]`. What's the cheapest way to check
whether `4` is in the sorted version?

<details><summary>Answer</summary>
Binary search: look at the middle (`4`) — found immediately. In the
unsorted version you'd scan every element. Sorted = pay once, search cheap
forever.
</details>

---

**Next →** [02 — What "sorted" means + stability](02-sorted-and-stability.md)
