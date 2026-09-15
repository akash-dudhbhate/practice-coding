# Lesson 02 — Refactoring Challenges

## Refactor 01 (Easy): Manual Loop
### Before
```python
def count_vowels(text):
    count = 0
    for c in text:
        if c in "aeiouAEIOU":
            count = count + 1
    return count
```
### Problems
1. `count = count + 1` → use `count += 1`
2. Manual loop when `sum()` works

### After
```python
def count_vowels(text):
    return sum(1 for c in text.lower() if c in "aeiou")
```

---

## Refactor 02 (Medium): String Concatenation in Loop
### Before
```python
def join_words(words):
    result = ""
    for word in words:
        result = result + word + " "
    return result
```
### Problems
1. `+=` on strings in loop is O(n²) — creates new string each time
2. Trailing space at end

### After
```python
def join_words(words):
    return " ".join(words)
```

---

## Refactor 03 (Hard): Repeated Method Calls
### Before
```python
def clean_text(text):
    text = text.strip()
    text = text.lower()
    text = text.replace("  ", " ")
    text = text.replace("  ", " ")
    return text
```
### Problems
1. Repeated `text =` assignment
2. `replace("  ", " ")` called twice for multiple spaces — fragile

### After
```python
import re
def clean_text(text):
    return re.sub(r"\s+", " ", text.strip().lower())
```
