# 19 — Generic constraints: `T extends { id: number }`

> **Interview question:** "What does `extends` mean inside a generic like `<T extends { id: number }>` — and how would you write a `getById` function that works on any type that has an `id`?"
> **What the interviewer is really testing:** Do you understand that unconstrained generics are *opaque* (you can't touch `.id` on a bare `T`) and that `extends` here means "must satisfy this shape," not class inheritance?

## Theory — what it is

A **generic** is a placeholder type — written as `<T>` — that the *caller* fills in when using your function or class. `function first<T>(arr: T[]): T` says "whatever element type the array has, that's what I return."

A **generic constraint** narrows what `T` is allowed to be. You write it with `extends`: `<T extends { id: number }>` means "T can be any type, *as long as* it has an `id` property of type `number`." It's a minimum requirement, not an exact match — a `User` with `id`, `name`, and `email` still qualifies because it *contains* `id: number`.

Important: `extends` here is **not** the same as `class Foo extends Bar` inheritance. In generic position it means "is assignable to" — the type must be structurally compatible with the constraint. TypeScript checks **structure** (does it have the required properties?), not class lineage.

Without a constraint, `T` is treated as a black box: the compiler knows nothing about it, so `item.id` is an error. With the constraint, the compiler *guarantees* `T` has `id: number`, so `item.id` is safe inside the function — while the caller still gets back their exact original type.

## Why it was needed

Generics alone create a dilemma. `function getById<T>(items: T[], id: number)` — inside the body, what can you do with each `item`? Nothing useful. The compiler can't let you write `item.id === id` because `T` might be `string`, `boolean`, or a function — none of which have `.id`.

You could fall back to `any[]`, but then callers lose all type safety: `getById(users, 5)` would return `any`, and `result.name.toUpperCase()` on a typo like `result.nmae` would compile fine and crash at runtime. Constraints give you the middle path: the function is flexible about *what* type it accepts, but strict about the *shape* it requires. The caller keeps their precise return type; the implementation gets the properties it needs.

## Where it's used in a real project

- **Repository/data-access layers:** `getById<T extends { id: number }>(items: T[], id: number)` works for `User`, `Product`, `Order` — anything with a numeric id — without duplicating code.
- **ORM-style helpers:** `mergeEntity<T extends object>(base: T, patch: Partial<T>)` — constraining to `object` prevents callers from passing `number` or `string` where spreading is expected.
- **Component props in React:** `function Table<T extends { id: string }>(props: { rows: T[]; renderRow: (row: T) => ReactNode })` — a table that accepts any row type as long as rows are keyed.
- **Logging/audit utilities:** `function logChange<T extends { updatedAt: Date }>(entity: T)` — guarantees a timestamp exists without caring what the entity is.

## Diagram

```
<T> unconstrained                     <T extends { id: number }> constrained

Caller passes:                        Caller passes:
  string   -> T = string   OK           string   -> has no .id        COMPILE ERROR
  number   -> T = number   OK           User     -> has id: number    OK
  User     -> T = User     OK           Product  -> has id: number    OK

Inside the function:                  Inside the function:
  item.id   -> ERROR:                   item.id   -> SAFE: guaranteed number
  "Property 'id' does not               item.name -> ERROR: not part of
   exist on type 'T'"                            the constraint

         anything goes in                    must satisfy the contract
         nothing known inside                contract usable inside
```

## Code — explained

```typescript
// 1. The constrained generic signature
function getById<T extends { id: number }>(items: T[], id: number): T | undefined {
  return items.find((item) => item.id === id);
}

// 2. Two different types that both satisfy the constraint
interface User {
  id: number;
  name: string;
  email: string;
}

interface Product {
  id: number;
  title: string;
  price: number;
}

const users: User[] = [
  { id: 1, name: "Amy", email: "amy@x.com" },
  { id: 2, name: "Bob", email: "bob@x.com" },
];

const products: Product[] = [
  { id: 10, title: "Keyboard", price: 50 },
  { id: 20, title: "Mouse", price: 25 },
];

// 3. One function, two concrete types — T is inferred per call
const u = getById(users, 2);        // u: User | undefined
const p = getById(products, 10);    // p: Product | undefined

console.log(u?.name);               // "Bob"      — name exists on User
console.log(p?.price);              // 50         — price exists on Product
console.log(getById(users, 99));    // undefined  — find() found nothing

// 4. This would NOT compile — string has no numeric id:
// getById(["a", "b"], 1);
// Error: Argument of type 'string[]' is not assignable to
//        parameter of type '{ id: number }[]'

// 5. Extra safety: you can't access properties outside the constraint
function bad<T extends { id: number }>(items: T[]): void {
  // items[0].name;  // ERROR — T might be { id: 1 } with no name at all
  items[0].id;      // OK — id is part of the contract
}
```

1. `function getById<T extends { id: number }>` declares a type parameter `T` that *must* be an object containing `id: number`. `extends` = "must be assignable to this shape."
2. `items: T[]` and `id: number` are the parameters; the return type `T | undefined` says "you get back the same element type you put in, or `undefined` if nothing matches" — `find` can always miss.
3. `item.id === id` compiles *because of* the constraint. On a bare `<T>`, this line is a type error — the compiler doesn't know `T` has `.id`.
4. `users` and `products` both satisfy `{ id: number }` structurally — neither needs to declare "I implement Idable." TypeScript checks shape, not names.
5. `getById(users, 2)` infers `T = User`, so `u` keeps `name` and `email`. The constraint sets a *floor*, not a ceiling — extra properties are preserved.
6. `u?.name` uses optional chaining because the return type includes `undefined`; this is the honest signature (a lookup can fail).
7. `getById(["a","b"], 1)` fails to compile: `string` doesn't satisfy `{ id: number }`. The constraint catches misuse at compile time.
8. Inside `bad`, `items[0].name` errors even though `User` has `name` — the function must work for *every* `T` that satisfies the constraint, including `{ id: number }` exactly.

## Problems

### Easy — write `getById`
**Problem:** Write `getById` that takes an array of objects (each having `id: number`) and a target id, returning the matching object or `undefined`.
**Try this input:**
```typescript
const books = [
  { id: 1, title: "Dune" },
  { id: 2, title: "Neuromancer" },
];
getById(books, 2);
```
**Expected output:** `{ id: 2, title: 'Neuromancer' }`
**Solution:**
```typescript
function getById<T extends { id: number }>(items: T[], id: number): T | undefined {
  return items.find((item) => item.id === id);
}

const books = [
  { id: 1, title: "Dune" },
  { id: 2, title: "Neuromancer" },
];
console.log(getById(books, 2));
```
**Logic explained:**
1. `T extends { id: number }` guarantees every element has a numeric `id`, so `item.id` is legal inside `find`.
2. `Array.prototype.find` returns the first match or `undefined` — which is exactly why the return type is `T | undefined`.
3. `T` is inferred as `{ id: number; title: string }`, so the result keeps `title` accessible.

### Medium — sort by a required key
**Problem:** Write `sortByName` that sorts any array of objects ascending by their `name: string` property, mutating nothing (return a new array).
**Try this input:**
```typescript
const cities = [
  { name: "Paris", country: "FR" },
  { name: "Berlin", country: "DE" },
  { name: "Madrid", country: "ES" },
];
```
**Expected output:** `[ { name: 'Berlin', ... }, { name: 'Madrid', ... }, { name: 'Paris', ... } ]`
**Solution:**
```typescript
function sortByName<T extends { name: string }>(items: T[]): T[] {
  return [...items].sort((a, b) => a.name.localeCompare(b.name));
}

const cities = [
  { name: "Paris", country: "FR" },
  { name: "Berlin", country: "DE" },
  { name: "Madrid", country: "ES" },
];
console.log(sortByName(cities));
```
**Logic explained:**
1. The constraint `{ name: string }` guarantees `.name` exists on every element.
2. `[...items]` copies the array so `sort` (which mutates in place) doesn't touch the caller's data.
3. `localeCompare` returns a proper string comparison (negative/zero/positive), unlike `a.name - b.name` which would be `NaN` on strings.

### Hard — pluck a key with two constraints
**Problem:** Write `pluckIds` that takes an array of entities where `id` can be `number` *or* `string`, and returns the array of ids with the correct union type preserved.
**Try this input:**
```typescript
const events = [
  { id: "evt_1", kind: "click" },
  { id: "evt_2", kind: "scroll" },
];
```
**Expected output:** `[ 'evt_1', 'evt_2' ]` — and the return type is `(number | string)[]`, not `any[]`.
**Solution:**
```typescript
function pluckIds<T extends { id: number | string }>(items: T[]): Array<T["id"]> {
  return items.map((item) => item.id);
}

const events = [
  { id: "evt_1", kind: "click" },
  { id: "evt_2", kind: "scroll" },
];
const ids = pluckIds(events);
console.log(ids);              // [ 'evt_1', 'evt_2' ]
// ids: (number | string)[] — actually narrowed to string[] here
// because T["id"] resolves to string for this call
```
**Logic explained:**
1. The constraint widens `id` to `number | string`, so both numeric and string ids qualify.
2. `T["id"]` is an **indexed access type** — "the type of property `id` on `T`." For this call `T = { id: string; kind: string }`, so `T["id"] = string` and the result is precisely `string[]`.
3. Using the constraint's union (`(number|string)[]`) as the return type would also compile, but `T["id"]` is sharper — it preserves exactly what the caller passed instead of always widening to the full union.

## The 30-second interview answer

"`extends` in a generic declares a constraint — a minimum shape the type argument must satisfy, checked structurally, not by inheritance. Without it, `T` is opaque: I can't access `.id` or anything else inside the function. With `<T extends { id: number }>`, the compiler guarantees `.id` exists so I can use it in the implementation, while callers still get their exact type back — `getById(users, 2)` returns `User | undefined`, not some generic `{ id: number }`. A `User` qualifies because it *has* `id: number`; extra properties are fine. And if a caller passes `string[]`, it's a compile error, which is exactly the misuse the constraint exists to catch."

## Follow-up trap

**"So does `T extends { id: number }` mean `T` inherits from that object type, like a class?"** No — that's the trap. `extends` in generic position means *assignable to / structurally compatible with*, not prototypal inheritance. `{ id: 1, extra: true }` satisfies it via **excess structure** (more properties is fine), and the check is on shape, not declarations — no `implements` keyword needed. A related trap: **"why is `items[0].name` an error inside the function when I only ever call it with `User`?"** Because the function body is checked once, generically, against the *constraint* — not against every call site. If callers could pass `{ id: number }` exactly, `.name` wouldn't exist. If you need `name`, either widen the constraint (`T extends { id: number; name: string }`) or move that logic to the call site where the concrete type is known.
