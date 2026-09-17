# lesson-09-oop-basics — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: self
```python
class Test:
    def method(self):
        return self

t = Test()
print(t.method() is t)
```
<details><summary>Answer</summary>
`True` — `self` is the instance itself. `t.method()` is sugar for `Test.method(t)`.
</details>

## Check 02: Class vs Instance Attribute
```python
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print(Counter.count)
```
<details><summary>Answer</summary>
`2` — `count` is a CLASS attribute. Both increments affect the same counter. This tracks total instances.
</details>

## Check 03: __str__
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p)
```
<details><summary>Answer</summary>
`<__main__.Point object at 0x...>` — without `__str__`, Python shows the default representation. Define `__str__` for readable output.
</details>

## Check 04: Property
```python
class Temp:
    def __init__(self):
        self._c = 0
    @property
    def celsius(self):
        return self._c

t = Temp()
t.celsius = 100
```
<details><summary>Answer</summary>
**AttributeError** — `@property` without a setter makes the attribute read-only. Need `@celsius.setter` to allow assignment.
</details>

## Check 05: Inheritance
```python
class A:
    def who(self): return "A"
class B(A):
    def who(self): return "B"
b = B()
print(b.who())
```
<details><summary>Answer</summary>
`B` — method overriding. `B.who()` overrides `A.who()`. Use `super().who()` to call the parent.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Missing `self`
```python
class Dog:
    def __init__(name, age):
        name = name
        age = age

    def bark():
        return "Woof!"
```
<details><summary>Answer</summary>
**Bug:** Missing `self` parameter. Python methods need `self` as first param.
**Fix:** `def __init__(self, name, age): self.name = name; self.age = age` and `def bark(self):`.
</details>

## Debug 02 (Medium): Assigning Instead of Setting Attribute
```python
class Rectangle:
    def __init__(self, width, height):
        width = width
        height = height
```
<details><summary>Answer</summary>
**Bug:** `width = width` just reassigns the local variable, doesn't set the attribute. Need `self.width = width`.
**Fix:** `self.width = width; self.height = height`.
</details>

## Debug 03 (Hard): Mutable Class Attribute
```python
class Student:
    grades = []
    def add_grade(self, g):
        self.grades.append(g)

s1 = Student()
s2 = Student()
s1.add_grade(90)
print(s2.grades)
```
<details><summary>Answer</summary>
**Bug:** `grades = []` is a CLASS attribute, shared by all instances. `s2.grades` prints `[90]` — s1's grade!
**Fix:** Move to `__init__`: `self.grades = []`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Forgetting `self`
```python
# WRONG
def set_name(name):
    self.name = name

# CORRECT
def set_name(self, name):
    self.name = name
```

## Mistake 02: Class attribute for instance data
```python
# WRONG — shared across instances
class Student:
    grades = []

# CORRECT — per instance
class Student:
    def __init__(self):
        self.grades = []
```

## Mistake 03: Not using __str__
```python
# WRONG — unreadable default
class User:
    def __init__(self, name):
        self.name = name
print(user)  # <__main__.User at 0x...>

# CORRECT
class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"User({self.name})"
```

## Mistake 04: Directly accessing private attributes
```python
class Account:
    def __init__(self):
        self.__balance = 0

acc = Account()
acc.__balance = 1000  # WRONG — bypasses validation
# Actually creates a NEW attribute, doesn't modify __balance
```

## Mistake 05: Not using properties for computed values
```python
# WRONG — stored, can get out of sync
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.area = w * h  # doesn't update if w or h changes

# CORRECT — computed on access
class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
    @property
    def area(self):
        return self.w * self.h
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No __str__
### Before
```python
class User:
    def __init__(self, name):
        self.name = name
# print(user) → <__main__.User at 0x...>
```
### After
```python
class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"User({self.name})"
```

## Refactor 02 (Medium): Getter/Setter Instead of Property
### Before
```python
class Temperature:
    def __init__(self, c):
        self._c = c
    def get_celsius(self): return self._c
    def set_celsius(self, v): self._c = v
    def get_fahrenheit(self): return self._c * 9/5 + 32
```
### After
```python
class Temperature:
    def __init__(self, c): self._c = c
    @property
    def celsius(self): return self._c
    @celsius.setter
    def celsius(self, v): self._c = v
    @property
    def fahrenheit(self): return self._c * 9/5 + 32
```

## Refactor 03 (Hard): God Class
### Before
```python
class User:
    def __init__(self): ...
    def save_to_db(self): ...
    def send_email(self): ...
    def validate(self): ...
    def format_display(self): ...
```
### After
```python
class User: # data only
    def __init__(self): ...
class UserRepository: # persistence
    def save(self, user): ...
class EmailService: # email
    def send(self, user): ...
class UserValidator: # validation
    def validate(self, user): ...
```

---

## Approach Comparison — different ways to solve it

## Problem: Bank Account with Validation

### Approach 1: Public attributes
```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
```
**Cons:** Anyone can set `acc.balance = -1000` — no validation.

### Approach 2: Private + getters/setters
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0
    def get_balance(self):
        return self.__balance
    def set_balance(self, value):
        if value < 0:
            raise ValueError
        self.__balance = value
```
**Cons:** Java-style, not Pythonic. Verbose.

### Approach 3: Private + @property
```python
class BankAccount:
    def __init__(self):
        self.__balance = 0
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError
        self.__balance = value
```
**Pros:** Clean API (`acc.balance = 100`), validation built in. Pythonic.

**Winner:** Approach 3 — @property gives clean syntax with validation.
