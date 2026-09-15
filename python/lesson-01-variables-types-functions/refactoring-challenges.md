# Lesson 01 — Refactoring Challenges

> **Take working but ugly code and make it better.** Same output, cleaner code.
> This trains your eye for code quality — the skill that separates juniors from seniors.

---

## Refactor 01 (Easy): Verbose If/Else

### Before
```python
def check_number(n):
    if n > 0:
        return True
    else:
        return False
```

### Problems
1. `if/else` returning True/False is redundant — the condition IS a boolean
2. `else` is unnecessary when `if` returns

### After
```python
def check_number(n):
    return n > 0
```

### What you learned
**Return the condition directly.** `n > 0` already evaluates to `True` or `False`. Wrapping it in if/else adds 3 lines for nothing.

---

## Refactor 02 (Medium): Repeated Logic

### Before
```python
def process_data(data):
    result = []
    for item in data:
        if item > 0:
            result.append(item * 2)
    return result
```

### Problems
1. Manual loop + append is verbose
2. Filter and transform in one step is less readable

### After
```python
def process_data(data):
    return [item * 2 for item in data if item > 0]
```

### What you learned
**List comprehensions replace filter+transform loops.** One line, faster, more Pythonic. The pattern: `[transform for item in iterable if condition]`.

---

## Refactor 03 (Hard): Nested Conditionals

### Before
```python
def calculate_price(quantity, price, discount):
    if quantity > 0:
        if price > 0:
            if discount > 0:
                total = quantity * price
                total = total - (total * discount / 100)
                return total
            else:
                return quantity * price
        else:
            return 0
    else:
        return 0
```

### Problems
1. Deep nesting (3 levels) — hard to read
2. Repeated `return 0` for error cases
3. `total = total - ...` should use `-=` 
4. Discount logic mixed with validation

### After
```python
def calculate_price(quantity, price, discount):
    if quantity <= 0 or price <= 0:
        return 0
    total = quantity * price
    if discount > 0:
        total -= total * discount / 100
    return total
```

### What you learned
1. **Guard clauses first** — handle error cases early, return immediately. Flattens nesting.
2. **Combine conditions** — `quantity <= 0 or price <= 0` replaces two nested ifs.
3. **Use `-=`** — compound assignment is cleaner than `x = x - y`.

---

## Refactoring Checklist

When reviewing code, ask:
- [ ] Can an if/else returning True/False be just `return condition`?
- [ ] Can a loop with append be a list comprehension?
- [ ] Can nested ifs be flattened with guard clauses (early return)?
- [ ] Can repeated code be extracted to a function?
- [ ] Can `x = x + y` be `x += y`?
- [ ] Can verbose conditions be combined with `and`/`or`?
- [ ] Is the function doing ONE thing? (Single Responsibility)
- [ ] Are variable names descriptive? (`data` vs `user_emails`)

> **The goal:** After 100 refactoring challenges, you'll write clean code the first time — because your eyes have seen the difference 100 times.
