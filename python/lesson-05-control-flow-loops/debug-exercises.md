# Lesson 05 — Debug Exercises

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
