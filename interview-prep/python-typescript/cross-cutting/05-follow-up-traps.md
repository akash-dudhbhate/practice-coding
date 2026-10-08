# 05 — The 6 classic follow-up traps

Interviewers use your own correct answer as a springboard: you define the thing, they immediately ask you to *apply* it under pressure. Each trap below has the real test, a weak answer to avoid, a strong worked answer, and how to practice.

---

## Trap 1 — "You just explained decorators... write one that takes arguments"

**What they're really testing:** Whether you understand the decorator is a *factory* — three levels of nesting — not just the `@` syntax you memorized.

**Weak answer:** Writing a two-level decorator and then bolting arguments onto it, or confusing `functools.wraps` with the mechanism. Saying "you can't pass arguments to decorators" is an instant fail — `@app.route("/x")` is exactly that.

**Strong answer:** "A decorator with arguments is a function that *returns* a decorator — one extra nesting level. `@retry(3)` calls `retry(3)` first, and that returns the actual decorator that wraps the function."

```python
import functools, time

def retry(times: int, delay: float = 0.0):
    """Level 1: takes decorator ARGUMENTS, returns a decorator."""
    def decorator(func):                       # Level 2: the decorator itself
        @functools.wraps(func)                 # preserve __name__, __doc__
        def wrapper(*args, **kwargs):          # Level 3: replaces the function
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times:
                        raise                  # last attempt: let it fail
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(times=3, delay=0.5)
def fetch(url: str) -> bytes: ...

# Equivalent without sugar: fetch = retry(3, 0.5)(fetch)
```

The one line that proves understanding: **`retry(3)(fetch)`** — the call happens once at decoration time, returning the decorator that's then applied to `fetch`.

**How to practice:** Write `retry`, `rate_limit(n_per_sec)`, and `requires_role("admin")` from memory. Then write the same thing as a class with `__call__`. Explain aloud what `@retry(3)` desugars to.

---

## Trap 2 — "any vs unknown... give a real example where `as` broke prod"

**What they're really testing:** Whether you've felt the pain — `as` is a *claim, not a check*, and it erases the compiler's ability to protect you.

**Weak answer:** "Uhh, types don't exist at runtime so a cast can be wrong." Technically true, but it shows you've only read about it, not lived it. Also weak: an example so contrived it would never happen (`"5" as number` with no source of untyped data).

**Strong answer:** Tell a boundary story — an API contract that changed silently:

```typescript
// Backend used to send: { user: { name: string } }
// Backend v2 shipped:   { user: { displayName: string } }
// Frontend kept this old line:

const res = await fetch("/api/me");
const body = await res.json();
const user = body.user as { name: string };  // compiler now trusts the lie

render(`Hello, ${user.name.toUpperCase()}`); // 💥 TypeError in prod:
                                             // cannot read toUpperCase of undefined
```

"The compiler green-lit it, tests used mocked responses shaped the old way, and it only crashed for real users. The fix is to **parse, don't assert**: a zod schema at the boundary would have thrown a `ZodError` we could map to a 4xx/5xx, instead of a `TypeError` deep in render."

```typescript
const User = z.object({ name: z.string() });
const user = User.parse(body.user); // fails loudly at the boundary, not in UI
```

Bonus line: "`as` isn't always evil — it's fine when you *know* more than the compiler, e.g. narrowing after a check — but on untrusted data it's a loaded gun."

**How to practice:** Keep a mental list of every `as` in your codebase and ask "what validates this claim?" If the answer is "nothing," that's your story. Practice narrating: input → cast → silent wrongness → crash far away.

---

## Trap 3 — "You mentioned the GIL... so how DO you speed up a CPU-bound script?"

**What they're really testing:** Whether you understand *why* threads fail for CPU-bound work — one thread holds the GIL, so pure-Python threads never run in parallel — and whether you know the real escapes.

**Weak answer:** "Use `threading` anyway" or "use async." Async/await helps *I/O-bound* work (waiting on network/disk); for CPU-bound code, one busy coroutine still starves the event loop — same single thread, same GIL.

**Strong answer:** "Move the work off the single interpreter thread — `multiprocessing`/`ProcessPoolExecutor` gives each worker its own interpreter and its own GIL, so you get real parallelism across cores."

```python
from concurrent.futures import ProcessPoolExecutor
import hashlib, time

def crack(n: int) -> str:          # CPU-bound: pure computation
    return hashlib.sha256(str(n).encode()).hexdigest()

if __name__ == "__main__":          # REQUIRED guard (spawn re-imports the module)
    nums = range(5_000_000)
    t = time.time()
    with ProcessPoolExecutor() as pool:   # one process per core
        results = list(pool.map(crack, nums, chunksize=10_000))
    print(time.time() - t)          # ~Nx faster on N cores
```

Then name the other escapes — this is where you differentiate:

1. **Vectorize into C** — NumPy/pandas release the GIL inside C loops; `np.sum(big_array)` is parallel-ish and 100x faster than a Python loop.
2. **`concurrent.futures.ThreadPoolExecutor` is fine for I/O-bound work** — the GIL is released during blocking calls, so threads *do* help there. Contrast, don't dismiss.
3. **Free-threaded Python 3.13+** (`python3.13t`, no GIL) — worth one sentence; shows you're current.
4. **Outsource** — a compiled extension (Rust/Cython) or just send the work to a queue/cluster.

Rule to quote: **threads for waiting, processes for computing.**

**How to practice:** Time the same CPU-bound function under serial / `ThreadPoolExecutor` / `ProcessPoolExecutor` and see threads ≈ serial, processes ≈ N×. Know *why* the `__main__` guard exists (spawned workers re-import the module).

