# 15 — Closures and `nonlocal`

> **Interview question:** "What is a closure? Write a counter using a nested function and `nonlocal`."
> **What the interviewer is really testing:** Whether you know a function can carry state around in its *environment* — the mechanism behind decorators.

## Theory — what it is

A **closure** is a nested function that remembers variables from the function it was defined inside — even after that outer function has returned and its stack frame is gone.

```python
def outer():
    x = 10
    def inner():
        return x        # inner "closes over" x
    return inner
```

`outer()` finishes, but `x` isn't destroyed — `inner` keeps a private reference to it. That captured variable is called a **free variable**, and each call to `outer()` creates a *fresh* one.

Python resolves names by the **LEGB** rule: Local → Enclosing → Global → Built-in. Reading an enclosing variable is automatic. **Writing** is the catch: `count += 1` inside a nested function would normally make `count` *local* (assignment = local unless declared otherwise) → `UnboundLocalError`. `nonlocal count` tells Python: "don't create a local — write into the enclosing scope's `count`."

(`global` is the same idea but targets module scope; `nonlocal` targets the nearest enclosing *function* scope.)

## Why it was needed

Closures are "objects lite" — a way to give a function private, persistent state without writing a class:

- A class needs `__init__`, `self.count`, and boilerplate; a closure is 5 lines.
- The state is truly *private* — nothing outside can touch `count` except the inner function. With a class attribute, `obj.count` is public.
- Decorators (file 16) are closures: the wrapper remembers the function it wraps.

Without closures/`nonlocal`, you'd have to mutate a list (`count = [0]`) or use a class for every piece of function state.

## Where it's used in a real project

- **Decorators**: `wrapper` closes over the wrapped function and its config.
- **Callbacks/handlers**: `button.on_click(make_handler(user))` — the handler remembers `user`.
- **Factories**: `make_multiplier(3)` returns a specialized `times-3` function.
- **Memoization/`once` wrappers**: cache state lives in the enclosing scope.

## Diagram

```
def make_counter():
    count = 0  <---------------------------+   enclosing scope
    def inc():                             |   (survives after return!)
        nonlocal count  ---- reaches here -+
        count += 1
        return count
    return inc

c = make_counter()      d = make_counter()
c() -> 1   c() -> 2     d() -> 1   <- each call got its OWN count cell
```

## Code — explained

```python
def make_counter():
    count = 0                    # (1) enclosing-scope variable
    def inc():
        nonlocal count           # (2) write to enclosing count, not a new local
        count += 1
        return count
    return inc                   # (3) return the inner function itself

c = make_counter()               # (4) count=0 frame is captured by c
print(c())                       # 1
print(c())                       # 2
print(c())                       # 3

d = make_counter()               # (5) fresh, independent count
print(d())                       # 1 — not 4!
```

Line-by-line:

1. `count = 0` lives in `make_counter`'s scope — but because `inc` references it, Python stores it in a **cell** that outlives the function call.
2. `nonlocal count` — without it, `count += 1` reads `count` before assignment → `UnboundLocalError: local variable 'count' referenced before assignment`.
3. `return inc` — we return the *function object*; nobody ever calls `inc` inside `make_counter`.
4. Every call to `make_counter()` creates a **new** `count` cell — `c` and `d` don't share state.
5. Check it: `c.__closure__[0].cell_contents` literally shows the captured `count` — closures are inspectable.

## Problems

### Easy — Adder factory
**Problem:** Write `make_adder(n)` returning a function that adds `n` to its argument.
**Try this input:**
```python
add5 = make_adder(5)
print(add5(10), add5(1))
```
**Expected output:** `15 6`
**Solution:**
```python
def make_adder(n):
    def adder(x):
        return x + n             # reads enclosing n — no nonlocal needed (read-only)
    return adder

add5 = make_adder(5)
print(add5(10), add5(1))         # 15 6
```
**Logic explained:**
1. `n` is captured when `make_adder(5)` runs.
2. `adder` only *reads* `n` — `nonlocal` is only needed for rebinding.
3. `make_adder(5)` and `make_adder(2)` would create independent closures.

### Medium — Bank account
**Problem:** Write `make_account(balance)` returning a `dict` of `deposit`/`withdraw`/`balance` functions sharing one private `balance`. `withdraw` must reject overdrafts (return `"insufficient funds"`).
**Try this input:**
```python
acct = make_account(100)
acct["deposit"](50)
print(acct["withdraw"](30))
print(acct["withdraw"](500))
print(acct["balance"]())
```
**Expected output:**
```
120
insufficient funds
120
```
**Solution:**
```python
def make_account(balance):
    def deposit(amount):
        nonlocal balance
        balance += amount

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "insufficient funds"
        balance -= amount
        return balance

    def get_balance():
        return balance

    return {"deposit": deposit, "withdraw": withdraw, "balance": get_balance}

acct = make_account(100)
acct["deposit"](50)
print(acct["withdraw"](30))      # 120
print(acct["withdraw"](500))     # insufficient funds
print(acct["balance"]())         # 120
```
**Logic explained:**
1. All three inner functions close over the **same** `balance` cell.
2. `deposit`/`withdraw` rebind it → need `nonlocal`; `get_balance` only reads → doesn't.
3. `balance` is unreachable from outside — true privacy, no `_private` naming convention needed.

### Hard — `once` wrapper
**Problem:** Write `once(f)` — returns a function that runs `f` only the first time and returns that cached result on every later call.
**Try this input:**
```python
@once
def boot():
    print("booting")
    return 42

print(boot(), boot(), boot())
```
**Expected output:**
```
booting
42 42 42
```
("booting" prints **once**, before the three `42`s)
**Solution:**
```python
def once(f):
    called = False
    result = None
    def wrapper(*args, **kwargs):
        nonlocal called, result          # we're REBINDING both
        if not called:
            result = f(*args, **kwargs)
            called = True
        return result
    return wrapper

@once                                    # boot = once(boot)
def boot():
    print("booting")
    return 42

print(boot(), boot(), boot())
# booting
# 42 42 42
```
**Logic explained:**
1. `called`/`result` live in `once`'s scope — captured by `wrapper`.
2. First `boot()`: `called` is `False` → run `f`, cache `result`, flip the flag.
3. Later calls skip `f` entirely and return the cached `result`.
4. This is the skeleton of real memoization — and of decorators generally.

## The 30-second interview answer

"A closure is an inner function that captures variables from the enclosing function and keeps them alive after the outer function returns — Python stores each captured variable in a cell. Reading is automatic via LEGB; writing requires `nonlocal`, otherwise `x += 1` makes `x` a local and throws `UnboundLocalError`. Each call to the outer function creates fresh captured state. Closures are how decorators, callbacks, and lightweight stateful functions work — I'd demo it with `make_counter` returning an `inc` that does `nonlocal count`."

## Follow-up trap

**"What does this print, and why?"**

```python
fns = [lambda: i for i in range(3)]
print([f() for f in fns])       # [2, 2, 2] — NOT [0, 1, 2]!
```

Closures capture the **variable**, not its **value**. All three lambdas share one `i`, which is `2` when the loop ends. Fix by binding the value as a default argument — defaults are evaluated at definition time:

```python
fns = [lambda i=i: i for i in range(3)]
print([f() for f in fns])       # [0, 1, 2]
```

This "late binding" gotcha is the single most-asked closure trap — nail it.
