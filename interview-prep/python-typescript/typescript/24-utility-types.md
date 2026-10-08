# 24 — Utility types: `Partial`, `Required`, `Readonly`, `Pick`, `Omit` — implement `Partial` yourself

> **Interview question:** "What do `Partial`/`Pick`/`Omit` do — and can you write `Partial` yourself?"
> **What the interviewer is really testing:** Do you understand **mapped types** — `{ [K in keyof T]: ... }` — well enough that utility types are readable code, not magic; and do you derive types instead of duplicating interfaces?

## Theory — what it is

Utility types are built-in generic transforms over object types. They're not compiler magic — most are one-line **mapped types**, which iterate `keyof T` and rebuild a shape:

```typescript
type Partial<T>  = { [K in keyof T]?: T[K] };            // every key optional
type Required<T> = { [K in keyof T]-?: T[K] };           // strip every ?
type Readonly<T> = { readonly [K in keyof T]: T[K] };    // lock every key
type Pick<T, K extends keyof T> = { [P in K]: T[P] };    // keep only keys K
type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;  // drop keys K
```

How to read one: `[K in keyof T]` loops over each key of `T`; `T[K]` is that key's value type; the modifiers `?`, `-?`, `readonly` apply per key. `Pick` maps over `K` — a *subset* of keys — instead of `keyof T`. `Omit` isn't mapped directly: it's `Pick` over "all keys except `K`," which is why `Exclude` exists (file 27).

Caveats worth knowing:

