# 42 — Typing `debounce`/`throttle` while preserving the wrapped function's signature

> **Interview question:** "How do you type a `debounce` function so the debounced version has the same parameters as the original?"
> **What the interviewer is really testing:** Whether you know the trick — capture the parameter list as a **generic tuple** (`Args extends unknown[]`) and reuse it with `...args: Args`, instead of hard-coding `(…args: any[])` and losing all type safety.

## Theory — what it is

`debounce(fn, ms)` takes a function and returns a function that delays calling `fn` until `ms` after the *last* call. The untyped version throws away the signature:

```typescript
// the lazy version — Function erases the signature, anything calls it
function debounce(fn: Function, ms: number): Function {
  return fn;
}
```

The typed version captures the parameter tuple as a generic so `debounce(search, 300)` returns something callable with `search`'s exact parameters:

```typescript
function debounce<Args extends unknown[]>(
  fn: (...args: Args) => void,
  ms: number,
): (...args: Args) => void {
  let timer: ReturnType<typeof setTimeout>;
  return (...args: Args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}
```

Rules that matter:

- **`Args extends unknown[]` — the generic is the parameter *list*, captured as a tuple.** `search(q: string, limit: number)` → `Args = [string, number]` — a tuple of the params in order.
- **`...args: Args` spreads the tuple back out.** Wherever `Args` appears as a rest param, it's re-expanded to the original parameter list — same names, same types, same arity.
- **Return type is usually dropped on purpose:** debounced functions can't return `fn`'s value sensibly (the call happens later), so `(...args: Args) => void` is correct — it's a signature *minus the return*. If you need the result, use `Promise`-returning debounce or throttle (which *can* preserve the return by calling through on the leading edge).
- **`fn: (...args: Args) => void`** — the input is constrained to "any function with these params" — the generic is *inferred* from the passed function, so callers never write `Args` explicitly.
- **TS 4.7+ / generic rest params:** `extends unknown[]` (or `any[]`) is the standard constraint — it forces `Args` to be a tuple/array type, which is what makes `...args: Args` legal.
- **`this` context:** if `fn` is a method, `this` isn't captured by `Args` — you'd need `ThisParameterType`/explicit `this` handling. Worth mentioning as the edge case.

## Why it was needed

Without the generic-tuple trick, you had two bad options:

1. `debounce(fn: Function)` — return type `Function`, callable with anything, zero IntelliSense — `debounce(search, 300)(123, true)` compiles despite `search` wanting `(string, number)`.
2. Write an overload per arity — `debounce<A>(fn: (a: A) => void)`, `debounce<A,B>(fn: (a: A, b: B) => void)` — a table of overloads that stops at some arbitrary arity and still can't handle optional/rest params.

The `Args extends unknown[]` capture solves it in one signature: the parameter list becomes a *value-level* thing (a tuple) the type system can carry around. TypeScript 4.0's variadic tuple types made this clean — before that, tuple types couldn't spread generically and the overload table was the only option.

## Where it's used in a real project

- **Search-as-you-type:** `onChange={debounce(doSearch, 300)}` — the debounced handler must match the original `(e) => void` signature.
- **`lodash.debounce` typed via `@types/lodash`:** same machinery under the hood — `DebouncedFunc<T extends (...args: any) => any>`.
- **Throttle on scroll/resize:** `window.addEventListener("scroll", throttle(onScroll, 100))` — the handler signature is preserved so `e` stays typed.
- **Generic HOFs generally:** `memoize`, `once`, `retry` — the `Args extends unknown[]` capture is the standard idiom for "wrap a function without losing its signature."
- **React:** debounced callbacks passed to `onChange` need the exact handler type or JSX prop assignment fails.

## Diagram

```
search: (q: string, limit: number) => void
             │
             ▼  debounce(search, 300)
   Args inferred = [string, number]       <- whole param list as ONE tuple
             │
             ▼
   returns: (...args: [string, number]) => void
             │   ^ spread back out = same signature
             ▼
   debouncedSearch("cats", 10)   ✅ types checked
   debouncedSearch("cats")       ❌ Error: expected 2 args
   debouncedSearch(1, "x")       ❌ Error: wrong types

Compare with the lazy version:
   debounce(fn: Function, ms: number): Function
   debouncedSearch(123, true, {}, [])      ✅ compiles — silently wrong

throttle — same trick, but CAN keep the return type
(leading-edge call returns fn's actual result):
   throttle<Args, R>(fn: (...args: Args) => R, ms): (...args: Args) => R
```

