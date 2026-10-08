# lesson-02-arrays-strings — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Indexing vs membership
```python
nums = [10, 20, 30, 40, 50]
print(nums[3])
print(30 in nums)
```
Both "find 30-ish things" — which is O(1) and which is O(n)?

<details><summary>Answer</summary>
`nums[3]` → **30, O(1)** — a direct memory jump.
`30 in nums` → **True, O(n)** — a scan that got lucky early.
Indexing jumps; `in` searches.
</details>

---

## Check 02: Prefix sums
```python
nums = [2, 4, 6, 8]
P = [0, 2, 6, 12, 20]
# What is the sum of indices 1..2 inclusive?
```
- (A) P[2] - P[1] = 4
- (B) P[3] - P[1] = 10
- (C) P[2] - P[0] = 6

<details><summary>Answer</summary>
**(B) 10** — sum(i..j) = P[j+1] - P[i] = P[3] - P[1] = 12 - 2 = 10 (4+6).
The +1 shift is the #1 prefix-sum bug.
</details>

---

## Check 03: String building cost
```python
result = ""
for c in "abcde":
    result += c + "-"
```
Roughly how many characters get copied total?
- (A) 5
- (B) 10
- (C) ~30

<details><summary>Answer</summary>
**(C) ~30** — each `+=` copies the whole string so far: 2+4+6+8+10 = 30.
That's the O(n²) copying `join` avoids.
</details>

---

## Check 04: Kadane restart
```python
nums = [-5, 3, -1, 2]
# Trace cur = max(x, cur + x) at each element
```
What are the `cur` values?

<details><summary>Answer</summary>
`cur: -5, 3, 2, 4` → best = 4.
At index 1: `max(3, 3 + -5) = 3` — we *restarted*, dropping the -5 anchor.
A negative prefix can only hurt; cutting it loose is always free.
</details>

---

## Check 05: In-place vs new list
```python
def double(nums):
    nums = [x * 2 for x in nums]

a = [1, 2]
double(a)
print(a)
```
What prints?
- (A) [2, 4]
- (B) [1, 2]
- (C) Error

<details><summary>Answer</summary>
**(B) [1, 2]** — `nums = [...]` rebinds the *local* name; `a` still points at
the old list. In-place needs `nums[i] = nums[i] * 2` (mutating the same list).
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Running sum off-by-one

```python
def running_sum(nums):
    out = []
    total = 0
    for x in nums:
        out.append(total)
        total += x
    return out
```

**Hint:** `running_sum([1,2,3])` gives `[0,1,3]` — what's wrong?

<details><summary>Answer</summary>

**Bug:** Appends *before* adding x — every element is shifted one position
(the classic lag). `[1,2,3]` → `[0,1,3]` instead of `[1,3,6]`.
**Fix:** add first, then append: `total += x; out.append(total)`.
</details>

---

## Debug 02 (Medium): Kadane's all-negative trap

```python
def max_subarray(nums):
    cur = best = 0
    for x in nums:
        cur = max(0, cur + x)
        best = max(best, cur)
    return best
```

**Hint:** `max_subarray([-3, -1, -2])` should be -1, not 0.

<details><summary>Answer</summary>

**Bug:** `max(0, ...)` encodes "empty subarray allowed" — wrong when the
problem requires a non-empty subarray; all-negative input returns 0.
**Fix:** `cur = max(x, cur + x)` with `cur = best = nums[0]` start,
or use `-inf` initialization.
</details>

---

## Debug 03 (Hard): Subarray-sum-k missing seed

```python
def count_subarray_sum(nums, k):
    seen = {}                    # <- the bug
    P = 0
    count = 0
    for x in nums:
        P += x
        count += seen.get(P - k, 0)
        seen[P] = seen.get(P, 0) + 1
    return count
```

**Hint:** `count_subarray_sum([1,1,1], 2)` gives 1, not 2.

<details><summary>Answer</summary>

**Bug:** `seen` starts empty — a subarray beginning at index 0 has prefix
difference `P - 0 = P`, but 0 was never recorded, so it's never counted.
**Fix:** seed `seen = {0: 1}` — "an empty prefix sums to 0, once".
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: `+=` on strings in a loop
```python
# WRONG — O(n^2) copying
out = ""
for c in text:
    out += c.upper()

# CORRECT — O(n)
out = "".join(c.upper() for c in text)
```

## Mistake 02: Prefix-sum index shift
```python
# WRONG — returns sum(0..i) not sum(i..j)
return P[j] - P[i]

# CORRECT — P[i] = sum of first i elements; range i..j inclusive:
return P[j + 1] - P[i]
```

