# 41 — JSON from an API is `unknown` — narrowing vs schema parsing

> **Interview question:** "Why should `JSON.parse` / `res.json()` return `unknown` instead of `any` — and how do you actually use the value afterward?"
> **What the interviewer is really testing:** Whether you know `any` infects silently (any use compiles, no narrowing needed) while `unknown` forces a check — and the two real strategies for turning `unknown` into a usable type: **narrowing** (type guards, discriminated unions) vs **schema parsing** (Zod/io-ts — validate once, get the type free).

## Theory — what it is

`JSON.parse` is typed `any` in the standard lib — which means "the compiler will believe anything you say about this value." `unknown` is the opposite: "the compiler believes nothing — prove the shape before you use it."

```typescript
const raw = `{"id":"u1"}`;

const a: any = JSON.parse(raw);        // a.foo.bar.baz — compiles, might crash
const u: unknown = JSON.parse(raw);    // u.foo — ERROR: must narrow first
```

Rules that matter:

- **`unknown` is the type-safe top type.** Anything is assignable *to* it; nothing is assignable *from* it without narrowing. It accepts all data, permits no use.
- **Narrowing paths for `unknown`:**
  - `typeof x === "string"` — primitives
  - `Array.isArray(x)` — arrays
  - `typeof x === "object" && x !== null` — objects (then inspect fields)
  - Custom type guards: `function isUser(x: unknown): x is User`
  - `in` operator, `instanceof`, discriminated-union checks on a tag field
- **The `any` infection:** `const a: any = ...; const b: string = a` — `any` flows unchecked into every position it touches. `unknown` can't leak: `const b: string = u` is an error until narrowed.
- **Two honest strategies:**
  1. **Narrow manually** — guards you write by hand. Cheap, no deps, verbose.
  2. **Parse with a schema** — `UserSchema.parse(x)` returns the type or throws. The schema is a runtime artifact that *produces* the type (`z.infer`), so shape and type can't drift.
- **Narrowing ≠ validation** — a type guard *can* lie (`x is User` returning `true` unconditionally compiles fine). A schema parser *cannot* lie: it either returns validated data or throws.

## Why it was needed

`JSON.parse` returning `any` is a historical compromise — the correct type is "whatever the string held," which is unknowable statically. But `any` is the *worst* answer: it doesn't just permit misuse, it *silences the compiler entirely* — typos, wrong assumptions, renamed fields all compile.

The ecosystem converged on: **be honest at the boundary.** Type the JSON as `unknown` (or use libs that do), then either narrow with guards (small surface, few fields) or parse with a schema (complex/deep shapes, when "almost right" is a bug). This is the same philosophy as file 36's fetch wrapper — `unknown` is the *mechanism*; narrowing and schema parsing are the two ways to *escape* it safely.

## Where it's used in a real project

- **`JSON.parse` on API/localStorage data:** `JSON.parse(localStorage.getItem("settings") ?? "{}")` — classic `unknown` source; stale/corrupt data is common.
- **Webhook payloads:** third-party POSTs you don't control — schema-parse at the handler boundary.
- **`catch (e)` — `e` is `unknown` under `useUnknownInCatchVariables`:** same discipline — narrow before reading `.message`.
- **Message passing:** `postMessage`, WebSocket `onmessage.data`, worker messages — all arrive as `any`/`unknown`.
- **Config files:** `JSON.parse(fs.readFileSync(...))` — validate before trusting.

## Diagram

```
const raw = '{"id":"u1","name":"Ana"}'
const data = JSON.parse(raw)

as ANY:                          as UNKNOWN:
data.name.toUpperCase()  ✅      data.name               ❌ must narrow
data.nonexist.deep       ✅💥    if (typeof data === "object" && data !== null
                                 && "name" in data && typeof data.name === "string")
                                   data.name           ✅ — proved, not assumed

ESCAPE ROUTES from unknown:

  ┌─ NARROWING (guards) ──────────────┬─ SCHEMA PARSE ────────────────┐
  │ function isUser(x): x is User {   │ const S = z.object({...});    │
  │   return typeof x === "object"    │ type User = z.infer<typeof S> │
  │     && ...each field checked...   │ const u = S.parse(data);      │
  │ }                                 │ // throws OR returns User     │
  │ if (isUser(data)) use(data)       │                               │
  │                                   │                               │
  │ cheap, manual, can LIE            │ validates, earns the type,    │
  │ (guard can return true wrongly)   │ can't lie — parse() enforces  │
  └───────────────────────────────────┴───────────────────────────────┘

The discipline: unknown in -> narrow/parse -> typed value out.
Never: unknown -> as -> typed. That skips the check entirely.
```

