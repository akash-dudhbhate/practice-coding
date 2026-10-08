# 28 — Mapped types: `{ [K in keyof T]: T[K] }` — writing `Mutable<T>`

> **Interview question:** "What is a mapped type? Write a `Mutable<T>` that removes `readonly` from every property."
> **What the interviewer is really testing:** Can you *iterate over a type's keys* to mechanically produce a new type — and do you know the `-readonly` / `-?` modifiers that power `Partial`, `Required`, and `Readonly`?

## Theory — what it is

A **mapped type** is a `for` loop over the keys of a type. `{ [K in keyof T]: T[K] }` reads: "for every key `K` in `keyof T`, produce a property named `K` whose value type is `T[K]`." If `T` is `{ a: number; b: string }`, the result is `{ a: number; b: string }` — the identity map, a clone.

Three moving parts:

- `K` — a **type variable** bound to each key in turn (not a real type you could use elsewhere).
- `keyof T` — the union of keys to iterate: `"a" | "b"`.
- `T[K]` — **indexed access**: "the type of property `K` on `T`" — for `K = "a"`, that's `number`.

The useful part is what you add around the skeleton:

```typescript
type Mutable<T> = { -readonly [K in keyof T]: T[K] };  // strip readonly
type MyPartial<T> = { [K in keyof T]?: T[K] };         // add ?
type MyRequired<T> = { [K in keyof T]-?: T[K] };       // strip ?
type Nullable<T>  = { [K in keyof T]: T[K] | null };   // transform values
```

`-readonly` and `-?` *remove* a modifier; `+readonly` / `+?` (or bare `readonly` / `?`) *add* it. And a plain `{ [K in keyof T]: T[K] }` is **homomorphic** — it automatically copies `readonly`/`?` from `T`, which is why stripping them requires the explicit `-`.

Finally, `as` inside the brackets **remaps keys**: `{ [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K] }` renames every key — or drops it entirely by remapping to `never`.

## Why it was needed

Real code constantly needs "the same shape, but…": the same entity but every field optional (patch/updates DTOs), every field readonly (state snapshots), every field nullable (DB rows), the `Promise`-unwrapped version, getters generated from fields. Without mapped types you'd hand-write a parallel type per variation and keep them in sync forever — the drift problem again.

Mapped types are also how the standard library's utility types are implemented: `Partial<T>`, `Required<T>`, `Readonly<T>`, `Pick<T,K>`, `Record<K,V>` are all one-line mapped types. Understanding the syntax means you can read — and write — any of them.

## Where it's used in a real project

- **`Partial<Entity>` for update payloads:** `updateUser(id, patch: Partial<User>)` — PATCH endpoints everywhere.
- **`Readonly<State>` / `readonly T[]`:** Redux-style stores hand out immutable views.
- **DTO shaping:** `type PublicUser = Omit<User, "passwordHash" | "email">` — `Omit` is a mapped type under the hood.
- **Key remapping:** generating `getX`/`setX` method names, or `CamelCase`ing snake_case API fields.
- **Stripping modifiers from library types:** a third-party `readonly` config you need to build incrementally → `Mutable<Config>`.

## Diagram

```
        T = { readonly a: number; b?: string }
                     │ keyof T
                     ▼
             keys: "a" | "b"
                     │
        ┌────────────┴─────────────┐
        │  mapped type: for each K  │
        │  [K in keyof T] : T[K]    │
        └────────────┬─────────────┘
                     │ per-key loop
        ┌────────────┴────────────┐
        ▼                         ▼
  K = "a", T[K] = number    K = "b", T[K] = string | undefined
        │                         │
        └────────────┬────────────┘
                     ▼
   Mutable<T>  = { a: number; b?: string }        (-readonly strips flag)
   MyPartial<T> = { a?: number; b?: string }      (add ? to every key)
   Getters<T>  = { getA: () => number;            (as-remap renames keys)
                  getB: () => string | undefined }
```

## Code — explained

