# 07 — The Lowest-Bit Tricks

> 5-minute read. Three tricks, one bit: the lowest 1.

## The idea, plain words

The **lowest set bit** = the rightmost 1 in a number's bits. Three
famous one-liners all target it. First, watch what `n - 1` does: it
flips that lowest 1 to 0 and every 0 below it to 1:

```
x   = 12 = 1 1 0 0
x-1 = 11 = 1 0 1 1     ← lowest 1 became 0, everything below it flipped
x & (x-1) = 1 0 0 0    → 8 — the lowest 1-bit got erased
```

So **`x & (x-1)` clears the lowest set bit.** Every trick below is
that one move, reused.

## Trick 1 — is it a power of 2?

Powers of 2 are a single 1 followed by zeros (`8 = 1000`). Erase that
one bit → you get 0:

```
16 = 10000   15 = 01111   16 & 15 = 0        → power of 2
 6 = 00110    5 = 00101    6 &  5 = 4 ≠ 0    → not
```

## Trick 2 — count the 1-bits

Each `n &= n-1` erases exactly one 1. Count how many erases until 0:

```
n = 11 = 1011
step 1: 1011 & 1010 = 1010   count=1
step 2: 1010 & 1001 = 1000   count=2
step 3: 1000 & 0111 = 0000   count=3 → three 1-bits ✓
```

## Trick 3 — isolate the lowest 1: `x & -x`

Negation (two's complement) keeps the lowest 1 and flips everything
above it:

```
x  =  12 = ...001100
-x = -12 = ...110100      (flip all bits, add 1)
x & -x  = ...000100 = 4   ← exactly the lowest set bit, alone
```

You'll need this to split a group in chapter 08.

## Run all three

```python
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def count_bits(n):
    count = 0
    while n:
        n &= n - 1               # erase one 1-bit per round
        count += 1
    return count

print(is_power_of_two(16))   # True
print(is_power_of_two(6))    # False
print(is_power_of_two(0))    # False — the n>0 guard matters!
print(count_bits(11))        # 3   (1011)
print(12 & -12)              # 4   (lowest 1-bit of 1100 is 0100)
```

## Why it exists

These turn "examine every bit" loops into one-instruction answers —
and they're the exact operations interviewers name-drop ("can you test
power-of-two in O(1)?").

## Where it's used

Power-of-2 checks (memory sizes, hash-table capacities), bit-count /
Hamming-weight problems, Fenwick trees, and the two-loners partition
next chapter.

## Common mistake

Dropping the `n > 0` guard in `is_power_of_two`: `0 & -1 == 0`, so
without the guard `0` *lies* and returns True. Also — `x & (x-1)` on a
negative number misbehaves in Python (infinite sign bits, ch.08).

## Your turn

`count_bits(13)` — trace the `n &= n-1` loop. How many rounds?

<details><summary>Answer</summary>
**3 rounds.** `13 = 1101` → `1101 & 1100 = 1100` → `1100 & 1011 = 1000`
→ `1000 & 0111 = 0`. Three erases for three 1-bits (8+4+1).
</details>

---

**← Prev** [06 — XOR cancels pairs](06-xor-cancels-pairs.md) ·
**Next →** [08 — Two loners + Python's bit quirks](08-two-singles-and-python-quirks.md)
