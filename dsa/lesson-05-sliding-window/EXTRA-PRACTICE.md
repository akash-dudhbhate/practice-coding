# lesson-05-sliding-window — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Which window shape?

For each problem, say FIXED or VARIABLE:

1. Average of every 30-day slice of stock prices.
2. Longest substring containing at most 2 distinct characters.
3. Number of size-5 subarrays whose sum is negative.
4. Smallest subarray whose sum reaches a target.
5. Longest substring without a repeating character.

<details><summary>Answer</summary>
1. FIXED (30 is given) · 2. VARIABLE · 3. FIXED · 4. VARIABLE · 5. VARIABLE.

Rule of thumb: the size is stated in the problem → fixed. The size IS the question ("longest/shortest") → variable.
</details>

---

## Check 02: Trace the shrink

```python
nums = [1, 4, 2, 10, 2, 3]
target = 8
# window expands while sum < 8; when sum >= 8, record length then shrink
# How many times does the while-loop body run TOTAL across the whole pass?
```

<details><summary>Answer</summary>
**3 times.**

- right=3: sum=1+4+2+10=17 ≥ 8 → record len 4 → drop 1 → 16, drop 4 → 12, drop 2 → 10, drop 10 → wait...

Careful trace: after right=3, sum=17. Shrink: drop nums[0]=1 → 16 (left=1), still ≥8 → drop nums[1]=4 → 12 (left=2), ≥8 → drop nums[2]=2 → 10 (left=3), ≥8 → drop nums[3]=10 → 0 (left=4). That's **4** shrinks.

- right=4: sum=0+2=2 <8. right=5: sum=2+3=5 <8. No more shrinks.

Total shrink iterations = **4**, and every shrink moved `left` strictly right. left went 0→4: at most n moves total. That's the O(n) argument in action.
</details>

---

## Check 03: What does this print?

```python
s = "dvdf"
left, best = 0, 0
last = {}
for right, c in enumerate(s):
    if c in last:
        left = last[c] + 1            # BUGGY version — missing guard
    last[c] = right
    best = max(best, right - left + 1)
print(best)
```

<details><summary>Answer</summary>
**4** — WRONG (correct answer is 3, `"vdf"`).

Trace: at right=3, `c='f'`. `last` = {d:2, v:1}. 'f' not in last → window is `"vdf"` (left=1, len 3) → best=3.

Wait — recheck right=2: `c='d'`, `last`={d:0,v:1} → left = 0+1 = 1 → window "vd" len 2, best 2→(was already 2). last={d:2,v:1}.

So buggy version: when right=3 'f' not seen → window "vdf" len 3 → best=3. It prints **3**.

Hmm — where does it break? Try `"abba"`: right=3 'a' seen at 0 → left=1 → window "ba" ok. Try `"tmmzuxt"`-style... The real break case: `s = "abba"`, right=2 'b' seen at 1 → left=2, fine; right=3 'a' seen at 0 → `left = last['a']+1 = 1` — left moves BACKWARD from 2 to 1! Window becomes "bba" including the duplicate 'b's → records len 3, best=3 but true answer is 2.

So for `"dvdf"` it prints 3 by luck; for `"abba"` this buggy code prints **3** (true: 2). The missing guard is `if c in last and last[c] >= left:` — only jump if the old occurrence is INSIDE the current window.
</details>

---

## Check 04: Complexity spot-check

```python
def window_sums(nums, k):
    out = []
    for i in range(len(nums) - k + 1):
        out.append(sum(nums[i:i+k]))
    return out
```

What's the time complexity, and why doesn't the O(n) argument rescue it?

<details><summary>Answer</summary>
**O(n·k)** — roughly `n` windows, each `sum()` scans `k` elements. There is no persistent window state here: each `sum(nums[i:i+k])` recomputes from scratch, so the "each element enters/leaves once" argument doesn't apply. The fix is to keep a running `window_sum` and update it with 2 ops per slide.
</details>

---

## Check 05: Longest vs shortest

For `min_subarray_len`, why do we record the answer INSIDE the `while` loop instead of after it?

<details><summary>Answer</summary>
Because for a **shortest-valid** problem, the window stops being valid exactly when you shrink it — the valid windows only exist *inside* the `while total >= target` loop. Recording after the loop would record a shrunken invalid window (sum < target). For **longest-valid** problems it's the opposite: the window is valid only *after* the shrink loop finishes.
</details>

---

## Debug Exercises — find and fix the bug

