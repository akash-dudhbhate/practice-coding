# lesson-09-binary-search — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: How many probes?
```python
nums = list(range(1_000_000))   # sorted, one million elements
```
In the worst case, how many loop iterations does binary search take?
What about 8 elements?

<details><summary>Answer</summary>
~20 for a million (2²⁰ ≈ 1.05M), exactly 3 for 8 elements (8→4→2→1).
Each iteration halves the range, so iterations = ceil(log2(n)) + maybe 1.
This is why O(log n) is "free" in practice.
</details>

---

## Check 02: Which half dies?
```python
nums = [1, 4, 6, 9, 13, 17]
target = 5
```
`mid` lands on index 2 (value 6). Which elements are now provably dead?

<details><summary>Answer</summary>
**Index 2 and everything right of it.** `nums[2] = 6 > 5`, and the array is
sorted — everything at index ≥ 2 is ≥ 6 > 5. `hi = 1`; only `[1, 4]` survives.
</details>

---

## Check 03: Lower bound on absent target
```python
def lower_bound(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target: lo = mid + 1
        else: hi = mid
    return lo

print(lower_bound([1, 3, 5, 6], 4))
```
What prints? The target 4 isn't in the array.

<details><summary>Answer</summary>
`2` — the first index where `nums[i] >= 4` is index 2 (value 5). Lower bound
doesn't need the target to exist; it answers "where would it go?" That's why
it's also the insert-position function.
</details>

---

## Check 04: Is this predicate monotone?
```python
# Ship capacity problem. weights=[1..10], days=5.
# feasible(C) = "can all packages ship within 5 days at capacity C?"
```
`feasible(10)` is False, `feasible(15)` is True, `feasible(55)` is True.
Is `feasible` monotone, and can binary search use it?

<details><summary>Answer</summary>
**Yes — feasible(C) is False for small C and True for all large C.** More
capacity can never increase the day count, so once it's true it stays true:
false...false true...true. Monotone predicates are exactly what binary
search needs — search the boundary at C=15.
</details>

---

## Check 05: Rotated array — which half is sorted?
```python
nums = [4, 5, 6, 7, 0, 1, 2]
lo, hi = 0, 6
mid = 3     # nums[3] = 7
```
Which half is guaranteed sorted, and how do you know?

<details><summary>Answer</summary>
**Left half `[4,5,6,7]`.** `nums[lo] = 4 <= nums[mid] = 7` — a sorted run
from lo to mid. The rotation scar must be in the right half `[0,1,2]`...
which is itself sorted too (that's fine — the check just needs ONE reliable
side to do the range test).
</details>

---

## Check 06: Peak search — why does it terminate?
```python
nums = [1, 2, 1, 3, 5, 6, 4]
lo, hi = 0, 6
mid = 3    # nums[3] = 3, nums[4] = 5
```
`nums[mid] < nums[mid+1]`, so `lo = mid + 1 = 4`. Why is a peak guaranteed
to exist in `nums[4..6]`?

<details><summary>Answer</summary>
We're on an uphill step: `nums[4] = 5 > 3`. Keep walking right — either the
climb continues until index 6 (where -inf after the array forces a peak at
index 6) or it dips earlier (the dip's left neighbor is a peak). A strictly
rising slope can only end at the array edge or a peak.
</details>

---

## Debug Exercises — find and fix the bug

---

## Debug 01 (Easy): The classic infinite loop

```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid          # ???
        else:
            hi = mid          # ???
    return -1
```

**Hint:** try `binary_search([1, 3], 3)` — it hangs.

<details><summary>Answer</summary>

**Bug:** `lo = mid` doesn't shrink the range. When `lo=0, hi=1`, `mid=0`,
`nums[0]=1 < 3` → `lo = 0` again. Infinite loop.
**Fix:** this template needs `lo <= hi` plus mid-excluding updates:
```python
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target: return mid
    if nums[mid] < target: lo = mid + 1
    else: hi = mid - 1
```
(Or keep `lo < hi` + `hi = mid` only if you switch to the lower-bound
variant where mid itself stays a candidate.)
</details>

---

## Debug 02 (Easy): First occurrence returns the LAST match

```python
def first_occurrence(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

**Hint:** `first_occurrence([1,2,2,2,3], 2)` returns 2, not 1.

<details><summary>Answer</summary>

**Bug:** it returns on the FIRST mid hit — classic binary search finds *a*
match, not *the first* match.
**Fix:** record the hit as a candidate and keep searching left:
```python
answer = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
        answer = mid
        hi = mid - 1      # maybe an earlier occurrence exists
    elif nums[mid] < target: lo = mid + 1
    else: hi = mid - 1
return answer
```
</details>

---

## Debug 03 (Medium): Ship capacity — wrong bounds

```python
def min_ship_capacity(weights, days):
    lo, hi = 1, sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid): hi = mid
        else: lo = mid + 1
    return lo
