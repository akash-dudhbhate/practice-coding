# Lesson 02 — Concepts Explained (Arrays & Strings)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Arrays vs Python Lists (and why indexing is O(1))

**What:** An *array* is a block of contiguous memory — every element sits in the
slot right next to the previous one. A Python `list` is an array of *pointers*
(each slot holds the address of the actual object), but the array part is still
contiguous, which is what matters for speed.

**Why it exists:** Contiguity makes indexing arithmetic: element `i` lives at
`base_address + i × slot_size`. The computer jumps straight there — no
scanning, no searching. That's why `nums[5000]` is just as fast as `nums[0]`.

**Where it's used:** Everywhere. `nums[i]`, `s[i]`, matrix rows — any time you
reach into a sequence by position, you're using O(1) indexed access.

**What goes wrong without it:**
- If elements were scattered (like a linked list), `nums[i]` would cost O(i) —
  you'd walk there one node at a time.
- Insert/delete in the *middle* is the flip side: `list.insert(0, x)` shifts
  every element → O(n). Beginners put it in loops and get accidental O(n²).

**Worked example (real numbers):**

```python
nums = [10, 20, 30, 40, 50]
nums[2]      # -> 30 — one memory jump, O(1)
nums[4999]   # same cost — index 2 or 4999 doesn't matter
```

Compare with membership: `40 in nums` scans up to all 5 slots → O(n).
Indexing is a *jump*; `in` is a *search*.

---

## Python List Gotchas (append vs insert)

**What:** `list.append(x)` is O(1) amortized — it drops a value into a spare
slot. `list.insert(0, x)` / `list.pop(0)` shift every element → O(n). Strings
behave like arrays you can't modify: `s[i]` is O(1) but `s[i] = c` is a
TypeError.

**Why it exists:** The contiguous block can't grow "into" occupied neighbor
memory, so inserts must shuffle elements to make room.

**Where it's used:** Choosing the right end to mutate — always build with
`append`; treat the front of a list as expensive (use `collections.deque` if
you need cheap pops at both ends).

**What goes wrong without it:**

```python
# O(n) per insert * n inserts = O(n^2)
for x in reversed(data):
    result.insert(0, x)

# O(n) total — same result
result = list(reversed(data))
```

---

## Prefix Sums (the cumulative-total trick)

**What:** A prefix-sum array `P` stores running totals: `P[i]` = sum of all
elements *before* index `i`. Built once in O(n), it answers "sum of elements
from index i to j" in O(1) forever after: `sum(i..j) = P[j+1] - P[i]`.

**Why it exists:** Answering one range-sum by scanning is O(n). Answering a
*thousand* range-sum queries by scanning is O(1000·n). Paying O(n) once for a
prefix array makes every query O(1) — precomputation trading space for time.

**Where it's used:** Range-sum queries, "sum of last k days" dashboards,
subarray problems (subarray-sum-equals-k uses it), cumulative statistics,
2D prefix sums for image regions.

**What goes wrong without it:**
- Re-summing per query is the classic O(q·n) → O(q + n) optimization.
- Off-by-one in the P[i] vs P[i+1] definition is THE prefix-sum bug. Pick a
  convention: `P[0] = 0` and `P[i]` = sum of first i elements. Then
  `sum(i..j inclusive) = P[j+1] - P[i]` — always.

**Worked example (real numbers):**

```python
nums = [1, 2, 3, 4, 5]

# Build: P[i] = sum of first i elements
P = [0]
for x in nums:
    P.append(P[-1] + x)
# P = [0, 1, 3, 6, 10, 15]

# sum of indices 1..3 = 2 + 3 + 4 = 9
P[4] - P[1]      # 10 - 1 = 9 — one subtraction instead of a loop!
```

**Expected output:** each query that scanned `j-i+1` elements now costs 2
lookups and 1 subtraction — O(1) per query, O(n) total to build.

---

## In-Place Modification vs Building a New List

