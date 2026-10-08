# 23 — Generic interfaces: `interface ApiResponse<T> { data: T; error?: string }`

> **Interview question:** "How do you write a generic interface like `ApiResponse<T>`, and why would you?"
> **What the interviewer is really testing:** Do you understand that an interface can be *parameterized* — a reusable shape template where the caller fills in the payload type — and that this is the backbone of typed API layers?

## Theory — what it is

A **generic interface** is an interface with a type parameter — a "shape template." `interface ApiResponse<T> { data: T; error?: string }` doesn't describe one type; it describes a *family* of types. Each time you write `ApiResponse<User>` or `ApiResponse<Product[]>`, TypeScript substitutes that argument for every `T` in the body and produces a concrete type: `ApiResponse<User>` is `{ data: User; error?: string }`.

Two jargon points. The **type parameter** (`T`) is the placeholder; the **type argument** (`User` in `ApiResponse<User>`) is what the caller supplies. And unlike generic *functions* — where `T` can be inferred from arguments — a generic *interface* always needs its argument written out (or defaulted, `<T = unknown>`). There's nothing to infer from when you annotate `const r: ApiResponse = ...`.

Why interfaces specifically (not just `type` aliases)? Interfaces can be **extended**, **implemented by classes**, and **declaration-merged**. `interface PagedResponse<T> extends ApiResponse<T> { page: number }` composes templates. Practically, `interface` and `type` both support generics; interfaces edge ahead for object shapes because of `extends`/`implements` ergonomics and better error messages.

## Why it was needed

Every API returns envelopes: `{ data: ..., status: ..., error: ... }`. Without generics you either duplicate the envelope per payload (`UserResponse`, `ProductResponse`, `OrderResponse` — twenty near-identical interfaces that drift apart when someone adds `requestId` to one) or give up and write `data: any`, losing autocomplete and typo-checking on the most important field.

`ApiResponse<T>` solves it with one definition: the envelope shape lives in a single place, the payload is a parameter. Add a `meta` field once and every endpoint's response type updates. It's the same logic as generic functions (file 19) lifted from functions to *type declarations*: the structure is fixed, one slot varies.

## Where it's used in a real project

- **HTTP client layers:** `async function get<T>(url: string): Promise<ApiResponse<T>>` — `get<User>("/me")` gives you `res.data.name` fully typed; this is how typed `fetch`/`axios` wrappers work.
- **Paginated APIs:** `interface Page<T> { items: T[]; total: number; page: number }` — `Page<User>`, `Page<Order>` share pagination logic.
- **Discriminated result types:** `type Result<T, E = Error> = { ok: true; value: T } | { ok: false; error: E }` — Rust-style error handling in TS.
- **Form/table state:** `interface FieldState<T> { value: T; dirty: boolean; error?: string }` — one state shape reused for `FieldState<string>` (name field), `FieldState<Date>` (birthday field).
- **Cache layers:** `interface CacheEntry<T> { value: T; expiresAt: number }` — `CacheEntry<User>` vs `CacheEntry<Config>` in one `Map`.

## Diagram

```
interface ApiResponse<T> { data: T; error?: string; status: number }
                    ^
                    one template, infinitely many concrete types

ApiResponse<User>         ApiResponse<Product[]>       ApiResponse<void>
{ data: User;             { data: Product[];           { data: void;
  error?: string;           error?: string;              error?: string;
  status: number }          status: number }             status: number }

Flow at a call site:
  get<User>("/api/me")
      -> Promise<ApiResponse<User>>
      -> res.data is User  -> res.data.name type-checks
      -> res.error?: string — envelope fields identical everywhere

Extending the template:
  interface Paged<T> extends ApiResponse<T[]> { page: number; total: number }
      Paged<User> = { data: User[]; error?: string; status: number;
                      page: number; total: number }
```

## Code — explained

