# 15 — `as` casts — when they lie; safer alternatives

> **Interview question:** "When is an `as` cast a lie? What do you use instead?"
> **What the interviewer is really testing:** Do you know `as` emits zero runtime code and can silently produce `undefined` explosions — and can you reach for narrowing/guards/validation instead?

## Theory — what it is

`as T` is a **type assertion**: you telling the compiler "trust me, this value is a `T`." It emits **no JavaScript whatsoever** — it's erased at compile time, exactly like a type annotation. It performs no check, no conversion, no validation. At runtime, `x as string` is just `x`.

```typescript
const el = document.querySelector("#app") as HTMLDivElement;
// compiled JS: const el = document.querySelector("#app");
```

`as` can only *relabel* types that overlap: you can assert `string | number` → `string` (narrowing claim) or `string` → `unknown`. For totally unrelated types the compiler balks (`"abc" as number` errors) — but `as unknown as T` bypasses even that check, a double-hop that's almost always a code smell.

The danger: **`as` changes what the compiler believes, not what the value is.** `JSON.parse("{}") as User` gives you a `User` with no `name`, no `id` — and every downstream `.name.toUpperCase()` is a runtime crash the compiler approved.

Safer alternatives, in order of preference:

1. **Narrowing / control flow** — `typeof`, `instanceof`, `in`, truthiness.
2. **Custom type guards** — `x is T` backed by a real check.
3. **Runtime validators** — Zod/io-ts schemas, or hand-rolled validators at system boundaries.
4. **Better types upstream** — generic `JSON.parse<T>`-style wrappers, typed fetch helpers (that still validate).
5. `as` is legitimately fine for: asserting *narrower* types you know more about than the compiler (DOM lookups you control), `as const`, non-null `!` equivalents, and test fixtures.

## Why it was needed

TypeScript needs *some* escape hatch: the compiler can't know everything (which element `querySelector` found, what a protobuf decoded to). `as` is that hatch. The problem is it became the *first* tool people reach for instead of the last. Each `as` is an unchecked claim; codebases accumulate hundreds, and every refactor silently turns some into lies. The fix isn't banning `as` — it's knowing it never validates and choosing guards at boundaries.

## Where it's used in a real project

- **Legit:** `canvas.getContext("2d") as CanvasRenderingContext2D` — the runtime API can't express "2d → this type".
- **Legit:** test mocks, `as const` assertions, narrowing `unknown` after a check the compiler can't track.
- **Danger zone:** `response.json() as MyType`, `localStorage.getItem as Config`, `e as AxiosError` — anything crossing a boundary you don't control.
- **Refactor trap:** `user.account.plan as "pro"` — fine until `plan` becomes `"pro" | "pro-max"` and the cast hides the new case from every switch.

## Diagram

```
        source value
            │
   ┌────────┴─────────┐
   │                  │
   ▼ as T             ▼ guard / validate
 "trust me"        "check it"
   │                  │
   │             ┌────┴────┐
   │             │ pass → T │── safe ──┐
   │             │ fail → throw /      │
   │             │        fallback     │
   │             └─────────┘           │
   ▼                                  ▼
 compiler believes T            compiler believes T
 runtime: unchanged,            runtime: VERIFIED
 may explode later              actually is T
```

## Code — explained

```typescript
interface User { id: number; name: string }

// --- The lie ---
const raw = JSON.parse(`{"id": 1}`);          // (1) raw: any
const user = raw as User;                      // (2) compiles!
console.log(user.name.toUpperCase());          // (3) RUNTIME CRASH

// --- The safe version ---
function isUser(x: unknown): x is User {       // (4)
  return (
    typeof x === "object" && x !== null &&
    typeof (x as User).id === "number" &&
    typeof (x as User).name === "string"
  );
}

const data: unknown = JSON.parse(`{"id": 1}`); // (5)
if (isUser(data)) {
  console.log(data.name.toUpperCase());        // (6) only reachable if real
} else {
  console.log("invalid payload");              // (7) this branch runs
}
```

