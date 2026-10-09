# 05 — The Six Bit Operators

> 5-minute read. Six symbols, six tiny tables.

## The idea, plain words

Bit operators compare two numbers **column by column** — like grading
two answer sheets position-by-position. Line the bits up and apply one
rule per column:

```
   6 = 1 1 0        AND (&):  1 only where BOTH are 1  → 0 1 0 = 2
   3 = 0 1 1        OR  (|):  1 where EITHER is 1      → 1 1 1 = 7
                    XOR (^):  1 where bits DIFFER      → 1 0 1 = 5
```

The other three work on a single number:

- `~x` — flips every bit (has a Python quirk, below)
- `x << k` — shove bits left: **multiply by 2ᵏ** (`1 << 3 = 8`)
- `x >> k` — shove bits right: **halve, k times** (`12 >> 2 = 3`)

## Run every one — compare with the tables

```python
print(6 & 3)     # 2   (110 & 011 = 010)
print(6 | 3)     # 7   (110 | 011 = 111)
print(6 ^ 3)     # 5   (110 ^ 011 = 101)
print(1 << 3)    # 8   (1 → 10 → 100 → 1000 = ×2 three times)
print(12 >> 2)   # 3   (1100 → 110 → 11 = halve twice)
print(~5)        # -6  (?! explained below — and again in ch.08)
```

## Hand-trace — `12 & 10` column by column

```
  12 = 1 1 0 0
  10 = 1 0 1 0
  -----------
  &  = 1 0 0 0   ← only the leftmost column has two 1s → 8
  |  = 1 1 1 0   ← three columns have at least one 1  → 14
  ^  = 0 1 1 0   ← the two columns that differ        → 6
```

## Why it exists

These are *hardware-fast* (one CPU instruction) and unlock the
lesson-18 tricks: XOR's "differ" test is exactly what "pairs cancel"
needs (ch.06), and the masks behind `x & (x-1)` make powers of two
fall out for free (ch.07).

## Where it's used

Flag/permission checking (`flags & READ`), fast ×2 and ⌊÷2⌋, subset
masks (an integer IS a set of ≤32 items), and every bit trick in the
rest of this lesson.

## Common mistake — the `~` gotcha

In Python, `~x` is **not** "flip to a positive number." Python defines
`~x = -(x+1)`, so `~5 = -6`. Python ints have *infinite* sign bits, so
there's no fixed width to flip within. To invert the low `k` bits only:
`x ^ ((1 << k) - 1)`. Chapter 08 has the full story — for now just
don't trust `~`.

## Your turn

Column-by-column: what is `9 ^ 12`? (`9 = 1001`, `12 = 1100`)

<details><summary>Answer</summary>
**5.** Columns where they differ: `1001 ^ 1100 = 0101 = 4 + 1 = 5`.
Check: `9 ^ 12` → `5`.
</details>

---

**← Prev** [04 — What a bit actually is](04-what-is-a-bit.md) ·
**Next →** [06 — XOR cancels pairs](06-xor-cancels-pairs.md)