**What:** Two ways to transform data:
- **In-place:** mutate the input itself — `nums[i] = new_val`. Uses O(1)
  extra space but *destroys the original*.
- **New list:** build `out` separately — O(n) extra space, original preserved.

**Why it exists:** Memory constraints ("do it in O(1) space" is a common
interview requirement) and safety (callers may not expect their data mutated).

**Where it's used:** `list.sort()` (in place) vs `sorted()` (new list) is the
same choice. Move-zeros, reverse-in-place, and dedup-in-place all live here.

**What goes wrong without it:**
- Accidentally mutating the caller's list → spooky bugs far away.
- Returning a new list when "in-place" was required → fails space constraint.
- Writing-while-reading traps: when you write into the same list you're
  scanning, use a separate *write pointer* (the slow/fast pointer pattern).

**The write-pointer pattern (how in-place edits stay safe):**

```python
def move_zeros(nums):        # O(n) time, O(1) space, mutates input
    w = 0                    # write pointer: next slot for a non-zero
    for x in nums:           # read pointer scans everything
        if x != 0:
            nums[w] = x
            w += 1
    while w < len(nums):     # fill the tail with zeros
        nums[w] = 0
        w += 1

a = [0, 1, 0, 3, 12]
move_zeros(a)
# a is now [1, 3, 12, 0, 0] — order kept, done in place
```

---

## Two-Pass Patterns (count first, build second)

**What:** Some problems need information you only know after seeing *all* the
input — so you make two passes: pass 1 gathers (counts, sums, maxes), pass 2
produces the answer using that information.

**Why it exists:** You can't label element 0 with "how many times it appears
overall" until you've seen the whole input. Two passes turn "I'd need a
nested loop" into "scan, then scan again" — O(n) + O(n) = O(n), not O(n²).

**Where it's used:** Product-except-self (pass 1 prefix products, pass 2
suffix products), frequency-labeled strings, normalize-by-total transforms.

**What goes wrong without it:**
- The tempting alternative is a nested loop — for each element, rescan the
  input to gather its stats → O(n²).
- With product-except-self specifically: dividing `total_product / nums[i]`
  crashes on zeros — two passes avoid division entirely.

**Worked example — product except self:**

```python
def product_except_self(nums):     # no division allowed!
    n = len(nums)
    out = [1] * n
    left = 1
    for i in range(n):             # pass 1: out[i] = product of everything LEFT of i
        out[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1): # pass 2: multiply in everything RIGHT of i
        out[i] *= right
        right *= nums[i]
    return out

# nums = [1, 2, 3, 4]
# after pass 1: out = [1, 1, 2, 6]
# after pass 2: out = [24, 12, 8, 6]
```

---

## String Scanning: Counting Characters

**What:** Characters are numbers under the hood — `ord('a')` is 97. To count
frequencies you scan once and tally into a dict (or `collections.Counter`).

