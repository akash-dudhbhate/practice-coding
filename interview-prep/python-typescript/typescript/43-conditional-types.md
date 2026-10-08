# 43 — Conditional types and `infer` — `T extends U ? A : B` in the type system

> **Interview question:** "What are conditional types, and what does `infer` do?"
> **What the interviewer is really testing:** Whether you know TypeScript's type level is a *language* — `extends ? :` is its `if`, `infer` is its "capture into a variable" — and that built-in utilities like `ReturnType`, `Parameters`, `Awaited` are literally implemented with these.

## Theory — what it is

A **conditional type** selects a type based on a check, exactly like a ternary but at the type level:

```typescript
type IsString<T> = T extends string ? true : false;
type A = IsString<string>;   // true
type B = IsString<number>;   // false
```

**`infer`** declares a type variable *inside the pattern being matched* — "if `T` has this shape, grab this piece":

```typescript
type GetReturn<T> = T extends (...args: any[]) => infer R ? R : never;
// "if T is a function, infer its return type as R, give me R"
type R1 = GetReturn<() => number>;   // number
```

Rules that matter:

- **`extends` here means "is assignable to"** — not inheritance. `string extends string` is true; `number extends string` is false.
- **`infer` only works inside a conditional's `extends` clause** — it introduces a new type variable bound to whatever the pattern matched.
- **Multiple `infer` in one pattern:** `T extends (a: infer A) => infer R` captures param *and* return.
- **Distributivity — the big gotcha.** If `T` is a *naked* type parameter and a union, the conditional distributes: `ToArray<string | number>` becomes `ToArray<string> | ToArray<number>` = `string[] | number[]`. Wrap `T` in `[T]` to opt out: `[T] extends [string]`.
- **`never` for the false arm** — convention for "doesn't match, produce nothing" — `Exclude` uses it: `T extends U ? never : T`.
- **Recursion is allowed** — conditional types can call themselves (`Flatten<T>` recursing into nested arrays) — bounded by a depth limit (~50).
- **The built-ins are just these:** `ReturnType<T>`, `Parameters<T>`, `Awaited<T>`, `Exclude`, `Extract`, `NonNullable`, `InstanceType` — all conditional + `infer` under the hood.

## Why it was needed

Before conditional types (TS 2.8), type-level logic was impossible — you could name types and combine them, but couldn't *decide* based on a type. Utilities like `ReturnType` were hand-rolled per arity via overloads, and anything needing "extract the X from this type" was impossible.

Conditional types turned the type system Turing-complete: every utility type that does *analysis* (`ReturnType`, `Exclude`, `Awaited`) is expressible in the language itself — they shipped as library types written in `.d.ts`, not compiler magic. `infer` was the piece that made *extraction* possible — matching a shape and naming a sub-piece, the same way destructuring names parts of a value.

## Where it's used in a real project

- **`ReturnType<typeof fn>` / `Parameters<typeof fn>`:** grab types from existing functions — the daily-use cases.
- **`Awaited<T>`:** unwrap `Promise<User>` → `User` — essential for typing `await`ed results generically.
- **Type-level filtering:** `Exclude<keyof T, "id">`, `NonNullable<T>` — utility types built on the false-arm-never idiom.
- **Library internals:** `z.infer`, React's `ComponentProps<T>` — extraction via `infer`.
- **Custom utilities:** `UnwrapPromise`, `Flatten`, `FirstParam<F>` — bespoke type surgery in a codebase's `types.ts`.

## Diagram

```
type IsStr<T> = T extends string ? "yes" : "no";
                       │
              "is T assignable to string?"
                 ┌─────┴─────┐
              yes ▼           ▼ no
                "yes"       "no"

infer — capture a piece while matching:
type Ret<T> = T extends (...args: any[]) => infer R ? R : never;
                                              │
              for T = (s: string) => number:
                matches -> binds R = number -> result: number

DISTRIBUTION (the gotcha):
type ToArray<T> = T extends any ? T[] : never;
ToArray<"a" | "b">  distributes: ("a"[]) | ("b"[])  = "a"[] | "b"[]
ToArray<["a"|"b"]>  one value:  ("a"|"b")[]

BUILT-INS ARE JUST THIS:
  ReturnType<F> = F extends (...a:any[]) => infer R ? R : never
  Exclude<T,U>  = T extends U ? never : T
  Awaited<T>    = T extends Promise<infer U> ? Awaited<U> : T  (recursive!)
```

