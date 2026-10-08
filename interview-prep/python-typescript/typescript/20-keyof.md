# 20 — `keyof`: typing a property accessor safely

> **Interview question:** "What is `keyof`, and how would you write `getProp<T, K extends keyof T>(obj: T, key: K): T[K]`?"
> **What the interviewer is really testing:** Do you know that `keyof` produces a union of an object's property names, and can you chain it with generics so the *key argument itself* is type-checked and the *return type* matches the property's type?

## Theory — what it is

`keyof` is a **type operator** that takes an object type and returns a **union** (a "one of these" type) of all its property names, as string literals. `keyof { name: string; age: number }` is `"name" | "age"`. It works at the type level only — it produces no runtime code; at runtime the closest equivalent is `Object.keys`, which returns `string[]`.

On its own, `keyof` is just a union of names. The real power comes from pairing it with generics in the `getProp` pattern: two type parameters, where the second (`K`) is **constrained** by `keyof` of the first (`T`). `K extends keyof T` means "the key argument must be a real property name of this specific object." Then `T[K]` — an **indexed access type**, read as "the type of property K on T" — gives the return type: if `K` is `"age"`, `T[K]` is `number`.

So the signature `getProp<T, K extends keyof T>(obj: T, key: K): T[K]` creates a *chain of inference*: the caller passes an object, TypeScript infers `T`, restricts the second argument to that object's real keys, and computes the exact return type for whichever key was passed. Misspell the key — `getProp(user, "naem")` — and it's a compile error, not `undefined` at runtime.

## Why it was needed

JavaScript developers write `obj[key]` constantly — in table renderers, form builders, sorters, serializers. Without `keyof`, typing this is a lose-lose choice:

1. `function getProp(obj: User, key: string)` — accepts any string including typos; return type must be a union of *all* property types (`string | number`), so callers lose precision.
2. `key: "name" | "age" | ...` — handwritten unions drift out of sync the moment someone adds a property to `User`; the type lies.
3. `any` — no checking at all; `getProp(user, "nmae")` returns `undefined` silently at runtime.

`keyof` solves all three: the key union is *derived* from the type, so it can never drift; invalid keys are compile errors; and `T[K]` returns exactly the property's type, so `getProp(user, "age")` is `number`, not `string | number`.

## Where it's used in a real project

- **Generic table/grid components:** `<Table<T> columns={[{ key: "email" } as keyof T ...]}>` — column definitions reference real field names; renaming a field breaks the columns at compile time, which is what you want.
- **Sorting/filter helpers:** `sortBy(users, "createdAt")` — `sortBy<T>(arr: T[], key: keyof T)` refuses `sortBy(users, "creatdAt")`.
- **Form libraries:** `setFieldValue("email", "a@b.com")` — libraries like React Hook Form type field paths with `keyof`-family techniques so the value's type must match the field's type.
- **i18n/message lookup:** `t("checkout.title")` where valid keys come from `keyof Messages` — autocomplete and typo-checking on translation keys.

## Diagram

```
interface User { id: number; name: string; email: string }

keyof User  =  "id" | "name" | "email"        (union of key literals)

getProp<T, K extends keyof T>(obj: T, key: K): T[K]

call: getProp(user, "email")
        T = User, K = "email"  (inferred from args)
        check: "email" ∈ keyof User ?  YES
        return type: T[K] = User["email"] = string

call: getProp(user, "emial")   <- typo
        check: "emial" ∈ keyof User ?  NO
        -> COMPILE ERROR: '"emial"' is not assignable to
           parameter of type '"id" | "name" | "email"'

keyof vs Object.keys:
  keyof User       -> type-level: "id" | "name" | "email"   (compile time only)
  Object.keys(user)-> runtime:    string[]                  (exists at runtime)
```

## Code — explained

```typescript
// 1. keyof produces a union of property-name literals
interface User {
  id: number;
  name: string;
  email: string;
}

type UserKeys = keyof User;   // "id" | "name" | "email"

// 2. The classic getProp: two generics, K constrained by keyof T
function getProp<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user: User = { id: 1, name: "Amy", email: "amy@x.com" };

// 3. Each call infers T and K; return type is the property's exact type
const name = getProp(user, "name");    // name: string
const id   = getProp(user, "id");      // id: number
console.log(name, id);                 // Amy 1

// 4. Typos are caught at compile time:
// getProp(user, "nmae");
// Error: Argument of type '"nmae"' is not assignable to
//        parameter of type '"id" | "name" | "email"'

// 5. keyof on unions and primitives
type AB = keyof ({ a: number } | { b: string }); // never — only common keys
type StrKeys = keyof string;   // "length" | "charAt" | "concat" | ...

// 6. Practical use: a typed sorter
function sortBy<T>(items: T[], key: keyof T): T[] {
  return [...items].sort((a, b) =>
    a[key] < b[key] ? -1 : a[key] > b[key] ? 1 : 0
  );
}

const users: User[] = [
  { id: 2, name: "Bob", email: "b@x.com" },
  { id: 1, name: "Amy", email: "a@x.com" },
];
console.log(sortBy(users, "id").map((u) => u.name)); // [ 'Amy', 'Bob' ]
// sortBy(users, "nmae"); // <- compile error, typo caught
```

