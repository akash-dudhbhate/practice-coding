# Lesson 03 — Debug Exercises

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
