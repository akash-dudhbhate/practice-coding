# Lesson 12 — Intuition Checks

## Check 01: Decorator Execution
```python
def deco(func):
    print("decorating")
    def wrapper():
        print("calling")
        func()
    return wrapper

@deco
def hello(): print("hello")

print("defined")
hello()
```
<details><summary>Answer</summary>
```
decorating
defined
calling
hello
```
"decorating" runs at definition time (when @deco is applied). "calling" and "hello" run when called.
</details>

## Check 02: Context Manager
```python
class CM:
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self, *args):
        print("exit")

with CM() as cm:
    print("body")
```
<details><summary>Answer</summary>
```
enter
body
exit
```
</details>

## Check 03: Exception in Context Manager
```python
class CM:
    def __enter__(self): return self
    def __exit__(self, *args):
        print("exit")
        return True

with CM():
    raise ValueError("oops")
print("after")
```
<details><summary>Answer</summary>
```
exit
after
```
`__exit__` returning True SUPPRESSES the exception. If it returns False/None, the exception propagates.
</details>

## Check 04: contextlib
```python
from contextlib import contextmanager
@contextmanager
def cm():
    print("setup")
    yield
    print("teardown")

with cm():
    print("body")
```
<details><summary>Answer</summary>
```
setup
body
teardown
```
</details>

## Check 05: Stacked Decorators
```python
@decorator_a
@decorator_b
def func(): pass
```
Which applies first?
<details><summary>Answer</summary>
`decorator_b` applies first (closest to function), then `decorator_a`. Equivalent to `func = decorator_a(decorator_b(func))`.
</details>
