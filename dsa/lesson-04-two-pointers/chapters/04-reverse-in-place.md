# 04 — Reverse in Place

> 4-minute read. First real pattern — and the easiest.

## The idea, plain words

Swap the two end elements, then step both pointers inward and repeat.
When the pointers cross, every element has been swapped exactly once.

Real-life version: **a line of dancers turning around.** The two dancers
at the ends trade places, then the next-inner pair trades, until the two
in the middle are face to face. Line reversed, nobody left their spot
twice.

"**In place**" means: change the given list itself, using O(1) extra
memory — no second list allowed.

## In code

```python
def reverse_in_place(nums):
    L, R = 0, len(nums) - 1
    while L < R:
        nums[L], nums[R] = nums[R], nums[L]   # swap the ends
        L += 1
        R -= 1
    return nums                                # same list, flipped

arr = [10, 20, 30, 40]
reverse_in_place(arr)
print(arr)
```

Output:

```
[40, 30, 20, 10]
```

## Hand trace — `[10, 20, 30, 40]`

```
L → [10, 20, 30, 40] ← R     swap 10 ↔ 40 → [40, 20, 30, 10]
    L → [20, 30] ← R          swap 20 ↔ 30 → [40, 30, 20, 10]
        L,R cross             L=2, R=1 → done
```

Odd length? `[7, 8, 9]`:

```
L → [7, 8, 9] ← R     swap 7 ↔ 9 → [9, 8, 7]
        ↑
       L==R on the middle 8 → L < R fails → stop
```

The middle element is already in its final spot — it swaps with no one.
That's *why* the loop is `L < R`, not `L <= R`.

## Why it exists

`s[::-1]` or `reversed()` builds a **copy** — O(n) extra space. Interviews
and real systems (browsers flipping pixel rows, editors reversing text)
often can't afford a second array, so the swap-ends trick flips the data
where it sits.

## Where it's used

Directly: `easy/p01`. Indirectly everywhere — reversing is the mirror
half of palindrome checks (ch. 05), and "swap ends then step in" shows
up inside rotation and shuffling algorithms.

## Common mistake

Building a new list and returning it when the task says *in place* — the
caller's array stays untouched and you burned O(n) space. The fix: mutate
`nums` itself with swaps; the tests check the original list object.

## Your turn

Trace `reverse_in_place([1, 2, 3, 4, 5])` by hand. What are the swaps,
and what's the final array?

<details><summary>Answer</summary>
`L → [1, 2, 3, 4, 5] ← R` → swap 1↔5 → `[5, 2, 3, 4, 1]`;
`L → [2, 3] ← R` → swap 2↔4 → `[5, 4, 3, 2, 1]`; L,R land on the 3
together → stop. Final: `[5, 4, 3, 2, 1]`. Two swaps for 5 elements —
the middle never moves.
</details>

---

**← Prev** [03 — Opposite ends](03-opposite-ends.md) ·
**Next →** [05 — Palindrome check](05-palindrome-check.md)
