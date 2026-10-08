# 18 — `map` / `filter` / `reduce` vs comprehensions — which is preferred and why

> **Interview question:** "`map`/`filter`/`reduce` or list comprehensions — which do you use, and why?"
> **What the interviewer is really testing:** Whether you know comprehensions are the Pythonic default, `map`/`filter` return *lazy iterators* (not lists!), and `reduce` was demoted to `functools` because explicit loops/builtins read better.

## Theory — what it is

Three functional-style builtins/transformers, plus the Python-native alternative:

- `map(func, iterable)` — **lazy** iterator applying `func` to each item: `map(str, nums)`
- `filter(func, iterable)` — **lazy** iterator keeping items where `func(item)` is truthy; `filter(None, xs)` drops falsy items
- `functools.reduce(func, iterable, initial)` — **eager** fold: combines items pairwise down to one value — was a builtin in Python 2, moved to `functools` in Python 3
- **Comprehensions** — `[expr for x in xs if cond]` builds a **list eagerly**; `(...)` generator expression is the lazy equivalent

**Which is preferred: comprehensions.** Readability is the argument — the computation is spelled out inline instead of wrapped in a lambda:

```python
[x * x for x in nums if x % 2 == 0]                    # read it left to right
list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))  # nested lambdas — worse
```

`map(lambda ...)` is *strictly* worse than a comprehension — same laziness issues, plus lambda call overhead, plus harder to read. `map` only wins when you already have a **named/builtin function**: `map(str, items)` is slightly faster (no Python-level lambda) and honestly tidy.

**Laziness trap:** `map`/`filter` return iterators — consumed **once**, and printing them gives `<map object at 0x...>`, not values. You must `list(...)` them. Comprehensions hand you a real list immediately; use `(x*x for x in xs)` when you *want* lazy (huge data, pipelines).

**`reduce` reality check:** `reduce(lambda a, b: a + b, xs)` is just `sum(xs)`. `sum`, `min`, `max`, `any`, `all`, `math.prod`, `".".join` cover ~99% of folds readably — reach for `reduce` only when no builtin fits, and even then compare against an explicit loop.

`map` also takes **multiple iterables**: `map(add, xs, ys)` — stops at the shortest.

## Why it was needed

`map`/`filter`/`reduce` came from Lisp-style functional programming — apply/transform/collapse without loops. Comprehensions (added in Python 2.0) expressed the same ideas in syntax closer to math set-builder notation — and read dramatically better for the common case. `reduce` was deliberately demoted to `functools` in Python 3: Guido judged explicit accumulator loops clearer for every fold that isn't `sum`-shaped, and the builtins cover those. The functions survive for laziness and named-function pipelines — they're just no longer the default idiom.

## Where it's used in a real project

- **Comprehensions everywhere:** parsing rows, building dicts `{u.id: u for u in users}`, filtering records — the default in every modern codebase.
- **`filter(None, xs)`:** drop falsy values in one call — an accepted idiom even by comprehension fans.
- **`map` with named functions:** `list(map(int, row.split(",")))` — parsing CSV-ish input; `map(str.strip, lines)` on file handles (lazy, memory-friendly).
- **Lazy pipelines on huge data:** `map`/`filter` or genexps stream without materializing — pass them straight into `sum(...)`, `any(...)`.
- **`reduce`:** rare in the wild — merging dicts (`{"a":1} | {"b":2}` or `{k:v for d in dicts for k,v in d.items()}` is now preferred), or genuinely custom folds.

## Diagram

```
nums = [1, 2, 3, 4]

map:      each item -> f(item)          [1, 4, 9, 16]     ~ [x*x for x in nums]
filter:   keep if pred(item) truthy     [2, 4]            ~ [x for x in nums if x%2==0]
reduce:   fold pairwise -> ONE value    10                ~ sum(nums)  (or a loop)

  map/filter -> LAZY iterator (one-shot)   vs   [ ... ] -> eager list
                                              ( ... ) -> lazy like map
```

## Code — explained

```python
from functools import reduce

nums = [1, 2, 3, 4]

m = map(lambda x: x * x, nums)
print(m)                    # <map object at 0x...>  — LAZY: an iterator, not a list!
print(list(m))              # [1, 4, 9, 16]
print(list(m))              # []  — already consumed; iterators are one-shot

print([x * x for x in nums])            # [1, 4, 9, 16]  — same thing, clearer

print(list(filter(lambda x: x % 2 == 0, nums)))   # [2, 4]
print([x for x in nums if x % 2 == 0])            # [2, 4]  — clearer

print(reduce(lambda a, b: a + b, nums, 0))        # 10
print(sum(nums))                                  # 10 — the builtin wins

print(list(map(str, nums)))                       # ['1', '2', '3', '4']
print(list(filter(None, [0, 1, "", "x", None])))  # [1, 'x'] — drops falsy
```

1. `map`/`filter` return **iterators** — `print(m)` shows the object, not values; `list(m)` materializes them. They're **one-shot**: the second `list(m)` is empty because the iterator was exhausted.
2. The comprehension `[x*x for x in nums]` produces the same list eagerly — readable top-to-bottom, no lambda. That's why it's preferred.
3. `reduce(f, xs, init)` folds: `f(f(f(0,1),2),3)...` → `10`. `sum(nums)` says the same thing in one word — that's why `reduce` was moved out of builtins.
4. `map(str, nums)` — with a *named* function, `map` is clean and slightly faster than `[str(x) for x in nums]` (no Python-level call per item). `filter(None, xs)` keeps only truthy items — the one `filter` idiom that survives.