```typescript
// 1. The generic interface: T is a slot the caller fills
interface ApiResponse<T> {
  data: T;
  status: number;
  error?: string;
}

interface User {
  id: number;
  name: string;
}

// 2. Each usage substitutes a concrete type for T
const userResp: ApiResponse<User> = {
  data: { id: 1, name: "Amy" },
  status: 200,
};
const listResp: ApiResponse<User[]> = {
  data: [{ id: 1, name: "Amy" }, { id: 2, name: "Bob" }],
  status: 200,
};
console.log(userResp.data.name);              // Amy
console.log(listResp.data.length);            // 2

// 3. A typed fetch wrapper — the real-world payoff
async function get<T>(url: string): Promise<ApiResponse<T>> {
  const res = await fetch(url);
  const body = await res.json();
  return { data: body as T, status: res.status };
}
// get<User>("/api/me") then .data.name compiles; .data.nmae errors

// 4. Extending a generic interface — compose templates
interface Paged<T> extends ApiResponse<T[]> {
  page: number;
  total: number;
}
const page: Paged<User> = {
  data: [{ id: 1, name: "Amy" }],
  status: 200,
  page: 1,
  total: 40,
};
console.log(page.total, page.data[0].name);   // 40 Amy

// 5. Multiple type params: key and value vary independently
interface KV<K extends string, V> {
  key: K;
  value: V;
}
const entry: KV<"theme", "dark" | "light"> = { key: "theme", value: "dark" };
console.log(entry.key, entry.value);          // theme dark
```

1. `interface ApiResponse<T>` declares `T` once and uses it inside — every concrete instantiation swaps in the real type.
2. `ApiResponse<User>` vs `ApiResponse<User[]>` shows the same envelope serving a single entity or a collection — zero duplication.
3. `get<T>` is where the payoff lands: the *function's* generic flows into the *interface's* generic, so the endpoint's payload type travels from call site (`get<User>`) to `res.data`.
4. `Paged<T> extends ApiResponse<T[]>` composes generics — note `T[]`: the parent's `data` becomes an array of `T`. Interface inheritance works parametrically.
5. `KV<K extends string, V>` shows multiple parameters with a constraint on `K` — interfaces support the full generic toolkit (constraints, defaults, multiple params).

## Problems

### Easy — instantiate a generic interface
**Problem:** Define `ApiResponse<T>` with `data: T`, `ok: boolean`, optional `message: string`. Create one response for a `Product` (`{ sku: string; price: number }`) and one for a list of products.
**Try this input:**
```typescript
const one: ApiResponse<Product> = { data: { sku: "A1", price: 9 }, ok: true };
const many: ApiResponse<Product[]> = { data: [], ok: true };
```
**Expected output:** `console.log(one.data.price, many.data.length)` → `9 0`.
**Solution:**
```typescript
interface ApiResponse<T> {
  data: T;
  ok: boolean;
  message?: string;
}
interface Product {
  sku: string;
  price: number;
}
const one: ApiResponse<Product> = { data: { sku: "A1", price: 9 }, ok: true };
const many: ApiResponse<Product[]> = { data: [], ok: true };
console.log(one.data.price, many.data.length);   // 9 0
```
**Logic explained:**
1. `T` is substituted with `Product` in `one` — `data.price` is `number`.
2. `T = Product[]` in `many` — `data` is an array, `.length` is legal.
3. The envelope (`ok`, `message?`) is identical for both — that's the reuse.

