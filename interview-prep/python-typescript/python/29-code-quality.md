# 29 — Code quality

> **Interview question:** "How do you ensure code quality in a Python project?"
> **What the interviewer is really testing:** Do you know the standard toolkit — type hints, a linter/formatter, pre-commit hooks, and automated tests — and *why* each layer exists?

## Theory — what it is

**Type hints** are annotations like `def add(a: int, b: int) -> int`. Python ignores them at runtime — they're documentation that a **type checker** (`mypy`, `pyright`) reads to catch mistakes like passing a `str` where an `int` belongs, *before* the code ever runs.

A **linter** (`ruff`, older tools: `flake8`, `pylint`) reads code without running it and flags bugs (unused variables, undefined names, mutable default arguments) and style violations. A **formatter** (`ruff format`, `black`) rewrites code to one consistent style so diffs stay clean and style arguments end forever. Ruff does both jobs and is the modern default because it's extremely fast.

**Pre-commit** is a framework that runs checks automatically on `git commit` — via Git's hook system — so bad code can't enter the repository. Config lives in `.pre-commit-config.yaml`.

**Tests** (usually `pytest`) are functions that assert your code produces expected results, run in CI so regressions get caught. Together these layers catch different classes of problems at different times.

## Why it was needed

Python is dynamically typed — nothing stops you from passing a string into a function expecting a number until it explodes in production at 3 AM. And with a team, everyone formats differently, dead code accumulates, and "it worked on my machine" breaks main.

Each layer plugs a specific hole: type hints catch wrong-shape data; linters catch bugs and dead code; formatters kill style drift; pre-commit enforces the rules before code lands (humans forget to run tools manually); tests verify *behavior*, which none of the static tools can check. No single tool covers all of it — that's why the answer is a stack, not a product.

## Where it's used in a real project

- **CI pipeline**: `ruff check`, `ruff format --check`, `mypy`, `pytest` run on every pull request; merge is blocked on failure.
- **Pre-commit hooks**: ruff + formatting auto-fix staged files so the committed code is already clean.
- **Library/public API code**: type hints act as machine-checked documentation — editors show autocomplete and warn on misuse.
- **Legacy cleanup**: enabling ruff rules gradually on an old codebase to burn down warnings.

## Diagram

```
write code
    |
    v
+-----------+   caught WHILE typing    e.g. str passed where int expected
| type hints|   (editor + mypy/pyright)
+-----------+
    |
    v
+-----------+   caught at COMMIT       e.g. unused import, bad style
|  ruff +   |   (pre-commit hooks run
| formatter |    automatically)
+-----------+
    |
    v
+-----------+   caught at PUSH/PR      e.g. wrong result, regression
|   tests   |   (pytest in CI blocks
|  (pytest) |    the merge)
+-----------+
    |
    v
 merge to main — bad code had to survive 3 filters
```

## Code — explained

```python
# cart.py — annotated + tested
def total_price(prices: list[float], tax_rate: float) -> float:   # 1
    """Return the sum of prices with tax applied."""              # 2
    return sum(prices) * (1 + tax_rate)                           # 3


# test_cart.py — run with `pytest`
from cart import total_price                                      # 4

def test_total_price():                                           # 5
    assert total_price([10.0, 20.0], 0.1) == 33.0                 # 6

def test_empty_cart():                                            # 7
    assert total_price([], 0.1) == 0.0
```

```yaml
# .pre-commit-config.yaml — runs on every `git commit`
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.0
    hooks:
      - id: ruff            # lint: bugs + style violations
      - id: ruff-format     # format: consistent style
```

1. `list[float]` and `-> float` are type hints. If a caller writes `total_price("abc", 0.1)`, mypy flags it before runtime; editors autocomplete `.append()` etc. on `prices`.
2. Docstring: humans get the contract too — hints say *shape*, docstrings say *meaning*.
3. Plain function body; hints change nothing at runtime.
4. Test file imports the code under test — pytest convention: files named `test_*.py`, functions named `test_*`.
5. `assert` checks actual vs expected. `(10 + 20) * 1.1 = 33.0`.
6. Passing → pytest prints `2 passed`. A regression like `* (1 - tax_rate)` fails immediately in CI.
7. Edge-case test — empty cart should be `0.0`, not crash.

## Problems

