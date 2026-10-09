# 11 — Building strings: `join`, not `+=`

> 4-minute read. The chapter where immutability sends its bill.

## The idea, plain words

Chapter 04 said strings are immutable — every "change" builds a brand
new string. So `result += c` doesn't *add* a character to `result`; it
**photocopies the whole `result` plus `c`** into a new string and
throws the old one away.

In a loop that means: copy 1 char, then 2, then 3 ... then n. Total
work = `1 + 2 + 3 + ... + n` ≈ n²/2 → **O(n²)**.

`"".join(pieces)` does it once: measures all the pieces, allocates one
string of the right size, copies each character exactly once → **O(n)**.

Real-life version: **writing a report**. `+=` is retyping the entire
report from page 1 every time you add a sentence. `join` is writing
sentences on index cards, then photocopying the stack once at the end.

## Feel the difference

```python
text = "hello"

# SLOW: each += copies everything built so far
result = ""
for c in text:
    result += c.upper()
# copies: 1 + 2 + 3 + 4 + 5 = 15 chars for a 5-char string!

# FAST: collect pieces, glue once
pieces = []
for c in text:
    pieces.append(c.upper())     # append is O(1) — chapter 03
result = "".join(pieces)
print(result)                    # -> 'HELLO'

# The idiomatic one-liner you'll see everywhere:
result = "".join(c.upper() for c in text)
print(result)                    # -> 'HELLO'
```

Scale it up: for n = 100,000, `+=` copies ~**5 billion** characters;
`join` copies **100,000**. Same output, ~50,000× the work.

## The full round-trip: split → process → join

```python
s = "the cat sat"
words = s.split()                       # -> ['the', 'cat', 'sat']
shouted = [w.upper() for w in words]    # -> ['THE', 'CAT', 'SAT']
print(" ".join(shouted))                # -> 'THE CAT SAT'
```

`split` breaks a string into pieces (O(n)), you edit the *list* (lists
are mutable — ch 04's rule doesn't apply), and `sep.join(list)` glues
it back with `sep` between pieces (O(n)). `""` glues with nothing;
`" "` with spaces; `"-"` with dashes.

## Why it exists

Immutability (ch 04) keeps strings safe to share — this is the price.
`join` exists precisely so you pay that price once instead of n times.

## Where it's used

Every string-building loop: encoders (`hard/p03`!), formatters, CSV/JSON
emission, palindrome normalization, reversing words. Any `+=` on a
string inside a `for` is a bug-shaped smell.

## Common mistake

- `result += piece` in a loop — quadratic copying, invisible until
  input gets big.
- `nums.join(...)` — backwards! It's `glue.join(pieces)`:
  `"-".join(["a","b"])` → `'a-b'`. The separator owns the method.
- Joining non-strings: `",".join([1, 2])` → TypeError. Map first:
  `",".join(str(x) for x in [1, 2])` → `'1,2'`.

## Your turn

Rewrite without `+=`: build `"p-y-t-h-o-n"` from `"python"`.

<details><summary>Answer</summary>
```python
print("-".join("python"))        # -> 'p-y-t-h-o-n'
```
join treats the string as a sequence of 1-char pieces. Manual version:
`"-".join(c for c in "python")` — same thing.
</details>

---

**← Prev** [10 — Counting characters in one pass](10-counting-characters.md) ·
**Next →** [12 — Prefix sums + a dict: subarrays that sum to k](12-subarray-sum-k.md)
