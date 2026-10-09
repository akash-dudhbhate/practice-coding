# 05 — The Variable-Size Window Pattern

> 6-minute read. The harder shape — and the one interviews love.

## The idea, plain words

Fixed windows had it easy: the size was given. Now the size is the
**question** — "the *longest* chunk with no repeats," "the *shortest*
subarray reaching the target." Nobody tells you how wide the window is.

The answer is a window that **breathes**:

- `right` always grows the window (one step per loop round).
- `left` shrinks it — but **only while the window is invalid**.

```python
left = 0
for right in range(n):              # EXPAND: nums[right] enters
    add nums[right] to state
    while window_is_invalid:        # SHRINK until it's legal again
        remove nums[left]
        left += 1
    record answer                   # window [left..right] is valid here
```

Both pointers only ever move **forward**. `left` chases `right`; the
segment between them is always the current candidate.

## Hand-trace — smallest window reaching a target

**Problem:** smallest subarray with sum ≥ 7 in `[2, 3, 1, 2, 4, 3]`.
Here "valid" means `sum >= 7`, and we want it *short* — so we record
while valid and then shrink to squeeze it smaller.

```
right=0  [2]            sum=2   <7 → keep growing
right=1  [2,3]          sum=5   <7
right=2  [2,3,1]        sum=6   <7
right=3  [2,3,1,2]      sum=8   ≥7! len=4 → shrink: drop 2 → [3,1,2] sum=6
right=4  [3,1,2,4]      sum=10  ≥7! len=4 → drop 3 → [1,2,4] sum=7 len=3! → drop 1 → [2,4] sum=6
right=5  [2,4,3]        sum=9   ≥7! len=3 → drop 2 → [4,3] sum=7 len=2! → drop 4 → [3] sum=3
answer: 2   (the subarray [4,3])
```

## The code

```python
def min_subarray_len(target, nums):
    left, total, best = 0, 0, float("inf")
    for right in range(len(nums)):
        total += nums[right]                # expand
        while total >= target:              # valid → record, then squeeze
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float("inf") else best

print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))   # 2
```

## The two shapes of `while`

Same skeleton, but *when* you record flips with the question:

| Asked for | Shrink condition | Record when |
|-----------|------------------|-------------|
| **Longest** valid window | `while invalid` | AFTER the loop (window is now guaranteed valid) |
| **Shortest** valid window | `while valid` | INSIDE the loop, before each shrink |

Getting this backwards is the #1 logic error in the whole lesson — say
"longest or shortest?" out loud before writing the loop.

## Why it exists

"Expand right unconditionally; shrink left until valid" visits every
*maximal* valid window exactly once — you never miss the answer, and you
never redo work. This loop literally IS the algorithm for every
variable-size problem.

## Where it's used

Longest substring with no repeats, min-size subarray sum, longest run of
1s after k flips — the entire `medium/` and `hard/` sets are this skeleton
with different "invalid" tests.

## Common mistake

`if` where `while` belongs:

```python
if total >= target:        # WRONG — shrinks once, may still be valid
    left += 1
while total >= target:     # RIGHT — squeeze until it breaks
    left += 1
```

One step isn't enough when the shrink must remove several elements. The
bug passes small tests and silently fails on inputs needing multi-step
shrinks — exactly like the trace above, where `left` moved twice in one
round.

## Your turn

In the trace above, `right=4` shrank the window twice (`[3,1,2,4]` →
`[1,2,4]` → `[2,4]`). Why did it stop at `[2,4]`?

<details><summary>Answer</summary>
After dropping `3`, the window `[1,2,4]` still had sum 7 ≥ 7 — valid, so
record len 3 and shrink again. After dropping `1`, `[2,4]` sums to 6 < 7 —
invalid, so the `while` exits and `right` resumes expanding.
</details>

---

**← Prev** [04 — Fixed-size windows](04-fixed-size-windows.md) ·
**Next →** [06 — Windows + a count dict](06-window-with-a-count-dict.md)
