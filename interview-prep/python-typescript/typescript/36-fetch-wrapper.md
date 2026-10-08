# 36 — Typing a fetch wrapper: why `Promise<T>` is a lie without runtime validation

> **Interview question:** "You write `async function get<T>(url: string): Promise<T>` — what's wrong with this signature?"
> **What the interviewer is really testing:** Whether you understand the generic lies: `get<User>` claims `User` comes back, but `res.json()` returns `any` — the server could send *anything*. The type is a promise the compiler can't keep; without runtime validation, `T` is just a cast wearing a generic costume.

## Theory — what it is

The canonical "typed fetch" wrapper:

```typescript
async function get<T>(url: string): Promise<T> {
  const res = await fetch(url);
  return res.json();          // res.json() returns Promise<any>
}

interface User {
  name: string;
}

async function demoGet() {
  const user = await get<User>("/api/user/1");   // typed as User
  user.name.toUpperCase();                        // compiles — but is it true?
}
```

The problem in three parts:

- **`res.json()` is `Promise<any>`.** `any` is assignable to `T` — the compiler happily "returns" `User` while at runtime the body could be an error object, an array, `null`, or a different shape entirely.
- **The generic doesn't check anything — it *asserts*.** `get<User>` doesn't fetch a `User`; it fetches *whatever the server sent* and *labels* it `User`. `T` is caller-chosen, not server-verified.
- **The lie compounds downstream.** Once typed `User`, every use — `.name.toUpperCase()`, passing to components — is trusted. A shape mismatch crashes *far* from the fetch, in a component that "can't possibly get bad data."

This is `as` at a distance: `get<User>(url)` ≈ `(await fetch(url)).json() as User`. The generic just makes the cast look respectable.

**The fix — validation at the boundary.** Two levels:

1. **Manual type guard** — `function isUser(x: unknown): x is User`, then `if (!isUser(data)) throw`. The type becomes *earned*.
2. **Schema library (Zod/io-ts)** — `UserSchema.parse(data)` throws on mismatch *and* returns `User` — validation and typing fused: `z.infer<typeof Schema>` *is* the type.

## Why it was needed

TypeScript's types are erased at runtime — `interface User` leaves zero trace in the emitted JS. So at the network boundary, types can't *descend* from the wire; they have to be *built* from untrusted data. `JSON.parse` and `res.json()` are typed `any` precisely because nothing can be known statically about a response body.

