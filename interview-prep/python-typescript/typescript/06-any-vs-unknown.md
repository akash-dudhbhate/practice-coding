# 06 — `any` vs `unknown`

> **Interview question:** "What's the difference between `any` and `unknown`, and when would you use each?"
> **What the interviewer is really testing:** Whether you know `unknown` is the *safe* top type — usable at system boundaries because it forces narrowing — while `any` silently turns off the type checker for everything it touches.

## Theory — what it is

Both are **top types** — every value is assignable *to* them. They differ completely in what you can do *with* them:

- **`any`** — the escape hatch. A value typed `any` allows *any* operation (`x.foo.bar()`, `x + 1`, calling it) and is assignable *to* every type. It doesn't mean "could be anything" — it means "stop checking this." Worse, it's **contagious**: `const n: number = someAny` compiles, so one `any` at a boundary infects everything downstream.
- **`unknown`** — the *safe* top type (added in TS 3.0). You can put anything into an `unknown`, but you can't do anything with it — no property access, no calls, no assignment to a narrower type — until you **narrow** it with `typeof`, `instanceof`, `in`, a type guard, or a cast.

Rule of thumb: **`unknown` at the boundary, narrow before use.** `JSON.parse`, API responses, `catch` variables, `localStorage`, message events — anything that crosses into your program from outside is honestly `unknown`, and claiming it's `any` (or worse, `as User`) is lying to the compiler.

## Why it was needed

`any` existed from day one to make JS→TS migration painless — but it became the default annotation for "I don't want to think about this type," and the compiler can't tell the difference between deliberate and lazy `any`. The problem: `any` doesn't just skip checking one value, it propagates wrongness. `const user: any = fetchUser()` means `user.email.toLowerCase()` compiles even if `email` doesn't exist — the typo becomes a runtime crash, silently.

`unknown` was added so that "this could be anything" could be expressed *without* abandoning safety: the compiler still forces you to prove what the value is before using it. Under `strict` + `useUnknownInCatchVariables`, `catch (e)` gives `e: unknown` for exactly this reason — a thrown value can be anything (`throw "oops"` is legal), so reading `e.message` requires an `instanceof Error` check.

## Where it's used in a real project

- **Deserialization boundaries:** `const data: unknown = JSON.parse(raw)` — then validate/narrow once into a real type. (Note: `JSON.parse` is typed `any` in the stdlib — annotating the result `unknown` is your first safety upgrade.)
- **Error handling:** `catch (e)` is `unknown` under strict — `if (e instanceof Error)` before `e.message`.
- **Event/messaging payloads:** `window` `message` events, WebSocket frames, queue message bodies — all honestly `unknown`.
- **Generic constraints:** `function f<T extends unknown>()` — same as unconstrained, but signals intent; `Partial<Record<string, unknown>>` for option bags.
- **Config/secrets plumbing:** values read from env files or headers start as `unknown`/`string`, get validated once at startup.

## Diagram

```
        everything is assignable UP to both:
            string, number, Dog... 
              |            |
              v            v
            any         unknown
              |            |
   assignable / usable   NOT usable directly:
   as ANYTHING:          u.foo    -> ERROR
   x.foo()  OK           u + 1    -> ERROR
   x + 1    OK           const n: number = u -> ERROR
   number = x  OK              |
                               |  must narrow first:
                               v
                     typeof u === "string" ?
                     instanceof / in / guard
                               |
                               v
                     now u is safe to use
        any = trust me      unknown = prove it
        (compiler: off)     (compiler: on)
```

## Code — explained

