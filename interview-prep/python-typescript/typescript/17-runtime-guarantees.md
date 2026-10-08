# 17 — What TypeScript does NOT guarantee at runtime

> **Interview question:** "If `getUser(): Promise<User>` compiles, can the runtime value still not be a `User`?"
> **What the interviewer is really testing:** Do you understand type erasure — types exist only at compile time — so anything crossing a boundary (JSON, env vars, localStorage, other people's code) must be *validated*, not just annotated?

## Theory — what it is

`tsc` emits plain JavaScript. Every annotation, interface, generic argument, `as` cast, and `satisfies` is **erased** — there is no `User` at runtime, only values. Consequences:

- **Boundary data is unchecked.** `JSON.parse`, `res.json()`, `localStorage.getItem`, `process.env`, `postMessage`, DB driver results — all arrive as `any`/`unknown`. Whatever type you write next to them is a *claim*, not a fact.
- **No runtime representation of your types.** You can't `instanceof` an interface — interfaces don't exist in emitted code. `typeof` only sees JS's primitives plus `object`/`function`.
- **Escape hatches are unverified.** `as`, `!`, `any`, and `// @ts-ignore` all tell the compiler to stop checking; the runtime value is whatever it actually is.
- **Other code doesn't share your contract.** A `.js` file, a third-party lib, another team's service, a renamed API field — your types can't reach across the wire.
- **What DOES hold:** inside purely-typed code with no escape hatches, "if it compiles, it's consistent" is real. The holes are exactly (a) boundaries and (b) escape hatches.
- **What runtime CAN check:** real JavaScript — `typeof`, `instanceof`, `Array.isArray`, `in`, discriminant fields — plus validator libraries (Zod, valibot, io-ts, AJV) that verify a shape once and let you *derive* the type from the schema.

Mental model: types are a contract enforced *inside* your program. Anything crossing the wall — in or out — is outside its jurisdiction.

## Why it was needed

TypeScript was designed to *layer onto* JavaScript without changing its runtime: zero-cost types means zero runtime types. That's why it can type-check existing JS and emit identical code — and why it structurally cannot validate runtime data. Languages with runtime type info (Java, C#) pay for it with reflection and heavier runtimes. So the ecosystem's answer became: **check once at the boundary** with real code (guards or schema validators), then trust types inside. Every mature TS codebase has a validation layer exactly at the edges — *parse, don't annotate*.

## Where it's used in a real project

- `await res.json()` → typed `any` → validate before use (`UserSchema.parse(data)` or `isUser(data)`).
- `process.env.PORT` → `string | undefined`, always a string even when it looks numeric — needs `Number(...)` + a `NaN` check.
- `localStorage.getItem("prefs")` → stale or corrupt shapes written by older app versions.
- `JSON.parse` of dates → `"2024-05-01T10:00:00Z"` arrives as a **string** — `.getTime()` crashes despite `interface Event { at: Date }`. JSON has no `Date`, `Map`, `undefined`, or functions.
- WebSocket / `postMessage` payloads, URL query params (always strings), webhook bodies, ORM results typed by hand.

## Diagram

```
   compile time                     runtime (types erased)
 ┌──────────────────┐    tsc      ┌──────────────────────────┐
 │ interface User    │   emits   │  const res = fetch(...)  │
 │ user.name: string │ ────────► │  const u = res.json()    │
 │ compiler enforces │   plain   │  // u is just an object  │
 │ inside your code  │   JS      │  // no User exists here  │
 └──────────────────┘            └───────────┬──────────────┘
                                             │
        boundary — outside the contract:      │
        network / disk / env / other code ────┘
                                             │
                              validate here ─┤ isUser(x) / schema.parse
                                             │
                              ┌──────────────┴──────────────┐
                              │ interior: trust the types   │
                              │ edges:    verify with code  │
                              └─────────────────────────────┘
```

## Code — explained

```typescript
interface User { id: number; name: string }

// 1. The annotation trusts; the JSON lies.
const u1: User = JSON.parse(`{"id":"abc","name":"x"}`);   // (1) compiles fine
console.log(typeof u1.id);                                // "string" — type was fiction

// 2. Missing fields are invisible to the compiler.
const u2 = JSON.parse(`{"id":1}`) as User;
// console.log(u2.name.toUpperCase());                    // (2) TypeError at runtime
// (Bonus trap: JSON has no Date — an `at: Date` field arrives as a string.)

// 3. Validate at the boundary — then the interior can trust.
function isUser(x: unknown): x is User {                  // (3)
  if (typeof x !== "object" || x === null) return false;
  const o = x as Record<string, unknown>;
  return typeof o.id === "number" && typeof o.name === "string";
}

const raw: unknown = JSON.parse(`{"id":"abc"}`);          // (4)
if (!isUser(raw)) {
  console.log("bad payload:", raw);                       // bad payload: { id: 'abc' }
}
```

1. `JSON.parse` returns `any`, which is assignable to *anything* — `{"id":"abc"}` is cheerfully typed `User`, and `typeof u1.id` reveals the runtime truth: `"string"`.
2. `as User` makes the same lie explicit: missing `name` compiles, crashes later. JSON also can't represent `Date`, `Map`, `undefined` — they serialize to strings/objects/nothing.
3. The guard runs real checks on every call — `unknown` forces the proof, and `Record<string, unknown>` is the honest intermediate shape for property access.
4. Failure is logged *at the boundary* with the offending data visible — instead of `undefined` weirdness surfacing deep in business logic.

## Problems

### Easy — Env-var-style config
**Problem:** Config arrives as strings: `const env: Record<string, string | undefined> = { PORT: "3000", DEBUG: "false" }`. `const debug: boolean = env.DEBUG` doesn't compile — and `if (env.DEBUG)` is buggy in a sneakier way. Write `getBool` and `getPort`.
**Try this input:** `env.DEBUG = "false"`, `env.PORT = "3000"`
**Expected output:** `getBool(env, "DEBUG")` → `false` (the string `"false"` is *truthy* — `if (env.DEBUG)` would run!); `getPort(env)` → `3000`.
**Solution:**
```typescript
const env: Record<string, string | undefined> = { PORT: "3000", DEBUG: "false" };

function getBool(env: Record<string, string | undefined>, key: string): boolean {
  return env[key] === "true";                 // exact compare — strings aren't booleans
}

function getPort(env: Record<string, string | undefined>): number {
  const n = Number(env.PORT);
  if (Number.isNaN(n)) throw new Error("PORT is not a number");
  return n;
}

console.log(getBool(env, "DEBUG"));   // false — "false" would be truthy in an if!
console.log(getPort(env));            // 3000
```
**Logic explained:**
1. Env vars are always `string | undefined` — the runtime has no `boolean` or `number` for you, so the type `boolean` could never be guaranteed anyway.
2. `"false"` is a non-empty string → truthy. `if (env.DEBUG)` turns debug *on* — a silent, classic bug. `=== "true"` is explicit and correct.
3. `Number()` + `Number.isNaN` validates the conversion at the boundary instead of letting `NaN` leak into the config.

### Medium — The JSON Date trap
**Problem:** `interface Event { name: string; at: Date }`; the server sends `{"name":"launch","at":"2024-05-01T10:00:00Z"}`. `ev.at.getTime()` crashes because `at` is a *string*. Write `parseEvent` that validates and converts.
**Try this input:** `{"name":"launch","at":"2024-05-01T10:00:00Z"}`
**Expected output:** `ev.at instanceof Date` → `true`; `ev.at.toISOString()` → `2024-05-01T10:00:00.000Z`.
**Solution:**
```typescript
interface Event { name: string; at: Date }

function parseEvent(text: string): Event {
  const data: unknown = JSON.parse(text);
  if (typeof data !== "object" || data === null) throw new Error("bad event");
  const o = data as Record<string, unknown>;
  if (typeof o.name !== "string") throw new Error("event.name must be string");
  if (typeof o.at !== "string") throw new Error("event.at must be ISO string");
  const at = new Date(o.at);
  if (Number.isNaN(at.getTime())) throw new Error("event.at is not a valid date");
  return { name: o.name, at };              // real Date, constructed at the boundary
}

const ev = parseEvent(`{"name":"launch","at":"2024-05-01T10:00:00Z"}`);
console.log(ev.at instanceof Date);         // true
console.log(ev.at.toISOString());           // 2024-05-01T10:00:00.000Z
```
**Logic explained:**
1. JSON has no `Date` type — the interface's `at: Date` is a compile-time hope; the wire sends a string. Validation alone isn't enough — you must also *convert*.
2. `new Date(o.at)` rebuilds the real object; the `NaN` check catches garbage strings (`new Date("junk")` is an Invalid Date, not an exception).
3. After `parseEvent`, the interior genuinely holds `at: Date` — the type becomes true *because code made it true*. A `reviver` callback in `JSON.parse(text, reviver)` is the alternative hook for this.

### Hard — A validating parser with precise errors
**Problem:** Write `parseUser(text): User` (`User` = `id: number`, `name: string`, `email: string`) that throws ONE error listing every bad/missing field, e.g. `invalid user: id expected number got string; email missing`.
**Try this input:** `{"id":"abc","name":"x"}`
**Expected output:** throws `Error: invalid user: id expected number got string; email missing`; a valid payload returns the `User`.
**Solution:**
```typescript
interface User { id: number; name: string; email: string }

function parseUser(text: string): User {
  let data: unknown;
  try {
    data = JSON.parse(text);
  } catch {
    throw new Error("invalid user: not JSON");
  }
  if (typeof data !== "object" || data === null) {
    throw new Error("invalid user: not an object");
  }
  const o = data as Record<string, unknown>;

  const problems: string[] = [];
  if (!("id" in o)) problems.push("id missing");
  else if (typeof o.id !== "number") problems.push(`id expected number got ${typeof o.id}`);
  if (!("name" in o)) problems.push("name missing");
  else if (typeof o.name !== "string") problems.push(`name expected string got ${typeof o.name}`);
  if (!("email" in o)) problems.push("email missing");
  else if (typeof o.email !== "string") problems.push(`email expected string got ${typeof o.email}`);

  if (problems.length) throw new Error("invalid user: " + problems.join("; "));
  return o as User;   // the one legitimate `as` — every field just got proven
}

try {
  parseUser(`{"id":"abc","name":"x"}`);
} catch (e) {
  console.log((e as Error).message);
  // invalid user: id expected number got string; email missing
}
console.log(parseUser(`{"id":1,"name":"x","email":"e@x.com"}`).id);   // 1
```
**Logic explained:**
1. Even `JSON.parse` itself can throw — wrap it so the *only* error shape callers see is `invalid user: ...`.
2. Collecting `problems` instead of failing on the first field gives the caller the full diagnosis in one shot — the difference between a validator and a guard.
3. The final `as User` is honest: every field was just proven present and correctly typed. This is the *one* sanctioned use of assertion — after verification, not instead of it.
4. In production you'd write this once in Zod (`z.object({...}).parse`) and get the same guarantees plus generated error messages — but the hand-rolled version is what interviewers want to see you reason through.

## The 30-second interview answer

"TypeScript types are erased at compile time — there's no `User` at runtime, only values. So nothing about a compiled annotation guarantees the runtime shape: `JSON.parse`, `res.json()`, `process.env`, `localStorage`, and DB rows all arrive as `any`/`unknown`, and `as` casts claim rather than check. Inside fully-typed code, 'if it compiles it's consistent' holds — the holes are exactly boundaries and escape hatches. My rule is *parse, don't annotate*: validate once at the edge with `typeof`/`in` guards or a schema library like Zod that verifies the data and hands me the type for free — then trust the types inside. Classic gotchas: JSON has no `Date`, env vars are always `string | undefined`, and `res.json()` returning `any` will lie to you with a straight face."

## Follow-up trap

**"If types are erased, why does `Array.isArray(x)` narrowing still work?"** — because narrowing tracks *runtime checks you wrote*; the check is real JavaScript that survives erasure, and the compiler models what it proves. Erasure removes annotations, not your code. Related traps: **"why can't you `instanceof` an interface?"** — interfaces don't exist at runtime; `instanceof` needs a constructor function. **"does `satisfies` or `as const` add runtime checks?"** — no, erased like everything else; `as const` only changes the *inferred type*. And **"is `unknown` safer than `any`?"** — yes, and it's the right boundary type: `any` lets you do anything unchecked, `unknown` forces you to *prove* the shape before use — which is the whole point of this file.
