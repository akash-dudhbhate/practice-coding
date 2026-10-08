# 01 — Python type hints vs TypeScript types: what's enforced at runtime?

> **Interview question:** "What's the difference between Python type hints and TypeScript types — and what actually gets enforced at runtime?"
> **What the interviewer is really testing:** Do you understand that *neither* system checks types while the program runs — and do you know what to do about it at trust boundaries?

## Theory — what it is

**TypeScript types** are annotations you write in `.ts` files (e.g. `age: number`). The TypeScript compiler (`tsc`) checks them when you build, then **erases them completely** — the emitted `.js` file has zero type information. Once your code runs in Node or a browser, `age: number` is just a comment that no longer exists. This is called **type erasure**.

**Python type hints** are annotations like `def greet(name: str) -> str`. CPython (the standard Python interpreter) **ignores them entirely at runtime** — you can pass an `int` where a `str` is hinted and nothing complains. They're stored in `__annotations__` for tools to read, but nothing enforces them by default. A separate static checker (`mypy`, `pyright`) reads the hints and reports violations before you run the code.

So the punchline is the same on both sides: **static types are a pre-flight check, not a seatbelt.** They catch bugs at compile/lint time. At runtime, data from outside your program (HTTP bodies, env vars, JSON files, user input) is untyped — and that's where you need *runtime validation* (pydantic in Python, zod in TypeScript).

## Why it was needed

Without static types, a typo like `user.adress` or passing a `string` where a `number` was expected only blows up in production — or worse, silently produces `NaN` / wrong output. Type systems move those failures to development time, where they're cheap.

But static types can't verify data that doesn't exist yet at compile time — like the JSON a client POSTs to your API. If you `JSON.parse(body)` and cast it, TypeScript happily believes your lie; Python doesn't even check. The boundary between "untrusted outside world" and "my typed program" needs real, executable validation — that's the gap runtime validators fill.

## Where it's used in a real project

1. **API boundary validation** — parse request bodies with pydantic `BaseModel` (FastAPI does this automatically) or `zodSchema.parse(req.body)` in Express/Nest.
2. **Config loading** — validate `process.env` / `os.environ` at startup so the app crashes fast with a clear message instead of mysteriously failing later.
3. **Internal code safety** — mypy/pyright in CI for Python; `tsc --noEmit` in CI for TypeScript. Types also power autocomplete and safe refactors in the editor.
4. **Sharing types across the stack** — generate TypeScript types from pydantic models (or vice versa via OpenAPI) so the frontend and backend can't drift apart.

## Diagram

```
                    WRITE TIME                     RUNTIME
                ┌──────────────────┐        ┌──────────────────────┐
 TypeScript     │ tsc checks types │  ───▶  │ types ERASED         │
                │ then strips them │        │ pure JS, no checks   │
                └──────────────────┘        └──────────────────────┘
                ┌──────────────────┐        ┌──────────────────────┐
 Python         │ mypy/pyright     │  ───▶  │ interpreter IGNORES  │
                │ check hints      │        │ hints; runs anyway   │
                └──────────────────┘        └──────────────────────┘

   Untrusted data enters ──▶ runtime validator parses it ──▶ typed object
                            (pydantic / zod)      or it throws
```

## Code — explained

```python
# ---------- PYTHON ----------
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)          # fine
add("1", "2")      # mypy flags this... but Python RUNS it and returns "12"!
                   # hints are ignored at runtime.

# Runtime enforcement needs a validator:
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

User.model_validate({"name": "Ada", "age": "36"})   # OK — "36" coerced to 36
User.model_validate({"name": "Ada", "age": "xyz"})  # raises ValidationError NOW
```

```typescript
// ---------- TYPESCRIPT ----------
function add(a: number, b: number): number {
  return a + b;
}
add("1", "2"); // tsc errors at compile time — this file won't even build.

// But at runtime, types are gone:
const body: { age: number } = JSON.parse('{"age":"abc"}'); // tsc trusts the cast
console.log(body.age + 1); // runtime: "abc1" — no error, silent corruption

// Runtime enforcement needs a validator:
import { z } from "zod";
const User = z.object({ name: z.string(), age: z.number() });
User.parse({ name: "Ada", age: 36 });       // OK
User.parse({ name: "Ada", age: "abc" });    // throws ZodError NOW
```

Key point for the interview: `as { age: number }` in TS and `x: int` in Python are both *claims*, not *checks*. Only a runtime validator turns a claim into a guarantee.

## Problems