## Code — explained

```typescript
// 1. The typed debounce — Args captures the param list as a tuple
function debounce<Args extends unknown[]>(
  fn: (...args: Args) => void,
  ms: number,
): (...args: Args) => void {
  let timer: ReturnType<typeof setTimeout> | undefined;
  return (...args: Args) => {                       // (2) same params out
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);      // (3) spread back in
  };
}

// 4. Inference in action — no <Args> written by the caller
function search(query: string, limit: number): void {
  console.log(`searching "${query}" (max ${limit})`);
}

const debouncedSearch = debounce(search, 300);
//    ^? (query: string, limit: number) => void — signature preserved!

debouncedSearch("cats", 10);       // ✅ correct args
// debouncedSearch("cats");         // ❌ Error: Expected 2 arguments
// debouncedSearch(1, "x");         // ❌ Error: number not assignable to string

// 5. Throttle — same Args trick, return type CAN be kept (leading edge)
function throttle<Args extends unknown[], R>(
  fn: (...args: Args) => R,
  ms: number,
): (...args: Args) => R {
  let last = 0;
  let lastResult: R;
  return (...args: Args): R => {
    const now = Date.now();
    if (now - last >= ms) {
      last = now;
      lastResult = fn(...args);
    }
    return lastResult;                               // (6) real return
  };
}

const throttledAdd = throttle((a: number, b: number) => a + b, 100);
const sum: number = throttledAdd(1, 2);   // returns number — preserved
console.log(sum);                          // 3
```

1. `Args extends unknown[]` — `Args` is constrained to be an array/tuple type. When `search` is passed, TS infers `Args = [query: string, limit: number]` — the parameter list as an ordered tuple.
2. `(...args: Args) => void` on the *returned* function — spreading the tuple back out reconstructs the exact parameter list: names, types, arity, optional markers.
3. `fn(...args)` — `args: Args` spreads back into `fn`, which requires `Args` — the tuple round-trips intact.
4. The caller never names `Args` — it's inferred from `typeof search`. The signature flows through automatically.
5. Throttle uses two generics: `Args` for params, `R` for return — throttle can return `R` because the leading call actually runs `fn` synchronously.
6. `lastResult` caches the real return — subsequent in-window calls return the previous result rather than `undefined`, keeping the `R` honest.
7. Why debounce returns `void`: the wrapped call happens in a `setTimeout`, *after* the caller's call returns — there's no synchronous value to hand back. `=> R` would be a lie.

## Problems

### Easy — debounce preserves params
**Problem:** Type `debounce` so `debounce(fn, 300)` where `fn = (s: string) => void` returns `(s: string) => void` — and calling it with a number errors.
**Try this input:** `debounce(s => console.log(s), 300)("hi")`.
**Expected output:** compiles and calls fn after 300ms; `debounced(123)` is a compile error.
**Solution:**
```typescript
function debounce<Args extends unknown[]>(
  fn: (...args: Args) => void,
  ms: number,
): (...args: Args) => void {
  let timer: ReturnType<typeof setTimeout>;
  return (...args: Args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}

const d = debounce((s: string) => console.log(s), 300);
d("hi");          // ✅
// d(123);        // Error: Argument of type 'number' is not assignable to 'string'
```
**Logic explained:**
1. `Args = [string]` inferred from the arrow function's `(s: string)` — the tuple carries the one param.
2. The returned closure's `...args: Args` is `(s: string)` — so `d(123)` fails exactly like `search(123)` would.
3. Without `Args` (e.g. `(...args: any[])`), `d(123)` would compile — the generic is what preserves the contract.