## Code — explained

```typescript
// 1. The honest boundary — type JSON as unknown, not any
const raw = `{"id":"u1","name":"Ana","tags":["a","b"]}`;
const data: unknown = JSON.parse(raw);

// data.name;                       // Error: 'data' is of type 'unknown'

// 2. Narrowing path 1: typeof for primitives
if (typeof data === "string") {
  console.log(data.toUpperCase());    // string — narrowed by typeof
}

// 3. Narrowing path 2: object check + property inspection
if (typeof data === "object" && data !== null && "id" in data) {
  const obj = data as Record<string, unknown>;   // (4) peek with Record
  if (typeof obj.id === "string") {
    console.log(obj.id);              // u1 — field proven string
  }
}

// 5. A real type guard — the reusable narrowing tool
interface User {
  id: string;
  name: string;
  tags: string[];
}

function isUser(x: unknown): x is User {
  if (typeof x !== "object" || x === null) return false;
  const o = x as Record<string, unknown>;
  return (
    typeof o.id === "string" &&
    typeof o.name === "string" &&
    Array.isArray(o.tags) &&
    o.tags.every((t) => typeof t === "string")
  );
}

if (isUser(data)) {
  console.log(data.name, data.tags.length);   // Ana 2 — data: User now
}

// 6. The lying guard — compiles fine, cheats anyway
function isUserLazy(x: unknown): x is User {
  return true;                          // compiles! and lies
}
// isUserLazy(5) -> true -> 5 is now typed User. Guards can lie;
// schemas can't — that's why Zod wins for real validation.
```

1. Typing the parse result `unknown` is the entire discipline — it declares "I don't know what this is" so the compiler keeps you honest.
2. `typeof` narrows primitives — `unknown → string` with a real runtime check.
3. Object narrowing: `typeof === "object"` plus `!== null` (typeof null is "object"!) plus `in` to test for a key — the manual field-by-field climb.
4. `x as Record<string, unknown>` isn't cheating here — after the `object`+`!null` check, `Record` is a *safe* retype that lets you inspect fields (still `unknown` values, still must narrow).
5. `isUser` bundles the field checks into one named guard — the `x is User` return type is the magic: inside `if (isUser(d))`, `d` narrows to `User` for the compiler.
6. The trap: `x is User` is a *claim* the compiler takes on faith — `return true` compiles while lying. Guards are honest only if the person who wrote them was.

## Problems

### Easy — narrow `unknown` to a primitive
**Problem:** `JSON.parse` result is `unknown`. Safely extract a `string` field `name` and log it upper-cased, or log `"no name"` — without using `any`.
**Try this input:** `{"name":"ana"}` then `{"id":1}` then `null`.
**Expected output:** `ANA`, `no name`, `no name`.
**Solution:**
```typescript
function getName(data: unknown): string {
  if (typeof data !== "object" || data === null) return "no name";
  const o = data as Record<string, unknown>;
  return typeof o.name === "string" ? o.name.toUpperCase() : "no name";
}

console.log(getName(JSON.parse(`{"name":"ana"}`)));   // ANA
console.log(getName(JSON.parse(`{"id":1}`)));          // no name — no name field
console.log(getName(JSON.parse(`null`)));              // no name — typeof null is "object"
```
**Logic explained:**
1. The `object && !null` check is the mandatory gate before touching fields — `typeof null === "object"` is the classic JS wart that bites here.
2. `Record<string, unknown>` lets you index in without `any` — fields come out `unknown`, still needing their own checks.
3. `typeof o.name === "string"` earns the `string` — the compiler narrows `o.name` for the `toUpperCase` call.

