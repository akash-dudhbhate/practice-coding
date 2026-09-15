# Lesson 06 — Intuition Checks

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
