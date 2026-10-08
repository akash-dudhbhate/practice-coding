# 17 — `functools.wraps`: why it exists and what breaks without it

> **Interview question:** "Why do decorators always have `@functools.wraps(f)` on the wrapper — what breaks if you leave it off?"
> **What the interviewer is really testing:** Whether you understand that decorating *replaces* the function — so the wrapper must borrow the original's identity (`__name__`, `__doc__`, signature) or introspection, docs, and frameworks break.

## Theory — what it is

`@deco` means `f = deco(f)` — the name `f` ends up pointing at **`wrapper`**, a brand-new function object. `wrapper` has its own metadata: `__name__` is `"wrapper"`, `__doc__` is whatever docstring `wrapper` has (usually `None`), `__module__` is the decorator's module, and `inspect.signature` shows `(*args, **kwargs)` — the wrapper's generic signature.

`@functools.wraps(f)` is a decorator you put **on the wrapper** that copies the original's identity onto it:

- `__name__`, `__qualname__`, `__doc__`, `__module__`, `__annotations__` — copied over
- `__dict__` — merged (wrapper's attributes updated with `f`'s)
- `__wrapped__` — set to `f`, a pointer back to the original; `inspect.signature` and `inspect.unwrap` follow it to reveal the *real* signature

Under the hood `wraps` is just `partial(update_wrapper, f)` — `update_wrapper(wrapper, f)` does the attribute copying.

**What breaks without it:**

- `help(f)` / `f.__doc__` → shows the wrapper's docs (usually nothing)
- `f.__name__` → `"wrapper"` for *every* decorated function — wrong names in logs, tracebacks, profilers
- `inspect.signature(f)` → `(*args, **kwargs)` — the true signature is hidden
- **Frameworks that key on function identity** — Flask registers routes under `view_func.__name__`; two decorated views both become `"wrapper"` → `AssertionError: View function mapping is overwriting an existing endpoint function`
- Sphinx autodoc, CLI generators, `functools.singledispatch`-style registries — all read the wrong metadata

## Why it was needed

Decorators exist to wrap functions transparently — the decorated function should look and behave like the original to *both callers and tools*. But so much of Python tooling is built on introspection — `help()`, `inspect.signature`, logging `f.__name__`, doc generators, web frameworks registering endpoints by name — that an opaque `wrapper` breaks the transparency. `wraps` is the standard, one-line fix: preserve the identity, hide the plumbing.

## Where it's used in a real project

- **Flask/FastAPI routes:** `app.route` defaults the endpoint name to `view_func.__name__` — without `wraps`, your second decorated view collides with the first (`"...overwriting an existing endpoint function: wrapper"`).
- **Introspection-driven frameworks:** FastAPI, `typer`, DI containers read `inspect.signature` to build dependencies/CLI args — `wraps` (via `__wrapped__`) is what keeps the real params visible.
- **Logging/tracing decorators:** `log.info("%s called", f.__name__)` prints the right name only because `wraps` preserved it on the wrapper.
- **pytest & test tooling:** fixture/report names, `inspect.unwrap` to reach the original under test.
- **Documentation:** Sphinx autodoc pulls `__doc__`/`__name__` — unwrapped decorators produce docs full of functions called "wrapper".

## Diagram

```
@logged                      WITHOUT wraps              WITH wraps
def add(a, b):               add -> wrapper             add -> wrapper
    """Add numbers."""       __name__   "wrapper"       __name__   "add"
                             __doc__    None            __doc__    "Add numbers."
                             signature  (*args, **kw)   signature  (a, b)
                                                        __wrapped__ -> real add

   Flask registers by __name__: two decorated views -> BOTH "wrapper" -> COLLISION
```

## Code — explained

```python
import functools, inspect

def logged_bad(f):                       # no wraps
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

def logged_good(f):
    @functools.wraps(f)                  # copy f's identity onto wrapper
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@logged_bad
def add(a, b):
    """Add two numbers."""
    return a + b

print(add.__name__)            # wrapper      <- identity lost
print(add.__doc__)             # None         <- docstring lost
print(inspect.signature(add))  # (*args, **kwargs) <- real params hidden

@logged_good
def mul(a, b):
    """Multiply two numbers."""
    return a * b

print(mul.__name__)            # mul                    <- preserved
print(mul.__doc__)             # Multiply two numbers.  <- preserved
print(inspect.signature(mul))  # (a, b)    <- signature() follows __wrapped__
print(mul.__wrapped__(2, 3))   # 6         <- original still reachable
```

1. `add` points at `wrapper` — so `__name__`, `__doc__`, and the signature all describe `wrapper`, not `add`. `help(add)` is useless; logs say "wrapper called."
2. `@functools.wraps(f)` on `wrapper` copies `f`'s metadata — `mul.__name__` is `"mul"`, docstring intact.
3. `wraps` also sets `mul.__wrapped__ = f` — `inspect.signature` follows it and reports `(a, b)`, not `(*args, **kwargs)`. This is how introspection tools "see through" the decoration.
4. `mul.__wrapped__(2, 3)` calls the original directly — handy for tests that want the unwrapped function.

## Problems

