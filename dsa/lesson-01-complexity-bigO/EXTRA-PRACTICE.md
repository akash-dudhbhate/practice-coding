# lesson-01-complexity-bigO — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Sequential loops add, they don't multiply
```python
def f(nums):
    for x in nums:
        print(x)
    for x in nums:
        print(x * 2)
```
What is the complexity?
- (A) O(n)
- (B) O(n²)
- (C) O(2)

<details><summary>Answer</summary>
**(A) O(n)** — Two loops *side by side* do n + n = 2n ops. Drop the constant → O(n). Nested loops multiply; sequential loops add.
</details>

---

## Check 02: The hidden inner loop
```python
def has_dup(nums):
    seen = []
    for x in nums:
        if x in seen:
            return True
        seen.append(x)
    return False
```
What is the worst-case complexity?
- (A) O(n)
- (B) O(n²)
- (C) O(log n)

<details><summary>Answer</summary>
**(B) O(n²)** — `x in seen` on a *list* scans the whole list — a hidden inner loop doing up to n ops, inside a loop doing n iterations. Swap `seen` for a `set` to get O(n).
</details>

---

## Check 03: Doubling experiment
```python
# You measure: n=100 -> 200 ops, n=200 -> 400 ops, n=400 -> 800 ops
```
Which Big-O class fits best?

<details><summary>Answer</summary>
**O(n)** — Ops double when n doubles (ratio 2). O(n²) would quadruple; O(1) would stay flat; O(2ⁿ) would square.
</details>

---

## Check 04: Constant time is not "fast time"
```python
def slow_but_constant():
    for i in range(1_000_000):
        print(i)
```
Is this O(1)? Is it fast?

<details><summary>Answer</summary>
**O(1) — but slow.** There is no input `n`; the work is fixed at a million iterations. Big-O measures *growth with input*, not speed. This is constant AND slow — both can be true.
</details>

---

## Check 05: Recursive calls
```python
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```
`fib(5)` makes 15 calls. Roughly how many does `fib(10)` make?
- (A) 30
- (B) 60
- (C) ~180

<details><summary>Answer</summary>
**(C) ~177 calls** — each level roughly doubles the calls: 15, 25, 41, 67, 109, 177. That's why naive fib is O(2ⁿ), not O(2n).
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Op counter that lies

```python
def count_loop_ops(n):
    count = 0
    for i in range(n):
        pass          # the "work" happens here
    return count
```

**Hint:** The function should return how many times the body runs.

<details><summary>Answer</summary>

**Bug:** `count` is never incremented — always returns 0.
**Fix:** add `count += 1` inside the loop, or just `return n` once you see the pattern.
</details>

---

## Debug 02 (Medium): Wrong case analysis

```python
def find_first_even(nums):
    for x in nums:
        if x % 2 == 0:
            return x
    return None

# Claim: "this is O(1) because it returns early"
```

**Hint:** What happens with `[1, 3, 5, 7]` — or a million odd numbers?

<details><summary>Answer</summary>

**Bug:** Early exit gives a *best case* of O(1), but Big-O quotes the worst case. All-odd input scans everything → **O(n)**.
**Fix:** The code is fine; the claim is wrong. Correct statement: "best O(1), worst O(n)".
</details>

---

## Debug 03 (Hard): "O(n)" dedup that's really O(n²)

```python
def dedup(nums):          # author claims O(n)
    out = []
    for x in nums:
        if x not in out:
            out.append(x)
    return out
```

**Hint:** What is `x not in out` actually doing each iteration?

<details><summary>Answer</summary>

**Bug:** `in` on a list is a linear scan — hidden inner loop → O(n²) worst case.
**Fix:** keep a parallel `set` for membership (`if x not in seen_set`), or use `dict.fromkeys(nums)` — O(n) average.
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: Multiplying sequential loops
```python
# WRONG analysis — "two loops, so O(n²)"
for x in nums: ...
for x in nums: ...

# CORRECT — n + n = 2n → O(n)
```

## Mistake 02: Quoting best case
```python
# WRONG — "found early, so O(1)"
# CORRECT — complexity = worst case unless asked → O(n) for linear search
```

## Mistake 03: Forgetting `in`/`count`/`index` scan lists
```python
# WRONG — O(n²) disguised as O(n)
for x in nums:
    if x in big_list: ...

# CORRECT — O(n): set membership is O(1) average
big_set = set(big_list)
for x in nums:
    if x in big_set: ...
```

## Mistake 04: Counting the wrong thing as n
```python
# For a matrix n×n, elements = n².
# A single pass over the matrix is O(n²) in "side-length" terms —
# or O(m) if you define m = total elements. DEFINE YOUR n.
```

## Mistake 05: Ignoring space complexity
```python
# WRONG — claims O(1) space
def double(nums):
    return [x * 2 for x in nums]   # allocates n new items

# CORRECT — O(n) auxiliary space (the new list)
```

## Mistake 06: Believing constants never matter
```python
# Big-O drops constants for ANALYSIS, but at small n a low-constant
# O(n log n) can beat a high-constant O(n). Big-O is about growth.
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual doubling loop
### Before
```python
def doubled(nums):
    out = []
    for i in range(len(nums)):
        out.append(nums[i] * 2)
    return out
```
### Problems
1. Indexing when you can iterate directly
2. Manual loop when a comprehension does it

### After
```python
def doubled(nums):
    return [x * 2 for x in nums]
```

---

## Refactor 02 (Medium): O(n²) membership check
### Before
```python
def common(a, b):
    return [x for x in a if x in b]   # `in` scans b — O(len(a)*len(b))
```
### Problems
1. `x in b` on a list scans all of b each time

### After
```python
def common(a, b):
    b_set = set(b)                     # build once: O(len(b))
    return [x for x in a if x in b_set]  # O(1) per check → O(len(a)+len(b))
```

---

## Refactor 03 (Hard): Exponential fib → memoized
### Before
```python
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)   # O(2ⁿ) — recomputes everything
```
### Problems
1. Every value is recomputed many times (fib(3) alone is computed 3× for n=5)

### After
```python
def fib(n, memo={}):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]                    # O(n) — each value computed once
```

---

## Approach Comparison — different ways to solve it

## Problem: Find if any two numbers sum to target

### Approach 1: Nested loops — O(n²) time, O(1) space
```python
def pair_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False
```
**Pros:** No extra memory, easy to see. **Cons:** checks all ~n²/2 pairs.

### Approach 2: Set of complements — O(n) time, O(n) space
```python
def pair_sum(nums, target):
    seen = set()
    for x in nums:
        if target - x in seen:
            return True
        seen.add(x)
    return False
```
**Pros:** One pass. **Cons:** Allocates a set (up to n entries).

**Winner:** Approach 2 for time, Approach 1 when memory is tight. Classic
time–space trade-off — the pattern behind most "optimize this" answers.

---

## Problem: Remove duplicates while keeping order

### Approach 1: `x not in result` on a list — O(n²)
```python
def dedup(nums):
    out = []
    for x in nums:
        if x not in out:
            out.append(x)
    return out
```

### Approach 2: parallel set — O(n)
```python
def dedup(nums):
    seen, out = set(), []
    for x in nums:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
```

### Approach 3: dict.fromkeys — O(n), shortest
```python
def dedup(nums):
    return list(dict.fromkeys(nums))
```
(Dicts preserve insertion order since Python 3.7.)

**Winner:** Approach 3 for brevity; Approach 2 when you need the `seen` set
for other checks too.