### Medium — discriminated union from JSON
**Problem:** An API returns `{"type":"ok","data":{...}}` or `{"type":"err","message":"..."}` — a discriminated union. Type it as `unknown`, narrow on `type`, and handle each arm.
**Try this input:** `{"type":"ok","data":{"value":42}}` then `{"type":"err","message":"boom"}`.
**Expected output:** `got 42` then `error: boom`.
**Solution:**
```typescript
type ApiResponse =
  | { type: "ok"; data: { value: number } }
  | { type: "err"; message: string };

function isApiResponse(x: unknown): x is ApiResponse {
  if (typeof x !== "object" || x === null) return false;
  const o = x as Record<string, unknown>;
  if (o.type === "ok") {
    const d = o.data as Record<string, unknown>;
    return typeof d?.value === "number";
  }
  if (o.type === "err") {
    return typeof o.message === "string";
  }
  return false;
}

function handle(raw: string) {
  const data: unknown = JSON.parse(raw);
  if (!isApiResponse(data)) throw new Error("bad shape");
  // discriminated union: check the tag, get the arm
  if (data.type === "ok") {
    console.log(`got ${data.data.value}`);       // value: number
  } else {
    console.log(`error: ${data.message}`);       // message: string
  }
}

handle(`{"type":"ok","data":{"value":42}}`);   // got 42
handle(`{"type":"err","message":"boom"}`);      // error: boom
```
**Logic explained:**
1. The union has a `type` *tag* — that's what makes it discriminated: checking `data.type === "ok"` narrows to the `ok` arm automatically.
2. `isApiResponse` validates each arm's fields — nested `data.value` needs its own `Record` peek + `typeof` check.
3. After the guard passes, the compiler tracks the discriminant: inside `data.type === "ok"`, `data.data` is known to exist — no `?.` needed.
4. This is the narrowing strategy at full strength: union + tag + guard → type-safe handling of genuinely-variable JSON.

### Hard — schema parse: validate once, infer the type
**Problem:** Replace the manual guard with a Zod schema so the `ApiResponse` type is *derived* from the validator — and show a malformed payload being rejected with the field named.
**Try this input:** valid `ok` response, then `{"type":"ok","data":{"value":"x"}}` (string where number expected).
**Expected output:** first logs `got 42`; second throws naming `data.value`.
**Solution:**
```typescript
import { z } from "zod";

const ApiResponseSchema = z.discriminatedUnion("type", [
  z.object({ type: z.literal("ok"), data: z.object({ value: z.number() }) }),
  z.object({ type: z.literal("err"), message: z.string() }),
]);

type ApiResponse = z.infer<typeof ApiResponseSchema>;
// = { type:"ok"; data:{value:number} } | { type:"err"; message:string }

function handle(raw: string) {
  const res = ApiResponseSchema.parse(JSON.parse(raw));   // throws OR ApiResponse
  if (res.type === "ok") {
    console.log(`got ${res.data.value}`);
  } else {
    console.log(`error: ${res.message}`);
  }
}

handle(`{"type":"ok","data":{"value":42}}`);       // got 42
// handle(`{"type":"ok","data":{"value":"x"}}`);    // ZodError: data.value: expected number
```
**Logic explained:**
1. `z.discriminatedUnion` validates the tag *and* routes to the right sub-schema — the same "check the tag" logic as the manual guard, but executable.
2. `z.infer<typeof Schema>` means the TypeScript type is *generated from* the validator — edit the schema and the type updates; they can never drift, unlike a hand-written `type ApiResponse` + hand-written `isApiResponse`.
3. `parse` either returns the typed value or throws `ZodError` with the exact path (`data.value`) — the failure is precise, not "bad shape."
4. The core comparison: manual guard = two artifacts that can disagree (the type + the checks). Schema = one artifact that *is* both.

## The 30-second interview answer

"`JSON.parse` returning `any` is the problem — `any` silences the compiler, so a typo'd field or wrong shape compiles fine and crashes at runtime. Typing it `unknown` is the honest move: `unknown` accepts everything but permits nothing — you can't touch a field until you *prove* the shape. Two ways to prove it: narrowing — `typeof`, `Array.isArray`, `in`, or a custom `x is User` type guard checking each field — which is cheap but the guard itself can lie, since `x is User` is trusted. Or schema parsing — `UserSchema.parse(data)` in Zod/io-ts — which actually validates and either returns the typed data or throws, with `z.infer` deriving the type from the schema so validator and type can never drift. Rule of thumb: `unknown` in, narrow or parse, *then* use — never `as` straight out, that skips the check entirely."

## Follow-up trap

**"Can't a type guard lie? `x is User` returning `true` unconditionally compiles."** — Yes — that's the deep trap. A guard is a *claim* the compiler believes; `return true` compiles while claiming `5` is a `User`. Guards are only as honest as their author — which is why schema parsing is stronger: `parse` can't lie, it either returns validated data or throws. Second trap: **"`typeof data === 'object'` — is `data` now safe to read fields from?"** — No: `typeof null === "object"`, so `data` could be `null` — `!== null` is mandatory. Also `typeof` gives `"object"` for arrays too — `Array.isArray` is the array check. Third: **"why not `const d = JSON.parse(raw) as User`?"** — `as` skips validation *and* tells the compiler to trust you — it's the `any` lie with extra steps; a renamed field compiles clean and crashes. `as` on `unknown` is `any`-tier dishonesty wearing a cast.