```typescript
// --- any: everything compiles, nothing is checked ---          // 1
const a: any = JSON.parse('{"id": 1}');
a.user.name.toUpperCase();   // compiles — RUNTIME crash: cannot read 'name' of undefined
const n: number = a;         // compiles — a is actually {id:1}, not a number

// --- unknown: same value, but the compiler makes you prove it --- // 2
const u: unknown = JSON.parse('{"id": 1}');
// u.id;                     // ERROR: 'u' is of type 'unknown'
// const m: number = u;      // ERROR: 'unknown' not assignable to 'number'

// --- narrowing unknown ---                                     // 3
if (typeof u === "object" && u !== null && "id" in u) {
  console.log(u.id);         // OK — u.id is unknown, reading is allowed
}

// --- the real-world pattern: validate at the boundary ---       // 4
interface User { id: number; name: string }

function isUser(x: unknown): x is User {                         // 5
  if (typeof x !== "object" || x === null) return false;
  const o = x as Record<string, unknown>;
  return typeof o.id === "number" && typeof o.name === "string";
}

const data: unknown = JSON.parse('{"id":1,"name":"Ada"}');
if (isUser(data)) {
  console.log(data.name.toUpperCase());  // OK — data is User here
}
```

1. `a.user.name.toUpperCase()` — three levels of property access on `any`, zero checking. If the JSON lacks `user`, this is a production crash, not a compile error. `const n: number = a` shows the contagion: `any` flows into typed slots.
2. `unknown` refuses *everything* — reading `.id`, arithmetic, assignment to `number`. The type says "I don't know," and the compiler holds you to it.
3. Narrowing is the contract: `typeof` for primitives, `!== null` because `typeof null === "object"` (JS's oldest bug), `"id" in u` to prove the key exists. After the guard, `u.id` is readable (still `unknown` — you'd narrow again to *use* it as a number).
4. The pattern that scales: one validator function at the boundary converts `unknown` → concrete type; everything downstream is fully typed.
5. `x is User` makes this a **type predicate** — inside `if (isUser(data))`, `data` is narrowed to `User` automatically. `x as Record<string, unknown>` is the honest cast: "it's an object with unknown values," not "it's a User, trust me."

## Problems

### Easy — fix the unknown
**Problem:** This fails to compile. Fix it idiomatically.

```typescript
function shout(x: unknown): string {
  return x.toUpperCase();
}
```

**Try this input:** `shout("hi")` and `shout(42)`.
**Expected output:** Original: `error TS2339: Property 'toUpperCase' does not exist on type 'unknown'`. Fixed: `"HI"` for `"hi"`, throws or returns `""` for `42`.
**Solution:**

```typescript
function shout(x: unknown): string {
  if (typeof x !== "string") return "";   // narrow or reject
  return x.toUpperCase();                 // x: string here
}

console.log(shout("hi"));  // "HI"
console.log(shout(42));    // ""
```

**Logic explained:**
1. `x.toUpperCase()` on `unknown` is exactly what `unknown` exists to prevent — no method calls until you've proven the type.
2. `typeof x !== "string"` is a **negated guard**: after it, TS narrows `x` to `string` in the remaining code.
3. Rejecting with `""` (or `throw`) keeps the signature honest — the caller never receives a surprise type.

### Medium — write the boundary guard
**Problem:** `JSON.parse` returns `any`. Write a guard `isUser` for `{ id: number; name: string }`, and use it so `process(raw)` takes `raw: string` and returns a typed `User` or `null` — no `any`, no `as User` on the parsed value.
**Try this input:** `process('{"id":1,"name":"Ada"}')`, `process('{"id":"1"}')`, `process("null")`.
**Expected output:** `{id:1,name:"Ada"}` as `User`; `null` for wrong shape and for `null`.
**Solution:**

```typescript
interface User { id: number; name: string }

function isUser(x: unknown): x is User {
  if (typeof x !== "object" || x === null) return false;
  const o = x as Record<string, unknown>;          // honest intermediate cast
  return typeof o.id === "number" && typeof o.name === "string";
}

function process(raw: string): User | null {
  const data: unknown = JSON.parse(raw);           // immediately hide the any
  return isUser(data) ? data : null;
}

console.log(process('{"id":1,"name":"Ada"}'));   // { id: 1, name: 'Ada' }
console.log(process('{"id":"1"}'));              // null — id is string
console.log(process("null"));                    // null — JSON null !== object
```

