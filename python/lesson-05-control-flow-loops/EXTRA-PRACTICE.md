# lesson-05-control-flow-loops — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: For vs While
```python
# Which loop for: "print 1 to 10"?
# A: for
# B: while
```
<details><summary>Answer</summary>
**A (for)** — When you know the count, use `for`. Use `while` for unknown iterations (e.g., "keep asking until valid input").
</details>

## Check 02: Range
```python
for i in range(3, 10, 2):
    print(i)
```
What prints?

<details><summary>Answer</summary>
```
3
5
7
9
```
`range(start, stop, step)` — 3 to 9 (exclusive 10), step 2.
</details>

## Check 03: Break vs Continue
```python
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)
```
What prints?

<details><summary>Answer</summary>
```
0
1
3
```
`continue` at i=2 skips printing 2. `break` at i=4 exits the loop before printing 4. 3 prints because continue only skips that one iteration.
</details>

## Check 04: Else on Loop
```python
for i in range(5):
    if i == 3:
        break
else:
    print("completed")
```
What prints?

<details><summary>Answer</summary>
Nothing. The `else` on a `for` loop runs only if the loop completes WITHOUT `break`. Since we broke at i=3, the else doesn't run.
</details>

## Check 05: Nested Loop Complexity
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```
How many times does print run (in terms of n)?

<details><summary>Answer</summary>
**n² times.** Nested loops over the same range are O(n²). For n=100, that's 10,000 iterations. Be careful with nested loops on large data.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Classify Number — Missing Zero Case
```python
def classify_number(n):
    if n > 0:
        return "positive"
    else:
        return "negative"
```
**Hint:** What about n = 0?

<details><summary>Answer</summary>
**Bug:** 0 is classified as "negative" but should be "zero". Missing the `elif n == 0` case.
**Fix:** Add `elif n == 0: return "zero"` before the else.
</details>

## Debug 02 (Medium): First Even — Break in Wrong Place
```python
def first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
        break
    return None
```
**Hint:** The break runs on the FIRST iteration if the number is odd.

<details><summary>Answer</summary>
**Bug:** `break` is after the `if` but not inside it — it runs on every iteration where the number is NOT even. So the loop only checks the first element.
**Fix:** Remove `break` entirely — `return n` exits the loop. The `return None` after the loop handles the "not found" case.
</details>

## Debug 03 (Hard): Find Pair — Wrong Loop Range
```python
def find_pair(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None
```
**Hint:** This can return (0, 0) if nums[0] * 2 == target. Also checks pairs twice.

<details><summary>Answer</summary>
**Bug 1:** `j` starts at 0, so it checks (i, i) — pairing an element with itself. `find_pair([5], 10)` returns (0, 0) but shouldn't.
**Bug 2:** Checks (i, j) and (j, i) — redundant.
**Fix:** `for j in range(i + 1, len(nums)):`
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Using while when for is better
```python
# WRONG — manual counter
i = 0
while i < 10:
    print(i)
    i += 1

# CORRECT
for i in range(10):
    print(i)
```

## Mistake 02: Off-by-one in range
```python
# WRONG — misses the last element
for i in range(1, len(items)):  # skips index 0
# CORRECT
for i in range(len(items)):
```

## Mistake 03: Forgetting break/else pattern
```python
# VERBOSE
found = False
for item in items:
    if item == target:
        found = True
        break
if not found:
    print("not found")

# PYTHONIC — for/else
for item in items:
    if item == target:
        print("found")
        break
else:
    print("not found")
```

## Mistake 04: Modifying list during iteration
```python
# WRONG — skips elements after removal
for item in items:
    if item < 0:
        items.remove(item)

# CORRECT — list comprehension
items = [item for item in items if item >= 0]
```

## Mistake 05: Infinite while loop
```python
# WRONG — no exit condition update
while True:
    user_input = input("Enter q to quit: ")
    if user_input == "q":
        break
    # if user never types q, infinite loop!
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Find with Flag
### Before
```python
def find_even(nums):
    found = False
    result = None
    for n in nums:
        if n % 2 == 0:
            found = True
            result = n
            break
    if found:
        return result
    return None
```
### After
```python
def find_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None
```

## Refactor 02 (Medium): Nested If to Early Return
### Before
```python
def classify(n):
    if n > 0:
        if n > 100:
            return "large positive"
        else:
            return "small positive"
    else:
        if n < 0:
            return "negative"
        else:
            return "zero"
```
### After
```python
def classify(n):
    if n > 100: return "large positive"
    if n > 0: return "small positive"
    if n < 0: return "negative"
    return "zero"
```

## Refactor 03 (Hard): Loop with Index
### Before
```python
def print_pairs(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            print(lst[i], lst[j])
```
### After
```python
from itertools import combinations
def print_pairs(lst):
    for a, b in combinations(lst, 2):
        print(a, b)
```

---

## Approach Comparison — different ways to solve it

## Problem: Find First Even Number

### Approach 1: For loop with break
```python
def first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n
    return None
```
**Pros:** Clear, O(n), early exit. **Cons:** None.

### Approach 2: Filter + next
```python
def first_even(nums):
    return next((n for n in nums if n % 2 == 0), None)
```
**Pros:** One line, Pythonic. **Cons:** Less readable for beginners.

### Approach 3: List comprehension + index
```python
def first_even(nums):
    evens = [n for n in nums if n % 2 == 0]
    return evens[0] if evens else None
```
**Bug!** This checks ALL elements even after finding the first even. O(n) always, not early-exit.

**Winner:** Approach 1 for clarity. Approach 2 for Pythonic one-liner.

---

## Problem: Check if Palindrome (two-pointer)

### Approach 1: Two pointers
```python
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```
**Pros:** O(n) time, O(1) space, early exit. **Cons:** More code.

### Approach 2: Slicing
```python
def is_palindrome(s):
    return s == s[::-1]
```
**Pros:** One line. **Cons:** O(n) space (creates reversed copy), no early exit.

**Winner:** Approach 2 for simplicity. Approach 1 for interviews (shows algorithm thinking).