> Fix the broken code. Find bugs mentally before running.

---

## Debug 01 (Easy): Fixed window — re-summing

```python
def max_sum_k(nums, k):
    best = 0
    for i in range(len(nums) - k + 1):
        best = max(best, sum(nums[i:i+k]))
    return best
```

**Hint:** Two bugs — one about correctness on negative inputs, one about complexity.

<details><summary>Answer</summary>

**Bug 1:** `best = 0` fails all-negative inputs: `max_sum_k([-1,-2,-3], 2)` returns 0 instead of -3. Initialize from the first window: `best = sum(nums[:k])`.
**Bug 2:** `sum(nums[i:i+k])` inside the loop makes it O(n·k) — the whole point of the window is a running sum. Fix: `window_sum += nums[i+k-1] - nums[i-1]` per step (or the standard right/left-k form).
</details>

---

## Debug 02 (Medium): No-repeat substring — `if` instead of `while`

```python
def length_of_longest_substring(s):
    left, best, seen = 0, 0, set()
    for right, c in enumerate(s):
        if c in seen:                 # BUG: single-step shrink
            seen.remove(s[left])
            left += 1
        seen.add(c)
        best = max(best, right - left + 1)
    return best
```

**Hint:** Try `"abba"` — walk it through.

<details><summary>Answer</summary>

**Bug:** `if` shrinks only once, so `c` can still be in `seen` when re-added. Trace `"abba"`: right=2 'b' in seen → remove s[0]='a' (wrong char!), left=1; seen={b,a} still has 'b' → add 'b' again (no-op); window "bb" is invalid but counted → best=3 wrongly.

Wait, more carefully: after right=1, seen={a,b}. right=2 'b' in seen → remove s[0]='a' → seen={b}; left=1 → seen.add('b') no-op → window s[1..2]="bb" len 2 counted. right=3 'a' not in seen({b}) → add → window s[1..3]="bba" len 3 → best=3. True answer 2.
**Fix:** `while c in seen:` — shrink until the duplicate actually leaves.
</details>

---

## Debug 03 (Medium): Min-subarray — recording after the shrink

```python
def min_subarray_len(target, nums):
    left, total, best = 0, 0, float("inf")
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            total -= nums[left]
            left += 1
        best = min(best, right - left + 1)   # BUG: too late
    return 0 if best == float("inf") else best
```

**Hint:** What's `total` after the while loop ends?

<details><summary>Answer</summary>

**Bug:** After the while loop, `total < target` — the window is INVALID, but we record its length anyway. E.g. `min_subarray_len(7, [2,3,1,2,4,3])`: after shrinking at right=5, window "3" (len 1) has sum 3 < 7 yet gets recorded → returns 1 instead of 2.
**Fix:** record INSIDE the while, before shrinking:
```python
while total >= target:
    best = min(best, right - left + 1)
    total -= nums[left]
    left += 1
```
</details>

---

## Debug 04 (Hard): K-distinct — zombie keys

```python
def length_of_longest_k_distinct(s, k):
    left, best, count = 0, 0, {}
    for right, c in enumerate(s):
        count[c] = count.get(c, 0) + 1
        while len(count) > k:
            count[s[left]] -= 1      # BUG: never deletes
            left += 1
        best = max(best, right - left + 1)
    return best
```

**Hint:** What does `len(count)` count once a key hits 0?

<details><summary>Answer</summary>

**Bug:** Keys with count 0 stay in the dict, so `len(count)` keeps growing — `while` never terminates correctly (well, it loops until left > right, shrinking to empty) and results are wrong. `"eceba", k=2` → returns 1-ish instead of 3.
**Fix:**
```python
count[s[left]] -= 1
if count[s[left]] == 0:
    del count[s[left]]
```
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: `while` written as `if`
```python
# WRONG — may still be invalid after one step
if invalid:
    left += 1

# CORRECT — shrink until valid
while invalid:
    left += 1
```

## Mistake 02: `left` moves backward (stale index)
```python
# WRONG — last['a']=0 but left is already 2 → left=1, backward!
if c in last:
    left = last[c] + 1

# CORRECT — only jump if old occurrence is inside the window
if c in last and last[c] >= left:
    left = last[c] + 1
```

## Mistake 03: Recording at the wrong moment
```python
# LONGEST-valid: record AFTER the while (window guaranteed valid)
while invalid: shrink
best = max(best, right - left + 1)

# SHORTEST-valid: record INSIDE the while (valid only before shrinking)
while valid:
    best = min(best, right - left + 1)
    shrink
```