### Easy — Spot the runtime lie
**Problem:** This TypeScript compiles fine. What does it print, and why?

```typescript
const n = "42" as unknown as number;
console.log(n + 1);
```

**Try this input:** run it after `tsc` compiles it.
**Expected output:** `421` (string concatenation — `n` is still the string `"42"` at runtime).
**Solution:**

```typescript
const n = Number("42"); // actually convert, don't just assert
console.log(n + 1);     // 43
```

**Logic explained:**
1. `as number` is erased at compile time — it's a promise to the compiler, not a conversion.
2. At runtime `n` holds `"42"`, so `+ 1` does string concatenation.
3. `Number()` performs a real conversion that exists at runtime.

### Medium — Find every unsafe boundary
**Problem:** Review this FastAPI-adjacent Python snippet and list every place a bad type can slip through at runtime despite correct-looking hints.

```python
import json, os

def discount(price: float, pct: float) -> float:
    return price * (1 - pct / 100)

payload = json.loads('{"price": "19.99", "pct": 10}')
workers = int(os.environ.get("WORKERS", "4"))
print(discount(payload["price"], payload["pct"]))
```

**Try this input:** the JSON shown, `WORKERS=abc`.
**Expected output:** `discount` returns `"19.9919.99..."`-style garbage or raises; `int("abc")` raises `ValueError`.
**Solution:**

```python
from pydantic import BaseModel

class Payload(BaseModel):
    price: float
    pct: float

p = Payload.model_validate(json.loads(raw))  # coerces "19.99" -> 19.99
print(discount(p.price, p.pct))              # 17.991
```

**Logic explained:**
1. `json.loads` returns `dict[str, Any]` — hints on `discount` never see the actual values.
2. `"19.99"` is a `str`; `str * float` inside the formula misbehaves (string repetition/`TypeError` depending on op order).
3. Env vars are always strings — `int()` is runtime conversion, and it raises on `"abc"`.
4. pydantic validates AND coerces at the boundary, so `discount` receives real floats.

### Hard — Prove the guarantee
**Problem:** You're designing a TypeScript API handler. Write a function `parseOrder(raw: unknown)` that returns a *fully trusted* `Order` type or throws — such that no `as` cast is needed and the compiler can prove the shape. Show the equivalent in Python.

**Try this input:** `parseOrder({id: "o1", total: "12.5"})` and `parseOrder({id: 7})`.
**Expected output:** first throws (or you add `.coerce.number()` to accept it), second throws — both with clear errors.
**Solution:**

```typescript
import { z } from "zod";

const OrderSchema = z.object({
  id: z.string(),
  total: z.number().positive(),
});
type Order = z.infer<typeof OrderSchema>; // TS type DERIVED from the schema

function parseOrder(raw: unknown): Order {
  return OrderSchema.parse(raw); // returns a REAL Order — no `as` needed
}
```

```python
from pydantic import BaseModel, PositiveFloat

class Order(BaseModel):
    id: str
    total: PositiveFloat

def parse_order(raw: dict) -> Order:
    return Order.model_validate(raw)  # returns a REAL Order
```

**Logic explained:**
1. Accept `unknown` / `dict` — never trust the caller's claimed shape.
2. Define the schema once; derive the static type *from* it (`z.infer`, pydantic model) so they can't drift.
3. `.parse()` / `.model_validate()` returns a value the type system knows is an `Order` — the runtime check produces the compile-time guarantee.
4. This is the "parse, don't validate/assert" pattern — the strongest possible answer to "what's enforced at runtime."

## The 30-second interview answer

"Neither is enforced at runtime. TypeScript erases every type when it compiles to JavaScript, and Python's interpreter ignores hints — they're only checked by separate tools: `tsc`/`eslint` for TS, `mypy`/`pyright` for Python, before the code runs. That means static types catch internal bugs, but anything entering from outside — request bodies, env vars, files — is untyped. So at every trust boundary I validate at runtime: pydantic in Python, zod in TypeScript. The ideal pattern is 'parse, don't validate': the validator returns a value whose type is derived from the schema, so the runtime check produces the compile-time guarantee — no `as` casts, no lying to the compiler."

## Follow-up trap

"So if types are erased, how do you share types between your Python backend and TypeScript frontend?" — Strong answer: generate them from one source of truth. Either define pydantic models and emit an OpenAPI schema, then generate TS types from it (`openapi-typescript`), or define zod schemas in a shared package. The point: never hand-maintain two copies — they will drift.