---

## Trap 4 — "interface vs type... which for a public library API, and why?"

**What they're really testing:** Whether you know **declaration merging** — the one capability `interface` has that `type` doesn't — and its consumer-facing consequence.

**Weak answer:** "They're basically interchangeable, use either." That's true for internal code but misses the question's point. Also weak: "interface is faster" (technically true for the compiler, but it's a weak reason to pick it for an API).

**Strong answer:** "For a public library API, `interface` — because of **declaration merging**. If I ship an interface, consumers can augment it in their own projects; a `type` alias would be a duplicate-identifier error."

```typescript
// library ships:
export interface ClientOptions {
  baseUrl: string;
  retries?: number;
}

// a CONSUMER can extend it in their codebase — this merges, no error:
declare module "mylib" {
  interface ClientOptions {
    apiKey?: string;              // my plugin adds a field
  }
}
// vs `export type ClientOptions = {...}` -> redeclaring it = error.
```

That's how Express's `Request`, `Request`-augmentation middleware, and library plugin systems work — consumers merge `interface Request { user?: User }` to add typed fields.

Then show range — `type` is right elsewhere: "I'd still use `type` for unions (`type Status = 'a' | 'b'`), mapped/conditional types, and function signatures — interfaces can't express those. So: **interfaces for object shapes others might extend; types for everything else** — and for the compiler, interfaces also produce slightly nicer error messages and marginally better perf."

**How to practice:** Write a small lib exporting `interface Config`, then a fake consumer file that augments it via `declare module`. Try the same with `type` and watch it fail. Memorize the rule: interface = extendable contract; type = composable expression.

---

## Trap 5 — "You explained generators... write one that paginates an API until empty"

**What they're really testing:** Can you combine laziness with real-world messiness — stop conditions, `yield from`, async — instead of reciting `def gen(): yield` examples?

**Weak answer:** A generator that fetches *all pages into a list first* (defeats laziness), or one with no termination condition (infinite loop on a buggy API), or `while True` with no page-size check.

**Strong answer:** "Lazy by construction — fetch a page, yield items, only request the next page when the consumer asks for it. The stop condition: an empty page (or a short page / missing cursor, depending on the API)."

```python
import requests

def paginate(url: str, page_size: int = 100):
    """Yield items one at a time; stop when a page comes back empty."""
    page = 1
    while True:
        resp = requests.get(url, params={"page": page, "size": page_size})
        resp.raise_for_status()
        items = resp.json()["items"]
        if not items:                # empty page -> done
            return
        yield from items             # hand each item out lazily
        if len(items) < page_size:   # short page = last page (belt & suspenders)
            return
        page += 1

# Memory stays O(1) no matter how many pages exist:
for user in paginate("https://api.example.com/users"):
    process(user)
```

If they push further: "For an async client I'd make it an `async def` generator and `yield`/`async for` — same laziness, non-blocking I/O. For cursor-based APIs I'd thread `next_cursor` through instead of incrementing `page`."

```python
async def paginate_async(client, url):
    cursor = None
    while True:
        data = await client.get(url, params={"cursor": cursor})
        yield from data["items"]
        cursor = data.get("next_cursor")
        if not cursor:
            return
```

**How to practice:** Write it three ways — page-number, cursor-based, and link-header (`rel="next"`). Test against a mock that returns `[]` on page 3. Be ready for "why not just `return list`?" — answer: bounded memory + consumer can stop early without fetching everything.

---

## Trap 6 — "You used a generic... now constrain it: the arg must have an `id`"

**What they're really testing:** Whether you know `extends`/`:` bounds — and understand that constraints let you *use* properties inside the function, not just restrict callers.

**Weak answer:** Using a union of concrete types (`User | Order`) — doesn't scale and loses the link between input and output type. Or constraining but then still casting inside because you don't realize the bound makes `.id` legal.

**Strong answer:** "A bound on the type parameter — `extends` in TS, `TypeVar` bound in Python — so the compiler knows the property exists *inside* the function."

```typescript
// ---------- TypeScript ----------
interface HasId { id: string }

function byId<T extends HasId>(items: T[], id: string): T | undefined {
  return items.find((i) => i.id === id);   // .id is legal BECAUSE of the bound
}

byId([{ id: "u1", name: "Ada" }], "u1");   // OK — returns {id, name} | undefined
byId([{ name: "no id" }], "u1");           // compile error — doesn't satisfy HasId
// Note: return type is T, not HasId — you keep the FULL concrete type.
```

```python
# ---------- Python ----------
from typing import Protocol, TypeVar

class HasId(Protocol):            # structural typing: anything with .id: str
    id: str

T = TypeVar("T", bound=HasId)

def by_id(items: list[T], id_: str) -> T | None:
    return next((i for i in items if i.id == id_), None)
```

Key insight to say out loud: "The bound does double duty — it *rejects* callers without `id`, and it *lets me use* `.id` inside without a cast. And Python's `Protocol` makes it structural, like TS's default: no inheritance needed, just the right shape."

**How to practice:** Write `T extends HasId`, then `T extends keyof U` ("key must be a real key of the object"), then a generic `get<T, K extends keyof T>(obj: T, key: K)` that returns `T[K]`. That last one is the natural follow-up they'd ask next.

---

## Pattern across all six

Every trap follows the same move: **you stated a concept; they ask you to wield it.** The defense is identical too — write each worked answer from memory *before* the interview, and always end with the "why": factory-not-decorator, claim-not-check, waiting-vs-computing, merging-for-consumers, laziness-with-termination, bound-enables-usage.
