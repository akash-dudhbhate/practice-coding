# 10 — When Two Pointers FAILS

> 4-minute read. The dangerous failure is the silent one.

## The idea, plain words

Chapter 06's blame rule — "too small → move L" — only works because
**sorted order makes the blame true.** On unsorted data there is no
direction to blame: a small sum doesn't mean the left element is useless,
because a bigger partner could sit *anywhere*, including behind L or
ahead of R.

Real-life version: **the number-guessing game, but the list isn't
ordered.** "Higher" / "lower" hints are meaningless when the numbers
aren't arranged — you eliminate nothing with each guess.

## Watch it fail silently — `[3, 0, 5, 1]`, target 8

Sorted-logic applied to unsorted data (a pair **does** exist: 3+5):

```
L → [3, 0, 5, 1] ← R    3 + 1 = 4 < 8  → "blame L" → L right (wrong!)
    L → [0, 5, 1] ← R   0 + 1 = 1 < 8  → L right
        L → [5, 1] ← R  5 + 1 = 6 < 8  → L right
        L and R cross → "no pair found"   ← WRONG: 3 + 5 = 8 existed
```

No error. No crash. Just a wrong answer — because moving L right threw
away the 3 that was part of the real pair. `if s < target: L += 1` on
unsorted data is a coin flip dressed up as logic.

## In code — the guard

```python
def pair_sum_sorted(nums, target):
    # PRECONDITION: nums must be sorted ascending.
    # If it isn't, sort first — or use a hash set instead.
    assert nums == sorted(nums), "two pointers needs sorted input"
    L, R = 0, len(nums) - 1
    while L < R:
        s = nums[L] + nums[R]
        if s == target: return [L, R]
        L, R = (L + 1, R) if s < target else (L, R - 1)
    return []

print(pair_sum_sorted([1, 3, 5], 8))    # [1, 2] — fine, it's sorted
```

Output:

```
[1, 2]
```

## Why it exists (knowing limits = knowing the tool)

Two pointers needs **structure to exploit**: sortedness (blame rules),
symmetry (palindrome/reverse), or an in-place read/write split. Where
none exists, the technique has no leverage — so recognizing the missing
precondition IS a skill, not a failure.

## Where it's used (the right side of the line)

- Sorted arrays → opposite ends (ch. 04–06).
- Any array, in-place compaction → read/write (ch. 07–08).
- Unsorted array, indices needed, or stream → **hashing instead**.

**Don't reach for it when:**

- Input is unsorted **and** you need original indices → hash set.
- You need **all** pairs, not one → the walk finds at most one per pass.
- No random access — a linked list can't do `arr[R]`; it uses the
  slow/fast *node* variant instead (lesson on linked lists).
- The relationship isn't monotone — if "too small" doesn't point at one
  end to discard, no move rule exists.

## Common mistake

Assuming "it ran without error" means "it's correct." Two-pointer code on
unsorted input returns *a* answer smoothly — test your precondition first
(`assert nums == sorted(nums)` during development, or just sort).

## Your turn

`[5, 3, 9, 0]`, target 8 — trace the blame rule. A real pair exists
(3+5). Does the walk find it?

<details><summary>Answer</summary>
**No — silent miss.** `L → [5,3,9,0] ← R`: 5+0=5<8 → "blame L" → the 5,
half of the real pair, is discarded. `L → [3,9,0] ← R`: 3+0=3<8 → the 3
goes too. `L → [9,0] ← R`: 9+0=9>8 → R left → L,R cross → "no pair."
Both halves of 3+5=8 were individually "blamed" and thrown away. On
unsorted data the answer is correct only by luck.
</details>

---

**← Prev** [09 — Two pointers vs hashing](09-vs-hashing.md) ·
**Next →** [11 — Leveling up](11-leveling-up.md)