## Problems

### Easy — rewrite as a comprehension
**Problem:** Rewrite these two expressions as comprehensions — same results, no lambdas.
```python
nums = [1, 2, 3, 4]
list(map(lambda x: x * 2, nums))
list(filter(lambda x: x % 2 == 0, nums))
```
**Try this input:** `nums = [1, 2, 3, 4]`
**Expected output:** `[2, 4, 6, 8]` then `[2, 4]`
**Solution:**
```python
nums = [1, 2, 3, 4]
print([x * 2 for x in nums])          # [2, 4, 6, 8]
print([x for x in nums if x % 2 == 0])  # [2, 4]
```
**Logic explained:**
1. `map(lambda x: x * 2, nums)` → the lambda's body becomes the comprehension's expression: `[x * 2 for x in nums]`.
2. `filter(lambda x: x % 2 == 0, nums)` → the predicate moves to the `if` clause: `[x for x in nums if x % 2 == 0]`.
3. Same output, but the comprehension reads left-to-right and needs no `list(...)` wrapper — it's already a list.

### Medium — collapse the map+filter chain
**Problem:** This pipeline squares only the even numbers, but nests `map` inside `filter` — rewrite it as ONE comprehension.
```python
nums = [1, 2, 3, 4, 5, 6]
list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))
```
**Try this input:** `nums = [1, 2, 3, 4, 5, 6]`
**Expected output:** `[4, 16, 36]`
**Solution:**
```python
nums = [1, 2, 3, 4, 5, 6]
print([x * x for x in nums if x % 2 == 0])   # [4, 16, 36]
```
**Logic explained:**
1. Read the nested version inside-out: `filter` keeps evens (`2, 4, 6`), `map` squares them → `4, 16, 36`.
2. One comprehension does both: `for x in nums` → `if x % 2 == 0` (filter) → `x * x` (map). Order in the comprehension is: loop → filter → expression.
3. The comprehension is a real list — no `list(...)` needed — and there's exactly one place to read the logic instead of two nested calls.
4. If the data were huge and you wanted lazy output, the equivalent is a **generator expression**: `(x * x for x in nums if x % 2 == 0)` — same laziness as `map`/`filter`, still readable.

### Hard — `reduce` for merging, then the modern way
**Problem:** Merge a list of dicts into one (later dicts win on key clashes) using `reduce` — then write the preferred modern equivalent and show they agree.
**Try this input:** `dicts = [{"a": 1}, {"b": 2}, {"a": 9}]`
**Expected output:** `{'a': 9, 'b': 2}` twice.
**Solution:**
```python
from functools import reduce

dicts = [{"a": 1}, {"b": 2}, {"a": 9}]

merged = reduce(lambda acc, d: {**acc, **d}, dicts, {})
print(merged)                                    # {'a': 9, 'b': 2}

modern = {k: v for d in dicts for k, v in d.items()}
print(modern)                                    # {'a': 9, 'b': 2}
```
**Logic explained:**
1. `reduce` folds left: `{}` → `{"a":1}` → `{"a":1,"b":2}` → `{"a":9,"b":2}` — each step unpacks the accumulator and the new dict, later keys overwriting earlier.
2. The dict comprehension iterates `d.items()` per dict — same overwrite rule since later writes win — no lambda, no import, and it builds exactly one dict instead of a fresh dict per step.
3. This is the `reduce` story in miniature: it *works*, but a comprehension is shorter, faster (no intermediate dicts), and needs no `functools` import — which is why `reduce` got demoted from builtin status in Python 3.
4. Note: a third way exists — `dicts[0] | dicts[1] | ...` via `reduce(lambda a, b: a | b, dicts)` — but the comprehension still beats it here.

## The 30-second interview answer

"Comprehensions are the Pythonic default — `[f(x) for x in xs if p(x)]` reads left-to-right and beats `map`/`filter` with lambdas on readability and even speed, since there's no lambda call overhead. `map`/`filter` return *lazy one-shot iterators* — you must `list()` them, and they can't be re-iterated — which catches people printing them. `map` earns its place when the function is already named — `map(int, strs)` — or for lazy pipelines on big data; `filter(None, xs)` to drop falsy values is a fine idiom. `reduce` was demoted to `functools` because `sum`, `min`, `max`, `any`, `all` cover most folds and explicit loops beat it for the rest — I reach for it only when nothing else expresses the fold clearly."

## Follow-up trap

**"Why did `reduce` leave builtins?"** — Guido's call: explicit accumulator loops are clearer, and `sum`/`max`/`any`/`join` cover the common folds — `reduce` optimized for a case that's already served better. Second trap: *"`map` returns what?"* — an **iterator**, not a list: `print(map(str, xs))` shows `<map object at ...>`, and after one `list()` call it's *exhausted* — a classic "my map only worked once" bug. Third: *"How do you get lazy evaluation with a comprehension?"* — generator expression `(x*x for x in xs)`. Fourth: *"Multiple iterables to `map`?"* — `map(f, xs, ys)` passes items pairwise and stops at the shortest — `[x+y for x,y in zip(xs,ys)]` is the comprehension spelling.