1. `keyof User` evaluates to the union `"id" | "name" | "email"` — three string-literal types, usable anywhere a type is.
2. `K extends keyof T` links the two generics: after `T` is inferred from `obj`, `K` may only be one of `T`'s real keys.
3. `T[K]` is the indexed access type — "look up property K's type on T." With `K = "name"`, the return type is `string`.
4. `obj[key]` compiles inside the body precisely because `K extends keyof T` guarantees `key` is a valid index for `obj`.
5. `getProp(user, "nmae")` fails: `"nmae"` is not in the `keyof User` union. This is the entire point — the *argument* is type-checked, not just the return value.
6. `keyof (A | B)` yields only keys present on **every** member — `{a} | {b}` share none, so it's `never`. `keyof string` shows primitives have keys too (their methods).
7. `sortBy` shows `keyof T` without a second generic — fine when you don't need `T[K]`'s precision in the return type, just key validation.

## Problems

### Easy — write `getProp`
**Problem:** Write a type-safe `getProp` that returns `obj[key]` — the key must be a real property of the object, and the return type must match that property.
**Try this input:**
```typescript
const car = { make: "Toyota", year: 2020, electric: false };
getProp(car, "year");
```
**Expected output:** `2020` — and `getProp(car, "yaer")` must be a compile error.
**Solution:**
```typescript
function getProp<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const car = { make: "Toyota", year: 2020, electric: false };
console.log(getProp(car, "year"));   // 2020, typed as number
```
**Logic explained:**
1. `T` infers as `{ make: string; year: number; electric: boolean }` from `car`.
2. `K` must satisfy `keyof T` = `"make" | "year" | "electric"` — `"year"` passes, `"yaer"` doesn't.
3. `T[K]` resolves to `number` for `K = "year"`, so callers get `number`, not a union of all property types.

### Medium — setProp with matching value type
**Problem:** Write `setProp` that assigns `obj[key] = value`, where `value` must have the *correct type for that specific key* — `setProp(user, "id", "abc")` must fail because `id` is a number.
**Try this input:**
```typescript
const profile = { username: "dev_ak", level: 3 };
setProp(profile, "level", 5);     // OK
setProp(profile, "level", "5");   // must be a compile error
```
**Expected output:** `profile.level === 5`; the second call errors: `Argument of type 'string' is not assignable to parameter of type 'number'`.
**Solution:**
```typescript
function setProp<T, K extends keyof T>(obj: T, key: K, value: T[K]): void {
  obj[key] = value;
}

const profile = { username: "dev_ak", level: 3 };
setProp(profile, "level", 5);              // OK
// setProp(profile, "level", "5");         // ERROR: string ≠ number
console.log(profile.level);                // 5
```
**Logic explained:**
1. `value: T[K]` ties the value's type to whichever key was chosen — `"level"` requires `number`, `"username"` would require `string`.
2. `K extends keyof T` still guards the key argument; `T[K]` then guards the value argument.
3. This is the same pattern typed form libraries use: field name and field value can't drift apart.

### Hard — groupBy keyed on a real property
**Problem:** Write `groupBy` that groups an array of objects by a given key, returning a `Record` keyed by that property's values — and the key must actually exist on the objects.
**Try this input:**
```typescript
const tasks = [
  { id: 1, status: "done" },
  { id: 2, status: "todo" },
  { id: 3, status: "done" },
];
groupBy(tasks, "status");
```
**Expected output:** `{ done: [ { id: 1, status: 'done' }, { id: 3, status: 'done' } ], todo: [ { id: 2, status: 'todo' } ] }`
**Solution:**
```typescript
function groupBy<T, K extends keyof T>(
  items: T[],
  key: K
): Record<string, T[]> {
  const result: Record<string, T[]> = {};
  for (const item of items) {
    const groupKey = String(item[key]);
    (result[groupKey] ??= []).push(item);
  }
  return result;
}

const tasks = [
  { id: 1, status: "done" },
  { id: 2, status: "todo" },
  { id: 3, status: "done" },
];
console.log(groupBy(tasks, "status"));
// { done: [{id:1,...},{id:3,...}], todo: [{id:2,...}] }
// groupBy(tasks, "stats");  // compile error — typo rejected
```
**Logic explained:**
1. `K extends keyof T` guarantees `item[key]` is legal and `String(item[key])` produces a usable `Record` key.
2. `result[groupKey] ??= []` uses logical assignment: create the bucket on first sight, then `push`.
3. Return type `Record<string, T[]>` is honest — property values can be any primitive, so keys stringify; a fully literal-keyed result would need `Extract<T[K], PropertyKey>` (a level deeper than most interviews go, but worth mentioning).

## The 30-second interview answer

"`keyof` takes an object type and returns a union of its property names as string literals — `keyof User` is `"id" | "name" | "email"`. Its main use is constraining a second generic, like `getProp<T, K extends keyof T>(obj: T, key: K): T[K]`. `T` infers from the object, `K` is restricted to that object's real keys so typos are compile errors, and `T[K]` — the indexed access type — returns the exact type of the chosen property instead of a union of all of them. It's what makes helpers like `sortBy(users, 'createdAt')` or typed form `setValue` calls safe: the key argument itself is validated. And it's purely compile-time — `keyof` emits no JavaScript; `Object.keys` is the runtime cousin and just gives you `string[]`."

## Follow-up trap

**"What's the difference between `keyof` and `Object.keys`?"** The classic trap — one is a type operator, the other is a runtime function, and their results *disagree*. `keyof User` is the union `"id" | "name" | "email"`, erased at compile time. `Object.keys(user)` returns `string[]` at runtime — and notably it's typed `string[]`, *not* `keyof`-precise, because runtime objects can carry extra keys beyond their static type (e.g. a subtype). If an interviewer pushes further: **`keyof` on a union type gives only keys common to all members** (`keyof ({a} | {b})` is `never`), while `keyof` on an intersection gives all keys. And `keyof any` is `string | number | symbol` — the full domain of valid JS property keys, which is why `PropertyKey` exists as a built-in alias for that union.
