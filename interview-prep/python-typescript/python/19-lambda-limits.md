# 19 — Lambda limits: what can't a lambda do?

> **Interview question:** "What are the limitations of lambda functions in Python?"
> **What the interviewer is really testing:** Do you know that a lambda is a single *expression*, not a mini `def` — and can you explain why that restriction exists?

## Theory — what it is

A **lambda** is a small anonymous (unnamed) function created with the `lambda` keyword. Its full syntax is: `lambda arguments: expression`. It takes any number of arguments, but its body is exactly **one expression** — a single piece of code that produces a value.

An **expression** is anything that evaluates to a value: `x + 1`, `name.upper()`, `[i*i for i in nums]`. A **statement** is an instruction that *does* something rather than producing a value: `x = 5`, `return x`, `if ...:`, `for ...:`, `import os`. This distinction is the heart of every lambda limitation.

Because the body must be one expression, a lambda **cannot contain statements**. That means no `return` (the expression's value is returned automatically), no assignments, no `if/else` blocks (only the *ternary* expression `a if cond else b`), no loops (only comprehensions), no `try/except`, no `raise`, no `while`, no `del`, and no multi-line logic.

Two more limitations interviewers love: a lambda **cannot have annotations** (type hints like `lambda x: int -> x` are a `SyntaxError`), and it **cannot have a docstring**. It also can't be "multi-line" in the statement sense — you can break one expression across lines with parentheses, but you can never have a second line of logic.

## Why it was needed

Lambdas were borrowed from functional programming (Lisp) to write tiny throwaway functions inline — mainly as `key=` functions or callbacks — without the ceremony of `def name(...): return ...`. Guido van Rossum deliberately kept them limited: he felt that anything needing more than one expression deserves a real name, because a name documents *intent*. `sorted(users, key=lambda u: u.age)` reads clearly; a 5-line anonymous block would not.

The restriction also keeps the grammar simple. Python uses indentation for blocks, and allowing statements inside an inline lambda would create an ambiguous mess (where does the lambda end?). So the rule "one expression only" is a design choice, not a technical accident — it forces you to `def` when the logic is real.

## Where it's used in a real project

- `key=` functions: `sorted(orders, key=lambda o: o.total)`, `max(files, key=lambda f: f.size)`, `list.sort(key=lambda s: s.lower())`
- `map`/`filter` in quick scripts: `list(filter(lambda x: x > 0, nums))` (though comprehensions are usually preferred)
- Callbacks in GUIs/frameworks: `button.on_click(lambda e: self.save())`, `functools.reduce(lambda a, b: a + b, nums)`
- `defaultdict` factories and sorting dicts: `defaultdict(lambda: 0)`, `sorted(d.items(), key=lambda kv: kv[1])`

## Diagram

```
def vs lambda — what fits inside the body

def f(x):                    lambda x: ...
├─ statement: x = x + 1      ├─ ONE expression only:
├─ statement: y = x * 2      │   x + 1                     ✔
├─ return y                  │   x if x > 0 else -x        ✔ (ternary = expression)
│                            │   [i*i for i in x]          ✔ (comprehension = expression)
allowed: many statements     │   x = 5        ✘ assignment is a statement
+ name + docstring           │   return x     ✘ return is a statement
+ annotations                │   for i in x   ✘ for-loop is a statement
                             │   try/except   ✘ statement
                             └─ annotations/docstrings     ✘ SyntaxError
```

## Code — explained

```python
# 1. A lambda IS just a function object — these are equivalent
square = lambda x: x * x

def square_def(x):
    return x * x

print(square(5), square_def(5))          # 25 25
print(type(square), square.__name__)     # <class 'function'> <lambda>

# 2. Ternary and comprehension ARE expressions — allowed in lambda
sign    = lambda x: "pos" if x > 0 else ("zero" if x == 0 else "neg")
squares = lambda xs: [i * i for i in xs]
print(sign(-3), squares([1, 2, 3]))      # neg [1, 4, 9]

# 3. These all raise SyntaxError — statements are banned:
# lambda x: return x            # 'return' is a statement
# lambda x: (y := x) is fine,   # walrus IS an expression (3.8+)
# but lambda x: y = x           # plain assignment is a statement — SyntaxError
# lambda x: for i in x: ...     # 'for' statement — SyntaxError
# lambda x: int: x              # annotations — SyntaxError

# 4. Multi-"line" is OK only if it's still ONE expression
total = lambda a, b, c: (
    a + b + c
)
print(total(1, 2, 3))                    # 6

# 5. Need real logic? Use def — that's the intended escape hatch
def classify(x):
    if x < 0:
        return "negative"
    return "nonnegative"

print([classify(x) for x in [-2, 0, 5]]) # ['negative', 'nonnegative', 'nonnegative']
```

1. `square = lambda x: x * x` creates a function object and binds it to a name — identical behavior to the 3-line `def` version. Both print `25`.
2. `type(square)` shows a lambda is a normal `function` object; `__name__` is the literal string `"<lambda>"` because it was anonymous (assigning it to `square` doesn't rename it).
3. `sign` shows nested **ternary** expressions are legal — they produce a value, so they count as expressions.
4. `squares` shows a **list comprehension** is legal — comprehensions evaluate to a value.
5. The commented-out lines show the classic `SyntaxError`s: `return`, plain `=`, `for`, and annotations are all statements/invalid in a lambda body.
6. `total` shows you *can* wrap one expression across lines with parentheses — it's still a single expression, not multi-statement code.
7. `classify` is the point: once logic needs an `if` block, write a `def`. Lambdas are for one-liners.

## Problems

### Easy — sort by last letter
**Problem:** Sort the list `words` alphabetically by each word's *last* character using a lambda.
**Try this input:** `words = ["apple", "banana", "cherry", "date"]`
**Expected output:** `['banana', 'apple', 'date', 'cherry']`
**Solution:**
```python
words = ["apple", "banana", "cherry", "date"]
result = sorted(words, key=lambda w: w[-1])
print(result)
```
**Logic explained:**
1. `sorted` calls `key` on each word; `w[-1]` gives the last character: `e, a, y, e`.
2. Sorting keys `a < e = e < y` gives order: `banana` (a), then `apple`/`date` (e, stable — original order kept), then `cherry` (y).

### Medium — group then sort dicts
**Problem:** Given a list of dicts, sort by `"age"` ascending, and for equal ages by `"name"` alphabetically — in one `key` lambda.
**Try this input:**
```python
people = [
    {"name": "zoe", "age": 30},
    {"name": "amy", "age": 25},
    {"name": "bob", "age": 30},
]
```
**Expected output:** `[{'name': 'amy', 'age': 25}, {'name': 'bob', 'age': 30}, {'name': 'zoe', 'age': 30}]`
**Solution:**
```python
people = [
    {"name": "zoe", "age": 30},
    {"name": "amy", "age": 25},
    {"name": "bob", "age": 30},
]
result = sorted(people, key=lambda p: (p["age"], p["name"]))
print(result)
```
**Logic explained:**
1. The lambda returns a **tuple** `(age, name)` — tuples compare element-by-element.
2. `amy` (25) sorts first. `bob` and `zoe` both have age 30, so the second element `name` breaks the tie: `bob < zoe`.
3. Returning a tuple is the standard trick for multi-key sorting in a single expression.

### Hard — conditional lambda with walrus
**Problem:** Write a lambda that, given a number, returns its square — but only if the square is under 100; otherwise return the string `"too big"`. Then use it in `map` over a list.
**Try this input:** `nums = [3, 9, 11, 5]`
**Expected output:** `[9, 81, 'too big', 25]`
**Solution:**
```python
nums = [3, 9, 11, 5]
check = lambda n: "too big" if (s := n * n) >= 100 else s
result = list(map(check, nums))
print(result)
```
**Logic explained:**
1. The body is one ternary expression — the only "if" a lambda allows.
2. `(s := n * n)` is the **walrus operator**: it assigns `s` *inside* an expression (unlike `=`, `:=` IS an expression, so it's legal in a lambda). This avoids computing `n * n` twice.
3. For `3`: `s=9`, `9 < 100` → returns `9`. For `11`: `s=121` → `"too big"`. Map applies it to each element.

## The 30-second interview answer

"A lambda is an anonymous function whose body is exactly one expression — that's the key limitation. Because it's an expression, it can't contain statements: no `return`, no assignments (though the walrus `:=` works since it's an expression), no `if`/`for` blocks (only ternaries and comprehensions), no `try/except`, and no annotations or docstrings. It's one expression that can span multiple lines only if wrapped in parentheses. The rule is deliberate: if your logic needs more than one expression, Python wants you to write a named `def` — the name itself documents intent. I use lambdas for short `key=` functions and callbacks, and reach for `def` the moment the logic isn't a one-liner."

## Follow-up trap

**"So when would you use a lambda over a def — or a lambda vs a comprehension?"** Don't say "lambdas are always fine." The accepted answer: lambdas shine only for *short, single-use* `key=` functions and callbacks. For transformations, `map`/`filter` + lambda is generally *less* readable than a comprehension: `[x*x for x in nums]` beats `list(map(lambda x: x*x, nums))`. And `functools.reduce` is so unloved that Guido moved it out of the builtins — use an explicit loop or `sum`/`math.prod` instead. If an interviewer asks "why is `lambda x: x*x` worse than a named function," mention: stack traces show `<lambda>` instead of a useful name, and you can't document it with a docstring or type it with annotations.
