# Lesson 06 — Debug Exercises

## Debug 01 (Easy): Default Argument Order
```python
def greet(greeting="Hello", name):
    return f"{greeting}, {name}!"
```
**Hint:** Can you have a defaulted arg before a non-defaulted one?

<details><summary>Answer</summary>
**Bug:** Python requires non-defaulted args BEFORE defaulted args. `greet("Hi")` is ambiguous — is "Hi" the greeting or the name?
**Fix:** `def greet(name, greeting="Hello"):`
</details>

## Debug 02 (Medium): Mutable Default
```python
def safe_append(item, lst=[]):
    lst.append(item)
    return lst
```
**Hint:** Call it twice.

<details><summary>Answer</summary>
**Bug:** Default list is shared across calls. `safe_append(1)` → [1], `safe_append(2)` → [1, 2].
**Fix:** `def safe_append(item, lst=None): if lst is None: lst = []`.
</details>

## Debug 03 (Hard): Closure Capturing Loop Variable
```python
def make_multipliers():
    return [lambda x: x * i for i in range(3)]
for f in make_multipliers():
    print(f(10))
```
**Hint:** All three print the same value. Why?

<details><summary>Answer</summary>
**Bug:** Lambdas capture `i` by REFERENCE, not value. By the time they're called, `i = 2` (last value). All print 20.
**Fix:** `lambda x, i=i: x * i` — default argument captures the current value.
</details>
