# 07 — Why Sliding Window is O(n), not O(n²)

> 4-minute read. A `while` inside a `for` — shouldn't that be quadratic?

## The idea, plain words

The variable-window skeleton *looks* nested — and nested loops multiply
(chapter 11 of lesson 01). But there's a loophole: **the inner `while`
doesn't restart.** `left` never goes back to 0. It only ever creeps
forward, chasing `right`.

## The proof in one picture

```
array index:   0  1  2  3  4  5  6  7
right visits:  →  →  →  →  →  →  →  →   each index ENTERS once
left  visits:  →  →  →  →  →  →  →  →   each index LEAVES once
```

Count moves, not loop rounds:

- `right` moves at most **n** times — it's the `for` loop.
- `left` moves at most **n** times *total across the whole program* — it
  never resets, never steps back.
- Each move does O(1) work (one `+=`/`-=` or one dict update).

Total: ≤ 2n moves × O(1) = **O(n)**. The `while` can shrink 5 times in
one round and 0 times in the next five — it doesn't matter. Add up every
shrink over the whole run and you still can't exceed n.

## Same input, both prices (from chapters 02–03)

n = 1,000, k = 500:

- Brute force: ~501 windows × ~500 adds ≈ **250,000 ops**
- Sliding: ~1,500 ops → **~170× less work**, and the gap grows with n.

This "total pointer movement" argument is *amortized analysis* — the same
reason `list.append` is O(1) amortized (lesson 01, chapter 14): occasional
expensive steps are fine if they're paid for by cheap ones.

## Why it exists

Because "a loop inside a loop" is a *shape*, not a cost. Cost comes from
how many times work actually runs — and you count that by asking "how far
can each variable travel?" Two pointers, one array, one-way tickets: 2n.

## Where it's used

Every sliding-window answer you give should end with this sentence:
**"O(n) time, because each element enters once and leaves once."**
Interviewers ask for it by name.

## Common mistake

Keeping the pointer argument intact while sneaking O(window) work inside:

```python
for right in range(n):
    if sum(nums[left:right+1]) > target:   # O(k) hidden scan — ruined!
        ...
```

`sum(...)` on the slice, `max(window)`, `s[left:right]` copying — each is
O(window size) per step → silently back to **O(n·k)**. The pointer-counting
proof only protects *O(1) updates*: `+=`, `-=`, dict bumps. Recompute state
from scratch and you're brute force wearing a costume.

(Copying the window is fine *only* for final output — e.g., saving the
best substring once per improvement, not every slide.)

## Your turn

```python
for right in range(n):
    total += nums[right]
    while total > target:
        seen = set(nums[left:right+1])   # rebuild a set each shrink
        total -= nums[left]
        left += 1
```

Still O(n)? Why or why not?

<details><summary>Answer</summary>
**No.** The `while` still runs ≤ n times total — but each iteration now
builds a set over the whole window, O(window size). That's O(n·k) work
overall. The "2n moves" argument only survives if every move costs O(1).
</details>

---

**← Prev** [06 — Windows + a count dict](06-window-with-a-count-dict.md) ·
**Next →** [08 — Windows vs two-pointers](08-windows-vs-two-pointers.md)
