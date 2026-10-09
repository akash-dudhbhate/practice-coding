# 12 — Best, Worst, Average Case

> 4-minute read.

## The idea, plain words

Same recipe, different work depending on the input's *luck*:

- **Best case** — luckiest input (answer found immediately)
- **Worst case** — unluckiest input (maximum possible work)
- **Average case** — typical input

Interview rule: **when asked "what's the complexity?", answer worst case.**
That's the guarantee.

## In code — linear search

```python
def find(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i          # stops EARLY when found
    return -1
```

`nums = [5, 9, 2, 7]`:

| call | steps taken | case |
|------|------------|------|
| `find(nums, 5)` | 1 comparison | **best** — first element |
| `find(nums, 7)` | 4 comparisons | **worst** — last element |
| `find(nums, 99)` | 4 comparisons | **worst** — never found |

Best = O(1), worst = O(n). The early `return` saves the lucky cases but
can't change the worst. Report: **O(n) worst case**.

## Why it exists

"It depends" is honest, but useless for planning. Worst case is the ceiling
— it's what you promise won't be exceeded. Real systems die on the worst
case: sorted input into naive quicksort (pivot = first element → every
split is lopsided → O(n²)), crafted hash collisions, the one pathological
input that a user *will* find.

## Where it's used

- Linear search: best O(1), worst O(n)
- Quicksort: average O(n log n), worst O(n²)
- Hash lookup (`dict`/`set`): average O(1), worst O(n) (all keys collide)
- `list.append`: amortized O(1) (next chapter)

## Your turn

`find` on a million items where the target is missing — best, or worst?

<details><summary>Answer</summary>
Worst: n comparisons — it had to check every element to be SURE the target
isn't there. "Not found" is always the full scan.
</details>

---

**← Prev** [11 — Nested vs sequential](11-nested-vs-sequential.md) ·
**Next →** [13 — Space complexity](13-space-complexity.md)
