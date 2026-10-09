# 05 — What Big-O Actually Means

> 5-minute read. The mystery notation, decoded.

## The idea, plain words

`O(n)` is not magic. It's a **shape label**.

- `O(n)` → "the work grows in a straight line with n" (linear)
- `O(n²)` → "the work grows like n-squared" (quadratic — explodes)
- `O(1)` → "the work doesn't grow at all" (constant)
- `O(log n)` → "the work grows super slowly" (halving — you'll see)

The `O(...)` is just a way to write the growth shape compactly. When someone
says "that's O(n²)" they mean: *"the steps grow like n² — roughly n×n."*

## Why we bother — keep only what matters

Say you count a recipe precisely: `3n² + 12n + 7` steps.

At n = 1,000,000:
- `3n²` = 3,000,000,000,000  (3 trillion)
- `12n` = 12,000,000  (0.0004% of the total — nothing)
- `7` = literally 7 steps

The n² term is doing ALL the work. The rest is noise. So we **drop
constants and small terms** and just say: `O(n²)`.

Two rules:
1. **Drop constants:** `O(2n)` → `O(n)`. (2× is a hardware-level detail.)
2. **Drop small terms:** `O(n² + n)` → `O(n²)`. (The big term wins.)

## The cheat table — memorize these shapes

| Label | Name | What it means | Feels like |
|-------|------|---------------|-----------|
| O(1) | constant | work never grows | instant, always |
| O(log n) | logarithmic | halve the problem each step | guessing 1–100 in ~7 tries |
| O(n) | linear | touch each item once | reading every page |
| O(n log n) | "n log n" | good sorting | splitting + merging piles |
| O(n²) | quadratic | every item pairs with every item | comparing all pairs |
| O(2ⁿ) | exponential | try every possibility | brute-forcing a lock |

**The only thing to feel viscerally:** n² at n=10 is 100. At n=1,000 it's a
million. At n=1,000,000 it's a trillion. That steep curve is the enemy —
most of DSA is learning to escape n².

## Your turn

A function does `2n + 500` steps. What's its Big-O?

<details><summary>Answer</summary>
`O(n)` — drop the 2 (constant) and the 500 (small term). The growth shape
is a straight line.
</details>

---

**← Prev** [04 — Why not seconds](04-why-not-seconds.md) ·
**Next →** [06 — O(1): constant time](06-o1-constant.md)