## Code — explained

```typescript
// 1. Basic conditional — a type-level if
type IsString<T> = T extends string ? "yes" : "no";
type T1 = IsString<"abc">;      // "yes"
type T2 = IsString<123>;        // "no"

// 2. infer — extract the return type (this IS how ReturnType works)
type MyReturnType<F> = F extends (...args: any[]) => infer R ? R : never;
type Fn = (a: string, b: number) => boolean;
type R = MyReturnType<Fn>;      // boolean — inferred from the pattern

// 3. Multiple infer — params AND return
type FirstAndRet<F> =
  F extends (first: infer A, ...rest: any[]) => infer R
    ? { arg: A; ret: R }
    : never;
type FR = FirstAndRet<Fn>;      // { arg: string; ret: boolean }

// 4. Exclude — false arm is never, "remove what matches"
type MyExclude<T, U> = T extends U ? never : T;
type E = MyExclude<"a" | "b" | "c", "a">;   // "b" | "c" — distributes!

// 5. Awaited — recursive conditional unwrapping nested promises
type MyAwaited<T> = T extends Promise<infer U> ? MyAwaited<U> : T;
type A1 = MyAwaited<Promise<Promise<string>>>;   // string — recursed twice

// 6. Distribution demo — the union explodes the conditional
type Wrap<T> = T extends any ? { v: T } : never;
type W = Wrap<"a" | "b">;
// { v: "a" } | { v: "b" }   — NOT { v: "a" | "b" } — distributed!

// 7. Opt out of distribution with [T]
type WrapNoDist<T> = [T] extends [any] ? { v: T } : never;
type W2 = WrapNoDist<"a" | "b">;   // { v: "a" | "b" } — single object
```

