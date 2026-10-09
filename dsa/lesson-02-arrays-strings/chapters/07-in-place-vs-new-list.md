# 07 — Change the list, or build a new one?

> 4-minute read. A fork in the road for every array problem.

## The idea, plain words

Every "transform this array" problem offers two roads:

- **In-place** — edit the input list itself: `nums[i] = new_val`.
  Uses **O(1) extra space** (a few variables), but the original data is
  *gone* — overwritten.
- **New list** — leave `nums` alone, build `out` next to it. Uses
  **O(n) extra space**, original preserved.

*In-place* just means "in its place" — changes happen inside the same
boxes, not in a copy.

Real-life version: **renovating a house vs building a new one**.
Renovating is cheap on land (no extra space) but the old rooms are
destroyed. A new house keeps the old one intact — at double the land.

## You've already seen this fork

```python
nums = [3, 1, 4]

nums.sort()             # in-place: nums itself becomes sorted
print(nums)             # -> [1, 3, 4]   original order is GONE

nums = [3, 1, 4]
copy = sorted(nums)     # new list: nums untouched, copy holds result
print(nums)             # -> [3, 1, 4]
print(copy)             # -> [1, 3, 4]
```

Same job, different deal: `sort()` spends no extra space but mutates;
`sorted()` spends O(n) space and preserves.

## Watch a real in-place edit

```python
nums = [1, 2, 3, 4]
for i in range(len(nums)):
    nums[i] = nums[i] * 10      # writing INTO the box, not a copy
print(nums)                     # -> [10, 20, 30, 40]
```

The caller's list changed. If some other part of the program still
expected `[1, 2, 3, 4]` — surprise. That's the cost of O(1) space.

## Why it exists

Two honest reasons:

1. **Memory limits.** "Do it in O(1) space" is a real constraint on
   huge inputs — and a famous interview requirement. Building a second
   n-element list may simply not be allowed.
2. **Safety.** Mutating data you don't own can cause bugs far away
   from where you wrote the code. Some problems *demand* in-place;
   others punish you for it.

## Where it's used

- `sort()` vs `sorted()`, `reverse()` vs `reversed()` — same choice.
- Move-zeros (medium/p02!), reverse-in-place, remove-duplicates —
  this lesson's in-place trio.
- Any function signature like `def f(nums) -> None` is whispering
  "in-place expected."

## Common mistake — the famous one

```python
nums = [3, 1, 4]
nums = nums.sort()      # WRONG: sort() returns None!
print(nums)             # -> None   ...and the list is lost
```

In-place methods (`sort`, `reverse`, `append`, `insert`) return
`None` — they already did their work on `nums`. Call them, don't
assign them.

## Your turn

`def double(nums) -> None` should double every element of the caller's
list in place. Write the one-line loop body (no new list).

<details><summary>Answer</summary>
```python
for i in range(len(nums)):
    nums[i] = nums[i] * 2
```
Check: `a = [1,2,3]; double(a)` → `a` is now `[2,4,6]`. Returning
`[x*2 for x in nums]` would be the *other* road — O(n) space, caller's
list untouched. Both are valid; the `-> None` contract picks this one.
</details>

---

**← Prev** [06 — Any range-sum in one subtraction](06-range-sum-one-subtraction.md) ·
**Next →** [08 — The write-pointer trick](08-write-pointer.md)
