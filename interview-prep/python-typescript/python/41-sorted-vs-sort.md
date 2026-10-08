# 41 — `sorted` vs `list.sort`: return values; `key=` and `reverse=` args

> **Interview question:** "What's the difference between `sorted()` and `list.sort()`?"
> **What the interviewer is really testing:** Whether you know in-place vs copy semantics, the `None` return trap, and how `key`/`reverse` work.

## Theory — what it is

`sorted(iterable)` is a **built-in function** that takes any iterable (list, tuple, dict, string, generator) and returns a **new list** with the elements sorted. The original is untouched.

`list.sort()` is a **method** that sorts the list **in place** — it rearranges the existing list's memory and returns **`None`**. This is deliberate Python design (also on `list.reverse()`, `dict.update()`): methods that mutate return `None` so you can't pretend they gave you a new object.

The classic bug: `a = a.sort()` silently turns `a` into `None`. If you want both worlds — keep the original AND have a sorted copy — use `sorted(a)`. If you don't need the original, `a.sort()` avoids a copy and is slightly more memory-efficient.

Both accept the same two keyword args: **`key=`** — a function applied to each element to produce a *sort key* (the comparison value), and **`reverse=`** — `True` for descending. Both use **Timsort**, which is **stable**: equal elements keep their original relative order — that enables multi-level sorts by sorting twice.

## Why it was needed

Two operations serve two real needs. Mutating in place (`sort`) matters when the list is big and you don't want a copy — sorting a million rows shouldn't double memory. Returning a new list (`sorted`) matters when callers rely on the original order — sorting `request.items` shouldn't reorder the user's cart for everyone else.

`key=` exists because elements often aren't directly comparable in the way you want: you sort users by age, strings by length, tuples by second element — without `key=` you'd have to write comparator functions (the old, slower `cmp=` removed in Python 3). `reverse=` exists purely for readability — `key=lambda x: -x` breaks on strings.

## Where it's used in a real project

- **API responses:** `return sorted(users, key=lambda u: u.last_active, reverse=True)` — new list, original untouched.
- **Report tables:** `rows.sort(key=lambda r: (-r.revenue, r.name))` — in-place on data you own; tuple keys give multi-level sort.
- **Sorting dict items:** `sorted(counts.items(), key=lambda kv: kv[1], reverse=True)` — sorted() accepts the `dict_items` iterable.
- **`min`/`max`/`heapq` use the same `key=` convention** — learn it once, use everywhere.

## Diagram

```
nums = [3, 1, 2]

sorted(nums)  ->  returns NEW list [1, 2, 3]
                  nums stays [3, 1, 2]          (copy, original safe)

nums.sort()   ->  returns None
                  nums becomes [1, 2, 3]        (in-place, original gone)

TRAP:  x = nums.sort()   # x is None — the #1 beginner bug

key= example:  sorted(["bb", "a", "ccc"], key=len)
               keys: 2, 1, 3  ->  result: ["a", "bb", "ccc"]
```

## Code — explained

```python
nums = [3, 1, 2]

s = sorted(nums)          # new list
print(s)                  # [1, 2, 3]
print(nums)               # [3, 1, 2] — untouched

r = nums.sort()           # in-place
print(r)                  # None — trap!
print(nums)               # [1, 2, 3]

words = ["bb", "a", "ccc"]
print(sorted(words, key=len))                  # ['a', 'bb', 'ccc']
print(sorted(words, key=len, reverse=True))    # ['ccc', 'bb', 'a']

pairs = [(1, "b"), (2, "a"), (1, "a")]
print(sorted(pairs))      # [(1,'a'),(1,'b'),(2,'a')] — tuple compares element-wise

# sorted() works on ANY iterable; .sort() is list-only
print(sorted("cab"))      # ['a', 'b', 'c']
```

