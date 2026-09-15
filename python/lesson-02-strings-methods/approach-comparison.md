# Lesson 02 — Approach Comparison

## Problem: Count Vowels

### Approach 1: Loop with counter
```python
def count_vowels(text):
    count = 0
    for c in text.lower():
        if c in "aeiou":
            count += 1
    return count
```
**Pros:** Clear, beginner-friendly. **Cons:** Verbose.

### Approach 2: Sum with generator
```python
def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")
```
**Pros:** One line, Pythonic. **Cons:** Less readable for beginners.

### Approach 3: Set intersection
```python
def count_vowels(text):
    return len(set(text.lower()) & set("aeiou"))
```
**Bug!** This counts UNIQUE vowels, not total. "aaee" → 2, not 4. Wrong approach.

**Winner:** Approach 2 for production, Approach 1 for learning.

---

## Problem: Reverse a String

### Approach 1: Loop
```python
def reverse_string(s):
    result = ""
    for c in s:
        result = c + result
    return result
```
**Pros:** Teaches string building. **Cons:** O(n²) — each `c + result` creates a new string.

### Approach 2: Slicing
```python
def reverse_string(s):
    return s[::-1]
```
**Pros:** One line, O(n), Pythonic. **Cons:** "Magic" — beginners don't understand `[::-1]`.

### Approach 3: reversed()
```python
def reverse_string(s):
    return "".join(reversed(s))
```
**Pros:** Explicit. **Cons:** Longer than slicing.

**Winner:** Approach 2 (slicing) — the standard Python way.

---

## Problem: Check Palindrome

### Approach 1: Slicing
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
```
**Pros:** One line, O(n). **Cons:** Creates a reversed copy.

### Approach 2: Two pointers
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```
**Pros:** O(1) space, early exit. **Cons:** More code.

**Winner:** Approach 1 for simplicity. Approach 2 for interviews (shows algorithm knowledge).
