# 40 — Typed errors — `catch (e: unknown)`, narrowing, and the Result pattern

> **Interview question:** "How do you handle errors in TypeScript — what type is the `catch` variable, and how do you get a typed error out of it?"
> **What the interviewer is really testing:** Whether you know `catch (e)` gives `unknown` under `strict` (because JS can throw *anything*), that `instanceof` is the narrowing tool — and whether you've seen the alternative: making errors part of the return type with a `Result<T, E>` union.

## Theory — what it is

In JavaScript, `throw` accepts anything: `throw "oops"`, `throw 42`, `throw null`, `throw new Error("x")` — all legal. So TypeScript honestly types the catch variable as **`unknown`** (since TS 4.4's `useUnknownInCatchVariables`, enabled by `strict`). Before that — or with the flag off — `e` was `any`, and `e.message` compiled even when someone threw a bare string.

Because `e: unknown`, you can't touch it until you **narrow**:

```typescript
catch (e) {
  if (e instanceof Error) console.log(e.message);   // safe: e is Error here
}
```

Three narrowing tools, in order of usefulness:

1. **`instanceof Error`** — the 90% case. Covers `TypeError`, `RangeError`, and your own `class HttpError extends Error`.
2. **Custom error classes** — `class NotFoundError extends Error { constructor(public id: string) { super(`not found: ${id}`); } }` — then `e instanceof NotFoundError` narrows *and* unlocks `e.id`.
3. **Manual shape checks** for non-Error throws (strings, Axios-style objects): `typeof e === "string"`, or `"message" in e`-style guards.

The bigger idea interviewers probe: **exceptions are invisible in the type signature.** `function getUser(): User` doesn't tell callers it throws. The **Result pattern** fixes that by returning errors as data:

```typescript
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };
```

Now `function getUser(): Result<User, NotFoundError>` *advertises* failure, and `if (r.ok)` narrows cleanly because `ok` is a discriminant.

## Why it was needed

Two distinct problems, two fixes:

1. **`catch (e: any)` lied.** JS lets you throw anything, but `any` let you write `e.response.data.message` with zero checking — a thrown string crashes your error handler itself. `unknown` forces you to *prove* the shape before reading it.
2. **Thrown errors don't appear in signatures.** Callers of `parseConfig()` can't see it throws `SyntaxError`; they find out in production. Result types make failure a first-class, checkable part of the contract — the same reason Rust has `Result<T, E>` and Go returns `(value, err)`.

## Where it's used in a real project

- **API layers:** `catch (e)` → `if (e instanceof HttpError) toast(e.status)` → else `throw e` (rethrow what you can't handle).
- **Domain errors:** `NotFoundError`, `ValidationError`, `AuthError` classes — `instanceof` dispatches to the right UI response.
- **Parsing/validation:** `Result<Config, string>` from `loadConfig()` instead of try/catch sprinkled through startup code.
- **Libraries:** `neverthrow`, `ts-results` wrap this pattern; Effect-TS builds a whole ecosystem on typed error channels.

## Diagram

```
throw side:                        catch side:
  throw "oops"        ─┐
  throw 42             │   catch (e)   e: unknown  (honest!)
  throw new HttpError ─┘        │
                                v
                     ┌── instanceof Error ──┐
                     │ yes                  │ no
                     v                      v
               e: Error              typeof e === "string"?
               e.message OK          e: string ...
                     │
        instanceof HttpError ──> e.status, e.body

Result<T,E> — errors as return values:
  getUser(id) -> { ok: true, value: User } | { ok: false, error: NotFoundError }
                      │ if (r.ok)
              ┌───────┴────────┐
           r.value: T      r.error: E      <- narrowing via discriminant
```

## Code — explained

```typescript
// 1. catch is `unknown` under strict — narrow before touching
class HttpError extends Error {
  constructor(public status: number, message: string) {
    super(message);
    this.name = "HttpError";
  }
}

function showError(e: unknown): void {
  if (e instanceof HttpError) {
    console.log(`HTTP ${e.status}: ${e.message}`);   // HttpError members visible
  } else if (e instanceof Error) {
    console.log(`Error: ${e.message}`);              // plain Error
  } else if (typeof e === "string") {
    console.log(`thrown string: ${e}`);              // legacy throw "x"
  } else {
    console.log("non-error thrown:", e);             // 42, null, objects...
  }
}

try { throw new HttpError(404, "user gone"); }        catch (e) { showError(e); }
try { throw "oops"; }                                 catch (e) { showError(e); }
try { (null as unknown as { x: number }).x; }         catch (e) { showError(e); }
// HTTP 404: user gone
// thrown string: oops
// Error: Cannot read properties of null (reading 'x')

// 2. Result pattern — error is part of the return type
type Result<T, E = Error> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function divide(a: number, b: number): Result<number, string> {
  if (b === 0) return { ok: false, error: "divide by zero" };
  return { ok: true, value: a / b };
}

const r = divide(10, 0);
if (r.ok) console.log(r.value);          // narrowed: r.value exists
else console.log("failed:", r.error);    // failed: divide by zero
```

1. `catch (e)` under `strict` is `unknown` — the three `if` branches narrow it: `instanceof` for classes, `typeof` for primitives, a fallback for everything else.
2. Order matters in the `if` chain: `HttpError` check comes **before** `Error`, since `HttpError instanceof Error` is also true — most specific first.
3. `this.name = "HttpError"` fixes `.name` (minification/prototype quirks can otherwise make `e.name` say `"Error"`).
4. `Result<T, E>` is a **discriminated union** — `ok` is the tag, so `if (r.ok)` gives you `value` and nothing else; `r.error` doesn't even compile on the success branch.
5. `divide` can't throw — the signature `Result<number, string>` *is* the contract. Callers are forced to handle the `!ok` case (or consciously ignore it).

## Problems

### Easy — safely log a caught error
**Problem:** Write `logCaught(e: unknown)` that prints `e.message` if it's an `Error`, `"string thrown: ..."` for strings, and `"unknown failure"` otherwise.
**Try this input:** `logCaught(new Error("boom"))`, `logCaught("oops")`, `logCaught(42)`
**Expected output:**
```
boom
string thrown: oops
unknown failure
```
**Solution:**
```typescript
function logCaught(e: unknown): void {
  if (e instanceof Error) {
    console.log(e.message);
  } else if (typeof e === "string") {
    console.log(`string thrown: ${e}`);
  } else {
    console.log("unknown failure");
  }
}

logCaught(new Error("boom"));   // boom
logCaught("oops");              // string thrown: oops
logCaught(42);                  // unknown failure
```
**Logic explained:**
1. `instanceof Error` narrows `unknown` → `Error`, unlocking `.message`.
2. `typeof e === "string"` catches the legacy `throw "string"` habit.
3. The `else` catches everything else — numbers, `null`, random objects — because `throw` accepts anything.

### Medium — dispatch on a custom error class
**Problem:** Define `ValidationError extends Error` carrying `field: string`. In a catch block, print `field failed: msg` for `ValidationError`, `other: msg` for other Errors, rethrow non-Errors.
**Try this input:** `throw new ValidationError("email", "bad format")` then `throw new TypeError("x")`
**Expected output:** `email failed: bad format` then `other: x`
**Solution:**
```typescript
class ValidationError extends Error {
  constructor(public field: string, message: string) {
    super(message);
    this.name = "ValidationError";
  }
}

function handle(e: unknown): void {
  if (e instanceof ValidationError) {
    console.log(`${e.field} failed: ${e.message}`);   // e.field available!
  } else if (e instanceof Error) {
    console.log(`other: ${e.message}`);
  } else {
    throw e;   // not ours — pass it up
  }
}

try { throw new ValidationError("email", "bad format"); } catch (e) { handle(e); }
try { throw new TypeError("x"); }                        catch (e) { handle(e); }
// email failed: bad format
// other: x
```
**Logic explained:**
1. `e instanceof ValidationError` narrows to the subclass — `e.field` compiles only inside that branch.
2. Check the *specific* class before the generic `Error` — `ValidationError` is also an `Error`, so ordering decides which branch wins.
3. `throw e` for unrecognized shapes keeps unknown failures loud instead of silently swallowing them.

### Hard — Result-returning pipeline with a combinator
**Problem:** Write `type Result<T, E>` plus `map<T, U, E>(r: Result<T, E>, f: (t: T) => U): Result<U, E>` that transforms success values and passes errors through. Then chain `parsePort("8080") -> double` where `parsePort` fails on non-numbers.
**Try this input:** `parsePort("8080")` then `parsePort("abc")`
**Expected output:** `16160` then `error: not a number: abc`
**Solution:**
```typescript
type Result<T, E = string> =
  | { ok: true; value: T }
  | { ok: false; error: E };

function map<T, U, E>(r: Result<T, E>, f: (t: T) => U): Result<U, E> {
  return r.ok ? { ok: true, value: f(r.value) } : r;
}

function parsePort(s: string): Result<number> {
  const n = Number(s);
  return Number.isNaN(n)
    ? { ok: false, error: `not a number: ${s}` }
    : { ok: true, value: n };
}

const a = map(parsePort("8080"), (p) => p * 2);
const b = map(parsePort("abc"), (p) => p * 2);

if (a.ok) console.log(a.value);          // 16160
if (!b.ok) console.log("error:", b.error);  // error: not a number: abc
```
**Logic explained:**
1. `map` is the standard Result combinator: apply `f` only on the `ok` branch, forward the error unchanged — same idea as `Array.prototype.map` but for "maybe-failed" values.
2. `r.ok ? ... : r` — on the error branch `r` is already `Result<U, E>`-compatible because the error channel `E` doesn't mention `T`. TypeScript accepts it since `{ ok: false; error: E }` is a valid `Result<U, E>` member.
3. `parsePort` never throws — `Number("abc")` gives `NaN`, which becomes `{ ok: false }`. Failure is in the signature, so callers can't forget to check `ok`.
4. This scales: `flatMap`/`andThen` lets you chain Result-returning steps (`parse -> validate -> save`) without nested `if`s — that's the `neverthrow` library's whole API.

## The 30-second interview answer

"Under `strict`, `catch (e)` is `unknown` — because JS lets you `throw` literally anything, `any` would be a lie. I narrow it: `instanceof Error` for the common case, custom subclasses like `ValidationError`/`HttpError` when I need extra fields, checking most-specific first, and `typeof e === 'string'` for legacy throws. If I can't handle it, I rethrow — never swallow. The deeper answer is that exceptions don't appear in signatures, so for errors that are part of the contract — validation, not-found — I prefer a `Result<T, E>` discriminated union: `{ ok: true; value: T } | { ok: false; error: E }`. The `ok` tag narrows cleanly, callers are forced to confront failure, and combinators like `map` let you compose without try/catch noise. Exceptions for truly exceptional paths, Results for expected failures."

## Follow-up trap

**"Why does `e instanceof Error` miss some real errors?"** Cross-realm objects (iframes, some VM contexts) and transpiled-to-ES5 custom classes can fail `instanceof` — a class extending `Error` compiled down can lose the prototype link unless you set `Object.setPrototypeOf` or target ES2015+. Also `e instanceof HttpError` won't catch a structurally-identical object `JSON.parse`d from a wire payload — `instanceof` checks prototype identity, not shape. For wire data, use a discriminant field (`e.kind === "http"`) or a user-defined guard instead. Second trap: **"`catch (e: any)` — why not just annotate?"** You can't — `catch` accepts no type annotation; the only control is the `useUnknownInCatchVariables` flag. Turning it off to get `any` back is trading honesty for convenience.
