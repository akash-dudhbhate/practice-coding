# 06 — `*args` / `**kwargs` and parameter ordering rules

> **Interview question:** "What do `*args` and `**kwargs` do, and what are the rules for ordering parameters in a function signature?"
> **What the interviewer is really testing:** Whether you know positional vs keyword arguments, how `*`/`**` pack and unpack them, the mandatory signature ordering — and the keyword-only trap hiding after `*args`.

## Theory — what it is

A function call has **two kinds of arguments**:

- **positional** — matched to parameters by position: `f(1, 2)`
- **keyword** — matched by name: `f(a=1, b=2)`

Inside a signature, `*` and `**` are **packing** operators — they collect leftovers:

- `*args` — "collect every extra **positional** argument into a **tuple**"
- `**kwargs` — "collect every extra **keyword** argument into a **dict**"

The names are pure convention — `*rest`, `**opts` work identically; `*`/`**` are the actual syntax. `args` is always a `tuple`, `kwargs` always a `dict` (empty when nothing extra was passed — never `None`).

**Ordering rules in a `def`** — parameters must appear in this order:

```python
def f(a, b=0, *args, c, **kwargs): ...
#     |  |      |     |    |
#     |  |      |     |    +-- leftover keyword args   (must be LAST)
#     |  |      |     +------- keyword-only params     (after *args)
#     |  |      +------------- leftover positionals -> tuple
#     |  +-------------------- normal param with default
#     +----------------------- normal positional param
```

- Everything after `*args` is **keyword-only** — `c` can *only* be passed by name; `f(1, 2, 3)` can't fill `c` positionally → `TypeError`.
- A bare `*` with no name — `def f(a, *, b)` — means "no `*args` collected, but `b` is keyword-only."
- Only one `*args` and one `**kwargs`; `**kwargs` must be last — `def f(**kw, *a)` is a `SyntaxError`.

**At the call site** the same operators do the opposite — they **unpack** (spread):

```python
f(*[1, 2, 3])      # same as f(1, 2, 3)   — iterable -> positional args
f(**{"a": 1})      # same as f(a=1)       — mapping  -> keyword args
```

Call-site rule: a positional argument can't follow a keyword argument — `f(a=1, 2)` is a `SyntaxError`. Since Python 3.5 multiple unpackings can interleave (`f(*x, *y, **d1, **d2)` is legal), but the readable order is always: positionals → `*unpacking` → keywords → `**unpacking`.

## Why it was needed

- **Variable arity:** `print(*values)`, `str.format(*args)`, `logging.info("x=%s", x)` accept any number of arguments — impossible with a fixed signature.
- **Argument forwarding:** a wrapper that must accept *any* signature and pass it through untouched — `def wrapper(*args, **kwargs): return f(*args, **kwargs)`. This is THE reason decorators (file 16) work generically.
- **Optional config as dicts:** `requests.get(url, **options)` — callers pass a dict of options instead of the function enumerating every parameter.
- **Keyword-only params:** force self-documenting calls (`timeout=5` beats a bare `5`) and let you add parameters later without breaking existing positional callers.

## Where it's used in a real project

- **Every decorator wrapper:** `def wrapper(*args, **kwargs): return f(*args, **kwargs)` — forwards any signature.
- **Cooperative `super()`:** `def __init__(self, *args, **kwargs): super().__init__(*args, **kwargs)` — forwards unknown args up the MRO chain (file 25).
- **Config merging:** `dict(**defaults, **overrides)` — later dict wins on key clashes.
- **API clients:** `requests.get(url, **kw)`, `subprocess.run(cmd, **opts)` — passthrough options.
- **Builtins:** `print(*values, sep=" ", end="\n")` — `sep`/`end` are keyword-only after `*values`.

## Diagram

```
SIGNATURE (packing):  call args -> parameter slots

  f(1, 2, 3, 4, c=5, x=6)
   |  |  |  |  |    |
   |  |  +--+  |    +--> kwargs = {'x': 6}
   |  |     |  +-------> c = 5          (keyword-only)
   |  |     +----------> args = (3, 4)  (tuple of leftover positionals)
   |  +----------------> b = 2
   +-------------------> a = 1

  def f(a, b=0, *args, c, **kwargs)     <- required order:
     positional -> *args -> keyword-only -> **kwargs

CALL SITE (unpacking):  collections -> call args

  f(*[1, 2], **{"c": 5})   ==   f(1, 2, c=5)
```

## Code — explained

```python
def f(a, b=0, *args, c, **kwargs):
    print(a, b, args, c, kwargs)

f(1, 2, 3, 4, c=5, x=6)     # 1 2 (3, 4) 5 {'x': 6}
# f(1, 2, 3, 4, 5)          # TypeError — c is keyword-only, no positional slot
# f(1, c=5, anything=9)     # works — 'anything' lands in kwargs

# unpacking at the call site:
def add3(x, y, z):
    return x + y + z

nums = [1, 2, 3]
print(add3(*nums))          # 6 — same as add3(1, 2, 3)

opts = {"sep": "-", "end": "!"}
print(1, 2, 3, **opts)      # 1-2-3! — dict spread as keyword args

# bare * makes params keyword-only without collecting *args:
def greet(name, *, excited=False):
    return f"hi {name}{'!' if excited else '.'}"

print(greet("sam"))                # hi sam.
print(greet("sam", excited=True))  # hi sam!
# greet("sam", True)               # TypeError — excited must be passed by name
```