### Medium — generic repository interface
**Problem:** Write `interface Repository<T>` with `find(id: number): T | undefined`, `save(item: T): void`, and `all(): T[]`. Then implement it in-memory for `User`.
**Try this input:** save two users, `find(1)`, `all()`.
**Expected output:** `find(1)` → `{ id: 1, name: 'Amy' }`; `all().length` → `2`.
**Solution:**
```typescript
interface Repository<T> {
  find(id: number): T | undefined;
  save(item: T): void;
  all(): T[];
}
interface User {
  id: number;
  name: string;
}
class UserRepo implements Repository<User> {
  private items: User[] = [];
  find(id: number) {
    return this.items.find((u) => u.id === id);
  }
  save(item: User) {
    this.items.push(item);
  }
  all() {
    return this.items;
  }
}
const repo = new UserRepo();
repo.save({ id: 1, name: "Amy" });
repo.save({ id: 2, name: "Bob" });
console.log(repo.find(1));          // { id: 1, name: 'Amy' }
console.log(repo.all().length);     // 2
```
**Logic explained:**
1. `Repository<T>` defines the contract once; `implements Repository<User>` makes the compiler check `UserRepo` method-by-method against it.
2. Because `T = User`, `find` must return `User | undefined` — the interface generic propagates into every signature.
3. A `ProductRepo implements Repository<Product>` would reuse the identical contract — the pattern scales per entity.

### Hard — discriminated generic result
**Problem:** Model a result that's either success or failure: `type Result<T, E = string> = { ok: true; data: T } | { ok: false; error: E }`. Write `unwrap<T, E>(r: Result<T, E>): T` that returns data or throws the error — correctly narrowed.
**Try this input:** `unwrap({ ok: true, data: 5 })` and `unwrap({ ok: false, error: "boom" })`.
**Expected output:** first returns `5`; second throws `"boom"`.
**Solution:**
```typescript
type Result<T, E = string> =
  | { ok: true; data: T }
  | { ok: false; error: E };

function unwrap<T, E>(r: Result<T, E>): T {
  if (r.ok) return r.data;          // narrowed to { ok: true; data: T }
  throw r.error;                    // narrowed to { ok: false; error: E }
}

console.log(unwrap({ ok: true, data: 5 }));    // 5
try {
  unwrap<number>({ ok: false, error: "boom" });
} catch (e) {
  console.log("caught:", e);                   // caught: boom
}
```
**Logic explained:**
1. `Result<T, E = string>` is a **discriminated union**: `ok` is the discriminator. When `r.ok` is true, TypeScript narrows to the first member, so `r.data` is legal and `r.error` is an error — both compile-time safe.
2. `unwrap` returns `T` — for `data: 5`, callers get `number` back; generics preserve precision through the union.
3. `E = string` defaults the error channel; `Result<User, ApiError>` overrides it. This pattern (aka the `Either`/`Result` type) is how mature TS codebases handle failures without exceptions leaking into types.

## The 30-second interview answer

"A generic interface is a shape template: `interface ApiResponse<T> { data: T; error?: string }` defines the envelope once and lets each call site fill in the payload — `ApiResponse<User>` has `data: User`, `ApiResponse<Product[]>` has `data: Product[]`. The win is single-source structure: add a `meta` field once and every endpoint type updates, versus duplicating `UserResponse`, `ProductResponse` and watching them drift. Interfaces compose well — `interface Paged<T> extends ApiResponse<T[]>` reuses the parent parametrically, and classes can `implements Repository<User>`. It's the foundation of typed API layers: `get<User>(url)` returns `Promise<ApiResponse<User>>`, so `res.data.name` autocompletes and typos are compile errors. The difference from a generic function: interface generics must be spelled out explicitly — there's nothing to infer them from."

## Follow-up trap

**"Interface vs `type` alias for generics — which and why?"** For object shapes, mostly interchangeable: `type ApiResponse<T> = {...}` works identically for instantiation. Interfaces win on `extends`/`implements` ergonomics, declaration merging (two `interface ApiResponse` declarations merge — types can't), and slightly better error messages/classes integration. `type` wins when the generic is a *union*, conditional, or mapped type — `interface` can't express `type Result<T> = {ok:true;data:T} | {ok:false;error:string}` (unions aren't object shapes). Second trap: **"can `T` be inferred when you write `const r: ApiResponse = ...`?"** No — interfaces require the argument or a default (`<T = unknown>`); there's no call site to infer from. If you write a bare generic interface without a default, TypeScript errors: `Generic type 'ApiResponse' requires 1 type argument(s)`.
