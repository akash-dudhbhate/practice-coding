# 26 — `ReturnType`, `Parameters`, `Awaited` — extracting a function's types

> **Interview question:** "How do you get the return type or parameter types of a function you didn't write — and why would you need to?"
> **What the interviewer is really testing:** Do you know type-level `infer` extraction — and the real motive: *derive* types from implementations so they can never drift?

## Theory — what it is

Three built-in conditional types that dissect a *function type* (they work on the type, so you pair them with `typeof fn` to grab a function's type):

```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
type Parameters<T> = T extends (...args: any[]) => infer P ? P : never;
// Awaited<T> recursively unwraps Promise:
//   Awaited<Promise<User>>          = User
//   Awaited<Promise<Promise<User>>> = User
//   Awaited<User>                   = User
```

`infer` introduces a type variable inside a conditional — "if `T` is a function shape, capture its return as `R`." `Parameters` returns a **labeled tuple**: `Parameters<typeof f>` for `(a: string, b: number) => void` is `[a: string, b: number]` — index it (`[0]`) or spread it (`...args: Parameters<F>`).

Why derive instead of annotate? **Single source of truth.** If `fetchUser` returns `Promise<User>` in one file and you hand-write `User` in five others, a signature change means five stale types. `Awaited<ReturnType<typeof fetchUser>>` recomputes itself. The killer combo is a wrapper that preserves a signature:

```typescript
function wrap<F extends (...a: any[]) => any>(
  fn: F
): (...args: Parameters<F>) => ReturnType<F> { /* ... */ }
```

## Why it was needed

Libraries wrap your functions constantly — logging, memoization, retries, React HOCs, `useCallback`, instrumentation. Each wrapper needs to declare "same params in, same return out" for a function it doesn't know. Without `Parameters`/`ReturnType`, wrapper authors fall back to overload lists or `any` — and every wrapped call loses its types. `Awaited` was added (TS 4.5) because async code made `ReturnType<typeof asyncFn>` = `Promise<X>` awkward — you usually want `X`, the resolved value. These utilities turn "repeat the signature" into "extract the signature," so the type always matches the code.

## Where it's used in a real project

- `Awaited<ReturnType<typeof loader>>` — React Router / TanStack patterns: the data type a loader produces.
- `Parameters<typeof api.login>[0]` — reuse the first param type in a request builder.
- Higher-order functions: `memoize`, `withLogging`, `retry` — preserve signatures exactly.
- `ComponentProps<typeof Button>` — React's extraction utility, built on the same idea.
- `ReturnType<typeof useCustomHook>` — type a hook's result without re-declaring its shape.
- Cousins: `ConstructorParameters`, `InstanceType`, `ThisParameterType` — same trick for classes and `this`.

## Diagram

```
async function fetchUser(id: number, verbose: boolean): Promise<User>

 typeof fetchUser  →  (id: number, verbose: boolean) => Promise<User>
        │
   ┌────┴──────────────┬───────────────────┐
   ▼                   ▼                   ▼
 Parameters<…>       ReturnType<…>      Awaited<ReturnType<…>>
 [id: number,        Promise<User>      User   ← "the data type"
  verbose: boolean]                          (Promise unwrapped)

 signature-preserving wrapper template:
   (…args: Parameters<F>) => ReturnType<F>
   ────── same params ──→ same return ──→ signature survives the wrap
```

## Code — explained

```typescript
interface User { id: number; name: string }

async function fetchUser(id: number, verbose: boolean): Promise<User> {
  if (verbose) console.log("fetching", id);
  return { id, name: "Amy" };
}

// 1. Extract pieces of the signature
type FetchParams = Parameters<typeof fetchUser>;   // [id: number, verbose: boolean]
type FetchReturn = ReturnType<typeof fetchUser>;   // Promise<User>
type FetchData   = Awaited<FetchReturn>;            // User — the useful one (1)

const args: FetchParams = [1, true];                // (2) a real tuple
const u: FetchData = { id: 1, name: "Amy" };        // (3) plain User, not a promise
console.log(args[0], u.name);                       // 1 Amy

// 2. A signature-preserving wrapper — the real-world use
function withLogging<F extends (...a: any[]) => any>(
  fn: F
): (...a: Parameters<F>) => ReturnType<F> {          // (4)
  return (...a: Parameters<F>) => {
    console.log("called with", a.length, "args");
    return fn(...a);                                 // (5)
  };
}

const loggedFetch = withLogging(fetchUser);           // same signature as fetchUser
const p = loggedFetch(2, false);                      // p: Promise<User>
console.log(p instanceof Promise);                    // true
```

1. `Awaited` unwraps `Promise<User>` → `User` — the standard way to name "the data an async function yields."
2. `Parameters` returns a labeled tuple — `args[0]` is `number`; you can spread it straight into the real call.
3. `u` is just `User` — the promise machinery was compile-time; the derived type is the plain resolved shape.
4. `F extends (...a: any[]) => any` accepts any function type; the returned function re-declares identical params and return via the extractors — `loggedFetch` stays fully typed.
5. `fn(...a)` compiles because `Parameters<F>` is a tuple matching `F`'s parameter list — TS verifies spread compatibility. The `any[]` in the constraint is fine: the constraint only *matches* functions; the extractors recover the precise types.

## Problems

### Easy — Name an async function's data type
**Problem:** Given `async function loadConfig(): Promise<{ port: number }>`, declare a variable of the *resolved* type without rewriting `{ port: number }` by hand.
**Try this input:** `const c: ??? = { port: 3000 }`
**Expected output:** `console.log(c.port)` → `3000`; accessing `c.host` is a compile error.
**Solution:**
```typescript
async function loadConfig(): Promise<{ port: number }> {
  return { port: 3000 };
}

type Config = Awaited<ReturnType<typeof loadConfig>>;   // { port: number }

const c: Config = { port: 3000 };
console.log(c.port);     // 3000
// c.host;               // compile error — the derived type stays exact
```
**Logic explained:**
1. `ReturnType` gets `Promise<{ port: number }>`; `Awaited` strips the `Promise` — the standard two-step for "what does this async fn give me."
2. Change `loadConfig` to also return `host` and `Config` updates itself — zero manual sync.
3. This is the everyday pattern for typing "what an API/loader function returns" in a different file from where it's defined.

### Medium — `Parameters` for a forwarding function
**Problem:** `function search(query: string, limit: number): string[]`. Build `callSearch` that accepts the same args — without retyping them — and forwards to `search`.
**Try this input:** `callSearch("ts", 10)`
**Expected output:** `[ 'ts#10' ]`; `callSearch("ts")` and `callSearch("ts", "10")` are compile errors — the tuple checks arity *and* per-position types.
**Solution:**
```typescript
function search(query: string, limit: number): string[] {
  return [`${query}#${limit}`];
}