## Mistake 03: "In-place" that rebinds instead of mutates
```python
# WRONG — creates a new list, caller's list unchanged
def move_zeros(nums):
    nums = [x for x in nums if x != 0] + [0] * nums.count(0)

# CORRECT — mutate the same list object
def move_zeros(nums):
    w = 0
    for x in nums:
        if x != 0:
            nums[w] = x; w += 1
    while w < len(nums):
        nums[w] = 0; w += 1
```

## Mistake 04: `count()`/`index()` inside a loop (O(n²))
```python
# WRONG — each count() rescans the whole string
for c in set(text):
    print(c, text.count(c))

# CORRECT — one scan, one dict
freq = {}
for c in text:
    freq[c] = freq.get(c, 0) + 1
```

## Mistake 05: Forgetting empty/all-negative edge cases
```python
# nums=[] crashes on nums[0]; all-negative breaks max(0,...) Kadane.
# Always test: [], [x], all-negative, all-same.
```

## Mistake 06: Nested loop when two passes suffice
```python
# WRONG — for each i, rescan to learn "what's left/right of i"  -> O(n^2)
# CORRECT — pass 1 collects left-products, pass 2 multiplies right -> O(n)
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual index loop
### Before
```python
def running_sum(nums):
    out = []
    for i in range(len(nums)):
        if i == 0:
            out.append(nums[i])
        else:
            out.append(out[i - 1] + nums[i])
    return out
```
### Problems
1. Indexing when direct iteration is clearer
2. Special-casing index 0 inside the loop

### After
```python
def running_sum(nums):
    out, total = [], 0
    for x in nums:
        total += x
        out.append(total)
    return out
```

---

## Refactor 02 (Medium): Re-summing per query
### Before
```python
def answer_queries(nums, queries):
    return [sum(nums[i:j + 1]) for i, j in queries]   # O(q * n)
```
### Problems
1. Every query rescans its range — fine for 3 queries, slow for 30,000

### After
```python
def answer_queries(nums, queries):
    P = [0]
    for x in nums:
        P.append(P[-1] + x)              # build once: O(n)
    return [P[j + 1] - P[i] for i, j in queries]   # O(1) each
```

---

## Refactor 03 (Hard): Kadane with flags
### Before
```python
def max_subarray(nums):
    best = None
    cur = 0
    started = False
    for x in nums:
        if not started or cur < 0:
            cur = x
            started = True
        else:
            cur += x
        if best is None or cur > best:
            best = cur
    return best
```
### Problems
1. `started`/`None` flags duplicate what `max()` already expresses
2. Cur < 0 check is a special case of `max(x, cur + x)`

### After
```python
def max_subarray(nums):
    cur = best = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

---

## Approach Comparison — different ways to solve it

## Problem: Move zeros to the end, keep order

### Approach 1: Write pointer (in-place) — O(n) time, O(1) space
```python
def move_zeros(nums):
    w = 0
    for x in nums:
        if x != 0:
            nums[w] = x
            w += 1
    while w < len(nums):
        nums[w] = 0
        w += 1
```
**Pros:** No extra memory, single pass + tail fill. **Cons:** Mutates input.

### Approach 2: New list — O(n) time, O(n) space
```python
def move_zeros(nums):
    nz = [x for x in nums if x != 0]
    nz += [0] * (len(nums) - len(nz))
    nums[:] = nz              # slice-assign keeps it "in-place" to callers
```
**Pros:** Dead simple. **Cons:** Allocates a second list (the `nums[:]`
copy-back hides it but doesn't remove it).

**Winner:** Approach 1 — it's the pattern interviews mean by "in-place".

---

## Problem: Count subarrays summing to k

### Approach 1: Brute force — O(n²)
```python
count = 0
for i in range(len(nums)):
    s = 0
    for j in range(i, len(nums)):
        s += nums[j]
        if s == k:
            count += 1
```
**Pros:** Obvious. **Cons:** ~n²/2 inner iterations.

### Approach 2: Prefix sums + dict — O(n)
```python
seen = {0: 1}
P = count = 0
for x in nums:
    P += x
    count += seen.get(P - k, 0)
    seen[P] = seen.get(P, 0) + 1
```
**Pros:** One pass, handles negatives. **Cons:** O(n) space.

**Winner:** Approach 2 always — it's the canonical "difference of prefixes
in a hashmap" trick. Note Approach 1's inner `s` accumulation is already
O(n²), not O(n³) — good instinct to carry a running sum.