```typescript
interface Config {
  readonly host: string;
  readonly port: number;
  readonly debug?: boolean;
}

// 1. Mutable<T>: -readonly removes the modifier from every property
type Mutable<T> = {
  -readonly [K in keyof T]: T[K];
};

const draft: Mutable<Config> = { host: "x", port: 80 };  // (2)
draft.port = 8080;                                       // (3) OK now
// const c: Config = { host: "x", port: 80 };
// c.port = 8080;                                        // (4) Error: readonly

// 5. MyPartial / MyRequired — the ? modifier in both directions
type MyPartial<T> = { [K in keyof T]?: T[K] };
type MyRequired<T> = { [K in keyof T]-?: T[K] };

const patch: MyPartial<Config> = { port: 3000 };         // (6) all optional
const full: MyRequired<Config> = { host: "x", port: 80, debug: false }; // (7) none optional

// 8. Key remapping with `as` — rename keys while mapping
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};
// Getters<Config> = { getHost: () => string; getPort: () => number;
//                     getDebug: () => boolean | undefined }

// 9. `as` + `never` — filter keys out entirely
type OnlyStrings<T> = {
  [K in keyof T as T[K] extends string ? K : never]: T[K];
};
type S = OnlyStrings<Config>;                            // { host: string }
```

1. `Mutable<T>` — the interview answer. `-readonly` removes the modifier; `T[K]` keeps each value type unchanged.
2. `Mutable<Config>` = `{ host: string; port: number; debug?: boolean }` — note `debug?` survives: `-readonly` only touches `readonly`, not `?`.
3. Mutating `draft.port` compiles — the properties are writable again.
4. The original `Config` still forbids it: `Cannot assign to 'port' because it is a read-only property.` `Mutable` produced a *new* type; it never edits `Config` itself.
5. `?` after `]` adds optionality; `-?` removes it — the same modifier syntax as `readonly`, applied to `?`.
6. `patch` may omit everything — exactly what `Partial<Config>` does (literally: lib's `Partial` is this one-liner).
7. `full` must supply `debug` too — `Required` stripped the `?`.
8. `as` remaps the output key: `get${Capitalize<...>}` builds `"getHost"` etc. `string & K` narrows `K` to string keys because `Capitalize` requires strings.
9. The conditional `T[K] extends string ? K : never` keeps the key when the value fits and remaps to `never` (drops it) otherwise — this is how `PickByType` works.

## Problems

### Easy — write `Mutable<T>` and prove it works
**Problem:** `interface Frozen { readonly id: number; readonly name: string }`. Write `Mutable<T>` and create a mutable copy you can reassign fields on.
**Try this input:** `const f: Mutable<Frozen> = { id: 1, name: "a" }; f.id = 2;`
**Expected output:** `console.log(f.id, f.name)` → `2 a` — while `const g: Frozen` rejects `g.id = 2` at compile time.
**Solution:**
```typescript
interface Frozen {
  readonly id: number;
  readonly name: string;
}

type Mutable<T> = {
  -readonly [K in keyof T]: T[K];
};

const f: Mutable<Frozen> = { id: 1, name: "a" };
f.id = 2;                       // fine — id is writable now
// const g: Frozen = { id: 1, name: "b" };
// g.id = 2;                    // Error: Cannot assign to 'id' (read-only)
console.log(f.id, f.name);      // 2 a
```
**Logic explained:**
1. `keyof Frozen` = `"id" | "name"` — the loop iterates both keys.
2. `-readonly` strips the modifier on each output property; `T[K]` keeps `number`/`string`.
3. The original `Frozen` is untouched — mapped types always produce a *new* type.

### Medium — build `Mutable` plus `Nullable` and combine them
**Problem:** Write `Nullable<T>` (every value type gets `| null`) and combine it with `Mutable` so `Draft<T> = Mutable<Nullable<T>>` gives a fully editable draft of a frozen settings object.
**Try this input:** `interface Settings { readonly theme: string; readonly size: number }` → `Draft<Settings>`.
**Expected output:** `d.theme = null; d.size = 12;` both compile; `console.log(d.theme, d.size)` → `null 12`.
**Solution:**
```typescript
interface Settings {
  readonly theme: string;
  readonly size: number;
}

type Mutable<T> = { -readonly [K in keyof T]: T[K] };
type Nullable<T> = { [K in keyof T]: T[K] | null };
type Draft<T> = Mutable<Nullable<T>>;

const d: Draft<Settings> = { theme: null, size: 10 };
d.theme = null;   // writable AND nullable
d.size = 12;
console.log(d.theme, d.size);   // null 12
```
**Logic explained:**
1. `Nullable<Settings>` first maps to `{ readonly theme: string | null; readonly size: number | null }` — the plain homomorphic map preserves `readonly`.
2. `Mutable<…>` then strips `readonly` — composition order matters if you think about which step owns which transform, but since they touch different modifiers it commutes here.
3. The result `{ theme: string | null; size: number | null }` — two orthogonal edits composed by nesting mapped types, the way real utility types stack.

### Hard — `PickByType<T, V>`: keep only keys whose value extends `V`
**Problem:** Write `PickByType<T, V>` that keeps only properties whose value type extends `V`. `PickByType<{a: number; b: string; c: number}, number>` must be `{ a: number; c: number }`.
**Try this input:** `interface Mixed { id: number; label: string; count: number; flag: boolean }` with `V = number`.
**Expected output:** `const n: PickByType<Mixed, number> = { id: 1, count: 2 }` compiles; including `label` errors; `console.log(n.id, n.count)` → `1 2`.
**Solution:**
```typescript
type PickByType<T, V> = {
  [K in keyof T as T[K] extends V ? K : never]: T[K];
};

interface Mixed {
  id: number;
  label: string;
  count: number;
  flag: boolean;
}

const n: PickByType<Mixed, number> = { id: 1, count: 2 };
// const bad: PickByType<Mixed, number> = { id: 1, label: "x" };
//   Error: 'label' does not exist in type ...
console.log(n.id, n.count);   // 1 2
```
**Logic explained:**
1. `K in keyof T as <newKey>` — the `as` clause decides each output key. `T[K] extends V ? K : never` keeps the key when the value's type fits `V`, else maps to `never`.
2. Keys remapped to `never` are dropped from the output entirely — this is filtering, done with renaming. (`never` as a key produces no property.)
3. For `Mixed` with `V = number`: `id` (`number extends number` ✓), `count` (✓), `label`/`flag` map to `never` → gone. Result `{ id: number; count: number }`.
4. This is the engine behind real utility types like `type FnKeys<T> = keyof PickByType<T, Function>` — "give me just the method names."

## The 30-second interview answer

"A mapped type is a loop over a type's keys: `{ [K in keyof T]: T[K] }` binds `K` to each key in `keyof T` and emits a property with value type `T[K]` — an indexed access. On its own it's the identity clone; the power is in modifiers: `-readonly` strips readonly, `?` adds optionality, `-?` removes it, and `as` remaps or filters keys — `K as never` drops a key entirely. So `Mutable<T>` is `{ -readonly [K in keyof T]: T[K] }`, and `Partial`, `Required`, `Readonly`, `Pick`, `Record` in the standard library are all one-line mapped types. I use them for DTO variations — `Partial<Entity>` for patch payloads, `PickByType` for filtering fields — anywhere I'd otherwise duplicate a shape and let the copies drift apart."

## Follow-up trap

**"Why did `{ [K in keyof T]?: T[K] }` keep `readonly` but my `Mutable` needed `-readonly`?"** — Because the bare form is *homomorphic*: when you map directly over `keyof T` to `T[K]`, TypeScript copies each property's `readonly`/`?` modifiers automatically. Adding `?` stacks on top of what's copied; removing needs the explicit `-` prefix. Related trap: **"`as` in a mapped type vs `as` casts — same thing?"** — no relation. The `as` in `[K in keyof T as X]` is key *remapping* (renaming/filtering output keys); `x as T` is a runtime-erased assertion. And: **"difference between mapped types and `keyof` loops over values?"** — mapped types run entirely at compile time; they emit zero JavaScript and can't touch runtime objects. `Object.keys` loops real objects; `keyof` loops the *type* of those keys.
