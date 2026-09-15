# Lesson 04 — Refactoring Challenges

## Refactor 01 (Easy): Manual Key Check
### Before
```python
def add_to_dict(d, key, value):
    if key in d:
        d[key] = d[key] + value
    else:
        d[key] = value
```
### After
```python
def add_to_dict(d, key, value):
    d[key] = d.get(key, 0) + value
```

## Refactor 02 (Medium): Manual Counting
### Before
```python
def count_words(text):
    counts = {}
    for word in text.split():
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    return counts
```
### After
```python
from collections import Counter
def count_words(text):
    return dict(Counter(text.split()))
```

## Refactor 03 (Hard): Nested Dict Access
### Before
```python
def get_value(data):
    if data is not None:
        if "user" in data:
            if "name" in data["user"]:
                return data["user"]["name"]
    return None
```
### After
```python
def get_value(data):
    return data.get("user", {}).get("name")
```
