# Lesson 03 — Common Mistakes

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
