# 06 — O(1): Constant Time

> 4-minute read. The fastest shape there is.

## The idea, plain words

`O(1)` means: **the work is the same no matter how big n gets.**

1 item or 1 billion items — the code does the same number of steps.

Real-life version: **opening a book to a specific page number.** You don't
flip through pages — you go straight to it. The book can be 10 pages or
1000 pages; the action is the same effort.

## In code

```python
def first_item(nums):
    return nums[0]          # jump straight to index 0 — always 1 step

def first_plus_last(nums):
    return nums[0] + nums[-1]   # 2 steps — still O(1)!
```

Even `nums[0] + nums[-1]` with 2 steps is O(1) — remember rule 1: drop
constants. `O(2)` → `O(1)`. What matters is it doesn't *grow* with n.

## Why it exists

Arrays store items in numbered slots. `nums[17]` isn't a search — the
computer jumps directly to slot 17. One step, always. That's why indexing
is the cheapest thing your code can do.

## Where it's used

- `nums[i]` — array/list indexing
- `dict[key]` — dictionary lookup (average case — hashing magic, lesson 03)
- `x in my_set` — set membership
- Push/pop at the end of a list

This is why "put it in a dict/set" is the #1 speed trick — lookup goes from
"scan everything" (O(n)) to "one step" (O(1)).

## Your turn

```python
def is_third_big(nums):
    return nums[2] == max(nums)
```

What Big-O? Careful — `max()` isn't free.

<details><summary>Answer</summary>
`O(n)` — `nums[2]` is O(1) but `max(nums)` scans the whole list: n steps.
The O(n) term dominates → O(n). A single `nums[i]` is O(1), but anything
that *visits* every element is O(n) minimum.
</details>

---

**← Prev** [05 — What Big-O means](05-what-big-o-means.md) ·
**Next →** [07 — O(n): linear time](07-on-linear.md)