- `Readonly` is **shallow** — nested objects stay mutable — and compile-time only (it doesn't freeze anything at runtime).
- `Partial` is shallow too: `Partial<{ a: { b: number } }>` still requires the whole `a` object if `a` is present.
- `x?: T` means "key may be *absent*" — distinct from `x: T | undefined` ("key must exist, may hold undefined"). `Partial` adds the former.

## Why it was needed

Real entities wear different costumes per context: the DB `User` has `passwordHash`; the API response shouldn't; the PATCH endpoint accepts any subset; the creation form omits `id`; the config object is frozen. Without utility types you hand-write `UserPatch`, `UserPublic`, `UserCreate` — five near-identical interfaces that silently drift when someone adds a field to `User`. Utility types make derived views **tracked**: `Omit<User, "passwordHash">` updates automatically when `User` changes. One source of truth, many shapes.

## Where it's used in a real project

- `Partial<User>` — PATCH/update handlers, `Object.assign(defaults, overrides)`, test factories `buildUser(o?: Partial<User>)`.
- `Required<Config>` — after merging defaults, prove nothing is optional anymore.
- `Readonly<State>` — immutable Redux-style state, frozen configs (plus `Object.freeze` for the runtime half).
- `Pick<User, "id" | "name">` — list-view DTOs, options objects, React prop subsets.
- `Omit<User, "passwordHash">` — public API payloads; `Omit<Props, "children">` when wrapping components.

## Diagram

```
interface User { id: number; name: string; email?: string; passwordHash: string }

                keyof User = "id" | "name" | "email" | "passwordHash"
                                    │
   ┌────────────┬─────────────┬─────┴────────┬──────────────┐
   ▼            ▼             ▼              ▼              ▼
 Partial<User> Required<User> Readonly<User> Pick<User,     Omit<User,
                                              "id"|"name">   "passwordHash">
 id?: number   id: number     readonly id    { id: number;  { id: number;
 name?: string name: string   readonly name    name: string } name: string;
 email?: str   email: string  readonly email                  email?: string }
 pwh?: string  pwh: string    readonly pwh   }

 myPartial = { [K in keyof T]?: T[K] }
   → loop each key, add ?, keep the value type T[K]
```

## Code — explained

```typescript
interface User {
  id: number;
  name: string;
  email?: string;
  passwordHash: string;
}

// 1. Partial implemented by hand — the mapped type
type MyPartial<T> = {
  [K in keyof T]?: T[K];            // (1) for each key K of T: optional K of type T[K]
};

// 2. Partial in its natural habitat — an update function
function updateUser(id: number, patch: Partial<User>): User {
  const existing: User = { id, name: "old", passwordHash: "h" };
  return { ...existing, ...patch, id };   // (2) spread order: patch can't overwrite id
}
console.log(updateUser(1, { name: "new" }));
// { id: 1, name: 'new', passwordHash: 'h' }

// 3. Required — the flip side
type FullUser = Required<User>;           // email is now mandatory
const fu: FullUser = { id: 1, name: "x", email: "e@x", passwordHash: "h" };
console.log(fu.email);                    // e@x

// 4. Readonly — compile-time freeze
const frozen: Readonly<User> = { id: 1, name: "x", passwordHash: "h" };
// frozen.name = "y";                     // (3) compile error — readonly
console.log(frozen.name);                 // x

// 5. Pick & Omit — subsets that track the source
type UserCard = Pick<User, "id" | "name">;         // just those keys
type PublicUser = Omit<User, "passwordHash">;       // everything but the hash

const card: UserCard = { id: 1, name: "Amy" };
const pub: PublicUser = { id: 1, name: "Amy", email: "a@x" };  // no passwordHash
console.log(card.name, "passwordHash" in pub);                 // Amy false
```

1. `[K in keyof T]` iterates `"id" | "name" | "email" | "passwordHash"`; each key keeps its value type `T[K]` and gains `?`. `MyPartial<User>` is identical to `Partial<User>`.
2. `{ ...existing, ...patch, id }` — spread order makes the patch unable to change `id`; `Partial` lets callers send any subset of the rest.
3. `Readonly` blocks assignment *through this reference only* — the same object via a mutable alias can still change; it's a view, not a freeze. `Object.freeze` is the runtime half.
4. `Pick`/`Omit` derive DTOs that track the source — rename `name` in `User` and every `Pick`/`Omit` either follows or errors. No silent drift.
5. `pub` proves `Omit` drops the key entirely — `"passwordHash" in pub` is `false` because the field was never allowed on `PublicUser`.

## Problems

### Easy — Merge defaults with `Partial`
**Problem:** `interface Config { port: number; host: string; debug: boolean }`. Write `makeConfig(overrides)` so callers pass only what they change; the result is a full `Config`.
**Try this input:** `makeConfig({ debug: true })`, `makeConfig({})`
**Expected output:** `{ port: 3000, host: 'localhost', debug: true }` then `{ port: 3000, host: 'localhost', debug: false }`.
**Solution:**
```typescript
interface Config { port: number; host: string; debug: boolean }

const DEFAULTS: Config = { port: 3000, host: "localhost", debug: false };

function makeConfig(overrides: Partial<Config>): Config {
  return { ...DEFAULTS, ...overrides };
}

console.log(makeConfig({ debug: true }));  // { port: 3000, host: 'localhost', debug: true }
console.log(makeConfig({}));               // { port: 3000, host: 'localhost', debug: false }
```
**Logic explained:**
1. `Partial<Config>` accepts any subset — callers get autocomplete, can't pass unknown keys, and aren't forced to repeat defaults.
2. Spread order does the merge: defaults first, overrides win.
3. The return type is the full `Config` — after merging, nothing is optional, so downstream code doesn't deal with `| undefined`.

### Medium — Implement `MyPick` and `MyOmit`
**Problem:** Without using the built-ins, write `MyPick<T, K>` and `MyOmit<T, K>` using a mapped type and `Exclude`. Apply them to `User`.
**Try this input:** `type Card = MyPick<User, "id" | "name">`, `const c: Card = { id: 1, name: "Amy" }`
**Expected output:** compiles; `console.log(c)` → `{ id: 1, name: 'Amy' }`; `MyOmit<User, "passwordHash">` rejects `passwordHash`.
**Solution:**
```typescript
interface User { id: number; name: string; email?: string; passwordHash: string }

type MyPick<T, K extends keyof T> = {
  [P in K]: T[P];                    // loop over the SUBSET K, not keyof T
};

type MyOmit<T, K extends keyof any> = MyPick<T, Exclude<keyof T, K>>;
//                                      └─ all keys of T minus K

type Card = MyPick<User, "id" | "name">;
const c: Card = { id: 1, name: "Amy" };
console.log(c);                                   // { id: 1, name: 'Amy' }

type Safe = MyOmit<User, "passwordHash">;
const s: Safe = { id: 1, name: "Amy" };           // hash not required, not allowed
// const bad: Safe = { id: 1, name: "A", passwordHash: "h" };  // compile error
console.log("passwordHash" in s);                 // false
```
**Logic explained:**
1. `MyPick` maps over `K` — constrained to `keyof T`, so you can't pick nonexistent keys — and keeps the original value type `T[P]`.
2. `MyOmit` = `MyPick` over `Exclude<keyof T, K>` — literally how the real `Omit` is defined; it also shows utilities compose.
3. `K extends keyof any` means omitting a key `T` doesn't have is harmless — the real `Omit` is deliberately lenient here, unlike `Pick`.
4. Both produce pure compile-time views — zero emitted code, zero runtime cost.

### Hard — A patch that can't touch `id`
**Problem:** `Partial<User>` lets callers send `{ id: 999 }` — you want update patches where `id` is *impossible* to pass. Define `Update<T>` and use it in `update`.
**Try this input:** `update({ name: "x" })` — should work; `update({ id: 2 })` — must not compile.
**Expected output:** `{ id: 1, name: 'x', passwordHash: 'h' }` for the valid call; the invalid call errors with `'id' does not exist in type 'Update<User>'`.
**Solution:**
```typescript
interface User { id: number; name: string; email?: string; passwordHash: string }

// every key except "id", all optional — id can't appear in a patch at all
type Update<T extends { id: number }> = Partial<Omit<T, "id">>;

function update(patch: Update<User>): User {
  const existing: User = { id: 1, name: "old", passwordHash: "h" };
  return { ...existing, ...patch };       // safe: patch has no id field to spread
}

console.log(update({ name: "x" }));
// { id: 1, name: 'x', passwordHash: 'h' }
// update({ id: 2 });        // compile error: 'id' does not exist in type 'Update<User>'
```
**Logic explained:**
1. `Omit<User, "id">` removes the key entirely, then `Partial` makes the rest optional — `id` isn't "optional," it's *absent*, so `{ id: 2 }` fails excess-property checking.
2. Composing utilities (`Partial` after `Omit`) is the real skill — most codebase-specific utility types are 2–3 built-ins stacked.
3. Different tool for a different rule: `Partial<User> & Pick<User, "id">` keeps `id` *required* — use that when the patch must identify its target. `Omit`-then-`Partial` is for "this field may never change."
4. The `T extends { id: number }` constraint makes `Update` reusable across any entity with a numeric id.

## The 30-second interview answer

"Utility types are built-in mapped-type transforms over object types. `Partial<T>` adds `?` to every key — for PATCH endpoints and config overrides; `Required<T>` strips them; `Readonly<T>` makes every key readonly — shallow, and compile-time only; `Pick<T, K>` keeps a key subset; `Omit<T, K>` drops keys. `Partial` itself is one line — `{ [K in keyof T]?: T[K] }`: iterate each key of `T`, keep its value type `T[K]`, add `?`. `Omit` is `Pick<T, Exclude<keyof T, K>>` — they compose. The reason they matter is derived views that track the source: `Omit<User, 'passwordHash'>` for API responses updates automatically when `User` changes, versus hand-maintained parallel interfaces that silently drift. Caveats to mention: everything is shallow — `Readonly` doesn't deep-freeze — and `x?: T` means 'key may be absent,' not 'key holds undefined.'"

## Follow-up trap

**"What's the difference between `x?: T` and `x: T | undefined`?"** — `?` means the key may be *absent entirely*; `| undefined` means the key must exist but may hold `undefined`. `{}` is a valid `Partial<User>` but not valid for a `{ x: string | undefined }` shape (missing key). With `exactOptionalPropertyTypes` enabled they diverge further: `x?: T` can't even be *assigned* an explicit `undefined`. Second trap: **"is `Readonly` deep?"** — no: `Readonly<{ a: { b: number } }>` still allows `obj.a.b = 1`; you'd need a recursive `DeepReadonly` mapped type, plus `Object.freeze` for the runtime. Third: **"`Pick` with a key not in `T`?"** — compile error, because `K extends keyof T` constrains it; `Omit` doesn't constrain (`K extends keyof any`), so `Omit<User, "nonexistent">` is harmless.