### Easy — add the hints
**Problem:** Add type hints to `greet(name, times=1)` so a checker knows `name` is a string, `times` is an int, and it returns a string.
**Try this input:** `greet("ada", 2)`
**Expected output:** `hello ada hello ada`
**Solution:**
```python
def greet(name: str, times: int = 1) -> str:
    return " ".join([f"hello {name}"] * times)

print(greet("ada", 2))
```
**Logic explained:**
1. `name: str` — annotation on a parameter; `times: int = 1` — annotation plus a default value (default comes after the hint).
2. `-> str` — return-type annotation, placed between `)` and `:`.
3. The body is unchanged; hints don't affect execution — `[f"hello ada"] * 2` → two copies, joined with a space.
4. Bonus: `mypy` would now reject `greet(5, "x")` before it ever ran.

### Medium — write the test
**Problem:** `add_item(cart, item)` returns a *new* list with the item appended. Write two pytest tests: adding to an empty cart, and that the original cart is NOT mutated.
**Try this input:** `pytest test_cart.py`
**Expected output:** `2 passed`
**Solution:**
```python
# cart.py
def add_item(cart: list[str], item: str) -> list[str]:
    return cart + [item]          # new list — original untouched

# test_cart.py
from cart import add_item

def test_add_to_empty():
    assert add_item([], "apple") == ["apple"]

def test_original_cart_not_mutated():
    cart = ["apple"]
    new_cart = add_item(cart, "pear")
    assert new_cart == ["apple", "pear"]
    assert cart == ["apple"]      # the original is unchanged
```
**Logic explained:**
1. `cart + [item]` builds a fresh list — unlike `cart.append(item)`, which mutates in place and returns `None`.
2. `test_add_to_empty` covers the base case.
3. `test_original_cart_not_mutated` checks a *property* callers rely on — this is what makes it a good test, not just a happy-path check.
4. `pytest` auto-discovers `test_*.py` files and `test_*` functions; each `assert` that holds counts as a pass.

### Hard — fix what the linter catches
**Problem:** This code passes review but ruff rule `B006` flags it, and it has a real bug. Find it and fix it — `add_tag` should return a one-item list on every fresh call.
**Try this input:**
```python
print(add_tag("a"))
print(add_tag("b"))   # fresh call, no list passed
```
**Buggy version:**
```python
def add_tag(tag, tags=[]):     # mutable default argument!
    tags.append(tag)
    return tags
```
**Expected output:**
```
['a']
['b']
```
**Solution:**
```python
def add_tag(tag: str, tags: list[str] | None = None) -> list[str]:
    if tags is None:
        tags = []
    tags.append(tag)
    return tags

print(add_tag("a"))
print(add_tag("b"))
```
**Logic explained:**
1. The bug: Python evaluates default arguments **once**, when the `def` executes — so every call that omits `tags` shares *the same list object*. With the buggy version, the second call returns `['a', 'b']`, not `['b']`.
2. Fix: default to `None` (immutable, safe), then create a fresh list inside the function body where it runs per call.
3. `list[str] | None` — the `|` means "or" (a union type); `None` is the sentinel.
4. Ruff rule `B006` (mutable-argument-default) exists precisely because this is one of Python's most famous footguns — the linter catches it statically so the bug never ships.

## The 30-second interview answer

"I use four layers. Type hints plus mypy catch wrong-shape data while typing. Ruff handles both linting — bugs like mutable defaults and unused imports — and formatting, so style is automatic. Pre-commit hooks run those tools on every commit so nothing slips in because someone forgot. And pytest tests verify actual behavior, running in CI to block regressions. Each layer catches what the others can't: static tools catch shape and smells, tests catch wrong answers."

## Follow-up trap

**"Do type hints make Python typed / do they do anything at runtime?"** — No. They're ignored at runtime (stored in `__annotations__`, mostly). `def f(x: int)` happily accepts a string. They only matter when a checker (mypy/pyright) or your editor reads them — think of them as executable documentation, not enforcement. (Exception: libraries like Pydantic/FastAPI *do* read them at runtime to validate data.)

**"If you have tests, why do you need a linter?"** — Different bugs. Tests check that correct inputs give correct outputs; they can't see dead code, unused variables, shadowed builtins, or mutable defaults in code paths your tests never hit. Linters read *all* the code; tests only exercise the paths you wrote tests for.
