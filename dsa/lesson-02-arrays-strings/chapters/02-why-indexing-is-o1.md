# 02 — Why is `nums[5000]` as fast as `nums[0]`?

> 4-minute read. The single most important fact about arrays.

## The idea, plain words

Indexing an array is **arithmetic, not searching**.

Remember: the boxes sit **contiguous** — side by side, no gaps (chapter
01). So the computer knows two things: where the row starts, and how
wide each box is. To find box `i` it computes:

```
address of box i = start_address + i × box_size
```

One multiply, one add, done. It **jumps** straight there — whether `i`
is 0 or 5000, the work is identical. That's why `nums[i]` is **O(1)**:
constant time, no matter how big the array is.

Real-life version: **apartment numbers**. Apartment 317 is on floor 3 —
you compute the floor from the number and take the elevator. You don't
knock on 101, 102, 103... until you hit 317.

## Watch the difference

```python
nums = [10, 20, 30, 40, 50]

print(nums[2])      # -> 30 — one jump to address "start + 2×size"
```

Now the trap — `in` is a completely different animal:

```python
print(40 in nums)   # -> True — but HOW did it find 40?
```

`in` can't jump. It checks box 0: is it 40? No. Box 1? No. Box 2? No.
Box 3? Yes. It **scans** up to every box → **O(n)**.

- `nums[2]` — a **jump** to a known address. O(1).
- `40 in nums` — a **search**, one box at a time. O(n).

Same list, same square brackets energy — wildly different cost.

## One honest detail (you can skim this)

A Python `list` actually stores *pointers* — each box holds the address
of the real object, not the object itself. Doesn't matter: the boxes
are still contiguous, the jump math still works, and `nums[i]` is still
O(1). The detail only explains how one list can hold mixed types.

## Why it exists

Because contiguity turns "find box i" into one formula. If the boxes
were scattered around memory (that's a *linked list* — later lessons),
`nums[i]` would cost O(i) — you'd walk there box by box. Arrays trade
flexibility for that O(1) jump.

## Where it's used

`nums[i]`, `s[i]` on strings, `grid[r][c]` (a jump plus a jump) — every
indexed access in every program you'll write.

## Common mistake

Thinking `in` is as cheap as `[i]` because both "use" the array.
`x in nums` inside a loop = a hidden O(n) inside your loop → accidental
O(n²). If you need fast membership checks, that's what `set` is for.

## Your turn

Which line is O(1), and why?

```python
big = list(range(1000000))   # a million items
print(big[999999])           # line A
print(999999 in big)         # line B
```

<details><summary>Answer</summary>
Line A. `big[999999]` is one address calculation — instant. Line B may
scan all million boxes — O(n). The *size* of the list doesn't change
the cost of `[i]` at all; that's what O(1) means.
</details>

---

**← Prev** [01 — What is an array, really?](01-what-is-an-array.md) ·
**Next →** [03 — Why is adding at the front expensive?](03-append-vs-insert.md)