1. `f(1, 2, 3, 4, c=5, x=6)` — `a`/`b` take the first two positionals; `3, 4` overflow into the `args` tuple; `c=5` fills the keyword-only param; `x=6` has no param so it lands in `kwargs`.
2. `f(1, 2, 3, 4, 5)` fails — once `*args` appears, `c` can only be bound by name. This is the #1 surprise with the ordering rule.
3. `add3(*nums)` — `*` at the *call site* spreads the list into three positional arguments. Packing in `def`, unpacking in calls — same symbol, opposite directions.
4. `print(1, 2, 3, **opts)` — `**` spreads a dict into keyword arguments; `sep`/`end` reach `print`'s keyword-only params.
5. `greet(name, *, excited=False)` — the bare `*` collects nothing but still forces `excited` to be keyword-only; `greet("sam", True)` is a `TypeError`.

## Problems

### Easy — `total(*nums)`
**Problem:** Write `total` that accepts any number of numeric arguments and returns their sum — including zero arguments.
**Try this input:** `total(1, 2, 3)`, `total()`, `total(5)`
**Expected output:** `6 0 5`
**Solution:**
```python
def total(*nums):          # nums is a tuple of ALL positionals
    return sum(nums)       # sum(()) is 0 — no special case needed

print(total(1, 2, 3), total(), total(5))   # 6 0 5
```
**Logic explained:**
1. `*nums` packs however many positionals arrive into one tuple.
2. With no arguments, `nums` is `()` and `sum(())` is `0` — the empty case falls out for free.
3. `total(5)` gives `nums = (5,)` — a one-element tuple, still summed correctly.

### Medium — force keyword-only arguments
**Problem:** `send(msg, retries, urgent)` is being called as `send("hi", 3, True)` — unreadable and fragile. Rewrite it so `retries` and `urgent` have defaults and can *only* be passed by name.
**Try this input:** `send("hi")`, `send("hi", retries=3, urgent=True)`, and confirm `send("hi", 3)` fails.
**Expected output:** `('hi', 0, False)` then `('hi', 3, True)`; the positional call raises `TypeError`.
**Solution:**
```python
def send(msg, *, retries=0, urgent=False):
    return msg, retries, urgent

print(send("hi"))                          # ('hi', 0, False)
print(send("hi", retries=3, urgent=True))  # ('hi', 3, True)
# send("hi", 3)                            # TypeError: takes 1 positional
```
**Logic explained:**
1. The bare `*` ends the positional zone — nothing after it accepts a positional argument.
2. `send("hi", 3)` raises `TypeError: send() takes 1 positional argument but 2 were given` — exactly the readability guard we wanted.
3. Defaults still apply — callers may pass zero, one, or both keyword args.
4. This is why `print(*values, sep=..., end=...)` can't be mis-called: `print("a", "b", "-")` joins values, never sets `sep`.

### Hard — `dispatch(cmd, *args, **kwargs)`
**Problem:** Implement a command dispatcher: `dispatch(cmd, *args, **kwargs)` looks up `cmd` in a handler table and forwards *all* remaining arguments to it — both positionals and keywords.
**Try this input:** `dispatch("add", 2, 3)`, `dispatch("greet")`, `dispatch("greet", name="sam")`
**Expected output:** `5` / `hi stranger` / `hi sam`
**Solution:**
```python
HANDLERS = {
    "add": lambda a, b: a + b,
    "greet": lambda name="stranger": f"hi {name}",
}

def dispatch(cmd, *args, **kwargs):
    return HANDLERS[cmd](*args, **kwargs)   # pack here, unpack there

print(dispatch("add", 2, 3))           # 5
print(dispatch("greet"))               # hi stranger
print(dispatch("greet", name="sam"))   # hi sam
```
**Logic explained:**
1. `dispatch` packs everything after `cmd` into `args`/`kwargs` — it doesn't need to know each handler's signature.
2. `HANDLERS[cmd](*args, **kwargs)` *unpacks* them back into the call — pack on the way in, unpack on the way out. This is the full `*args`/`**kwargs` round-trip.
3. `"add"` gets `(2, 3)` positionally; `"greet"` gets `()` → default `"stranger"`; `"greet", name="sam"` arrives via `kwargs`.
4. This is the same pattern decorators, `super().__init__`, and API wrappers use — an intermediary that forwards a signature it doesn't own.

## The 30-second interview answer

"`*args` collects leftover positional arguments into a tuple, `**kwargs` collects leftover keyword arguments into a dict — the names are convention, the `*`/`**` are the syntax. In a signature the order is fixed: normal parameters, then `*args`, then keyword-only parameters, then `**kwargs` last — anything after `*args` or a bare `*` is keyword-only and can't be passed positionally. At call sites the same operators do the reverse: `f(*list)` spreads a list into positionals and `f(**dict)` spreads a dict into keywords. The big use is forwarding — decorators and `super().__init__` accept any signature with `*args, **kwargs` and pass it straight through."

## Follow-up trap

**"What breaks if you put `**kwargs` before `*args`, or parameters after `**kwargs`?"** — both are `SyntaxError` at compile time; `**kwargs` must be last because it swallows every remaining keyword argument. Second trap: *"If `def f(a, **kwargs)` is called as `f(**{'a': 1, 'b': 2})`, where does `a` go?"* — `a=1` binds the named parameter first; only the *leftover* `{'b': 2}` lands in `kwargs`. Third: *"`def f(*args, *more)`?"* — `SyntaxError`, only one `*args` allowed. And the sneaky one: *"Is `f(b=1, *[2])` legal?"* — yes, since Python 3.5 unpacking order is flexible, though `f(2, b=1)`-style readability should be your guide.