function callSearch(
  ...args: Parameters<typeof search>
): ReturnType<typeof search> {
  return search(...args);
}

console.log(callSearch("ts", 10));   // [ 'ts#10' ]
// callSearch("ts");                 // compile error — missing tuple element
// callSearch("ts", "10");           // compile error — second arg is number
```
**Logic explained:**
1. `...args: Parameters<typeof search>` types the rest parameter as the exact tuple — arity and per-position types are both enforced.
2. `ReturnType` keeps the output honest too — the wrapper lies about nothing.
3. Refactor `search` to take a third parameter and `callSearch` follows automatically: derived, not duplicated. This is the skeleton of every logging/retry/memoize wrapper.

### Hard — Implement `MyReturnType` and `MyAwaited` yourself
**Problem:** Write `MyReturnType<F>` and `MyAwaited<T>` (recursively unwrapping nested promises) using `infer`. Verify on `() => Promise<Promise<number>>`.
**Try this input:** `type X = MyAwaited<MyReturnType<typeof f>>` where `f: () => Promise<Promise<number>>`
**Expected output:** `X = number` — proven by `const x: X = 5` compiling and `"s"` erroring.
**Solution:**
```typescript
type MyReturnType<F> = F extends (...a: any[]) => infer R ? R : never;
type MyAwaited<T> = T extends Promise<infer U> ? MyAwaited<U> : T;
//                                               └─ recurse: Promise<Promise<n>> → n

declare const f: () => Promise<Promise<number>>;
type X = MyAwaited<MyReturnType<typeof f>>;   // number

const x: X = 5;
console.log(x + 1);        // 6 — proof X really is number
// const bad: X = "s";     // compile error — X isn't string

type NotFn = MyReturnType<string>;            // never — conditional's false branch
```
**Logic explained:**
1. `F extends (...a: any[]) => infer R` pattern-matches the function shape and captures `R`; non-functions fall through to `never` (`MyReturnType<string>` = `never`).
2. `MyAwaited` recurses: each pass peels one `Promise` layer until `T` isn't a promise — that's why `Promise<Promise<number>>` becomes `number`. (The real `Awaited` is fancier — it handles "thenables" via `PromiseLike` — but the idea is identical.)
3. `infer` is the whole trick: it names a slot inside the matched shape so you can return it.
4. `declare const f` gives a function *type* without a body — a reminder that type extraction never needs runnable code.

## The 30-second interview answer

"`ReturnType<F>` and `Parameters<F>` dissect a function type with `infer`: `ReturnType` captures the return, `Parameters` captures the parameter list as a labeled tuple you can index or spread. `Awaited<T>` recursively unwraps `Promise` — so `Awaited<ReturnType<typeof fetchUser>>` gives the `User` an async function resolves to, which is usually what you actually want. The point is derivation over duplication: wrappers declare `(...args: Parameters<F>) => ReturnType<F>` so any function keeps its exact signature through logging/memoize/retry wraps, and types derived from an implementation can never drift from it. They're implemented with conditional types — `F extends (...a: any[]) => infer R ? R : never`. Same family: `ConstructorParameters`, `InstanceType`, React's `ComponentProps`."

## Follow-up trap

**"Why does the constraint use `any[]` — doesn't that lose types?"** — no: `F extends (...a: any[]) => any` is only a *shape test*; `infer R` / `infer P` recapture the *precise* types from whatever `F` actually is. `any` in constraint position means "match all functions," not "treat as any." Second trap: **"`ReturnType` of an async function gives `Promise<X>` — how do you get `X`?"** — that's exactly `Awaited`'s job. Third: **"`Parameters` of an overloaded function?"** — you get only the *last* overload signature; extraction sees one signature, not the overload set. And **"does `Parameters` preserve optional/rest params?"** — yes, as tuple optionality and rest elements: `(a: string, b?: number) => void` extracts `[a: string, b?: number]`.
