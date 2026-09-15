# Lesson 05 — Approach Comparison

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
