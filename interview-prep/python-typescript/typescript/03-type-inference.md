# 03 — Type inference

> **Interview question:** "How does TypeScript's type inference work, and where would you still write explicit annotations?"
> **What the interviewer is really testing:** That you know inference is automatic and *local*, and the judgment call: infer inside functions, annotate at module boundaries (public APIs, exported signatures).

## Theory — what it is

**Type inference** means TypeScript figures out types you didn't write. `let age = 30` gives `age` the type `number` — no annotation needed. Inference happens in several places:

- **Initializers:** `const name = "Ada"` → `name` is the literal type `"Ada"` (a `const` can't change, so the narrowest type is safe); `let name = "Ada"` → `string` (a `let` can be reassigned, so the type *widens* to allow other strings).
- **Return values:** `function add(a: number, b: number)` infers return type `number` from the returned expression.
- **Contextual typing:** inference flows *backwards* too — `users.map(u => u.name)` knows `u` is a `User` because `map` declared the callback's parameter type. You didn't annotate `u`; the context did.
- **Generics:** `["a", "b"].find(x => x === "a")` infers `T = string` from the array.

Inference is **local**, though. A function's inferred return type is computed from its body — if the body changes tomorrow (say, starts returning `null` in an edge case), the inferred return type silently changes too, and every caller's type changes with it. That's fine inside a module; it's dangerous at a module's *surface*.

So the working rule: **let inference handle locals; write annotations where your module meets the world** — exported function signatures, public class members, API response types — and wherever inference can't know your intent (empty literals, values that will be widened, parameters, which have no initializer to infer from).

## Why it was needed

Annotating everything would make TypeScript unusable — `const n: number = 30` is pure noise. Inference exists to keep TS feeling like JS: you get safety without ceremony in the 90% of code that's internal plumbing.

But inference has two failure modes that explicit annotations solve:

- **Silent contract drift.** `export function getUser()` infers its return from the implementation. A refactor that changes what's returned silently changes the public contract — callers may break far away, or worse, *not* break but re-infer a wider type than intended. Writing `: User` makes the contract explicit: the *body* is checked against it, and changes that break the contract error at the source.
- **Inference can't read your mind.** `const config = { method: "GET" }` infers `method: string`, not `method: "GET"` — object properties in a mutable binding widen. If you meant "exactly these literal values," you must say so (`as const`, or annotate `method: "GET"`). Similarly `const items = []` infers an evolving `any[]` — the compiler can't know what you plan to put in it.

Without the boundary-annotation convention, large codebases become fragile: every internal edit ripples outward through inferred public types, and `.d.ts` emit for libraries produces accidental, unstable public APIs.

## Where it's used in a real project

- **Exported functions get return types:** `export function parseUser(json: string): User` — the annotation is the contract; the body is checked against it.
- **Locals inferred:** inside the function, `const parts = json.split(",")` needs no `: string[]` — obvious and inferred.
- **Callbacks inferred contextually:** `orders.filter(o => o.total > 100)` — annotating `o` would be noise.
- **Literal-heavy configs annotated or `as const`:** fetch options, Redux action types, route tables — anywhere `"GET"` must stay `"GET"`.
- **Tests and scripts:** almost fully inferred — annotate only where inference gets confused.

## Diagram

```
        INSIDE a module                     BOUNDARY
  +-------------------------+      +-------------------------+
  | const x = 5             |      | export function f(): T  |
  | let s = "hi"   (string) |      | export interface Api {} |
  | return expr  --> infers |      | public methods, params  |
  | arr.map(x => ...)       |      +-----------+-------------+
  +-------------------------+                  |
            infer freely              annotate deliberately
            (local, cheap)            (contract, stable API,
                                       .d.ts emit, docs)

   widening gotcha:
   const o = { k: "v" }  -> { k: string }      (mutable -> widens)
   const o = { k: "v" } as const -> { readonly k: "v" } (frozen)
```

## Code — explained

```typescript
// 1. Inference doing its job — no annotations needed inside a function
export function summarizeOrder(order: Order): string {   // boundary: annotated
  const items = order.items;            // inferred: Item[]
  const count = items.length;           // inferred: number
  const names = items.map(i => i.name); // `i` inferred contextually: Item
  return `${count} items: ${names.join(", ")}`;         // return checked vs `string`
}

// 2. Widening — a common inference surprise
const options = { method: "GET" };      // inferred { method: string } — widened!
// fetch("/x", options);                // ERROR: string not assignable to "GET"|"POST"|...
const options2 = { method: "GET" } as const; // { readonly method: "GET" } — fixed

// 3. Literal inference with const vs let
const lit = "on";   // type "on"   (const: never reassigned -> literal kept)
let  str = "on";    // type string (let: may change -> widened)

interface Order { items: { name: string }[] }
interface Item  { name: string }
```

1. `summarizeOrder` is exported — a module boundary — so its signature (`order: Order` → `string`) is written explicitly. Anyone importing it sees a stable contract.
2. `items`, `count`, `names` are inferred — annotating them would add noise without adding safety.
3. `i => i.name` — the parameter type comes from `map`'s signature (contextual typing). Inference flows *into* callbacks.
4. `options.method` widened to `string` because object properties are mutable — TS assumes you might reassign. `fetch` requires a union of literals, hence the error. `as const` freezes inference at the literal.
5. `const` vs `let` shows the same widening rule on primitives: `const` keeps `"on"`, `let` widens to `string`.

## Problems

### Easy — predict the inferred type

**Problem:** Without running it, what are the inferred types of `a`, `b`, and `c` below? Then verify mentally by writing an assignment that fails for each.

```typescript
const a = "hello";
let b = "hello";
const c = { tag: "user" };
```

**Try this input:** `const x: "hello" = b` and `const y: "user" = c.tag`.
**Expected output:** Both lines error — `b` is `string` (not `"hello"`), `c.tag` is `string` (not `"user"`).
**Solution:**

```typescript
const a = "hello";            // type: "hello"  (const keeps literal)
let b = "hello";              // type: string   (let widens)
const c = { tag: "user" };    // type: { tag: string } (mutable prop widens)

const ok: "hello" = a;        // OK — a IS "hello"
// const x: "hello" = b;      // ERROR: string not assignable to "hello"
// const y: "user"  = c.tag;  // ERROR: string not assignable to "user"

const cFixed = { tag: "user" } as const; // { readonly tag: "user" }
const y2: "user" = cFixed.tag;           // OK now
```

**Logic explained:**
1. `const` bindings can never be reassigned, so keeping the literal type `"hello"` is sound — the value can only ever be `"hello"`.
2. `let` bindings can be reassigned to *any* string later, so inference widens to `string` to allow it.
3. Object properties are mutable even on a `const` object (`c.tag = "admin"` is legal), so `tag` widens to `string` — `as const` opts out.

### Medium — annotate the return type to stop a leak

**Problem:** `export function getDefaultUser()` was meant to return a `User` (`{ id, name }`). During a refactor someone added a debug field `passwordHash` to the returned object. Inference silently widened the public API — callers now depend on `passwordHash` existing. Fix it with one annotation.

**Try this input:** `export function getDefaultUser(): User { return { id: 1, name: "x", passwordHash: "secret" }; }`
**Expected output:** `error TS2353: Object literal may only specify known properties, and 'passwordHash' does not exist in type 'User'` — the leak is caught at the source.
**Solution:**

```typescript
interface User {
  id: number;
  name: string;
}

// Without `: User`, the inferred return is
// { id: number; name: string; passwordHash: string } — a leaked contract.
export function getDefaultUser(): User {
  return {
    id: 1,
    name: "x",
    // passwordHash: "secret", // <- now a compile error, not a silent API change
  };
}

export function displayName(u: User): string {
  return u.name.toUpperCase();
}

console.log(displayName(getDefaultUser())); // "X"
```

**Logic explained:**
1. Inferred return types are computed *from the body* — the body defines the contract by accident.
2. Writing `: User` flips it: the contract is declared, and the body is *checked against it*. Extra or missing fields error inside the function where the mistake lives.
3. This is the core of "annotate at boundaries": inference is still doing the work inside the function, but the module's surface is pinned down.

### Hard — the evolving array and the frozen config

**Problem:** Two inference traps in one exercise. (a) `const queue = []` — push strings later; why does `queue.push("job")` error, and how do you fix it? (b) Build a fetch wrapper `request(path, opts)` where `opts` must keep literal HTTP methods — show the widening bug and two ways to fix it.

**Try this input:** `queue.push("a")` on an un-annotated `[]`; `request("/u", { method: "GET" })`.
**Expected output:** (a) `error TS7034: Variable 'queue' implicitly has type 'any[]' in some locations` under `noImplicitAny`; (b) with the fix, compiles and `method` is `"GET"`.
**Solution:**

```typescript
// (a) `const queue = []` infers "evolving any[]" — under strict mode
//     calls like queue.push hit implicit-any errors (TS7034/TS7005).
//     Fix: tell the compiler the intent it can't see.
const queue: string[] = [];
queue.push("job");   // OK
// queue.push(42);   // ERROR: number not assignable to string — typed now

// (b) literal widening — annotate or freeze.
type Method = "GET" | "POST" | "DELETE";
interface RequestOpts { method: Method }

function request(path: string, opts: RequestOpts): string {
  return `${opts.method} ${path}`;
}

const bad = { method: "GET" };
// request("/u", bad);   // ERROR: { method: string } isn't RequestOpts

// Fix 1 — annotate the variable (declare the intent):
const good1: RequestOpts = { method: "GET" };
// Fix 2 — freeze inference at the literal:
const good2 = { method: "GET" } as const;

console.log(request("/u", good1), request("/u", good2)); // "GET /u GET /u"
```

**Logic explained:**
1. `[]` has no element to infer from. TS historically lets it "evolve" per push (implicit `any[]`); strict mode flags it. The compiler literally cannot know your intent — annotate.
2. `{ method: "GET" }` widens `method` to `string` because the property is mutable — the same rule as the Easy problem, now breaking a real call.
3. Two fixes, two philosophies: `RequestOpts` annotation says "this must satisfy the contract" (catches typos like `"GTE"`); `as const` says "freeze every literal exactly" (also freezes nested values — stronger than needed but precise). Pick annotations when there's a contract to satisfy; `as const` when you want the narrowest inferred type.

## The 30-second interview answer

"Inference means TypeScript deduces types from values — `let x = 5` is a `number`, return types come from returned expressions, callback params come contextually from signatures like `map`. It covers most code, so annotating locals is noise. The judgment call is at boundaries: I annotate exported function signatures and public APIs because inferred types are computed from the implementation — a body change silently changes the contract for every caller. I also annotate where inference can't know my intent: empty arrays, and literal values that would widen, which I fix with `as const` or a literal type."

## Follow-up trap

**"So should you annotate every function's return type?"** — The trap is answering with a purity rule instead of a trade-off. Strong answer: annotate *exported/public* functions (contract stability, better error locality, cleaner `.d.ts` emit — some lint setups enforce this via `explicit-function-return-type` scoped to exports); let inference handle private helpers and callbacks where the annotation duplicates information one line away. Bonus nuance that impresses: an explicit return type also makes errors *local* — a bug inside the function errors inside the function, instead of surfacing as a confusing mismatch at a distant call site.
