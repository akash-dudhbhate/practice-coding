# 06 — The Infinite-Loop Bug (and the Overflow Note)

> 5-minute read. The most common binary-search bug in the world — meet it now so it never owns you.

## The idea, plain words

`mid = (lo + hi) // 2` rounds **down** — toward `lo`. So when only two
elements remain (`lo=3, hi=4`), `mid` lands ON `lo`. If your update is
`lo = mid` — lo stays 3, mid stays 3, forever. The range never shrinks,
the loop never ends.

## Watch it hang (safely — we capped the loop)

```python
def buggy(nums, target):
    lo, hi = 0, len(nums) - 1
    steps = 0
    while lo <= hi and steps < 10:    # cap added so we can SEE the hang
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid                  # BUG: should be mid + 1
        else:
            hi = mid - 1
        steps += 1
    return "still looping — lo never moved"

print(buggy([1, 3], 3))
```

```
still looping — lo never moved
```

The trace of the hang, on `[1, 3]` target `3`:

```
lo=0 hi=1  mid=0  nums[0]=1 < 3  → lo = mid = 0   ← SAME state!
lo=0 hi=1  mid=0  nums[0]=1 < 3  → lo = mid = 0   ← forever...
```

The fix is `lo = mid + 1` — `mid` was checked and failed, so it must leave
the range:

```
lo=0 hi=1  mid=0  nums[0]=1 < 3  → lo = 1
lo=1 hi=1  mid=1  nums[1]=3      → FOUND, return 1
```

## The overflow footnote

In Java/C++/Go, `lo + hi` can overflow a 32-bit int on huge arrays —
that's why those languages write `mid = lo + (hi - lo) // 2`. In Python
integers never overflow, so `(lo + hi) // 2` is fine. You'll still see
the long form in interview answers; now you know it's not magic.

## Why it exists (why this bug is so common)

The rule "mid ± 1" feels arbitrary until you see the rounding. The real
rule is: **every update must strictly shrink `[lo, hi]`, and `mid` is
always inside `[lo, hi]` — so keeping `mid` alive can only shrink the
range when the range has 3+ elements.** At 2 elements, rounded-down mid
== lo, and `lo = mid` shrinks nothing.

## Where it's used

This exact bug is a classic interview trap and a real production outage
story — Google's own binary search had the *overflow* version for years.

## Common mistake

Also: `while lo < hi` paired with `hi = mid - 1` — different bug, same
family. With `lo=3, hi=4`, if mid rounds to lo and the answer IS index 4,
the loop exits before checking it. Consistent contracts matter (ch. 03).

## Your turn

In the inclusive template, why is `hi = mid - 1` safe but `hi = mid`
dangerous?

<details><summary>Answer</summary>
When `nums[mid]` is too big, `mid` itself is dead — so `hi = mid` keeps a
confirmed-dead index alive. If `nums[mid] > target` but mid was ALSO the
smallest index… you can get `mid == hi`, and `hi = mid` moves nothing.
`mid - 1` always strictly shrinks.
</details>

---

**← Prev** [05 — Why O(log n)](05-why-log-n.md) ·
**Next →** [07 — Lower bound & upper bound](07-lower-upper-bound.md)