### Medium — multi-param + optional param preserved
**Problem:** `debounce` a `log(level: string, msg: string, ctx?: object)` — show that optional params stay optional and arity is enforced.
**Try this input:** `debounced("info", "hello")` (2 args — ctx omitted) and `debounced("info")` (missing msg).
**Expected output:** 2-arg call compiles and works; 1-arg call is a compile error.
**Solution:**
```typescript
function debounce<Args extends unknown[]>(
  fn: (...args: Args) => void,
  ms: number,
): (...args: Args) => void {
  let timer: ReturnType<typeof setTimeout>;
  return (...args: Args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), ms);
  };
}

const log = (level: string, msg: string, ctx?: Record<string, unknown>) => {
  console.log(`[${level}] ${msg}`, ctx ?? "");
};

const dlog = debounce(log, 100);
dlog("info", "hello");                 // ✅ ctx optional — preserved
dlog("info", "hello", { user: "u1" }); // ✅ 3 args fine
// dlog("info");                        // ❌ Error: msg required
// dlog(1, "x");                        // ❌ Error: level must be string
```
**Logic explained:**
1. `Args` inferred as `[level: string, msg: string, ctx?: ...]` — the tuple captures *optional* markers too, so `ctx` stays optional through the wrapper.
2. Tuple types preserve optionality: `[string, string, ctx?: object]` is exactly "2 required + 1 optional" — the spread brings it back faithfully.
3. This is what the `any[]` version loses: `(...args: any[])` accepts *any* arity — `dlog()` alone would compile.

### Hard — throttle preserving the return type
**Problem:** Write `throttle` that calls `fn` at most once per `ms` on the *leading* edge AND preserves `fn`'s return type — subsequent calls within the window return the last computed result, not `undefined`.
**Try this input:** `throttle((n: number) => n * 10, 1000)` called with `5` then `7` immediately.
**Expected output:** first call returns `50` (real call), second returns `50` (cached last result — fn not re-run).
**Solution:**
```typescript
function throttle<Args extends unknown[], R>(
  fn: (...args: Args) => R,
  ms: number,
): (...args: Args) => R {
  let last = -Infinity;
  let lastResult: R;
  return (...args: Args): R => {
    const now = Date.now();
    if (now - last >= ms) {
      last = now;
      lastResult = fn(...args);         // real call -> real R
    }
    return lastResult;                  // cached R for in-window calls
  };
}

const t = throttle((n: number) => n * 10, 1000);
console.log(t(5));    // 50 — leading edge: fn actually ran
console.log(t(7));    // 50 — in window: returns cached result, fn NOT run
const r: number = t(1);                  // return type is number
// const s: string = t(1);               // Error: number not assignable
```
**Logic explained:**
1. Two generics: `Args` captures params, `R` captures the return — `R` flows to the output signature `(...args: Args) => R`.
2. `lastResult: R` stores the real return value — in-window calls return the *previous* `R`, so the type `R` is always honest (never `undefined | R`).
3. `last = -Infinity` makes the first call always fire — `now - (-Inf)` exceeds any `ms`.
4. Compare debounce: `debounce` *can't* preserve `R` — the call is deferred past the point the caller needs a value. `throttle`'s leading-edge call runs synchronously, so `R` is real. That asymmetry is the interview-worthy detail.

## The 30-second interview answer

"The trick is capturing the parameter list as a generic tuple: `function debounce<Args extends unknown[]>(fn: (...args: Args) => void, ms: number): (...args: Args) => void`. `Args` is inferred as the tuple of `fn`'s parameters — `[string, number]` for `(s: string, n: number)` — and `...args: Args` spreads it back out on the returned function, so the debounced version has the exact same signature: names, arity, optional params all preserved. Without it you'd write `(...args: any[])` and lose all checking — any args compile. Debounce returns `void` because the real call is deferred — there's no synchronous value to return. Throttle can preserve the return type with a second generic `<Args, R>` since its leading-edge call runs `fn` synchronously — I cache `lastResult: R` and return it for in-window calls. This `Args extends unknown[]` pattern is the standard idiom for any higher-order function — memoize, once, retry — that must not lose the wrapped signature."

## Follow-up trap

**"Why `unknown[]` as the constraint — why not just `Args`?"** — Because `...args: Args` requires `Args` to be a tuple/array type — the spread needs an array-like. `Args extends unknown[]` enforces that structurally; without it the spread is a type error. `any[]` works too but `unknown[]` is the modern choice. Second trap: **"does debounce preserve the return type?"** — It can't — `fn` runs inside `setTimeout`, after the debounced call has returned. Any `=> R` on a debounce is lying; that's why the standard signature is `=> void` and why throttle (leading edge) is the one that *can* keep `R`. Third: **"what about `this`?"** — `Args` captures params only — if `fn` is a method needing `this`, the wrapper loses it (`fn(...args)` calls it unbound). Fixing it needs `ThisType`/explicit `this: T` param — a real limitation worth naming. Bonus: **`Parameters<typeof fn>` / `ReturnType<typeof fn>`** — the utility-type way to grab the same tuple without a generic on the call site: `(...args: Parameters<F>) => ReturnType<F>`.
