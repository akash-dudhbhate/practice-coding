# lesson-03-lists-tuples — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: List Mutation
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```
What prints?
- (A) [1, 2, 3]
- (B) [1, 2, 3, 4]

<details><summary>Answer</summary>
**(B) [1, 2, 3, 4]** — `b = a` doesn't copy the list, it creates another reference to the SAME list. Modifying `b` modifies `a`. Use `b = a.copy()` or `b = a[:]` to copy.
</details>

## Check 02: Tuple Immutability
```python
t = (1, [2, 3])
t[1].append(4)
print(t)
```
What happens?

<details><summary>Answer</summary>
```
(1, [2, 3, 4])
```
Tuples are immutable — you can't change `t[1]` to a different list. But if a tuple contains a mutable object (like a list), you CAN modify that object. The tuple still points to the same list, but the list's contents changed.
</details>

## Check 03: List Comprehension
```python
nums = [1, 2, 3, 4, 5]
result = [n * 2 for n in nums if n > 2]
print(result)
```
What prints?

<details><summary>Answer</summary>
```
[6, 8, 10]
```
Filter first (n > 2: 3, 4, 5), then transform (×2: 6, 8, 10).
</details>

## Check 04: Append vs Extend
```python
a = [1, 2]
a.append([3, 4])
print(a)

b = [1, 2]
b.extend([3, 4])
print(b)
```
What prints (2 lines)?

<details><summary>Answer</summary>
```
[1, 2, [3, 4]]
[1, 2, 3, 4]
```
`append` adds the list as ONE element. `extend` unpacks and adds each element.
</details>

## Check 05: Sort vs Sorted
```python
nums = [3, 1, 4, 1, 5]
result = nums.sort()
print(result)
print(nums)
```
What prints (2 lines)?

<details><summary>Answer</summary>
```
None
[1, 1, 3, 4, 5]
```
`.sort()` sorts IN PLACE and returns `None`. The original list is modified. `sorted(nums)` returns a NEW sorted list and doesn't modify the original.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Sum List — Wrong Start
```python
def sum_list(nums):
    total = 1
    for n in nums:
        total += n
    return total
```
**Hint:** What should total start as?

<details><summary>Answer</summary>
**Bug:** `total = 1` should be `total = 0`. Starting at 1 adds 1 to the real sum. `sum_list([1,2,3])` returns 7, not 6.
</details>

## Debug 02 (Medium): Reverse List — Mutating Input
```python
def reverse_list(items):
    items.reverse()
    return items
```
**Hint:** The spec says "don't mutate the input."

<details><summary>Answer</summary>
**Bug:** `.reverse()` mutates the original list. The caller's list is now reversed too.
**Fix:** `return items[::-1]` or `return list(reversed(items))`.
</details>

## Debug 03 (Hard): Contains — Wrong Return Position
```python
def contains(items, target):
    for item in items:
        if item == target:
            return True
        else:
            return False
```
**Hint:** What happens if the first item doesn't match?

<details><summary>Answer</summary>
**Bug:** The `else: return False` is inside the loop — it returns False on the FIRST non-match, never checking the rest. `contains([1,2,3], 3)` returns False!
**Fix:** Move `return False` OUTSIDE the loop.
```python
def contains(items, target):
    for item in items:
        if item == target:
            return True
    return False  # only after checking ALL items
```
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Mutating input lists
```python
# WRONG — caller's list is modified
def reverse_list(items):
    items.reverse()
    return items

# CORRECT — return a new list
def reverse_list(items):
    return items[::-1]
```

## Mistake 02: Using `==` for list equality with nested lists
```python
# Can be surprising
a = [[1], [2]]
b = [[1], [2]]
print(a == b)  # True — compares values
print(a is b)  # False — different objects
```

## Mistake 03: Modifying list while iterating
```python
# WRONG — skips elements
nums = [1, 2, 3, 4, 5]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)  # modifies list during iteration!

# CORRECT — list comprehension
nums = [n for n in nums if n % 2 != 0]
```

## Mistake 04: Confusing append and extend
```python
# WRONG — nested list
a = [1, 2]
a.append([3, 4])  # [1, 2, [3, 4]]

# CORRECT — flat list
a.extend([3, 4])  # [1, 2, 3, 4]
```

## Mistake 05: Using `list()` vs `[]`
```python
# Both work, but [] is faster and more Pythonic
a = list()  # works but verbose
b = []      # preferred
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Manual Sum
### Before
```python
def total(numbers):
    result = 0
    for n in numbers:
        result = result + n
    return result
```
### After
```python
def total(numbers):
    return sum(numbers)
```

## Refactor 02 (Medium): Manual Filter
### Before
```python
def get_positives(nums):
    result = []
    for n in nums:
        if n > 0:
            result.append(n)
    return result
```
### After
```python
def get_positives(nums):
    return [n for n in nums if n > 0]
```

## Refactor 03 (Hard): Multiple Passes
### Before
```python
def process(items):
    filtered = []
    for x in items:
        if x is not None:
            filtered.append(x)
    transformed = []
    for x in filtered:
        transformed.append(x * 2)
    result = []
    for x in transformed:
        if x > 0:
            result.append(x)
    return result
```
### After
```python
def process(items):
    return [x * 2 for x in items if x is not None and x * 2 > 0]
```

---

## Approach Comparison — different ways to solve it

## Problem: Remove Duplicates

### Approach 1: Loop with set
```python
def remove_duplicates(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```
**Pros:** Preserves order. O(n). **Cons:** More code.

### Approach 2: set() directly
```python
def remove_duplicates(items):
    return list(set(items))
```
**Pros:** One line. **Cons:** Loses order (sets are unordered).

### Approach 3: dict.fromkeys() (Python 3.7+)
```python
def remove_duplicates(items):
    return list(dict.fromkeys(items))
```
**Pros:** One line, preserves order (dicts maintain insertion order). **Cons:** Less obvious.

**Winner:** Approach 1 for learning. Approach 3 for production (order-preserving, one line).

---

## Problem: Reverse a List

### Approach 1: Slicing
```python
def reverse_list(items):
    return items[::-1]
```

### Approach 2: reversed()
```python
def reverse_list(items):
    return list(reversed(items))
```

### Approach 3: In-place (if allowed)
```python
items.reverse()  # mutates original
```

**Winner:** Approach 1 (slicing) — most Pythonic for a new reversed list.
