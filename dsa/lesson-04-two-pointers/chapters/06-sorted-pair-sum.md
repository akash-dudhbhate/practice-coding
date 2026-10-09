# 06 — Sorted Pair-Sum: the Blame Rule

> 6-minute read. Take this one slowly — it's the heart of the lesson.

## The idea, plain words

Problem: in a **sorted** array, find two numbers that add to `target`.

Put `L` on the smallest number, `R` on the largest. Look at
`nums[L] + nums[R]`:

- **Sum too small?** `nums[L]` is to blame — it's the tiniest element, so
  it can't reach the target even with the BIGGEST partner. Discard it
  forever: `L += 1`.
- **Sum too big?** `nums[R]` is to blame — it's too large even for the
  smallest partner. Discard it: `R -= 1`.
- **Equal?** Found.

Real-life version: **picking two teammates whose weights sum to a limit.**
If lightest + heaviest is already over, the heaviest person can never
pair with anyone — send them home. Sorted order gives every comparison
*a direction to blame*.

## In code

```python
def pair_sum_sorted(nums, target):       # nums MUST be sorted
    L, R = 0, len(nums) - 1
    while L < R:
        s = nums[L] + nums[R]
        if s == target:
            return [L, R]
        if s < target:
            L += 1                     # too small → blame the left end
        else:
            R -= 1                     # too big → blame the right end
    return []

print(pair_sum_sorted([1, 2, 4, 7, 11, 15], 9))
print(pair_sum_sorted([1, 3, 5], 10))
```

Output:

```
[1, 3]
[]
```

## Hand trace — `[1, 2, 4, 7, 11, 15]`, target 9

The brackets show the **remaining search space** — watch it shrink:

```
L → [1, 2, 4, 7, 11, 15] ← R    1 + 15 = 16 > 9  → 15 too big → R left
L → [1, 2, 4, 7, 11] ← R        1 + 11 = 12 > 9  → 11 too big → R left
L → [1, 2, 4, 7] ← R            1 + 7  = 8  < 9  → 1 too small → L right
    L → [2, 4, 7] ← R           2 + 7  = 9  ==   → FOUND → [1, 3]
```

4 comparisons. The nested loop would check all 15 pairs. And each move
was *safe* because sorted order guarantees it: when 1+7 < 9, we know
1 paired with 2 or 4 is even smaller — so 1 is dead weight everywhere.

## Why it exists

Picture the n² table of all pairs. Sorted order makes each comparison
delete a whole **row or column**: "1 is too small for 7" secretly means
"1 is too small for 7 AND everything left of it." One check, an entire
row erased. That's how O(n²) collapses to O(n) — not by checking faster,
but by *skipping on principle*.

## Where it's used

`easy/p03` directly. Then it becomes the inner engine of 3-sum and 4-sum
(chapter 11): fix one element, run this exact walk on the rest.

## Common mistake

Moving the **wrong** pointer. Sum too small → some people move `R` left
("try a smaller number") — but R is already paired with the SMALLEST
remaining element; moving R only shrinks the sum further. Burn this in:

```
sum < target → need bigger → move L right (values grow rightward)
sum > target → need smaller → move R left
```

## Your turn

Trace `pair_sum_sorted([2, 3, 5, 8], 8)` by hand — which indices come back?

<details><summary>Answer</summary>
`L → [2, 3, 5, 8] ← R`: 2+8=10 > 8 → R left. `L → [2, 3, 5] ← R`:
2+5=7 < 8 → L right. `L → [3, 5] ← R`: 3+5=8 → return **[1, 2]**.
</details>

---

**← Prev** [05 — Palindrome check](05-palindrome-check.md) ·
**Next →** [07 — Pattern 2: read & write pointers](07-read-write-pointers.md)
