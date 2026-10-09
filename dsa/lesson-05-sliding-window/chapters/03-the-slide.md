# 03 — The Slide: one out, one in

> 5-minute read. This is the whole trick of the lesson.

## The idea, plain words

Same problem, same array: max sum of `k = 3` consecutive in
`[2, 1, 5, 1, 3, 2]`.

Here's the observation from last chapter: when the window slides one step,
**one element leaves on the left and one element enters on the right** —
the other `k − 1` stay put. So don't re-sum anything. Just update:

```
new_sum = old_sum − leaving_element + entering_element
```

Like a train: at each station, one passenger steps off, one steps on.
You don't recount the whole car.

## Hand-trace — same array as chapter 02

```
[2, 1, 5, 1, 3, 2]
 └─k=3─┘             sum = 2+1+5 = 8    best=8   (built once, honestly)
    └─k=3─┘          sum = 8 − 2 + 1 = 7 best=8   (drop 2, add 1)
       └─k=3─┘       sum = 7 − 1 + 3 = 9 best=9   (drop 1, add 3)
          └─k=3─┘    sum = 9 − 5 + 2 = 6 best=9   (drop 5, add 2)
```

**Count the work:** 3 adds to build + 3 slides × 2 ops (one subtract,
one add) = **9 ops**. Brute force did 12. Small difference here — but
watch it grow below.

## The code

```python
def max_sum_k(nums, k):
    window_sum = sum(nums[:k])        # build the first window once
    best = window_sum
    for right in range(k, len(nums)):
        window_sum += nums[right]         # enters on the right
        window_sum -= nums[right - k]     # leaves on the left
        best = max(best, window_sum)
    return best

print(max_sum_k([2, 1, 5, 1, 3, 2], 3))   # 9
```

`nums[right]` is the newcomer. `nums[right - k]` is the element that just
fell off the left edge (when `right` is at index 3, the window starts at
0, so index `3 − 3 = 0` leaves).

## The savings, at scale

n = 1,000, k = 500 (same as your "Your turn" last chapter):

- **Brute force:** ~501 windows × ~500 adds ≈ **250,000 ops**
- **Sliding:** 500 adds to build + 500 slides × 2 ops ≈ **1,500 ops**

That's a **~170× reduction** — and the gap *widens* as n grows, because
brute force is O(n·k) while sliding is O(n): each element enters once
and leaves once. (Chapter 07 proves it properly.)

## Why it exists

Because "recompute everything" ignores structure. Sliding exploits the
fact that consecutive windows overlap almost entirely — the only *new
information* is one element in, one element out.

## Where it's used

Every fixed-size problem: max/min k-window sum, rolling averages,
counting windows past a threshold — your `easy/` set is exactly this.

## Common mistake

Forgetting the subtract. `window_sum += nums[right]` alone makes the sum
grow forever — you've invented an expanding blob, not a sliding window.
The pair `+= enterer / −= leaver` is inseparable.

## Your turn

Hand-trace `max_sum_k([1, 4, 2, 3], 2)`. Write each `sum = … − … + …`
line like the trace above. What does it return?

<details><summary>Answer</summary>
Build: 1+4 = 5, best=5. Slide: 5 − 1 + 2 = 6, best=6.
Slide: 6 − 4 + 3 = 5, best=6. Returns **6** (the window `[4, 2]`).
</details>

---

**← Prev** [02 — The brute-force way](02-the-brute-force-way.md) ·
**Next →** [04 — Fixed-size windows](04-fixed-size-windows.md)
