# 08 — The `bisect` Module — Python Ships It

> 4-minute read. The standard library already solved chapter 07.

## The idea, plain words

Python's `bisect` module IS lower bound / upper bound, ready-made:

- `bisect_left(nums, x)` → first index where `x` could insert → **lower bound**
- `bisect_right(nums, x)` → index after all existing copies → **upper bound**
- `insort(nums, x)` → actually inserts `x`, keeping the list sorted

Memory hook: "left" = x goes left of equal items (first ≥), "right" =
x goes right of them (first >).

## Watch it work

```python
from bisect import bisect_left, bisect_right, insort

nums = [1, 2, 2, 2, 4]

print(bisect_left(nums, 2))                          # lower bound
print(bisect_right(nums, 2))                         # upper bound
print(bisect_right(nums, 2) - bisect_left(nums, 2))  # count of 2s
print(bisect_left(nums, 3))                          # slot for missing 3

insort(nums, 3)                                      # sorted insert
print(nums)
```

```
1
4
3
4
[1, 2, 2, 2, 3, 4]
```

Same answers as chapter 07's hand-rolled `lower_bound` — because it IS
the same algorithm, C-optimized and battle-tested.

## Why it exists

Real code shouldn't re-implement binary search — the bugs you met in
chapter 06 have already been fixed, once, correctly, in the stdlib.
You learned the template to *understand* and to *adapt* it (rotated
arrays, answer-spaces — bisect can't do those); for plain sorted lists,
use the tool.

## Where it's used

Insertion slots, counting occurrences, "smallest element ≥ x" lookups,
maintaining sorted lists. In interviews: acceptable in Python for simple
finds, but know the template cold — most problems bend it.

## Common mistake

`bisect_left` vs `bisect_right` confusion under pressure. Anchor it:
`bisect_left` = "**first ≥**" (x sits left of equals) → answers "first
occurrence". `bisect_right` = "**first >**" → answers "past the last".

## Your turn

`nums = [5, 10, 10, 15]`. What are `bisect_left(nums, 10)` and
`bisect_right(nums, 10)`? How many 10s?

<details><summary>Answer</summary>
bisect_left → 1, bisect_right → 3, count = 3 − 1 = 2. The left bound
points at the FIRST 10; the right bound sits after ALL of them.
</details>

---

**← Prev** [07 — Lower bound & upper bound](07-lower-upper-bound.md) ·
**Next →** [09 — Search the answer space](09-search-the-answer.md)