Early TS codebases typed the *happy path* and prayed. The recognition that "HTTP responses are `unknown`" — that `get<T>` is a footgun — pushed two idioms: make `json()` return `unknown` (forces you to validate) and let schema parsers return typed data (Zod's `parse` returns the inferred type). The type `User` then means "something that passed the validator," which is the only honest meaning it can have.

## Where it's used in a real project

- **API layers:** every fetch wrapper that returns `Promise<T>` unchecked — the most common typing lie in production code.
- **Zod/io-ts/valibot at the boundary:** `const user = UserSchema.parse(await res.json())` — parse-or-throw at the edge, trust inside.
- **Type guards for cheap validation:** `isUser(x)` in legacy code where adding a library isn't an option.
- **Error-shape checking:** validating the *error* response too — `{ error: string }` — because `res.ok` being false means the body is a different type entirely.
- **tRPC / generated clients:** the industrial answer — types shared end-to-end so the generic isn't a guess, it's generated from the same schema as the server.

## Diagram

```
THE LIE:
  get<User>("/api/user/1")
      │  caller picks T = User
      ▼
  fetch -> res.json() : any ──assignable to──► T = User
      │                                         │
      │  at runtime body could be:              │  compiler believes: User
      │    { id: "1", name: "Ana" }      ✅     │
      │    { error: "not found" }        💥     │  name.toUpperCase() — crash
      │    null                          💥     │
      ▼                                         ▼
   THE DATA            ≠ asserted to be ≠     THE TYPE

THE FIX — validate at the boundary:
  res.json() : unknown
      │
      ▼  schema.parse(data)  or  isUser(data) guard
   ┌──┴──────────────┐
   │ passes -> User  │  now the type is EARNED, not asserted
   │ fails  -> throw │  error at the boundary, not in a component
   └─────────────────┘
```

## Code — explained

```typescript
interface User {
  id: string;
  name: string;
  age: number;
}

// 1. The lying wrapper — T asserts, doesn't verify
async function getUnsafe<T>(url: string): Promise<T> {
  const res = await fetch(url);
  return res.json();                      // any -> T, no questions asked
}

// 2. Honest version 1: return unknown, force callers to validate
async function getRaw(url: string): Promise<unknown> {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);   // (3) check res.ok too
  return res.json();                    // unknown — caller must narrow
}

// 4. Type guard — the cheap validation
function isUser(x: unknown): x is User {
  return (
    typeof x === "object" && x !== null &&
    typeof (x as User).id === "string" &&
    typeof (x as User).name === "string" &&
    typeof (x as User).age === "number"
  );
}

async function getUser(url: string): Promise<User> {
  const data = await getRaw(url);          // unknown
  if (!isUser(data)) {                     // (5) validate
    throw new Error("API response is not a User");
  }
  return data;                             // data: User — EARNED
}

// 6. Honest version 2 (Zod) — schema does guard + type in one:
//   const UserSchema = z.object({ id: z.string(), name: z.string(), age: z.number() });
//   type User = z.infer<typeof UserSchema>;
//   const user = UserSchema.parse(await res.json());  // throws OR returns User

// The difference in caller experience:
async function demo() {
  // const u = await getUnsafe<User>("/x");   // typed User — maybe isn't
  const u = await getUser("/x");               // typed User — PROVEN is
  u.name.toUpperCase();                        // actually safe now
}
```

1. `getUnsafe<T>` — the generic is a *caller assertion*, not a check. The function returns `any` dressed as `T`; TypeScript can't and doesn't verify.
2. `getRaw` returns `Promise<unknown>` — the *honest* type: "I fetched something; what it is, we don't know." `unknown` forces every consumer to narrow before use.
3. `res.ok` check matters too — a 404 body is an *error shape*, not your `T`; treating non-ok responses as `T` is a second lie layered on the first.
4. `isUser` is a user-defined type guard — `x is User` teaches the compiler "if this returns true, narrow to `User`." Manual, verbose, but zero dependencies.
5. `if (!isUser(data)) throw` — the failure happens *at the boundary*, milliseconds after the fetch, with a clear message — not deep inside a component an hour later.
6. Zod's `parse` is the same idea, industrialized: the schema is both the validator *and* the type source (`z.infer`), so they can never drift apart.

## Problems

### Easy — fix the lying generic
**Problem:** `async function get<T>(url): Promise<T> { return (await fetch(url)).json(); }` is called as `get<number[]>("...")`. Show how it fails when the API returns `{ ids: [1,2] }` instead of an array — then fix the signature to be honest.
**Try this input:** API returns `{ ids: [1,2] }`, caller does `arr.map(...)`.
**Expected output:** the unsafe version crashes `arr.map is not a function`; the honest version forces a check.
**Solution:**
```typescript
async function getRaw(url: string): Promise<unknown> {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return res.json();
}

function isNumberArray(x: unknown): x is number[] {
  return Array.isArray(x) && x.every((n) => typeof n === "number");
}

async function demo() {
  const data = await getRaw("/api/ids");        // unknown — honest
  // data.map(...)                              // Error: unknown, must narrow
  if (isNumberArray(data)) {
    console.log(data.map((n) => n * 2));         // safe: proven number[]
  } else {
    console.error("unexpected shape:", data);    // handled, not crashed
  }
}
```
**Logic explained:**
1. With `Promise<T>` the caller's `T` is taken on faith — `{ ids: [1,2] }` got typed `number[]`, so `.map` compiled and crashed at runtime.
2. Returning `Promise<unknown>` is honest: the function *cannot* know the body's shape, so it shouldn't pretend.
3. `isNumberArray` narrows `unknown` → `number[]` with an actual runtime check — `Array.isArray` + element check. The type now reflects verified reality.

### Medium — validate the response shape with a guard
**Problem:** `fetchPost(id)` should return `Post` (`{ id, title, published }`). The API sometimes returns `{ error: "not found" }` with a 200. Write a guard and a wrapper that throws a descriptive error on shape mismatch.
**Try this input:** API returns `{ id: "p1", title: "Hi", published: true }` then `{ error: "not found" }`.
**Expected output:** first call returns the post; second call throws `Invalid Post response`.
**Solution:**
```typescript
interface Post {
  id: string;
  title: string;
  published: boolean;
}

function isPost(x: unknown): x is Post {
  if (typeof x !== "object" || x === null) return false;
  const o = x as Record<string, unknown>;
  return (
    typeof o.id === "string" &&
    typeof o.title === "string" &&
    typeof o.published === "boolean"
  );
}

async function fetchPost(url: string): Promise<Post> {
  const res = await fetch(url);
  const data: unknown = await res.json();       // unknown, not any
  if (!isPost(data)) {
    throw new Error(`Invalid Post response: ${JSON.stringify(data)}`);
  }
  return data;                                   // Post — verified
}
```
**Logic explained:**
1. Typing `const data: unknown` — not `any` — is the discipline: `any` would let `return data` compile silently; `unknown` *forces* the guard.
2. `isPost` checks each field's runtime type — verbose but explicit. `Record<string, unknown>` is the honest way to poke at an `unknown` object.
3. The throw carries the actual body — debugging a shape mismatch is trivial when the error includes what was received.
4. Note `res.ok` isn't even enough here: the *same* 200 response can be either shape — that's why field-level validation, not status-level, catches it.

### Hard — schema-driven validation (Zod-style), type inferred from the schema
**Problem:** Rewrite the wrapper so the `Post` type is *derived* from a schema, not declared separately — so the type and validator can never drift. Use Zod's API shape: `z.infer<typeof Schema>` gives the type, `Schema.parse(data)` validates and returns it.
**Try this input:** good post → returns typed `Post`; bad post missing `published` → `parse` throws.
**Expected output:** valid data flows through as `Post`; invalid throws a `ZodError` with the exact failing field.
**Solution:**
```typescript
// npm i zod
import { z } from "zod";

const PostSchema = z.object({
  id: z.string(),
  title: z.string(),
  published: z.boolean(),
});

type Post = z.infer<typeof PostSchema>;   // { id: string; title: string; published: boolean }
                                          // type DERIVED from schema — single source of truth

async function fetchPost(url: string): Promise<Post> {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
  return PostSchema.parse(await res.json());  // throws on mismatch, returns Post on match
}

// usage:
//   const p = await fetchPost("/posts/1");   // Post — proven by parse
//   p.title.toUpperCase();                    // safe — parse passed
```
**Logic explained:**
1. `PostSchema` is a *value* — a runtime object describing the shape — so it can actually check data, unlike an `interface` which is erased.
2. `z.infer<typeof PostSchema>` extracts the type *from* the schema — change the schema, the type follows automatically. No drift between "what we check" and "what we claim."
3. `parse` either returns data typed `Post` or throws a `ZodError` naming the failing path — validation and typing are one operation, not two that can disagree.
4. This is the mature pattern: the *generic* version asserts `T`; the *schema* version *earns* `T`. Interviewers who ask this question are fishing for exactly this distinction.

## The 30-second interview answer

"`get<T>(url): Promise<T>` looks type-safe but the generic is an assertion, not a check — `res.json()` returns `any`, which is assignable to anything, so `get<User>` just *labels* whatever came back as `User`. If the server sends a different shape — an error object, a renamed field — the code compiles clean and crashes somewhere far from the fetch. The honest approaches: return `Promise<unknown>` so callers *must* validate, or better, parse with a schema — `UserSchema.parse(data)` throws on mismatch and returns a genuine `User`, with `z.infer` deriving the type from the schema so validator and type can't drift. The principle: **types are erased at runtime, so at the network boundary a type can only be earned by validation — never asserted by a generic.**"

## Follow-up trap

**"Can't you just add `if (!res.ok) throw`?"** — That handles HTTP errors, not *shape* errors — a 200 with the wrong body still flows through typed as `T`. Status and shape are different failure axes. Second trap: **"is `res.json() as User` basically the same as `get<User>`?"** — Yes, exactly the same lie — the generic version just looks more respectable. Both assert without checking; both are erased at compile. Third: **"why not just trust the backend's OpenAPI types?"** — generated types describe the *contract*, not what the wire actually carried; a deploy skew between client and server, a proxy, or a bug upstream all mean the bytes don't match the docs. Validation at the boundary is the only thing that checks *this actual response*. Bonus: **`safeParse` vs `parse`** — `parse` throws; `safeParse` returns `{ success, data | error }` — the functional alternative when throwing isn't your style.
