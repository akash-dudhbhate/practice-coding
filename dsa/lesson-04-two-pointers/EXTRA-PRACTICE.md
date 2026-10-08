# lesson-04-two-pointers — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

> Don't run the code. Answer mentally first.

---

## Check 01: Which pointer moves?
```python
nums = [1, 2, 4, 7, 11]   # sorted
target = 5
L, R = 0, 4
```
`nums[L] + nums[R] = 1 + 11 = 12`. Which pointer moves, and why?

<details><summary>Answer</summary>
**R moves left (R -= 1).** 12 > target, so 11 — the largest remaining element —
is too big to pair with anything left. Discard it.
</details>

---

## Check 02: Loop bound
```python
arr = [1, 2, 3]
L, R = 0, 2
while L < R:
    arr[L], arr[R] = arr[R], arr[L]
    L += 1
    R -= 1
print(arr)
```
What prints? What if the condition were `L <= R`?

<details><summary>Answer</summary>
`[3, 2, 1]` — pointers stop when they cross. With `L <= R` the middle element
gets swapped with itself (harmless for reverse, but the wrong habit — and with
pair-sum it would let one element pair with itself).
</details>

---

## Check 03: Same-direction pointers
```python
nums = [0, 0, 1, 1, 2]
slow = 1
for fast in range(1, 5):
    if nums[fast] != nums[slow - 1]:
        nums[slow] = nums[fast]
        slow += 1
print(slow, nums[:slow])
```
What prints?

<details><summary>Answer</summary>
```
3 [0, 1, 2]
```
fast=1: 0==nums[0] skip. fast=2: 1!=0 write@1 → slow=2. fast=3: 1==nums[1] skip.
fast=4: 2!=nums[1]=1 write@2 → slow=3.
</details>

---

## Check 04: Unsorted input trap
```python
def pair_sum_sorted(nums, target):
    L, R = 0, len(nums) - 1
    while L < R:
        s = nums[L] + nums[R]
        if s == target: return [L, R]
        if s < target: L += 1
        else: R -= 1
    return []

print(pair_sum_sorted([3, 0, 5, 1], 4))
```
A pair summing to 4 exists (3+1). What prints?

<details><summary>Answer</summary>
`[]` — **silently wrong**. The input isn't sorted: `3+1=4` is missed because the
move rules only work on sorted data. Two pointers REQUIRE sorted input for
pair-sum; on unsorted data use a hash set.
</details>

---

## Check 05: Container — which side moves?
```python
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
```
L=0 (h=1), R=8 (h=7), area = min(1,7)·8 = 8. Which pointer moves?

<details><summary>Answer</summary>
**L moves right.** The shorter side (h=1) caps the height; keeping it and moving
R inward only shrinks width with no hope of more height. Moving L is the only
move that could possibly improve the area.
</details>

---

## Check 06: Back-merge order
```python
nums1 = [1, 2, 3, 0, 0, 0]   # m=3
nums2 = [2, 5, 6]            # n=3
```
Merging FORWARD (writing at index 0) — what's wrong with that?

<details><summary>Answer</summary>
Writing at index 0 would overwrite `nums1[0]=1` before it's been read — you'd
lose data unless you shifted everything (O(n) per step) or copied nums1 (O(m)
space). Writing from the back into the zero-buffer touches only unused space.
</details>

---

## Debug Exercises — find and fix the bug

---

## Debug 01 (Easy): Reverse — wrong loop bound

```python
def reverse_in_place(arr):
    L, R = 0, len(arr)
    while L < R:
        arr[L], arr[R] = arr[R], arr[L]
        L += 1
        R -= 1
    return arr
```

**Hint:** What's the valid range of indices?

<details><summary>Answer</summary>

**Bug:** `R = len(arr)` is out of bounds — `arr[len(arr)]` → IndexError.
**Fix:** `R = len(arr) - 1`.
</details>

---

## Debug 02 (Easy): Pair-sum — moves both pointers

```python
def pair_sum_sorted(nums, target):
    L, R = 0, len(nums) - 1
    while L < R:
        s = nums[L] + nums[R]
        if s == target:
            return [L, R]
        L += 1
        R -= 1
    return []
```

**Hint:** On `[1, 2, 4, 7, 11]` target 9 — the answer [1,3] (2+7) is skipped.

<details><summary>Answer</summary>

