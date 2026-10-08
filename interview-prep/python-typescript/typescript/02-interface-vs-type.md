# 02 — `interface` vs `type`

> **Interview question:** "What's the difference between `interface` and `type` in TypeScript, and when do you use each?"
> **What the interviewer is really testing:** Whether you know the two features mostly overlap, and can name the real differences — declaration merging, unions/primitives, `extends` vs `&` — plus a sane team convention.

## Theory — what it is

Both `interface` and `type` let you give a name to a shape so you can reuse it. For plain object shapes they are nearly interchangeable:

```typescript
interface UserI { id: number; name: string }
type      UserT = { id: number; name: string }
```

`interface` is the older, object-focused keyword. Its special powers: it can be **extended** (`interface Admin extends User`) and it supports **declaration merging** — if you declare `interface Config` twice in the same scope, TypeScript merges the members into one interface instead of erroring. That second power is what lets library authors and `.d.ts` files be *augmented* by consumers.

`type` creates a **type alias** — a name for *any* type, not just objects. Only `type` can name a **union** (`type Status = "a" | "b"`), a primitive (`type ID = string`), a tuple (`type Point = [number, number]`), or a function signature (`type Handler = (e: Event) => void`). Aliases combine with `&` (intersection) and `|` (union). Types do **not** merge — redeclaring `type X` in the same scope is a duplicate-identifier error.

Practical rule of thumb most teams use: **`interface` for object shapes you expect to be extended or implemented (public APIs, class contracts), `type` for unions, tuples, function types, and composed types.** Performance and error-message differences exist but are minor; consistency matters more than the choice.

## Why it was needed

JavaScript objects are just bags of keys, and early TypeScript needed a way to describe them — `interface` did that. But real programs also need names for things that aren't objects: "a string OR a number," "a pair of coordinates," "either Success or Failure." `type` fills that gap.

The concrete differences exist because of what each was built for:

- **Declaration merging** exists so interfaces can describe things that grow — like the DOM's `Window`, or an Express `Request` that middleware adds fields to. Two declarations in different files merge into one. Without it, library types would be sealed and un-augmentable.
- **Unions via `type`** exist because "this value is one of several shapes" is not an object shape at all — an interface literally cannot express `A | B`.
- **`extends` vs `&`:** `interface A extends B` is checked at *declaration* time (conflicting members error immediately), while `type A = B & C` is computed lazily — you can build contradictory types that only error when used. So `extends` fails earlier and gives better error messages; `&` is more flexible (works on unions, primitives).

## Where it's used in a real project

- **Interfaces for public contracts:** `interface Props { ... }` for React component props, `interface Repository { find(id: string): Promise<User> }` implemented by classes — consumers may extend them.
- **Declaration merging to augment libraries:** adding `user?: AuthUser` to Express's `Request` interface in a `express.d.ts` file — the classic real-world use of merging.
- **Types for domain unions:** `type PaymentMethod = Card | Cash | Crypto` — impossible with `interface`.
- **Types for functions and tuples:** `type Comparator<T> = (a: T, b: T) => number`, `type RGB = [number, number, number]`.
- **Types for composition:** `type UserWithPosts = User & { posts: Post[] }`, `type Preview = Pick<User, "id" | "name">`.

## Diagram

```
                 describe object shapes?
                 +-----------+-----------+
                 | YES (both work)       |
                 v                       v
           interface                 type alias
   +-----------------------+  +---------------------------+
   | extends B             |  | unions:  A | B            |
   | declaration merging   |  | tuples:  [number, string] |
   | implements (classes)  |  | primitives: type ID = str |
   | better decl-time errs |  | functions: (x) => void    |
   +-----------------------+  | intersections: A & B      |
                              | NO merging (dup = error)  |
                              +---------------------------+

   Only `type` can do:  |   &   [tuples]   primitives   fn types
   Only `interface`:    declaration merging (augmentation)
```

## Code — explained

```typescript
interface User {
  id: number;
  name: string;
}

interface Admin extends User {   // interface grows via `extends`
  role: "admin" | "superadmin";
}

// Declaration merging: a second `interface User` MERGES with the first.
interface User {
  email: string;                 // now User = { id, name, email }
}

type Status = "idle" | "loading" | "done";   // only `type` can name a union
type Handler = (s: Status) => void;          // ...or a function signature
type AdminAlt = User & { role: string };     // `&` composes without `extends`

const a: Admin = { id: 1, name: "Ada", email: "a@x", role: "admin" };
// type Status = "x";  // ERROR: duplicate identifier — types do NOT merge
```

1. `interface User` declares an object shape — the base contract.
2. `interface Admin extends User` inherits all of `User`'s members; conflicts (e.g. `id: string`) would error at declaration time.
3. The second `interface User` doesn't replace the first — it **merges**, adding `email`. This is the feature `type` lacks; it's how `.d.ts` augmentation works.
4. `type Status = ...` is a union — an interface can't express "one of several literals," so `type` is required here.
5. `type AdminAlt = User & { role: string }` shows the alias-style composition; roughly equivalent to `extends` for objects, but computed differently (conflicts collapse to `never` rather than erroring early).
6. Redeclaring `type Status` is a hard error — aliases are single-shot names, which is actually safer: nobody can silently grow your union.

## Problems

### Easy — same shape, both ways

