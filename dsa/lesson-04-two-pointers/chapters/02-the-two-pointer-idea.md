# 02 — The Two-Pointer Idea

> 4-minute read.

## The idea, plain words

Use **two index variables** into the same array, and move them by rules —
each step decides which pointer moves, and a moved pointer **never goes
back.** No restarts, no do-overs. One pass, O(n).

Real-life version: **two people searching a hallway from opposite ends.**
Person A starts at the left door, person B at the right door, and they
walk toward each other. When they meet, every inch of hallway has been
checked exactly once — nobody re-walks ground the other already covered.

Compare with the brute-force way to check pairs — nested loops:

```python
nums = [1, 3, 5]
checks = 0
# brute force: EVERY item meets EVERY other item
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        checks += 1                    # n²/2 checks — lesson 01
print(checks)                          # 3 checks for 3 items
```

Output: `3` (on 100 items it'd be ~5,000).

Two pointers instead — same `nums`, one walk:

```python
nums = [1, 3, 5]
L, R = 0, len(nums) - 1      # finger at each end
while L < R:
    # look at nums[L] and nums[R], decide, move ONE pointer inward
    L += 1                   # (real problems pick WHICH pointer by a rule)
    R -= 1
print("crossed at", L, R)
```

Output: `crossed at 1 1` — both pointers landed on the middle element;
the walk ends when `L < R` fails, every element touched at most once.

## Hand trace — the shape of it

On `nums = [1, 3, 5, 7, 9]` — whatever the rule is, each round one
pointer steps inward and the unchecked zone shrinks:

```
L → [1, 3, 5, 7, 9] ← R    check the ends, move one pointer
    L → [3, 5, 7] ← R      zone shrinks — ends are settled for good
        L → [5] ← R        one element left → done
```

3 rounds instead of the nested loop's `5·4/2 = 10` pair-checks. On
n = 100,000: ~100k steps vs ~5 billion. That's the whole motivation —
chapter 06 shows the rule that makes each move *safe*.

## Why it exists

Nested loops are O(n²) because they **re-look at everything** — after
checking pair (1, 9) they go back and check (1, 7), (1, 5)... Two
pointers exploit *structure* in the data so each comparison lets you
**throw away** a whole slice of remaining pairs and never reconsider it.

## Where it's used

Two flavors, and they split this lesson in half:

- **Opposite ends** — `L` and `R` walk toward each other: reversal,
  palindrome, pair-sum on sorted data (chapters 03–06).
- **Same direction** — `fast` scans, `slow` writes: in-place dedup and
  compaction (chapters 07–08).

## Common mistake

Moving **both** pointers unconditionally. The power comes from moving
exactly the pointer that can't produce a better answer — if both march
every round regardless, you're just doing a fixed scan and throwing away
no work. Also: pointers that can step backward (restart) break the O(n)
guarantee.

## Your turn

On a 6-element array, how many pair-checks does the nested loop do, vs
how many rounds does an L/R pointer walk take at most?

<details><summary>Answer</summary>
Nested loop: 6·5/2 = **15 checks**. Pointer walk: L and R start 5 apart
and each round closes the gap by at least 1 → **at most 5 rounds**.
That's n²/2 vs n — and the gap only widens as n grows.
</details>

---

**← Prev** [01 — A pointer is just an index](01-a-pointer-is-just-an-index.md) ·
**Next →** [03 — Pattern 1: opposite ends](03-opposite-ends.md)
