# 22 — Default generics: `<T = string>`

> **Interview question:** "What does a default type parameter like `<T = string>` do, and when is it useful?"
> **What the interviewer is really testing:** Do you understand that defaults make a generic *optional to specify* — and that they interact subtly with inference, ordering, and backwards compatibility?

## Theory — what it is

A **default type parameter** gives a generic a fallback type, exactly like a default function parameter gives an argument a fallback value. `interface ApiResponse<T = string>` means: if the caller writes `ApiResponse<number>`, `T` is `number`; if they write bare `ApiResponse`, `T` is `string`.

So `ApiResponse` and `ApiResponse<string>` are the *same type*. The generic is still fully overridable — the default only kicks in when no argument is supplied. This works on interfaces, type aliases, classes, and function generics.

Two rules to know. First, **ordering**: once a parameter has a default, every parameter after it must also have a default (or a constraint satisfied by earlier params) — same as optional function parameters, where `f(a, b = 1, c)` is illegal. Second, **defaults vs inference**: for functions, if TypeScript can *infer* `T` from the arguments, inference wins — the default is ignored. The default only applies when nothing tells the compiler what `T` should be. `function parse<T = string>(raw: string): T` called as `parse("x")` gets `T = string` (nothing to infer from), but `parse<number>("x")` overrides it.

## Why it was needed

Generics create a tension between flexibility and ergonomics. A type like `ApiResponse<T>` forces *every* call site to write `ApiResponse<Whatever>` — even in the extremely common case where the payload is `string` or `unknown`. That's noise: 90% of usages carry boilerplate.

Defaults solve three real problems:

1. **The common case stays short.** `ApiResponse` reads clean when `string` covers most APIs; the unusual `ApiResponse<User>` spells itself out.
2. **Backwards compatibility.** Adding `<T = Existing>` to a previously non-generic type lets you introduce flexibility *without breaking existing code* — all the `ApiResponse` references in the codebase keep working and mean `ApiResponse<Existing>`. This is how libraries evolve types without major version bumps.
3. **Un-inferrable positions.** When `T` only appears in the return type (not in parameters), TypeScript can't infer it — `function create<T>(): T` leaves `T` as `unknown` unless the caller annotates. A default `<T = string>` gives the common case a sane answer instead of `unknown`.

## Where it's used in a real project

- **API layers:** `interface ApiResponse<T = unknown> { data: T; status: number }` — handlers that don't care about payload shape use bare `ApiResponse`; typed endpoints write `ApiResponse<User>`.
- **React-style components (type level):** `interface Props<T = HTMLElement> { ref?: RefObject<T> }` — the generic defaults to the common element type.
- **Event systems:** `type EventMap<E extends string = string> = Record<E, unknown>` — default keeps simple usage simple.
- **Evolving library types:** a package that shipped `type Result = { ok: boolean }` can later ship `type Result<T = void> = { ok: boolean; value: T }` — old code still compiles.
- **Class generics:** `class Store<T = AppState>` — `new Store()` gets the default state shape; `new Store<DebugState>()` overrides.

## Diagram

```
interface ApiResponse<T = string> { data: T; ok: boolean }

Caller writes:              T resolves to:
  ApiResponse                 string          (default kicks in)
  ApiResponse<string>         string          (explicit = same as default)
  ApiResponse<User>           User            (override)

Ordering rule (like optional params):
  <T = string, U>            ILLEGAL — required after optional
  <T, U = number>            OK
  <T = string, U = number>   OK

Function inference beats the default:
  function wrap<T = number>(x: T): T
  wrap("hi")     -> T inferred as string (default ignored — args win)
  wrap           <- can't call with no args; nothing to infer
  function make<T = number>(): T
  make()         -> T = number (nothing to infer from -> default used)
```

## Code — explained

```typescript
// 1. Interface with a default: bare usage means T = string
interface ApiResponse<T = string> {
  data: T;
  status: number;
}

const plain: ApiResponse = { data: "ok", status: 200 };       // T = string
const typed: ApiResponse<{ id: number }> = {
  data: { id: 1 },
  status: 200,
};
console.log(plain.data.toUpperCase(), typed.data.id);         // OK 1

// 2. Backwards-compatible evolution: adding a generic doesn't break callers
type Result<T = void> = { ok: boolean; value: T };
const oldStyle: Result = { ok: true, value: undefined };      // T = void
const newStyle: Result<number> = { ok: true, value: 42 };
console.log(newStyle.value * 2);                              // 84

// 3. Un-inferrable T: default fills in when inference has nothing
function create<T = string>(label: string): { label: string; value?: T } {
  return { label };
}
const a = create("greeting");       // { label: string; value?: string }
const b = create<number>("count");  // T overridden to number
console.log(a.label, b.label);      // greeting count

// 4. Inference beats the default when args determine T
function wrap<T = number>(x: T): T {
  return x;
}
const s = wrap("hello");            // T = string (inferred!), not number
console.log(s.toUpperCase());       // HELLO

// 5. Defaults can reference earlier type params
type Pair<A, B = A> = { first: A; second: B };
const p: Pair<number> = { first: 1, second: 2 };   // B = A = number
console.log(p.first + p.second);                   // 3
```

1. `ApiResponse` with no `<>` uses the default `string`; `data.toUpperCase()` type-checks because `data` is `string`. `ApiResponse<{ id: number }>` overrides cleanly.
2. `type Result<T = void>` shows the evolution pattern: old `Result` references still compile with `T = void`, while new code can carry a real value.
3. `create<T = string>` — `T` appears only in the return type, so nothing in `create("greeting")` can infer it. The default `string` applies. `create<number>` overrides explicitly.
4. `wrap("hello")` proves **inference > default**: `T` is inferred as `string` from the argument; the `= number` default is ignored because the arguments settled it first.
5. `Pair<A, B = A>` shows a default depending on an earlier parameter — `Pair<number>` means `B = number` too. Only *earlier* params are visible to defaults.

