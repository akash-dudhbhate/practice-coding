# 27 — `Exclude`, `Extract`, `NonNullable` — filtering union members

> **Interview question:** "What do `Exclude` and `Extract` do, and how are they implemented?"
> **What the interviewer is really testing:** Do you understand **distributive conditional types** — a conditional over a naked union type parameter evaluates *per member* — the engine behind all union filtering?

## Theory — what it is

All three are one-line conditional types that filter a union member by member:

```typescript
type Exclude<T, U>  = T extends U ? never : T;                   // drop members in U
type Extract<T, U>  = T extends U ? T : never;                   // keep only members in U
type NonNullable<T> = T extends null | undefined ? never : T;    // drop null/undefined
```

The mechanism — **distributivity**: when `T` is a *naked* type parameter in `T extends U ? ... : ...`, TypeScript doesn't check the whole union at once. It evaluates the conditional once per member and re-unions the results:

```typescript
// Exclude<"a" | "b" | "c", "a">
//   = ("a" extends "a" ? never : "a")   → never
//   | ("b" extends "a" ? never : "b")   → "b"
//   | ("c" extends "a" ? never : "c")   → "c"
//   = "b" | "c"        (never members evaporate from unions)
```

What each is for:

- **`Exclude<T, U>`** — "the union minus these members": `Exclude<Status, "error">`, `Exclude<keyof T, "id">` (this is `Omit`'s engine), `Exclude<T, undefined>`.
- **`Extract<T, U>`** — "only the members that match": pull one member out of a discriminated union (`Extract<Event, { type: "click" }>`), or find shared keys (`Extract<keyof A, keyof B>`).
- **`NonNullable<T>`** — strip `null`/`undefined`: tighten `T | undefined` returns (like `Array.find`'s) to just `T`.

To *block* distribution, wrap `T` in a tuple — `[T] extends [U] ? ...` compares the union as one unit. That's how you test "is `T` exactly this union" instead of filtering it.

## Why it was needed

Unions model real domains — `type Status = "idle" | "loading" | "success" | "error"`. Constantly you need a *subview*: "statuses that mean finished," "events my handler cares about," "this value once we've ruled out null." Without union filtering you'd re-declare sub-unions by hand — `type FinishedStatus = "success" | "error"` — and they'd silently rot when `Status` grows. `Exclude`/`Extract` keep sub-views *derived*: change the parent union and every filter recomputes.

## Where it's used in a real project

- `Omit` internals: `Omit<T, K> = Pick<T, Exclude<keyof T, K>>`.
- `type NonError = Exclude<Status, "error">` — a function that can't accept the error state.
- `type ClickEvent = Extract<AppEvent, { type: "click" }>` — a handler signature for one union member.
- `NonNullable<ReturnType<typeof find>>` — after proving existence elsewhere, re-type as definite.
- `Extract<keyof A, keyof B>` — keys shared by two object types (merge-safe keys).
- Removing `""` or `null` from literal unions: `Exclude<string, "">`-style constraints.

## Diagram

```
type Status = "idle" | "loading" | "success" | "error"

Exclude<Status, "error">             → "idle" | "loading" | "success"
Extract<Status, "success"|"error">   → "success" | "error"
NonNullable<string | null | undef>   → string

distribution, member by member:

  "idle"    extends "error"? → keep "idle"
  "loading" extends "error"? → keep "loading"
  "success" extends "error"? → keep "success"
  "error"   extends "error"? → never   (evaporates)
                              ─────────────────────────
                              "idle" | "loading" | "success"

Extract on object unions — extends = assignable, not equal:
  Extract<Shape, { kind: "circle" }>
  → { kind: "circle"; r: number }   (it IS assignable to { kind: "circle" })
```

## Code — explained

```typescript
type Status = "idle" | "loading" | "success" | "error";

// 1. Exclude — drop members
type ActiveStatus = Exclude<Status, "error">;          // "idle"|"loading"|"success"
const ok: ActiveStatus = "loading";
// const bad: ActiveStatus = "error";                  // (1) compile error

// 2. Extract — keep members that match
type DoneStatus = Extract<Status, "success" | "error">;  // "success"|"error"
const done: DoneStatus = "error";

// 3. Extract on OBJECT unions — pulls a whole member by shape
type Shape =
  | { kind: "circle"; r: number }
  | { kind: "square"; side: number };

type Circle = Extract<Shape, { kind: "circle" }>;      // (2) the circle member
const c: Circle = { kind: "circle", r: 2 };
console.log(Math.PI * c.r ** 2);                        // 12.566370614359172

// 4. NonNullable — strip null/undefined
function find(): string | undefined {
  return Math.random() > 0.5 ? "hit" : undefined;
}
type Definite = NonNullable<ReturnType<typeof find>>;    // (3) string
const s: Definite = "always a string here";
console.log(ok, done, s.toUpperCase());                  // loading error ALWAYS A STRING HERE
```

1. `"error"` is no longer assignable to `ActiveStatus` — exclusion enforced at compile time; and if `Status` grows a `"fatal"` member, it flows into `ActiveStatus` automatically.
2. `Extract` uses *assignability*, not equality: `{ kind: "circle"; r: number }` extends `{ kind: "circle" }` → kept. That's why extracting union members by a partial shape works.
3. `ReturnType<typeof find>` is `string | undefined`; `NonNullable` removes `undefined` — useful when you've already proven existence elsewhere and want the definite type.

## Problems

### Easy — Exclude a state
**Problem:** `type Phase = "start" | "middle" | "end"`. A function accepts any phase except `"start"` (it's the entry point — you can't *advance from* it). Type the parameter without rewriting the union.
**Try this input:** `advance("middle")` ok; `advance("start")` must not compile.
**Expected output:** `advanced from middle`.
**Solution:**
```typescript
type Phase = "start" | "middle" | "end";

function advance(p: Exclude<Phase, "start">): string {
  return `advanced from ${p}`;
}

console.log(advance("middle"));   // advanced from middle
// advance("start");              // compile error — "start" not assignable
```
**Logic explained:**
1. `Exclude<Phase, "start">` = `"middle" | "end"` — derived, so adding `"final"` to `Phase` automatically allows it here.
2. Hand-writing `type NonStart = "middle" | "end"` would silently miss future members — the classic drift this family exists to prevent.
3. `Exclude` is compile-time only — nothing is emitted; the check lives purely in the signature.

### Medium — Extract a union member for a handler
**Problem:** `type AppEvent = { type: "click"; x: number; y: number } | { type: "key"; key: string } | { type: "scroll"; dy: number }`. Type a click handler that receives *only* the click member — via `Extract`, not by re-declaring it.
**Try this input:** `onClick({ type: "click", x: 10, y: 20 })`
**Expected output:** `click at 10,20`; passing the key member is a compile error.
**Solution:**
```typescript
type AppEvent =
  | { type: "click"; x: number; y: number }
  | { type: "key"; key: string }
  | { type: "scroll"; dy: number };

type ClickEvent = Extract<AppEvent, { type: "click" }>;

function onClick(e: ClickEvent): void {
  console.log(`click at ${e.x},${e.y}`);
}

onClick({ type: "click", x: 10, y: 20 });   // click at 10,20
// onClick({ type: "key", key: "a" });      // compile error — not the click member
```
**Logic explained:**
1. `Extract` keeps union members *assignable to* `{ type: "click" }` — the click member matches because it has `type: "click"` plus extra fields (assignability, not exact shape).
2. `e.x`/`e.y` type-check because `ClickEvent` is the *full* member, not just `{ type: "click" }`.
3. Add fields to the click member and `ClickEvent` tracks them — derived, not duplicated. This is how typed event systems pick apart discriminated unions for handler signatures.

### Hard — Filter object keys by value type
**Problem:** Write `KeysOfType<T, V>` — the keys of `T` whose values are assignable to `V` — then `PickByType<T, V>` on top of it. Use it to grab only the *string* fields of `User`.
**Try this input:** `interface User { id: number; name: string; email: string; age: number }` → `PickByType<User, string>`
**Expected output:** `{ name: string; email: string }` — provable by assigning `{ name: "a", email: "b" }` while `{ ..., id: 1 }` errors.
**Solution:**
```typescript
interface User { id: number; name: string; email: string; age: number }

// map each key to itself (if its value extends V) or to never (if not)...
type KeysOfType<T, V> = {
  [K in keyof T]: T[K] extends V ? K : never;
}[keyof T];                        // ...then index by all keys → union of survivors
//   for User, V=string:  { id: never; name: "name"; email: "email"; age: never }[keyof User]
//                      = never | "name" | "email" | never  =  "name" | "email"

type PickByType<T, V> = Pick<T, KeysOfType<T, V>>;

type StringsOnly = PickByType<User, string>;        // { name: string; email: string }
const s: StringsOnly = { name: "Amy", email: "a@x" };
console.log(s);                                     // { name: 'Amy', email: 'a@x' }
// const bad: StringsOnly = { name: "A", email: "e", id: 1 };   // compile error

type NumKeys = KeysOfType<User, number>;            // "id" | "age"
```
**Logic explained:**
1. The mapped type evaluates `T[K] extends V` per key — a conditional *inside* a map — emitting each surviving *key name* or `never`.
2. `[keyof T]` then indexes that object type by all its keys → a union of the surviving names; `never` members evaporate — the same trick `Exclude` relies on.
3. `Pick` keeps exactly those keys — three utility-type ideas composed into `PickByType`, a real helper in typed-ORM and form libraries.
4. Memorize the pattern **"map to `K | never`, index to union"** — it powers `FunctionKeys`, `RequiredKeys`, `OptionalKeys`, and half the advanced utility types you'll meet.

## The 30-second interview answer

"`Exclude<T, U>` removes union members assignable to `U`; `Extract<T, U>` keeps only them; `NonNullable<T>` is `Exclude` specialized to `null | undefined`. They're one-line conditional types — `T extends U ? never : T` — powered by *distribution*: a naked type parameter in a conditional is evaluated once per union member and the results re-unioned, with `never`s evaporating. So `Exclude<'a'|'b'|'c', 'a'>` is `'b'|'c'`. `Extract` works on object unions too because `extends` means assignable — `Extract<Event, { type: 'click' }>` pulls the whole click member out of a discriminated union for handler signatures. `Omit` is literally built on `Exclude<keyof T, K>`. The point: sub-unions stay *derived* from the parent, so adding a member updates every filter instead of silently rotting hand-copied unions. And to stop distribution, wrap `T` in a tuple — `[T] extends [U]`."

## Follow-up trap

**"Why does `[T] extends [U]` behave differently than `T extends U`?"** — wrapping `T` in a tuple (or any non-naked position) disables distribution: the whole union is compared as one unit. `Exclude` needs per-member checking; union-equality tests need the opposite. Second trap: **"`Extract` uses `extends` — is it shape equality?"** — no, assignability: `Extract<Shape, { kind: "circle" }>` keeps members that *have* `kind: "circle"`, extra fields included; and `Extract<Status, string>` keeps *every* string member — it filters by "is a," not "is exactly." Third: **"`NonNullable<T>` vs `x!`?"** — same claim-vs-check distinction as assertions: `x!` asserts at a value site and can be wrong; `NonNullable<T>` only retypes — honest when the type genuinely can't be null, a fiction when it can.