```

**Hint:** `min_ship_capacity([8, 9], 2)` — the answer should be 9, but what
happens at `cap = 4`?

<details><summary>Answer</summary>

**Bug:** `lo = 1` is below `max(weights)`. A capacity under the heaviest
package can NEVER work — `feasible` either crashes (load > cap forever,
infinite day count if written wrong) or returns False forever, so binary
search converges to `max(weights)` anyway but wastes iterations AND hides
the real constraint.
**Fix:** `lo = max(weights)` — the heaviest package sets the floor.
</details>

---

## Debug 04 (Medium): Koko — predicate flipped

```python
lo, hi = 1, max(piles)
while lo < hi:
    mid = (lo + hi) // 2
    if hours_needed(mid) <= h:
        lo = mid + 1
    else:
        hi = mid
return lo
```

**Hint:** `min_eating_speed([3,6,7,11], 8)` should be 4 — this returns 11.

<details><summary>Answer</summary>

**Bug:** the branches are swapped. If speed `mid` finishes in time, `mid` is
a CANDIDATE — you want to try SLOWER, i.e. `hi = mid`. Moving `lo` up
discards the valid answer region.
**Fix:**
```python
if hours_needed(mid) <= h: hi = mid      # works — try slower
else: lo = mid + 1                        # too slow — need faster
```
</details>

---

## Debug 05 (Hard): Rotated min overshoots

```python
def find_min_rotated(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid - 1
    return nums[lo]
```

**Hint:** `find_min_rotated([2, 1])` — should be 1. What does this return?

<details><summary>Answer</summary>

**Bug:** `hi = mid - 1` discards `mid`, but when `nums[mid] <= nums[hi]`,
mid itself may BE the minimum. On `[2,1]`: mid=0, `nums[0]=2 > nums[1]=1` →
lo=1, returns 1 — lucky. But on `[1,2]`: mid=0, `nums[0]=1 <= nums[1]=2` →
`hi = -1`, lo=0... loop ends `lo < hi` false? Actually lo=0, hi=-1 → loop
exits, returns nums[0]=1 — also lucky. Try `[3,1,2]`: mid=1, `nums[1]=1 <= 2`
→ hi=0. lo=0,hi=0 → returns nums[0]=3. WRONG — min is 1, and `hi = mid - 1`
skipped it.
**Fix:** `hi = mid` — keep mid as a candidate, it's the minimum-or-leftmost
boundary.
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: `lo = mid` / `hi = mid` in the classic template
```python
# WRONG — mid never gets excluded, hangs on two-element ranges
if nums[mid] < target: lo = mid

# CORRECT — inclusive template excludes mid
if nums[mid] < target: lo = mid + 1
else: hi = mid - 1
```

## Mistake 02: Mixing the two loop contracts
```python
# WRONG — lo<hi contract + hi=mid-1 skips the last candidate;
#         or lo<=hi contract + hi=mid hangs
while lo < hi:
    ...
    hi = mid - 1

# CORRECT pairs:
# lo <= hi  <->  lo = mid+1 / hi = mid-1      (exact match)
# lo < hi   <->  lo = mid+1 / hi = mid        (boundary search)
```

## Mistake 03: Integer overflow worry / wrong mid formula
```python
# In Python (lo + hi) // 2 can't overflow — but get in the habit:
mid = lo + (hi - lo) // 2     # same value, safe in C++/Java too
```

## Mistake 04: Lower bound returning out-of-range value
```python
# WRONG — lower bound can be len(nums); indexing crashes
i = lower_bound(nums, target)
if nums[i] == target: ...       # IndexError when i == len(nums)

# CORRECT
if i < len(nums) and nums[i] == target: ...
```

## Mistake 05: Non-monotone "search the answer"
```python
# WRONG — feasible(C) that can flip back to False as C grows
# means binary search narrows the wrong half. Verify:
#   feasible(x) == True  =>  feasible(x+1) == True   (or the exact mirror)
# before reaching for the template.
```

## Mistake 06: Rotated-array search comparing only to target
```python
# WRONG — in a rotated array, nums[mid] < target does NOT mean "go right"
if nums[mid] < target: lo = mid + 1   # [4,5,6,7,0,1,2], target=0, mid=3

# CORRECT — first find the sorted half, then range-check target inside it
```

## Mistake 07: ceil division via floats
```python
# WRONG — float precision on huge piles
hours += math.ceil(p / k)

# CORRECT — pure integer arithmetic
hours += (p + k - 1) // k
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Recursive binary search → iterative
### Before
```python
def binary_search(nums, target, lo=None, hi=None):
    if lo is None: lo, hi = 0, len(nums) - 1
    if lo > hi: return -1
    mid = (lo + hi) // 2
    if nums[mid] == target: return mid
    if nums[mid] < target: return binary_search(nums, target, mid + 1, hi)
    return binary_search(nums, target, lo, mid - 1)
```
### Problems
1. O(log n) stack frames for zero benefit — iteration is free
2. Extra parameters pollute the public signature
3. Recursion limit risk on adversarial inputs

### After
```python
def binary_search(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        if nums[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
```

---

## Refactor 02 (Medium): Linear scan for the answer → binary search
### Before
```python
def min_eating_speed(piles, h):
    k = 1
    while True:
        if sum((p + k - 1) // k for p in piles) <= h:
            return k
        k += 1
```
### Problems
1. O(max_pile · n) — for piles around 10⁹ that's a billion checks
2. It "works" on small tests then times out exactly when it matters

### After
```python
def min_eating_speed(piles, h):
    def hours(k):
        return sum((p + k - 1) // k for p in piles)
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours(mid) <= h: hi = mid
        else: lo = mid + 1
    return lo
```
O(n log max_pile) — ~30 simulations instead of up to 10⁹.

---

## Refactor 03 (Hard): Rotated search — find pivot then search
### Before
```python
def search_rotated(nums, target):
    # pass 1: binary search for the minimum (rotation point)
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]: lo = mid + 1
        else: hi = mid
    pivot = lo
    # pass 2: plain binary search on the correct side
    if nums[pivot] <= target <= nums[-1] if nums else False:
        lo, hi = pivot, len(nums) - 1
    else:
        lo, hi = 0, pivot - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        if nums[mid] < target: lo = mid + 1
        else: hi = mid - 1
    return -1
```
### Problems
1. Two binary searches = 2× the code, 2× the edge cases, same O(log n)
2. The branch picking which side to search is itself error-prone
   (empty array, target at pivot, pivot == 0...)

### After
```python
def search_rotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target: return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]: hi = mid - 1
            else: lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]: lo = mid + 1
            else: hi = mid - 1
    return -1
```
One pass: at each step the sorted half gives you a reliable range check.

---

## Approach Comparison — different ways to solve it

## Problem: Find target in a sorted array

### Approach 1: Linear scan
```python
for i, x in enumerate(nums):
    if x == target: return i
```
**Pros:** works on any input. **Cons:** O(n) — wasteful on sorted data.

### Approach 2: `bisect` module
```python
from bisect import bisect_left
i = bisect_left(nums, target)
return i if i < len(nums) and nums[i] == target else -1
```
**Pros:** stdlib, battle-tested. **Cons:** hides the skill; interviewers
usually want the manual loop.

### Approach 3: Hand-rolled binary search
The canonical template. **Winner** for interviews — and bisect is the
winner in production code. Know both.

---

## Problem: Minimum feasible value (ship capacity / koko)

### Approach 1: Increment and test
Try x = lo, lo+1, lo+2... until feasible. **Cons:** O(range·n) — dies on
large ranges.

### Approach 2: Binary search the answer
O(n log range). **Winner** — the pattern this lesson exists for. The only
precondition is a monotone feasibility check.

---

## Problem: Search a rotated sorted array

### Approach 1: Linear scan
O(n), ignores all structure.

### Approach 2: Find pivot + binary search correct half
O(log n) but two passes, more code, more edge cases.

### Approach 3: One-pass sorted-half elimination
O(log n), one loop. **Winner** once you can hold the invariant:
"one half is always sorted; range-check the target inside it."
