# 13 — Kadane's: extend or restart

> 6-minute read. Your first taste of dynamic programming — it's friendlier than the name.

## The idea, plain words

**Maximum subarray sum**: find the contiguous stretch with the biggest
total. There are O(n²) possible stretches — but Kadane's algorithm
answers it in **one pass** with two variables.

At each element ask one question:

> "Is my best run *ending here* better if I extend the previous run —
> or if I give up on it and restart fresh at this element?"

```
cur = max(x, cur + x)      # restart at x   vs   extend previous run
best = max(best, cur)      # remember the best run ever seen
```

- `cur` = best sum of a subarray that **must end at this index**.
- `best` = best `cur` ever seen → the answer.

Real-life version: **carrying a score on a hike**. Each segment adds or
subtracts points. If your running score drops *below zero*, the past
segments are pure dead weight — you'd do better pretending the hike
started right here.

## The famous trace — `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

```
x:        -2   1  -3   4  -1   2   1  -5   4
cur:      -2   1  -2   4   3   5   6   1   5
best:     -2   1   1   4   4   5   6   6   6
```

Read the interesting moments:

- **x=4 (index 3):** `cur` was `-2`. `max(4, 4 + (-2))` = `max(4, 2)` =
  **4** — we *restart*, dropping the dead weight `-2, 1, -3`.
- **x=-5 (index 7):** `max(-5, -5+6)` = `1` — extending hurt but still
  beat restarting. `best` stays `6` — it only goes up.

```python
def max_subarray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)      # extend or restart
        best = max(best, cur)
    return best

print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # -> 6
print(max_subarray([5, 4, -1, 7, 8]))                  # -> 23 (the whole thing!)
print(max_subarray([-3, -1]))                          # -> -1
```

O(n) time, O(1) space — two variables, one pass.

## Why it exists

Checking all subarrays is O(n²) pairs of endpoints. Kadane notices a
**negative running total can never help the future** — if `cur + x` is
worse than `x` alone, the old run only drags you down. Dropping it is
always free, so one pass suffices.

This is **dynamic programming** in seed form: "best ending here"
depends only on "best ending one step ago" — carry exactly that summary,
never rescan. Lesson 15 builds the full scaffolding on this intuition.

## Where it's used

`hard/p02` (exactly this), max-profit variants, "best contiguous
stretch" problems — and later, the mental model for all of 1D DP.

## Common mistakes (both are famous interview traps)

- **`cur = max(0, cur + x)` instead of `max(x, cur + x)`** — the `0`
  version silently allows the empty subarray. On `[-3, -1]` it answers
  `0`; the true answer is `-1`. Use `0` only if the problem permits
  empty picks.
- **Returning `cur` instead of `best`** — `cur` is "best ending *here*"
  (the last index by the end), not "best anywhere." Track both.
- **Initializing `cur = best = 0`** — same all-negative bug in disguise.
  Seed with `nums[0]`; every real subarray is at least as good as its
  worst element.

## Your turn

Trace `[2, -1, 2]` — write out `cur` and `best` after each element.

<details><summary>Answer</summary>
x=2: cur=2, best=2.
x=-1: cur=max(-1, 2+(-1))=1, best=2. (Extending still beats restarting.)
x=2: cur=max(2, 1+2)=3, best=3.
Answer: **3** — the whole array `[2,-1,2]`. The dip of -1 was worth
carrying because the +2 after it paid it back.
</details>

---

**← Prev** [12 — Prefix sums + a dict: subarrays that sum to k](12-subarray-sum-k.md) ·
**Next →** [14 — The big picture: three moves](14-the-big-picture.md)