**Why it exists:** Frequency is the backbone of half the string problems
(anagrams, most-common-char, window problems). A dict tally is O(n) — the
alternative, `s.count(c)` inside a loop, re-scans the string per character →
O(n²) (it's the `in` hidden loop again, one level down).

**Where it's used:** Anagram checks, encoding runs, "first unique character",
vowel counts, histogram building.

**What goes wrong without it:**

```python
# O(n) — the right way
def char_freq(text):
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1   # dict.get default: first sighting = 0
    return freq

char_freq("aab")     # {'a': 2, 'b': 1}

# O(n^2) — count() re-scans for every unique character
{c: text.count(c) for c in set(text)}
```

`Counter` does the same thing: `from collections import Counter;
Counter("aab")` → `Counter({'a': 2, 'b': 1})`. Learn `dict.get` first —
interviewers love seeing you can do it without imports.

---

## String Scanning: Building Strings (join, not +=)

**What:** Strings are immutable — every `+=` copies the whole string built so
far into a new one. `"".join(pieces)` allocates once and copies each piece in
place.

**Why it exists:** `+=` in a loop builds n intermediate strings: total copy
work is 1 + 2 + ... + n = O(n²) characters copied. `join` copies each
character exactly once → O(n).

**Where it's used:** Every string-building loop: encoders, formatters,
CSV/JSON emitters, palindrome normalization.

**What goes wrong without it:**

```python
# O(n^2) — quadratic copying
result = ""
for c in text:
    result += c.upper()

# O(n) — build a list of pieces, join once
pieces = []
for c in text:
    pieces.append(c.upper())
result = "".join(pieces)

# or the idiomatic one-liner
result = "".join(c.upper() for c in text)
```

For n = 100,000: `+=` copies ~5 billion characters; `join` copies 100,000.

---

## Prefix Sums + Hashing: Subarray-Sum-Equals-K

**What:** Combine prefix sums with a dict: while scanning, keep a count of
every prefix sum seen. If the current prefix is `P`, any earlier prefix of
`P - k` means the subarray between them sums to `k`.

**Why it exists:** Checking every subarray by summing is O(n²). The prefix
identity `sum(i..j) = P[j+1] - P[i]` rearranges to `P[i] = P[j+1] - k` — so
"does a subarray ending here sum to k?" becomes a single dict lookup.

**Where it's used:** Subarray sums, subarrays with equal 0s/1s, "number of
times we hit target balance" — the general trick is "difference of prefixes
in a hashmap".

**What goes wrong without it:**
- Forgetting to seed the dict with `{0: 1}` — a subarray starting at index 0
  sums to `P - 0`, and misses the count without the seed.
- Checking for `P - k` *after* inserting P — off-by-one ordering bugs.

**Worked example:**

```python
nums = [1, 1, 1]; k = 2
# prefixes: 0, 1, 2, 3
# at P=2: seen P-k=0 once -> +1 (subarray [1,1] at start)
# at P=3: seen P-k=1 once -> +1 (subarray [1,1] at end)
# answer: 2
```

---

## Kadane's Running Total (the seed of DP)

**What:** For "maximum subarray sum", scan once keeping `best_ending_here` —
the best sum of a subarray that *must end at this index*. At each step either
extend the previous run or restart here: `cur = max(x, cur + x)`. Answer =
best `cur` ever seen.

**Why it exists:** All subarrays = O(n²) pairs of endpoints; summing each =
O(n³) naive. Kadane notices a negative prefix can only hurt — dropping it
can never make things worse — so one pass suffices. It's the simplest dynamic
programming you'll ever meet: *optimal substructure* (best ending here
depends only on best ending there) + one variable of memory.

**Where it's used:** Max subarray, max profit variants, "best contiguous
stretch" problems, and as the mental model for 1D DP later (lesson 15).

**What goes wrong without it:**
- `cur = max(x, cur + x)` written as `cur = max(0, cur + x)` breaks on
  all-negative input: `[-3, -1]` should answer -1, not 0. (The `0` version
  means "empty subarray allowed" — only if the problem says so.)
- Tracking `cur` but forgetting `best` → returns the last `cur`, not the max.

**Worked example (real numbers):**

```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# cur:  -2  1  -2  4   3  5  6   1  5
# best: -2  1   1  4   4  5  6   6  6  -> answer 6 (subarray [4,-1,2,1])
```

At index 3 (value 4): `cur` was -2, so `max(4, 4 + -2) = 4` — we *restart*
rather than carry the dead weight of `-2, 1, -3`. That restart decision is
the whole algorithm.

---

## The Big Picture

Three reusable patterns from this lesson:

1. **Precompute once, query cheaply** (prefix sums) — pay O(n) up front to
   make each query O(1).
2. **Trade space for time** (hashmap of seen prefixes, frequency dicts) —
   O(n) memory buys O(n) time.
3. **One pass + running state** (Kadane, running max/min, write pointer) —
   carry exactly the summary you need; don't rescan.

Whenever a problem smells like "for each X, check all other Ys", ask: *can I
precompute, hash, or carry a running total instead?* That's the O(n²) → O(n)
instinct this lesson is building.