1. `JSON.parse` returns `any` — already zero safety, but at least honest about it.
2. `as User` relabels the `{id:1}` object as `User`. No code emitted; `name` does not exist.
3. `undefined.toUpperCase()` → `TypeError` at runtime. The compiler green-lit the whole path.
4. A real guard — every field checked. (Note: the `as User` inside is only for property *access*, and it's safe because we already proved `x` is a non-null object; the field values are then checked with `typeof`.)
5. Declaring the parse result `unknown` forces you to prove the shape before use.
6. Inside the `if`, `data` is `User` *because a runtime check proved it* — not because we claimed it.
7. Bad payloads take the `else` — a visible, handleable failure instead of a crash downstream.

## Problems

### Easy — Replace an `as` with `typeof`
**Problem:** `function len(x: string | number) { return (x as string).length; }` crashes on numbers. Fix it without `as`.
**Try this input:** `len(42)`
**Expected output:** before fix — `undefined` (numbers have no `.length`, silently wrong, not even a crash!); after fix — `2`.
**Solution:**
```typescript
function len(x: string | number): number {
  if (typeof x === "string") return x.length;  // narrowed — no cast needed
  return String(x).length;                      // number → digit count
}

console.log(len(42));      // 2
console.log(len("hello")); // 5
```
**Logic explained:**
1. `(x as string).length` claims `x` is a string; on `42` it reads `.length` off a number → `undefined` — a *silent* wrong answer, worse than a crash.
2. `typeof` narrows honestly: inside the `if`, `x` really is `string`.
3. The `else` branch knows `x: number` and converts explicitly.

### Medium — The `JSON.parse` cast lie
**Problem:** `const cfg = JSON.parse(fs.readFileSync(...)) as Config` — a missing key in the JSON crashes three files away. Write `loadConfig` that returns `Config` or throws at parse time.
**Try this input:** `{"port": "3000"}` (string, not number) for `interface Config { port: number; host: string }`
**Expected output:** throws `Error: invalid config` at load — not a `TypeError` later.
**Solution:**
```typescript
interface Config { port: number; host: string }

function isConfig(x: unknown): x is Config {
  if (typeof x !== "object" || x === null) return false;
  const o = x as Record<string, unknown>;
  return typeof o.port === "number" && typeof o.host === "string";
}

function loadConfig(json: string): Config {
  const data: unknown = JSON.parse(json);
  if (!isConfig(data)) throw new Error("invalid config");
  return data;   // proven Config
}

// loadConfig(`{"port":"3000"}`);  // throws: invalid config
console.log(loadConfig(`{"port":3000,"host":"localhost"}`).port); // 3000
```
**Logic explained:**
1. `JSON.parse` result typed `unknown` — can't even touch `.port` without checking.
2. `isConfig` checks the two required fields with `typeof` — a wrong-type `"3000"` fails fast.
3. The error surfaces *at the boundary* with a clear message, not deep in business logic as `undefined` weirdness.
4. In real code you'd often swap the hand-rolled guard for `ConfigSchema.parse(data)` (Zod) — same idea, less code.

### Hard — The double-hop `as unknown as`
**Problem:** A colleague wrote `const user = apiResponse as unknown as Admin` to silence an error where `apiResponse: ApiUser` and `Admin` has extra fields. Explain why `as unknown as` compiles, why it's dangerous, and rewrite it safely with a guard that checks the admin-only field `permissions: string[]`.
**Try this input:** `apiResponse = { id: 1, name: "x" }` (a plain user, no `permissions`)
**Expected output:** the cast version compiles then crashes on `user.permissions.map(...)`; the guard version returns `null`/throws cleanly.
**Solution:**
```typescript
interface ApiUser { id: number; name: string }
interface Admin extends ApiUser { permissions: string[] }

// --- the lie ---
declare const apiResponse: ApiUser;
const admin = apiResponse as unknown as Admin;  // compiles — bypasses ALL checking
// admin.permissions.map(...)                    // CRASH: permissions is undefined

// --- the fix ---
function isAdmin(u: ApiUser): u is Admin {
  return (
    "permissions" in u &&
    Array.isArray(u.permissions) &&
    u.permissions.every((p) => typeof p === "string")
  );
}

function requireAdmin(u: ApiUser): Admin | null {
  return isAdmin(u) ? u : null;   // honest: maybe not an admin
}

console.log(requireAdmin({ id: 1, name: "x" }));                          // null
console.log(requireAdmin({ id: 1, name: "x", permissions: ["all"] }));    // {...,permissions:["all"]}
```
**Logic explained:**
1. `as unknown` erases the type to the top type, then `as Admin` relabels it — the double hop defeats the "types must overlap" rule that blocks `apiResponse as Admin` directly. That block was the compiler *warning* you; the double hop ignores it.
2. `permissions` is never created — it's a compile-time fiction. First `.map` at runtime explodes.
3. `isAdmin` checks the discriminating field: `"permissions" in u` plus `Array.isArray` plus element type — a real proof.
4. Returning `Admin | null` makes "not an admin" an explicit, handleable outcome — the signature tells the truth.

## The 30-second interview answer

"`as` is a type assertion — it changes what the compiler believes about a value while emitting zero runtime code. It lies whenever the runtime value doesn't match the claim: `JSON.parse(x) as User` compiles even when the JSON is missing fields, and the crash lands far from the cast. It can only relabel between overlapping types — `as unknown as T` bypasses even that, which is a red flag. My rule: at boundaries (JSON, localStorage, API responses, caught errors) I narrow or validate — `typeof`, `instanceof`, `x is T` guards, or a Zod schema. `as` is fine for things the compiler genuinely can't know, like `querySelector` returning a specific element type, or `as const`."

## Follow-up trap

**"What's the difference between `as` and a type annotation?"** — `const x: T = v` *checks* that `v` is assignable to `T`; `const x = v as T` *claims* it without a real check (only the weaker "do these types overlap" rule). So annotation can catch a mistake; `as` mostly suppresses the check. Expect also: *"is `!` (non-null assertion) the same problem?"* — yes, `x!.foo` is `x as NonNullable` — same lie potential, same "only when you truly know" rule. And *"when does `as` error at compile time?"* — when the types don't sufficiently overlap (`"abc" as number`), which is exactly why `as unknown as` exists as an escape.
