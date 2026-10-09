# 09 — Search the Answer Space

> 7-minute read. The interview pattern that looks impossible until you see it once.

## The idea, plain words

Plot twist: sometimes **there is no array**. The search space is a range
of possible *answers* — a ship capacity, a speed, a minimum time.

The trick: if you can write `feasible(x)` — "does answer x work?" — and
feasibility is **monotone** (fails below some cutoff, works above it —
never flips back), then you binary search the ANSWER range:

```
capacity:  10  11  12  13  14 | 15  16  17  ...  55
feasible?   F   F   F   F   F |  T   T   T       T
                              ^ answer = first T
```

That's just lower bound over a predicate — chapter 07 wearing a costume.

## The three steps, every time

1. **Bound the answer** — capacity must be ≥ `max(weights)` (can't carry
   the heaviest box below it) and ≤ `sum(weights)` (one giant trip).
2. **Write `feasible(x)`** — a plain O(n) check: "can I ship in `days`
   days at capacity x?"
3. **Confirm monotone** — bigger x never makes it harder. Check!

## Watch it work — ship all weights in 5 days

```python
def days_needed(weights, cap):          # greedy loading, left to right
    days, load = 1, 0
    for w in weights:
        if load + w > cap:
            days += 1
            load = 0
        load += w
    return days

def min_capacity(weights, days):
    lo, hi = max(weights), sum(weights)     # answer range, NOT indices!
    while lo < hi:
        mid = (lo + hi) // 2
        if days_needed(weights, mid) <= days:
            hi = mid                        # works — try smaller
        else:
            lo = mid + 1                    # too slow — need more capacity
    return lo

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min_capacity(weights, 5))
print(days_needed(weights, 15))
```

```
15
5
```

The search trace — same `hi = mid` shape as lower bound:

```
lo=10 hi=55  mid=32 → needs 2 days  ✓ → hi=32
             mid=21 → needs 3 days  ✓ → hi=21
             mid=15 → needs 5 days  ✓ → hi=15
lo=10 hi=15  mid=12 → needs 6 days  ✗ → lo=13
lo=13 hi=15  mid=14 → needs 6 days  ✗ → lo=15
lo=15 hi=15 → return 15
```

Brute force tries all 45 capacities × O(n) each. Binary search: ~6
checks. The bigger the answer range, the bigger the win.

## Why it exists

"Find the smallest x such that condition holds" is EVERYWHERE —
Koko's bananas, minimum ship capacity, split-array-largest-sum. The array
was never the point; the monotone predicate was.

## Where it's used

Any problem phrased "minimum/maximum value so that..." with a
simulatable check. Spot it by the FFFFF|TTTTT shape hiding in the problem.

## Common mistake

Wrong bounds: starting `lo = 1` when the answer can't be below
`max(weights)` — harmless here (binary search just climbs), but in
variants `feasible` can crash or lie outside the valid range. Bound tight.

## Your turn

Why must `feasible` be monotone? What breaks if it's
`T F T F T` as x grows?

<details><summary>Answer</summary>
Binary search's bet is "x fails → every smaller x fails too." If a
bigger x can flip back to failing, "go right" throws away the half that
actually contains answers. No monotone predicate, no binary search.
</details>

---

**← Prev** [08 — The bisect module](08-bisect-module.md) ·
**Next →** [10 — Rotated sorted array](10-rotated-array.md)