## Mistake 04: Recomputing window state from scratch
```python
# WRONG — O(n·k), defeats the whole point
for i in range(len(nums) - k + 1):
    total = sum(nums[i:i+k])

# CORRECT — O(1) per slide
window_sum += nums[right] - nums[right - k]
```

## Mistake 05: Initializing `best = 0` for max problems
```python
# WRONG — all-negative input returns 0, which isn't even a window
best = 0

# CORRECT — seed with the first real window
best = window_sum   # or float('-inf')
```

## Mistake 06: Forgetting `del` on zero counts
```python
# WRONG — len(count) counts zombie keys
count[s[left]] -= 1

# CORRECT
count[s[left]] -= 1
if count[s[left]] == 0:
    del count[s[left]]
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual first-window + index soup
### Before
```python
def max_sum_k(nums, k):
    best = sum(nums[:k])
    s = best
    i = 0
    while i + k < len(nums):
        s = s - nums[i] + nums[i + k]
        best = max(best, s)
        i += 1
    return best
```
### Problems
1. `i` and `i + k` is hard to read; a `for right in range(k, n)` names the entering index directly.

### After
```python
def max_sum_k(nums, k):
    window_sum = best = sum(nums[:k])
    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        best = max(best, window_sum)
    return best
```

---

## Refactor 02 (Medium): Counter boilerplate
### Before
```python
count = {}
for c in t:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1
```
### Problems
1. Four lines for what `collections.Counter` or `.get` does in one.

### After
```python
from collections import Counter
need = Counter(t)
# or: need[c] = need.get(c, 0) + 1
```

---

## Refactor 03 (Hard): Copying the answer window every iteration
### Before
```python
while formed == required:
    cur = s[left:right+1]
    if len(cur) < len(best_str):
        best_str = cur          # O(window) copy EVERY iteration
    # ... shrink ...
```
### Problems
1. String slice is O(window length) — copied every shrink step.
2. You only need the *positions*; slice once at the end.

### After
```python
while formed == required:
    if right - left + 1 < best_len:
        best_len, best_left = right - left + 1, left   # just indices
    # ... shrink ...
return s[best_left:best_left + best_len]               # slice once
```

---

## Approach Comparison — different ways to solve it

## Problem: Longest substring without repeating characters

### Approach 1: count dict + `while` shrink
```python
def f(s):
    left, best, count = 0, 0, {}
    for right, c in enumerate(s):
        count[c] = count.get(c, 0) + 1
        while count[c] > 1:
            count[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```
**Pros:** Mirrors the generic template — shrink until valid. Easiest to transfer to other problems. **Cons:** `left` walks step by step when it could jump.

### Approach 2: last-seen index + jump
```python
def f(s):
    last, left, best = {}, 0, 0
    for right, c in enumerate(s):
        if c in last and last[c] >= left:
            left = last[c] + 1
        last[c] = right
        best = max(best, right - left + 1)
    return best
```
**Pros:** `left` teleports — fewer inner iterations. Same O(n) but snappier. **Cons:** the `last[c] >= left` guard is subtle; forgetting it breaks `"abba"`.

### Approach 3: brute force — all substrings
```python
def f(s):
    best = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if len(set(s[i:j+1])) == j - i + 1:
                best = max(best, j - i + 1)
    return best
```
**Pros:** Obvious. **Cons:** O(n³) — n² substrings, each set-scan is O(len). n=1000 → ~10⁹ ops. Interview-red-flag.

**Winner:** Approach 2 for interviews (shows you know the jump trick), Approach 1 when in doubt (the template always works).

---

## Problem: Min-size subarray sum ≥ target

### Approach 1: sliding window (this lesson)
```python
def f(target, nums):
    left, total, best = 0, 0, float("inf")
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]; left += 1
    return 0 if best == float("inf") else best
```
**Time O(n), space O(1). Requires positive numbers** (shrinking must only decrease the sum).

### Approach 2: prefix sums + binary search
```python
# works even with negatives
prefix = [0]
for x in nums: prefix.append(prefix[-1] + x)
# for each i, binary-search smallest j with prefix[j]-prefix[i] >= target
# O(n log n), more code
```
**Pros:** handles negative numbers (window method can't). **Cons:** O(n log n) and far more error-prone.

**Winner:** Approach 1 — the problem guarantees positives, so the window is both faster and simpler. If negatives appear, the window invariant breaks and you must switch to prefix sums.