**Logic explained:**
1. `const data: unknown = JSON.parse(raw)` — annotate the `any` away on arrival; nothing can leak.
2. `typeof x === "object"` alone is not enough — `typeof null === "object"`, so `x === null` must be ruled out before property access.
3. `x as Record<string, unknown>` is safe *here* because we've already proven `x` is a non-null object; it lets us read fields while keeping each field `unknown` until its own `typeof` check.
4. `x is User` carries the narrowing into the caller — `data` is `User` inside the ternary, no second cast needed.

### Hard — validate a config object into a discriminated union
**Problem:** A YAML/env loader gives you `unknown`. Write `parseConfig(raw: unknown)` that returns `{ retries: number; mode: "fast" | "safe" }` — and throws a `TypeError` naming the *bad field* when validation fails. Then explain why `as Config` would have been wrong.
**Try this input:** `{retries: 3, mode: "fast"}`, `{retries: "3", mode: "fast"}`, `{retries: 3, mode: "turbo"}`, `42`.
**Expected output:** Config for the first; `TypeError` naming `retries`, `mode`, and "not an object" for the rest.
**Solution:**

```typescript
type Config = { retries: number; mode: "fast" | "safe" };

function parseConfig(raw: unknown): Config {
  if (typeof raw !== "object" || raw === null) {
    throw new TypeError("config: not an object");
  }
  const o = raw as Record<string, unknown>;

  if (typeof o.retries !== "number") {
    throw new TypeError("config.retries: must be a number");
  }
  if (o.mode !== "fast" && o.mode !== "safe") {
    throw new TypeError("config.mode: must be 'fast' | 'safe'");
  }
  return { retries: o.retries, mode: o.mode };      // fully typed out
}

console.log(parseConfig({ retries: 3, mode: "fast" }));        // OK
for (const bad of [{ retries: "3", mode: "fast" }, { retries: 3, mode: "turbo" }, 42]) {
  try { parseConfig(bad); } catch (e) { console.log((e as Error).message); }
}
// config.retries: must be a number
// config.mode: must be 'fast' | 'safe'
// config: not an object
```

**Logic explained:**
1. Each field gets its own check *and its own error message* — ops sees `config.retries: must be a number`, not a generic failure. This is the manual version of what zod/io-ts do.
2. `o.mode !== "fast" && o.mode !== "safe"` narrows `o.mode` to the literal union — comparing `unknown` against literals is allowed, and after the check TS knows the type.
3. `as Config` would *assert* the shape without checking — `{retries:"3"}` would pass and crash downstream. `unknown` + validation *proves* the shape. The cast we used (`as Record<string, unknown>`) is the narrow one that's actually justified: we already proved it's an object.
4. The return builds a fresh `Config` — so even if `raw` had extra junk fields (`{retries:3, mode:"fast", evil:...}`), the output is exactly the declared shape.

## The 30-second interview answer

"Both are top types — everything is assignable to them — but `any` opts out of checking entirely: you can call anything on it and assign it to anything, and it silently poisons downstream types. `unknown` accepts any value but permits *no* operations until you narrow it with `typeof`, `instanceof`, `in`, or a type guard. So the rule is: `unknown` at system boundaries — `JSON.parse`, API responses, catch variables — then validate once and everything inside is fully typed. `any` survives only as a migration crutch; new code at a boundary should never be `any` — it's `unknown` plus a guard, or a cast that a validator justifies."

## Follow-up trap

**"Why not just write `JSON.parse(raw) as User`?"** — Because `as` is an *assertion*, not a check: it compiles for `{id: "oops"}` and the crash just moves downstream to wherever `.id` is used as a number. `unknown` forces validation that *proves* the shape at the exact point data enters — the failure message even names the field. Second trap: **"Is there any legit use for `any`?"** — yes: migrating JS incrementally, or working around a third-party type hole you can't fix — but scope it tightly and never let it cross a module boundary; a `// TODO` plus lint rule (`@typescript-eslint/no-explicit-any` warn) keeps it from spreading. Bonus: `never` is the *bottom* type — assignable to everything, holds nothing — which is why `const x: never = anyValue` errors but `const y: any = anything` doesn't.
