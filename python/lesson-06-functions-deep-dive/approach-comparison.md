# Lesson 06 — Approach Comparison

## Problem: Flexible Sum Function

### Approach 1: Fixed params
```python
def sum_two(a, b): return a + b
def sum_three(a, b, c): return a + b + c
```
**Cons:** Need a new function for each count. Not scalable.

### Approach 2: *args
```python
def sum_all(*nums):
    return sum(nums)
```
**Pros:** Works for any number of args. **Cons:** None — this is the right way.

### Approach 3: List param
```python
def sum_list(nums):
    return sum(nums)
sum_list([1, 2, 3])
```
**Pros:** Clear. **Cons:** Caller must create a list. Less natural than `sum_all(1, 2, 3)`.

**Winner:** Approach 2 (*args) — most flexible, most Pythonic.

---

## Problem: HTML Tag Builder

### Approach 1: String concatenation
```python
def make_tag(tag, text, **attrs):
    attr_str = ""
    for k, v in attrs.items():
        attr_str += f' {k}="{v}"'
    return f"<{tag}{attr_str}>{text}</{tag}>"
```

### Approach 2: Join
```python
def make_tag(tag, text, **attrs):
    attr_str = "".join(f' {k}="{v}"' for k, v in attrs.items())
    return f"<{tag}{attr_str}>{text}</{tag}>"
```

**Winner:** Approach 2 — join is more efficient than += for strings.
