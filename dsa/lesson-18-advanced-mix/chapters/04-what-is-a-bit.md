# 04 — What a Bit Actually Is

> 4-minute read. Binary from zero — no prior knowledge assumed.

## The idea, plain words

You already know **place value** — it's how you read any number:

```
base 10:  403  =  4×100 + 0×10 + 3×1     (each digit × a power of 10)
base  2:  110  =  1×4   + 1×2  + 0×1  = 6 (each digit × a power of 2)
```

A **bit** is just a base-2 digit — a slot that can only be 0 or 1. Read
the columns right-to-left as 1, 2, 4, 8, 16… and add up the slots that
hold a 1:

```
        8 4 2 1          8 4 2 1
  6 =   0 1 1 0 → 4+2    13 = 1 1 0 1 → 8+4+1
```

That's *all* binary is. Every integer in Python is secretly stored as a
row of these.

## Why computers bother

A wire inside a chip is either ON or OFF — two states, not ten. So
hardware natively speaks base 2. "Bit manipulation" = talking to the
number in its native clothing, which unlocks tricks impossible in
ordinary arithmetic (next three chapters).

## In Python — peek at the bits

```python
print(bin(6))          # 0b110   — Python shows base 2
print(bin(13))         # 0b1101  — that's 8+4+1
print(int("110", 2))   # 6       — read a binary string back
print(6 >> 1)          # 3       — push bits right = halve (next ch.)
```

## Hand-trace — count like a computer

```
decimal   binary      because
   0        0
   1        1
   2       10          the 1s column "rolled over" like 9→10 in base 10
   3       11          2+1
   4      100          rolled over again — 4s column
   5      101          4+1
   6      110          4+2
   7      111          4+2+1
   8     1000          every power of 2 = a single 1 followed by zeros
```

Memorize that last line — it powers half the tricks coming.

## Why it exists (in this lesson)

Some interview problems are secretly about *parity and patterns* —
"everything appears twice except one thing," "is n a power of 2," "count
the 1-bits." Base-2 thinking turns them into one-liners. You can't see
the tricks until you can see the bits.

## Where it's used

Everywhere low-level: file permissions (`rwx` = 3 bits), network masks,
compression, checksums, cryptography — and the "constant space" family
of interview questions.

## Common mistake

Reading `110` as "one hundred ten." In bit-land that's **six**. Always
say the columns: "four-two-one." Also — `bin()` returns a *string* like
`'0b110'`; arithmetic on it fails. It's for eyeballing only.

## Your turn

What number is `1010` in binary? Do it by columns before checking.

<details><summary>Answer</summary>
**10.** Columns are 8-4-2-1: `1×8 + 0×4 + 1×2 + 0×1 = 8 + 2 = 10`.
Sanity check: `bin(10)` → `'0b1010'`.
</details>

---

**← Prev** [03 — Coding a trie: the `is_end` flag](03-trie-code-is-end.md) ·
**Next →** [05 — The six bit operators](05-six-bit-operators.md)
