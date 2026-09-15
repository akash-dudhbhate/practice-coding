# Lesson 09 — Intuition Checks

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
