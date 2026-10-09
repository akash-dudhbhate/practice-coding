# 04 — The Fixed-Size Window Pattern

> 4-minute read. One reusable template.

## The idea, plain words

When the problem **hands you the size** (`k = 3`, "every 30 days", "groups
of 5"), the window never changes shape. The whole algorithm is:

1. **Build** the first window's state once.
2. **Slide:** one element enters, one leaves → update state in O(1).
3. **Record** the answer at each stop.

The "state" is whatever the problem asks about — a sum, an average, a
count of even numbers. The sliding mechanics are always identical.

## The template, run it yourself

```python
def window_sums(nums, k):
    if k > len(nums):               # edge case: no full window exists
        return []
    state = sum(nums[:k])           # 1. build first window
    out = [state]                   # 3. record it
    for right in range(k, len(nums)):
        state += nums[right]        # 2. enterer
        state -= nums[right - k]    #    leaver
        out.append(state)           # 3. record every stop
    return out

print(window_sums([2, 1, 5, 1, 3, 2], 3))
# [8, 7, 9, 6]
```

Change what `state` tracks and the same skeleton solves "averages of every
window" (divide by k at the end), "how many windows beat a target"
(count instead of append), or "which window is biggest" (keep `max`).

## Watch it slide

```
[2, 1, 5, 1, 3, 2]     k = 3
 └─┘                  state=8 → record 8
    └─┘               +1 −2 → state=7 → record 7
       └─┘            +3 −1 → state=9 → record 9
          └─┘         +2 −5 → state=6 → record 6
```

Each stop costs **2 operations** no matter how big k is. That's the
superpower: k = 3 or k = 300,000 — same work per slide.

## Why it exists

Fixed windows are the mechanical half of sliding window. The size is a
gift, so the only real question is "how do I update my state in O(1) when
one element swaps?" Master that update and every easy problem in this
lesson falls over.

## Where it's used

Rolling averages in metrics dashboards, k-day sales peaks, "how many
windows of size k satisfy X" counts — `easy/` problems 1–3 verbatim.

## Common mistakes

- **Starting `best = 0` on a max problem.** If every window sum is
  negative, 0 is wrong — it's not even a real window. Initialize
  `best = window_sum` (the actual first window). `[-1,-2,-3], k=2 → −3`.
- **Forgetting `k > len(nums)`.** There IS no size-k window on a shorter
  array — return `[]` or `0`, don't crash.
- **Recording before the window is full** if you write the loop from
  `right = 0`. Only record once `right >= k - 1`.

## Your turn

Using the `window_sums` template, what changes to return **averages** of
each size-k window instead of sums? `window_averages([1,2,3,4], 2)` → ?

<details><summary>Answer</summary>
Only the record step: append `state / k` instead of `state`
(or append sums and divide at the end).
`window_averages([1,2,3,4], 2)` → sums `[3, 5, 7]` → **`[1.5, 2.5, 3.5]`**.
</details>

---

**← Prev** [03 — The slide](03-the-slide.md) ·
**Next →** [05 — Variable-size windows](05-variable-size-windows.md)
