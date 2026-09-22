# lesson-06-functions-deep-dive — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: *args Type
```python
def func(*args):
    print(type(args))
func(1, 2, 3)
```
What prints?

<details><summary>Answer</summary>
`<class 'tuple'>` — `*args` is always a tuple, not a list.
</details>

## Check 02: **kwargs Type
```python
def func(**kwargs):
    print(type(kwargs))
func(a=1, b=2)
```
What prints?

<details><summary>Answer</summary>
`<class 'dict'>` — `**kwargs` is always a dict.
</details>

## Check 03: Default Evaluation
```python
def func(x, lst=[]):
    return lst

a = func(1)
b = func(2)
print(a is b)
```
What prints?

<details><summary>Answer</summary>
`True` — the default `[]` is created ONCE. Both calls share the same list object. `a` and `b` point to the same list.
</details>

## Check 04: Keyword Args Order
```python
def func(a, b, c):
    return f"{a}{b}{c}"
print(func(c=3, a=1, b=2))
```
What prints?

<details><summary>Answer</summary>
`123` — When using keyword arguments, order doesn't matter. `c=3, a=1, b=2` maps correctly.
</details>

## Check 05: Lambda vs Def
```python
f = lambda x: x * 2
def g(x): return x * 2
print(f(5) == g(5))
```
What prints?

<details><summary>Answer</summary>
`True` — lambda is just syntactic sugar for a one-line function. `f` and `g` are both function objects that do the same thing. Lambda is anonymous (no `__name__`).
</details>

---

## Debug Exercises — find and fix the bug

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

---

## Common Mistakes — the traps learners hit

## Mistake 01: Mutable default arguments
```python
# WRONG
def func(lst=[]):
    lst.append(1)
    return lst

# CORRECT
def func(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst
```

## Mistake 02: Default args before required args
```python
# WRONG — SyntaxError
def func(a=1, b):

# CORRECT
def func(b, a=1):
```

## Mistake 03: Using lambda for complex logic
```python
# WRONG — unreadable
func = lambda x: x * 2 if x > 0 else -x if x < 0 else 0

# CORRECT — use def
def func(x):
    if x > 0:
        return x * 2
    elif x < 0:
        return -x
    return 0
```

## Mistake 04: Forgetting return in lambda
```python
# WRONG — lambda doesn't need return, but def does
f = lambda x: return x * 2  # SyntaxError!

# CORRECT
f = lambda x: x * 2
```

## Mistake 05: Not using *args and **kwargs flexibly
```python
# VERBOSE — fixed params
def add(a, b, c, d, e):
    return a + b + c + d + e

# FLEXIBLE
def add(*nums):
    return sum(nums)
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Repeated Function Calls
### Before
```python
def get_info(user):
    name = user.get("name")
    age = user.get("age")
    email = user.get("email")
    return f"{name}, {age}, {email}"
```
### After
```python
def get_info(user):
    return ", ".join(str(user.get(k, "")) for k in ("name", "age", "email"))
```

## Refactor 02 (Medium): Boolean Flag Parameter
### Before
```python
def process(data, is_upper):
    if is_upper:
        return data.upper()
    else:
        return data.lower()
```
### After
```python
def process(data, transform=str.upper):
    return transform(data)
```

## Refactor 03 (Hard): Long Parameter List
### Before
```python
def create_user(name, age, email, role, dept, salary, start_date):
    # ... 7 params, hard to read calls
```
### After
```python
from dataclasses import dataclass
@dataclass
class UserConfig:
    name: str
    age: int
    email: str
    role: str = "member"
    dept: str = "general"
    salary: float = 0
    start_date: str = ""

def create_user(config: UserConfig):
    # ... use config.name, config.age etc.
```

---

## Approach Comparison — different ways to solve it

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