1. `IsString<T>` is a function at the type level: `T` in, `"yes"`/`"no"` out. `extends` = assignability check.
2. `infer R` inside `(...args) => infer R` — when `F` matches the function pattern, `R` binds to its return type; the true branch returns `R`. `MyReturnType` is literally how lib's `ReturnType` is implemented.
3. Multiple `infer` — pattern-matching the signature's shape captures `A` (first param) and `R` (return) in one go — destructuring, at the type level.
4. `MyExclude` — when `T` is assignable to `U`, produce `never` (nothing); else keep `T`. On a union it distributes (see 6) so each member is tested individually — `"a"` drops out.
5. `MyAwaited` recurses: `Promise<Promise<string>>` → `Promise<string>` → `string`. Real `Awaited` is more complex (handles thenables) but this is the idea.
6. `Wrap<"a" | "b">` distributes: conditional runs per union member → `{v:"a"} | {v:"b"}` — usually desired (that's how `Exclude` filters unions) but surprising when unwanted.
7. `[T] extends [any]` — wrapping in a tuple makes `T` non-naked, so the union is tested as a *whole* — distribution off.

## Problems

### Easy — write `MyNonNullable`
**Problem:** Write `MyNonNullable<T>` that removes `null` and `undefined` from `T` — using a conditional type.
**Try this input:** `MyNonNullable<string | null | undefined>`.
**Expected output:** type `string`.
**Solution:**
```typescript
type MyNonNullable<T> = T extends null | undefined ? never : T;

type X = MyNonNullable<string | null | undefined>;   // string
type Y = MyNonNullable<number | null>;               // number
```
**Logic explained:**
1. `T extends null | undefined ? never : T` — if the member is null/undefined, drop it (`never`); else keep it.
2. Distribution does the work: `string | null | undefined` runs the check per-member — `string` stays, `null`/`undefined` become `never`, and `never` members vanish from the union.
3. This is exactly the built-in `NonNullable<T>` — same implementation.

### Medium — write `MyParameters` and `MyInstanceType`
**Problem:** Implement `MyParameters<F>` (tuple of a function's params) and `MyInstanceType<C>` (instance type of a constructor). Test on `(a: string, b: number) => void` and `class Foo { x!: number }`.
**Try this input:** `MyParameters<(a: string, b: number) => void>`, `MyInstanceType<typeof Foo>`.
**Expected output:** `[a: string, b: number]` and `Foo`.
**Solution:**
```typescript
type MyParameters<F> = F extends (...args: infer P) => any ? P : never;
type P = MyParameters<(a: string, b: number) => void>;   // [a: string, b: number]

type MyInstanceType<C> = C extends new (...args: any[]) => infer I ? I : never;

class Foo { x = 1; }
type I = MyInstanceType<typeof Foo>;   // Foo — constructor's return inferred
```
**Logic explained:**
1. `(...args: infer P)` — `infer` on a *rest* position captures the whole param list as a tuple — that's why `P` comes out `[a: string, b: number]` not `string | number`.
2. `new (...args: any[]) => infer I` — the *constructor* pattern: `infer I` binds to what `new C()` produces — the instance type.
3. Both are the actual built-ins (`Parameters`, `InstanceType`) — same `infer`-in-rest / `infer`-in-return mechanics.

### Hard — `Flatten` for nested arrays + a distributive `ElementType`
**Problem:** Write `Flatten<T>` that recursively unwraps arrays — `number[][][]` → `number` — then `ElementType<T>` that gets the element of a single array level. Show both distributing correctly.
**Try this input:** `Flatten<number[][][]>`, `ElementType<string[]>`, `Flatten<"x">`.
**Expected output:** `number`, `string`, `"x"` (non-array passes through).
**Solution:**
```typescript
// element type of ONE array level
type ElementType<T> = T extends (infer E)[] ? E : T;
type E1 = ElementType<string[]>;        // string
type E2 = ElementType<number>;          // number — not array, passthrough

// recursively unwrap nested arrays
type Flatten<T> = T extends (infer E)[] ? Flatten<E> : T;
type F1 = Flatten<number[][][]>;   // number — unwraps 3 levels
type F2 = Flatten<string>;         // string — not an array, returns T
type F3 = Flatten<string[] | number[]>;  // string | number — distributes
```
**Logic explained:**
1. `T extends (infer E)[]` — pattern-match "array of something": `infer E` captures the element type; if `T` isn't an array, the false arm returns `T` unchanged.
2. `Flatten` recurses: `number[][][]` → `Flatten<number[][]>` → `Flatten<number[]>` → `number`. Each `extends` check peels one array level.
3. `F3` distributes over the union: `Flatten` runs on `string[]` and `number[]` separately → `string | number`.
4. The recursion depth limit (~50 levels) is the practical bound — `Flatten` on a 100-deep array errors with "type instantiation excessively deep." Worth knowing it exists.

## The 30-second interview answer

"Conditional types are `if` at the type level: `T extends U ? A : B` picks `A` if `T` is assignable to `U`, else `B` — `extends` here means assignability, not inheritance. `infer` is the capture operator — inside the `extends` pattern it binds a type variable: `T extends (...args) => infer R ? R : never` pulls the return type out of a function type, which is literally how `ReturnType` is implemented. The utilities are all built this way — `Parameters`, `Awaited`, `Exclude`, `InstanceType`. Two gotchas: conditional types *distribute* over union `T`s — `ToArray<string|number>` gives `string[] | number[]`, and you opt out by wrapping `[T] extends [U]` — and they can recurse, so `Awaited` unwraps nested promises and custom types like `Flatten` peel nested arrays, bounded by a ~50-level depth limit. They're how you do type-level surgery: extract a piece, filter a union, unwrap a wrapper."

## Follow-up trap

**"What's the difference between `extends` in a conditional type and `extends` on a class/interface?"** — Class `extends` is inheritance (runtime). Conditional `extends` is *assignability* — `T extends string` asks "could a `T` value be assigned to a `string` variable?" — a subtype check, not an OO relationship. Same keyword, different meaning — like `typeof` in values vs types. Second trap: **"why does `IsUnion`/`ToArray<"a"|"b">` give a union of arrays instead of an array of the union?"** — Distribution: when the checked type is a naked `T`, the conditional runs *per union member* — `"a"[] | "b"[]`. It's a feature (`Exclude` relies on it) and a gotcha (wrap `[T]` to disable). Third: **"can `infer` be used outside a conditional?"** — No — `infer` is only legal inside an `extends` clause of a conditional type; it's meaningless without the pattern-match that binds it. And: **"how does `Exclude` remove union members?"** — exactly by distribution: `T extends U ? never : T` on a union keeps non-matching members and turns matching ones into `never`, which drops out of the union.
