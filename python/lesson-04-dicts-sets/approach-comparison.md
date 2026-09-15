# Lesson 04 — Approach Comparison

## Problem: Word Count

### Approach 1: Manual loop with .get()
```python
def word_count(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts
```

### Approach 2: defaultdict
```python
from collections import defaultdict
def word_count(text):
    counts = defaultdict(int)
    for word in text.lower().split():
        counts[word] += 1
    return dict(counts)
```

### Approach 3: Counter
```python
from collections import Counter
def word_count(text):
    return dict(Counter(text.lower().split()))
```

**Winner:** Approach 3 (Counter) — built for exactly this. One line, tested, fast.

---

## Problem: Unique Items (order-preserving)

### Approach 1: Set + loop
```python
def unique_items(items):
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

### Approach 2: dict.fromkeys()
```python
def unique_items(items):
    return list(dict.fromkeys(items))
```

**Winner:** Approach 2 — one line, preserves order, O(n).