## Problems

### Easy — default a generic interface
**Problem:** Define `Page<T = string>` with `content: T` and `page: number`. Then type a variable `simplePage` using the default and one `userPage` with `User = { id: number }`.
**Try this input:**
```typescript
const simplePage: Page = { content: "hello", page: 1 };
const userPage: Page<User> = { content: { id: 7 }, page: 2 };
```
**Expected output:** both compile; `console.log(simplePage.content.toUpperCase(), userPage.content.id)` → `HELLO 7`.
**Solution:**
```typescript
interface Page<T = string> {
  content: T;
  page: number;
}
interface User {
  id: number;
}
const simplePage: Page = { content: "hello", page: 1 };
const userPage: Page<User> = { content: { id: 7 }, page: 2 };
console.log(simplePage.content.toUpperCase(), userPage.content.id); // HELLO 7
```
**Logic explained:**
1. `Page` with no argument makes `T = string`, so `content.toUpperCase()` is valid.
2. `Page<User>` overrides — `content` is now a `User`, giving `content.id`.
3. The same interface serves both the quick case and the precise case.

### Medium — generic function whose T can't be inferred
**Problem:** Write `deserialize<T = unknown>(raw: string): T` that returns `JSON.parse(raw)` — show a call where the default applies and one where it's overridden.
**Try this input:**
```typescript
const x = deserialize("{}");
const y = deserialize<number>("42");
```
**Expected output:** `x` has type `unknown` (default), `y` is `number`, `console.log(y + 1)` → `43`.
**Solution:**
```typescript
function deserialize<T = unknown>(raw: string): T {
  return JSON.parse(raw) as T;
}

const x = deserialize("{}");          // x: unknown — default used
const y = deserialize<number>("42");  // y: number  — overridden
console.log(y + 1);                   // 43
// x + 1 would ERROR: 'x' is of type 'unknown' — the default is honest
```
**Logic explained:**
1. `T` never appears in the parameters — inference has nothing to grab, so `deserialize("{}")` falls back to the default `unknown`.
2. `deserialize<number>` overrides explicitly — the caller asserts what the JSON contains.
3. Defaulting to `unknown` (not `any`) is the honest choice: it forces callers to either annotate or narrow before using the result.

### Hard — default + constraint together
**Problem:** Write `class Buffer<T extends ArrayLike<unknown> = number[]>` holding `data: T`, with `length` derived from `data.length`. Show `new Buffer()` defaulting to `number[]` and `new Buffer<string>()` failing the constraint.
**Try this input:**
```typescript
const buf = new Buffer([1, 2, 3]);
console.log(buf.length);
// new Buffer<string>("abc")
```
**Expected output:** `3`; `new Buffer<string>` errors: `Type 'string' does not satisfy the constraint 'ArrayLike<unknown>'` (string is actually `ArrayLike` — see note) — better: `new Buffer<number>(5)` errors: `Type 'number' is not assignable to 'ArrayLike<unknown>'`.
**Solution:**
```typescript
class Buffer<T extends ArrayLike<unknown> = number[]> {
  constructor(public data: T) {}
  get length(): number {
    return this.data.length;
  }
}

const buf = new Buffer([1, 2, 3]);          // T inferred = number[]
const strBuf = new Buffer<string>("abc");   // T = string — legal, strings are ArrayLike
const typedBuf = new Buffer<Uint8Array>(new Uint8Array(4));
console.log(buf.length, strBuf.length, typedBuf.length);   // 3 3 4
// new Buffer<number>(5);                   // ERROR: number isn't ArrayLike
```
**Logic explained:**
1. `<T extends ArrayLike<unknown> = number[]>` combines both features: `extends` sets the floor (must have `.length` and indexable elements), `= number[]` sets the fallback.
2. `new Buffer([1,2,3])` infers `T = number[]` from the constructor arg — matching the default anyway.
3. `new Buffer<string>("abc")` is *legal* — strings satisfy `ArrayLike` (`s.length`, `s[0]`). `new Buffer<number>` is the true failure case: `number` has no `.length`. The constraint, not the default, is what rejects it.
4. Key interview point: `extends` restricts what you *may* pass; `=` decides what you get when you pass *nothing*. They're orthogonal.

## The 30-second interview answer

"A default type parameter is a fallback for the generic itself — `<T = string>` means bare `ApiResponse` is shorthand for `ApiResponse<string>`, while `ApiResponse<User>` still overrides. It's useful in three spots: the common case stays terse, you can add a generic to an existing type without breaking old code — huge for library evolution — and it rescues positions where inference is impossible, like `T` appearing only in the return type. The subtlety: defaults lose to inference — if arguments determine `T`, the default is ignored; it only applies when nothing else pins `T` down. And the ordering rule mirrors optional parameters: once a param has a default, everything after it needs one too."

## Follow-up trap

**"If `T` has a default, why did `wrap("hi")` get `T = string` instead of `T = number`?"** Because for *functions*, TypeScript tries inference first — arguments beat defaults. The default is only consulted when inference draws a blank (`T` unused in parameters, or no relevant argument). This surprises people who expect `= number` to act like a coercion; it's a fallback, not a cast. Second probe: **"can a default violate its own constraint?"** — `<T extends number = string>` is a compile error; the default itself must satisfy `extends`. And one more: **`unknown` vs `any` as a default** — defaulting to `any` silently disables checking at every unannotated call site; `unknown` keeps callers honest by forcing a narrowing or explicit annotation. Interviewers reward that distinction.
