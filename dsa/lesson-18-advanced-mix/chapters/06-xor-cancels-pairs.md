# 06 — XOR Cancels Pairs

> 4-minute read. The magic trick of this lesson.

## The idea, plain words

Remember XOR's rule: **1 where bits differ, 0 where they match.** Now
XOR a number with *itself* — every column matches, so every bit is 0:

```
x ^ x = 0        (a number cancels itself)
x ^ 0 = x        (xoring with 0 changes nothing)
```

And XOR doesn't care about order: `a ^ b ^ c = c ^ a ^ b`.

Real-life analogy: a **light switch**. Flip it twice and you're back
where you started — paired actions cancel. XOR-ing the same number
twice is the same: the second flip undoes the first.

## The famous problem it solves

*"Every element appears twice except one. Find it. O(1) space."*

A `Counter` or `set` works but uses O(n) memory — and interviewers ask
"can you do it in constant space?" precisely to force this trick:
XOR everything together. Every pair cancels; the loner survives.

## Hand-trace — `[4, 1, 2, 1, 2]`

```
0 ^ 4 = 4
4 ^ 1 = 5        (100 ^ 001 = 101)
5 ^ 2 = 7        (101 ^ 010 = 111)
7 ^ 1 = 6        (111 ^ 001 = 110)
6 ^ 2 = 4        (110 ^ 010 = 100)   ← the loner, standing alone

shorter way to see it:
4 ^ 1 ^ 2 ^ 1 ^ 2 = 4 ^ (1^1) ^ (2^2) = 4 ^ 0 ^ 0 = 4
```

## In code — three lines

```python
def single_number(nums):
    result = 0
    for x in nums:
        result ^= x          # pairs cancel; loner survives
    return result

print(single_number([4, 1, 2, 1, 2]))   # 4
print(single_number([-1, -1, -2]))      # -2  (works on negatives too)
```

No hash map. No counting. One accumulator — truly O(1) space.

## Why it exists

"Pairs cancel / find the odd one out" appears constantly — and this is
the *only* O(1)-space answer. It's also the foundation for the harder
version (two loners — ch.08) and the bitwise trie (ch.09).

## Where it's used

The single-number interview family, checksums (XOR all bytes — errors
flip detectable bits), RAID parity disks, and "which item changed" diff
tricks.

## Common mistake

Assuming XOR needs the pairs *adjacent* — it doesn't, order is
irrelevant. Also note XOR cancels *even counts*: three copies of `x`
leave `x` behind (`x^x^x = x`). The trick works because the problem
*guarantees* exactly-two-versus-one.

## Your turn

`single_number([7, 3, 5, 3, 7])` — what's the result, and which
operations cancelled?

<details><summary>Answer</summary>
**5.** `7^7 = 0` and `3^3 = 0`; `5` has no partner. Order doesn't
matter: `7^3^5^3^7 = (7^7)^(3^3)^5 = 0^0^5 = 5`.
</details>

---

**← Prev** [05 — The six bit operators](05-six-bit-operators.md) ·
**Next →** [07 — The lowest-bit tricks](07-lowest-bit-tricks.md)