**Bug:** moving both pointers unconditionally skips halves of the search space —
it only ever tries symmetric pairs. (1,11)→(2,7): 2+7=9 actually hits here, but
[2,4,7] target 9 misses (4,5-ish pairs). The pattern relies on moving ONLY the
pointer that can't work.
**Fix:**
```python
if s < target: L += 1
else: R -= 1
```
</details>

---

## Debug 03 (Medium): Remove duplicates — compares wrong slots

```python
def remove_duplicates(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

**Hint:** `[1,1,2]` → returns 3 with prefix `[2,1,2]`?? Trace it.

<details><summary>Answer</summary>

**Bug:** two issues. (1) `slow` starts at 0 and the first element is never
"kept" — it gets overwritten by the first new value. (2) Comparing
`nums[fast]` to `nums[fast-1]` is fine for detecting new values, but writes
land starting at index 0, clobbering the original first element.
**Fix:** start `slow = 1` (element 0 is always kept) and compare against
`nums[slow - 1]` or `nums[fast - 1]`:
```python
slow = 1
for fast in range(1, len(nums)):
    if nums[fast] != nums[slow - 1]:
        nums[slow] = nums[fast]
        slow += 1
return slow
```
</details>

---

## Debug 04 (Medium): 3-sum — duplicate triplets

```python
def three_sum(nums):
    nums = sorted(nums)
    res = []
    for i in range(len(nums) - 2):
        L, R = i + 1, len(nums) - 1
        while L < R:
            s = nums[i] + nums[L] + nums[R]
            if s == 0:
                res.append([nums[i], nums[L], nums[R]])
                L += 1
                R -= 1
            elif s < 0:
                L += 1
            else:
                R -= 1
    return res
```

**Hint:** `three_sum([0,0,0,0])` returns `[[0,0,0],[0,0,0]]`.

<details><summary>Answer</summary>

**Bug:** no dedup — repeated i values and repeated pair values each produce the
same triplet again.
**Fix:** `if i > 0 and nums[i] == nums[i-1]: continue` and after a hit, advance
L/R past equal neighbors.
</details>

---

## Debug 05 (Hard): Rain water — wrong side processed

```python
def trap(height):
    L, R = 0, len(height) - 1
    left_max = right_max = water = 0
    while L < R:
        left_max = max(left_max, height[L])
        right_max = max(right_max, height[R])
        if left_max < right_max:          # process LEFT
            water += left_max - height[L]
            L += 1
        else:                             # process RIGHT
            water += right_max - height[R]
            R -= 1
    return water
```

**Hint:** This one is actually correct — but explain WHY processing the smaller
side is safe.

<details><summary>Answer</summary>

**Not a bug — but understand the invariant:** if `left_max < right_max`, then for
position L the true `min(max_left, max_right)` is `left_max` (the real right max
can only be ≥ current right_max). So `left_max - height[L]` is final. Moving the
larger side would use a bound that isn't confirmed yet.
Common actual bug: processing the LARGER side — the bound there isn't
guaranteed, so you'd over-count water.
</details>

---

## Common Mistakes — the traps learners hit

---

## Mistake 01: Using `<=` in the pair loop
```python
# WRONG — element pairs with itself
while L <= R:

# CORRECT
while L < R:
```

## Mistake 02: Moving the wrong pointer on sorted pair-sum
```python
# WRONG — sum already too small, shrinking R makes it smaller
if s < target: R -= 1

# CORRECT
if s < target: L += 1   # need a bigger left value
else: R -= 1
```

## Mistake 03: Forgetting in-place means mutate
```python
# WRONG — caller's list unchanged, O(n) space used
def remove_duplicates(nums):
    return len(list(dict.fromkeys(nums)))

# CORRECT — write back into nums[:k], return k
```

## Mistake 04: Reading past the new length
```python
# WRONG — tail values are stale garbage
k = remove_duplicates(nums)
print(nums)          # [0,1,2,3,4,1,2,3,3,4] ???

# CORRECT — only nums[:k] is valid
print(nums[:k])
```

## Mistake 05: Two pointers on unsorted data
```python
# WRONG — silent wrong answers; move rules assume sorted
pair_sum_sorted([3, 0, 5, 1], 4)

