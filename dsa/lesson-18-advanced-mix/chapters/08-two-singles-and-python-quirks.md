# 08 — Two Loners + Python's Bit Quirks

> 5-minute read. Chapter 06's hard mode — then the gotchas.

## The idea, plain words

Same problem as chapter 06, but **two** elements appear once
(`[1,2,1,3,2,5]` → `3` and `5`). XOR everything and you get `a ^ b`
— the two loners mashed together. Useless? Not quite:

- `3 ^ 5 = 6 = 110`. Every 1-bit is a column where **3 and 5 differ**.
- Grab one differing bit with `x & -x` (ch.07) → `6 & -6 = 2`.
- Split the array by "has this bit / doesn't": 3 and 5 land in
  *different* groups, and every duplicate pair lands in the *same* group.
- XOR each group → each reveals its loner.

## Hand-trace — `[1, 2, 1, 3, 2, 5]`

```
XOR all → 3 ^ 5 = 6 = 110        (1s cancel, 2s cancel)
diff bit = 6 & -6 = 2 = 010      a bit where 3 and 5 disagree

group "bit 010 set":   3(011), 2(010), 2(010) → 3^2^2 = 3
group "bit 010 clear": 1(001), 1(001), 5(101) → 1^1^5 = 5
answer: [3, 5]
```

## In code

```python
def single_numbers(nums):
    xor_all = 0
    for x in nums:
        xor_all ^= x                  # = a ^ b, the two loners
    diff = xor_all & -xor_all         # a bit where they differ
    a = 0
    for x in nums:
        if x & diff:                  # one side of the partition
            a ^= x
    return [a, a ^ xor_all]           # other loner = what's left

print(sorted(single_numbers([1, 2, 1, 3, 2, 5])))   # [3, 5]
```

## Python's bit quirks — read before they bite you

**1. `~x` is NOT a positive flip.** Python defines `~x = -(x+1)`, so
`~5 = -6`. To invert only the low `k` bits:

```python
print(~5)                    # -6   (not some big positive number!)
print(5 ^ ((1 << 3) - 1))    # 2    (101 ^ 111 = 010 — flip within 3 bits)
```

**2. Infinite sign bits.** Python ints have no fixed width — `-1` is
"…infinite 1s". If a problem says *32-bit integer*, say it in code:
`n &= 0xFFFFFFFF`. Otherwise `x & (x-1)` loops can behave oddly on
negatives.

**3. `>>` keeps the sign.** `-8 >> 1 = -4` (arithmetic shift — the
sign bit copies in). Want a logical shift? Mask to width first.

## Why it exists

This is the deepest bit trick in the set — it *composes* the previous
three (XOR-all, `x & -x`, group-and-cancel). If you can narrate this
trace in an interview, bit manipulation is officially yours.

## Where it's used

LeetCode "single number III", anywhere "find both uniques" appears, and
the partition-by-one-bit idea echoes into bit DP and hashing.

## Common mistake

Forgetting the second pass — after `diff` you must XOR *within one
group only* (`if x & diff`), not the whole array again. Xor-ing
everything twice just gets `a ^ b` back.

## Your turn

In `single_numbers`, why are duplicate pairs *guaranteed* to land in
the same group?

<details><summary>Answer</summary>
A pair is the *same number twice* — same bits, so `x & diff` gives the
same verdict for both copies. They fall in one group together, cancel
each other there, and can't pollute the other group.
</details>

---

**← Prev** [07 — The lowest-bit tricks](07-lowest-bit-tricks.md) ·
**Next →** [09 — The bitwise trie: max XOR](09-bitwise-trie-max-xor.md)
