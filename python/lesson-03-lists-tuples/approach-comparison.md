# Lesson 03 — Approach Comparison

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