1. `sorted(nums)` allocates a new list; `nums` keeps its order — safe for shared data.
2. `nums.sort()` mutates `nums` and returns `None`; assigning the result destroys your data.
3. `key=len` sorts by each string's length, not alphabetically.
4. Tuples sort element-by-element — `(1, "a") < (1, "b")` — a free multi-key sort.
5. `sorted("cab")` proves it works on any iterable; `"cab".sort()` doesn't exist.

## Problems

### Easy — sort a dict's items by value
**Problem:** Given a counts dict, print `[(name, count), ...]` sorted by count descending.
**Try this input:** `{"a": 3, "b": 1, "c": 2}`
**Expected output:** `[('a', 3), ('c', 2), ('b', 1)]`
**Solution:**
```python
counts = {"a": 3, "b": 1, "c": 2}
out = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)
print(out)   # [('a', 3), ('c', 2), ('b', 1)]
```
**Logic explained:**
1. `counts.items()` is a view of `(key, value)` tuples — an iterable, so `sorted()` accepts it.
2. `key=lambda kv: kv[1]` extracts the count as the sort key.
3. `reverse=True` flips to descending — `.sort()` couldn't be used anyway (items() isn't a list).

### Medium — sort by last name, then first name
**Problem:** Sort full names by last name; ties broken by first name.
**Try this input:** `["John Smith", "Ann Smith", "Bob Adams"]`
**Expected output:** `['Bob Adams', 'Ann Smith', 'John Smith']`
**Solution:**
```python
names = ["John Smith", "Ann Smith", "Bob Adams"]
out = sorted(names, key=lambda n: tuple(reversed(n.split())))
print(out)   # ['Bob Adams', 'Ann Smith', 'John Smith']
```
**Logic explained:**
1. `n.split()` -> `["John", "Smith"]`; `reversed` -> `("Smith", "John")`.
2. Tuple keys compare element-wise: last name first, first name breaks ties — leverages tuple comparison instead of a custom comparator.
3. `sorted` returns a new list — `names` is preserved.

### Hard — stable multi-level sort (two passes)
**Problem:** Sort people by age ascending, and within same age by name descending — using **two** sorts, exploiting stability.
**Try this input:** `[("Ann", 30), ("Bob", 25), ("Cat", 30)]` (name, age)
**Expected output:** `[('Bob', 25), ('Cat', 30), ('Ann', 30)]`
**Solution:**
```python
people = [("Ann", 30), ("Bob", 25), ("Cat", 30)]
people.sort(key=lambda p: p[0], reverse=True)   # secondary key first: name desc
people.sort(key=lambda p: p[1])                 # primary key last: age asc
print(people)
# [('Bob', 25), ('Cat', 30), ('Ann', 30)]
```
**Logic explained:**
1. Timsort is **stable**: equal elements keep their previous relative order.
2. Sort by the *secondary* key first (name descending) — establishes order within ties.
3. Sort by the *primary* key (age) — ties in age keep the name-desc order from step 2.
4. This is the classic interview trick; alternatively one pass with `key=lambda p: (p[1], ...)` works for ascending-only keys (strings can't be negated).

## The 30-second interview answer

"`sorted()` returns a **new sorted list** from any iterable and leaves the original alone; `list.sort()` sorts **in place** and returns `None` — assigning `a = a.sort()` is a classic bug that loses your list. Both take `key=` — a function producing the comparison value per element, like `key=len` or `key=lambda u: u.age` — and `reverse=` for descending. Both use Timsort, which is stable, so equal elements keep their order and you can do multi-level sorts in multiple passes. Rule of thumb: `.sort()` when you own the list and don't need the original order; `sorted()` for everything else."

## Follow-up trap

**"How do you sort descending on one field and ascending on another in a single pass?"** Numeric fields: negate the ascending ones — `key=lambda e: (-e.age, e.name)`. Can't negate strings — use the stability trick (two sorts) or `functools.cmp_to_key`. Also expect: *"Is `key` called once per element or once per comparison?"* — once per element, cached (Schwartzian transform internally) — that's why `key=` beat the old `cmp=` which called the comparator O(n log n) times.