### Easy — predict the lost metadata
**Problem:** Without running it, predict what `__name__` and `__doc__` print for this decorated function.
**Try this input:**
```python
def trace(f):
    def wrapper(*a, **k):
        return f(*a, **k)
    return wrapper

@trace
def double(x):
    """Doubles x."""
    return x * 2

print(double.__name__, double.__doc__)
```
**Expected output:** `wrapper None`
**Solution:**
```python
def trace(f):
    def wrapper(*a, **k):
        return f(*a, **k)
    return wrapper

@trace
def double(x):
    """Doubles x."""
    return x * 2

print(double.__name__, double.__doc__)   # wrapper None
```
**Logic explained:**
1. `@trace` makes `double = trace(double)` → `double` is the `wrapper` function object.
2. `wrapper.__name__` is `"wrapper"` and `wrapper.__doc__` is `None` (no docstring written) — so those print.
3. The function still *works* — `double(4)` returns `8` — only its identity is wrong. That's what makes the bug sneaky.

### Medium — fix the decorator and prove it
**Problem:** Fix `trace` so the decorated function keeps its name, docstring, and signature. Prove all three.
**Try this input:** decorate `double(x)` and print `__name__`, `__doc__`, `inspect.signature(double)`.
**Expected output:** `double` / `Doubles x.` / `(x)`
**Solution:**
```python
import functools, inspect

def trace(f):
    @functools.wraps(f)
    def wrapper(*a, **k):
        return f(*a, **k)
    return wrapper

@trace
def double(x):
    """Doubles x."""
    return x * 2

print(double.__name__)            # double
print(double.__doc__)             # Doubles x.
print(inspect.signature(double))  # (x)
```
**Logic explained:**
1. `functools.wraps(f)` copies `__name__`, `__doc__`, `__module__`, `__qualname__`, `__annotations__` and updates `__dict__` — the wrapper now *wears* `f`'s identity.
2. `__wrapped__` is set to the original — `inspect.signature` follows it, so `(x)` shows instead of `(*a, **k)`.
3. Placement matters: `wraps` decorates `wrapper`, taking `f` as its argument — `@functools.wraps(f)` inside `trace`, not on `trace` itself.

### Hard — the Flask route collision
**Problem:** This mini router registers each decorated view under `wrapper.__name__` — the Flask default endpoint behavior. Register two views and watch it blow up; then fix the decorator with `wraps`.
**Try this input:** decorate `home()` and `about()` with `@route("/")` / `@route("/about")`.
**Expected output (fixed):** `{'/': 'home', '/about': 'about'}`
**Solution:**
```python
import functools

routes = {}

def route(path):
    def deco(f):
        @functools.wraps(f)          # without this, endpoint is "wrapper" for ALL views
        def wrapper(*a, **k):
            return f(*a, **k)
        endpoint = wrapper.__name__          # Flask's default endpoint
        if endpoint in routes.values():
            raise AssertionError(f"overwriting endpoint: {endpoint}")
        routes[path] = endpoint
        return wrapper
    return deco

@route("/")
def home():
    return "home page"

@route("/about")
def about():
    return "about page"

print(routes)   # {'/': 'home', '/about': 'about'}
```
**Logic explained:**
1. Without `wraps`, `wrapper.__name__` is `"wrapper"` for *both* views — the second registration sees `"wrapper"` already in `routes.values()` and raises `AssertionError` — verbatim what Flask does (`"View function mapping is overwriting an existing endpoint function"`).
2. With `wraps`, each wrapper keeps its own function's name: `home` and `about` register cleanly.
3. This is the concrete reason `wraps` is non-optional in framework-facing decorators — the decorator doesn't just hide a docstring, it breaks name-keyed registration.
4. Debugging tip when you see this in the wild: the fix is one line — `@functools.wraps(f)` on the inner wrapper — not renaming your views.

## The 30-second interview answer

"Decorating replaces the function — `@deco` makes the name point at `wrapper`, so without help the decorated function reports `__name__` as `'wrapper'`, loses its docstring, and `inspect.signature` shows `(*args, **kwargs)` instead of the real parameters. `functools.wraps(f)` copies `__name__`, `__doc__`, `__module__`, `__qualname__`, `__annotations__`, and `__dict__` onto the wrapper, and sets `__wrapped__` back to the original — which is what lets `signature` and `inspect.unwrap` see through it. What breaks without it: `help()`, logging, Sphinx docs — and real frameworks: Flask registers views by `__name__`, so two decorated endpoints both become `'wrapper'` and the second raises 'overwriting an existing endpoint function.' It's one line — always add it."

## Follow-up trap

**"Does `wraps` fix `inspect.signature` too — or just `__name__`/`__doc__`?"** — yes, via `__wrapped__`: `wraps` stores a pointer to the original, and `inspect.signature`/`inspect.unwrap` follow the chain. Without `__wrapped__`, signature sees only `(*args, **kwargs)`. Second trap: *"What happens with stacked decorators?"* — every layer needs `wraps`; one naked layer in the middle hides everything below it (the outer `wraps` copies the *inner wrapper's* metadata, which is already lost). Third: *"Can you reach the original function?"* — `f.__wrapped__` gives it to you directly — useful for unit-testing the undecorated logic. Bonus: `wraps` is `partial(update_wrapper, f)` — knowing `update_wrapper(wrapper, wrapped)` exists is the deeper answer.