**Problem:** Define a `Product` with `sku: string`, `price: number`, and `inStock: boolean` — once as an interface, once as a type alias — and prove a value satisfies both.

**Try this input:** `const p = { sku: "A1", price: 9.99, inStock: true }` assigned to both types.
**Expected output:** Compiles cleanly; `console.log` prints the object.
**Solution:**

```typescript
interface ProductI {
  sku: string;
  price: number;
  inStock: boolean;
}

type ProductT = {
  sku: string;
  price: number;
  inStock: boolean;
};

const p = { sku: "A1", price: 9.99, inStock: true };

const pi: ProductI = p; // OK — structural typing: shapes match
const pt: ProductT = p; // OK

console.log(pi, pt);
// { sku: 'A1', price: 9.99, inStock: true } { sku: 'A1', price: 9.99, inStock: true }
```

**Logic explained:**
1. TypeScript is *structurally* typed — `p` works for both because its shape matches, not because of the name it was declared with.
2. For plain object shapes, `interface` and `type` are interchangeable — the differences only appear with unions, merging, etc.
3. This is why style guides exist: when both work, pick one convention and be consistent.

### Medium — augment, don't edit

**Problem:** A shared `interface AppConfig` lives in a file you shouldn't modify. You need to add a `featureFlags: string[]` field for your module — *without* touching the original declaration.

**Try this input:** declare a second `interface AppConfig` in your file and construct a config with all fields.
**Expected output:** Compiles cleanly — the two declarations merged into one shape; a config missing either half errors.
**Solution:**

```typescript
// ---- shared/config.d.ts (imagine this file is read-only to you) ----
interface AppConfig {
  env: "dev" | "prod";
  apiUrl: string;
}

// ---- your file: augment via declaration merging ----
interface AppConfig {
  featureFlags: string[];   // merged INTO the interface above
}

const config: AppConfig = {
  env: "dev",
  apiUrl: "http://localhost:3000",
  featureFlags: ["new-checkout"], // required — both declarations apply
};

console.log(config.featureFlags); // ["new-checkout"]

// This is exactly how you augment Express:
//   declare module "express" { interface Request { user?: AuthUser } }
```

**Logic explained:**
1. Two `interface` declarations with the same name in compatible scopes merge into a single interface containing all members — `AppConfig` now requires `env`, `apiUrl`, *and* `featureFlags`.
2. This is impossible with `type` — a second `type AppConfig` is a duplicate-identifier error.
3. It's the mechanism behind library augmentation (`declare module` + merged interfaces), ambient globals like `Window`, and `Array.prototype` extensions in `.d.ts` files.

### Hard — pick the right tool per job

**Problem:** Model domain events: every event has `id` and `timestamp`; a `UserCreated` adds `email`, an `OrderPlaced` adds `total`. A `DomainEvent` can be *either*. Then write `handle(e: DomainEvent)` that safely reads `email`/`total`. Which parts must be `interface` vs `type`, and why?

**Try this input:** `handle({ id: "1", timestamp: 0, kind: "order", total: 42 })`.
**Expected output:** Prints `order total: 42`; accessing `e.total` outside the `"order"` branch is a compile error.
**Solution:**

```typescript
interface BaseEvent {
  id: string;
  timestamp: number;
}

interface UserCreated extends BaseEvent {
  kind: "user";
  email: string;
}

interface OrderPlaced extends BaseEvent {
  kind: "order";
  total: number;
}

// MUST be `type` — an interface cannot be a union:
type DomainEvent = UserCreated | OrderPlaced;

function handle(e: DomainEvent): string {
  if (e.kind === "user") {
    return `user email: ${e.email}`; // narrowed to UserCreated
  }
  return `order total: ${e.total}`;  // narrowed to OrderPlaced
}

console.log(handle({ id: "1", timestamp: 0, kind: "order", total: 42 }));
// "order total: 42"
```

**Logic explained:**
1. Variants use `interface ... extends BaseEvent` — shared fields are declared once, and `extends` errors early if a variant conflicts with the base.
2. `DomainEvent` **must** be a `type` alias — unions are the one thing interfaces fundamentally can't express.
3. `e.kind` is the discriminant: checking it *narrows* the union to one variant, unlocking `email` or `total` safely. This "interfaces for variants + type alias for the union" pattern is the idiomatic split you'll see in real codebases.

## The 30-second interview answer

"For object shapes they're interchangeable — both are checked structurally. The real differences: `interface` supports declaration merging, so two declarations combine — that's how library augmentation like adding `user` to Express's `Request` works — and it extends with `extends`, which validates conflicts at declaration time. `type` can name *any* type — unions, tuples, primitives, function signatures — which interfaces can't, and aliases don't merge, so they're closed to outside edits. My convention: interfaces for object contracts meant to be implemented or extended, types for unions and composed types. On a team, consistency matters more than which you pick."

## Follow-up trap

**"Which should you use for a public library API — and why might `interface` be better there?"** — They're probing whether you understand *open vs closed* contracts. Answer: `interface`, because declaration merging intentionally lets consumers augment your types (the Express `Request` pattern) — a feature, not a bug, for extensible library surfaces. Counterpoint worth raising: for app-internal domain models, `type` being *closed* is a feature — nobody can silently grow your `Status` union from another file. Also know the micro-difference interviewers love: `extends` errors eagerly on conflicts; `&` produces an intersection that may quietly reduce a property to `never` and only fail at use sites.