# CORRECT — sort first, or use hashing when order/indices matter
nums.sort()
```

## Mistake 06: Forgetting to skip duplicates in k-sum
```python
# WRONG — [0,0,0,0] produces duplicate triplets
res.append([nums[i], nums[L], nums[R]])

# CORRECT — advance past equal neighbors after each hit + skip dup i's
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Palindrome via cleaned copy
### Before
```python
def is_palindrome(s):
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]
```
### Problems
1. Two extra O(n) allocations (list + reversed copy)
2. Works, but an interviewer will ask for O(1) space

### After
```python
def is_palindrome(s):
    L, R = 0, len(s) - 1
    while L < R:
        while L < R and not s[L].isalnum(): L += 1
        while L < R and not s[R].isalnum(): R -= 1
        if s[L].lower() != s[R].lower(): return False
        L += 1; R -= 1
    return True
```
(The cleaned-copy version is fine for production readability — know both.)

---

## Refactor 02 (Medium): 3-sum brute force
### Before
```python
def three_sum(nums):
    res = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return sorted(map(list, res))
```
### Problems
1. O(n³) time plus a sort of every candidate — dies on n ≳ 300

### After
```python
def three_sum(nums):
    nums = sorted(nums)
    res = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        L, R = i + 1, len(nums) - 1
        while L < R:
            s = nums[i] + nums[L] + nums[R]
            if s == 0:
                res.append([nums[i], nums[L], nums[R]])
                L += 1; R -= 1
                while L < R and nums[L] == nums[L - 1]: L += 1
                while L < R and nums[R] == nums[R + 1]: R -= 1
            elif s < 0: L += 1
            else: R -= 1
    return res
```
O(n²) — fixed element + sorted pair-sum.

---

## Refactor 03 (Hard): Rain water with prefix arrays
### Before
```python
def trap(height):
    n = len(height)
    max_left = [0] * n
    max_right = [0] * n
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], height[i - 1])
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], height[i + 1])
    return sum(max(0, min(max_left[i], max_right[i]) - height[i])
               for i in range(n))
```
### Problems
1. Correct, but O(n) extra space for the two arrays
2. Three passes

### After
```python
def trap(height):
    if not height: return 0
    L, R = 0, len(height) - 1
    left_max, right_max, water = height[L], height[R], 0
    while L < R:
        if left_max < right_max:
            L += 1
            left_max = max(left_max, height[L])
            water += left_max - height[L]
        else:
            R -= 1
            right_max = max(right_max, height[R])
            water += right_max - height[R]
    return water
```
One pass, O(1) space — the prefix arrays' information is carried in two
variables because each side only ever needs its running max.

---

## Approach Comparison — different ways to solve it

## Problem: Pair Sum

### Approach 1: Hash set (unsorted input)
```python
seen = {}
for i, x in enumerate(nums):
    if target - x in seen: return [seen[target - x], i]
    seen[x] = i
```
**Pros:** O(n), works unsorted, keeps indices. **Cons:** O(n) space.

### Approach 2: Two pointers (sorted input)
```python
L, R = 0, len(nums) - 1
while L < R:
    s = nums[L] + nums[R]
    if s == target: return [L, R]
    if s < target: L += 1
    else: R -= 1
```
**Pros:** O(1) space. **Cons:** needs sorted input; indices refer to the sorted
order unless you carry (value, index) pairs.

**Winner:** hashing for unsorted/indices-needed; two pointers when input is
already sorted or O(1) space is required.

---

## Problem: Remove Duplicates

### Approach 1: New list
```python
return len(set(nums))   # loses order/in-place contract
```
**Cons:** wrong contract — must be in place; `set` also loses order.

### Approach 2: Write pointer
```python
slow = 1
for fast in range(1, len(nums)):
    if nums[fast] != nums[slow - 1]:
        nums[slow] = nums[fast]; slow += 1
return slow
```
**Pros:** O(n) time, O(1) space, in place, preserves order. 

**Winner:** Approach 2 — it's the canonical answer and the whole point of the
problem.

---

## Problem: Trapping Rain Water

### Approach 1: Prefix arrays
Two O(n) arrays for left/right maxima, one more pass to sum. O(n) space.

### Approach 2: Two pointers
Carry the two running maxima; process the smaller side. O(1) space.

**Winner:** Approach 2 for interviews; Approach 1 is easier to reason about —
learn it first, then compress the arrays into two variables.
