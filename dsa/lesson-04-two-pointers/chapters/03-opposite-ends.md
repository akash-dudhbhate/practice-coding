# 03 — Pattern 1: Opposite Ends (Meet in the Middle)

> 4-minute read.

## The idea, plain words

Put `L` on the first index and `R` on the last. Each round: look at the
two elements, decide which one is "settled," move that pointer inward.
Stop when they cross.

Real-life version: **zipping a jacket from both ends.** Or checking a
long hallway: you don't need to stand in every spot — you verify the two
ends, then move in. Everything behind a pointer is done *forever*.

The skeleton — you'll see this exact shape in the next three chapters:

```python
def meet_in_middle(nums):
    L, R = 0, len(nums) - 1
    while L < R:                   # while there's a gap between fingers
        print("looking at", nums[L], "and", nums[R])
        L += 1                     # ← the move RULE lives here —
        R -= 1                     #   each problem fills it differently

meet_in_middle([2, 4, 6, 8])
```

Output:

```
looking at 2 and 8
looking at 4 and 6
```

Every opposite-ends problem = this skeleton + **one move-rule**:

| Problem | Rule for moving |
|---|---|
| Reverse (ch. 04) | swap the ends, move BOTH inward |
| Palindrome (ch. 05) | ends match? move BOTH inward |
| Pair-sum (ch. 06) | too small → `L += 1`, too big → `R -= 1` |

## Hand trace — small data

Watching the fingers converge on `[2, 4, 6, 8]` (both-move version):

```
L → [2, 4, 6, 8] ← R     round 1: ends are 2 and 8
    L → [4, 6] ← R       round 2: ends are 4 and 6
        L,R cross        L=2, R=1 → gap closed → stop
```

Two rounds touched all 4 elements. The array behind L and ahead of R is
never visited again — that's where the O(n) comes from.

## Why it exists

Some questions are **symmetric** — "does the left end agree with the
right end?" (palindrome, reversal). Others need *one pair hiding
somewhere* (pair-sum). In both cases the only pairs that can matter are
the ones the pointers haven't passed yet, so walking inward visits every
relevant pair exactly once — never twice, never zero.

## Where it's used

Reverse in place, palindrome checks, pair-sum on sorted arrays, and —
escalated — container-with-most-water, trapping rain water, and the
inner engine of 3-sum/4-sum (chapter 11).

## Common mistake

- `while L <= R` when swapping: at the middle element L==R and you swap
  it with itself — harmless there, but the `<=` habit causes real bugs
  (double-processing) elsewhere. Use `<` unless you specifically need to
  process the middle.
- A rule that sometimes moves **no** pointer → infinite loop. Every
  branch of your rule must move at least one pointer inward.

## Your turn

`L, R = 0, 5` on a 6-element array, rule = "move both every round."
How many rounds before `L < R` fails?

<details><summary>Answer</summary>
3 rounds: (0,5) → (1,4) → (2,3) → (3,2), and `3 < 3` is False.
In general, both-move converging takes ~n/2 rounds — still O(n).
</details>

---

**← Prev** [02 — The two-pointer idea](02-the-two-pointer-idea.md) ·
**Next →** [04 — Reverse in place](04-reverse-in-place.md)
