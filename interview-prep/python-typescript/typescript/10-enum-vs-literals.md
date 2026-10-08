# 10 — Enums vs union of literals — why many teams ban `enum`

> **Interview question:** "Would you use a TypeScript `enum` or a union of string literals? Why do some teams ban `enum`?"
> **What the interviewer is really testing:** Do you know enums emit real runtime code (with surprising behavior), and can you pick the simpler tool for the job?

## Theory — what it is

An **enum** is a TypeScript-only feature (it has no equivalent in plain JavaScript) that declares a named set of constants:

```typescript
enum Status { Active, Inactive, Banned }
```

A numeric enum like this compiles to a **real JavaScript object** with a *reverse mapping*: `Status.Active === 0` AND `Status[0] === "Active"`. String enums (`Active = "ACTIVE"`) also emit an object, just without the reverse lookup. Either way, actual code is generated and shipped to the browser — enums are one of the very few TS features that produce runtime output.

A **union of literals** is purely compile-time — zero emitted code:

```typescript
type Status = "active" | "inactive" | "banned";
```

At runtime a status is just the plain string `"active"`. The type exists only while `tsc` checks your code, then it's erased.

The modern middle ground is a **`const` object + `as const` + a derived type**: the object gives you named values at runtime, the derived union gives you the type — with no enum magic.

## Why it was needed

Enums were added early in TypeScript's life (2012) to mimic C#/Java, where enums are idiomatic. They solve a real problem: "I want named constants AND a type that accepts only those constants."

But they brought baggage that unions don't have:

1. **Runtime cost + non-JS semantics.** Enums emit an IIFE-built object; nothing else in TS does that except classes and decorators. Under `isolatedModules` / `esbuild` / `babel` (which strip types file-by-file without type info), `const enum` is outright **broken** — the compiler can't inline it because it can't see the declaration in another file.
2. **The reverse mapping footgun.** `Object.keys(Status)` on a numeric enum returns `["0","1","2","Active","Inactive","Banned"]` — double the entries. Loops over enums surprise people.
3. **Loose numeric checking.** A function taking `Status` accepts `Status.Active` but *also* accepts the raw number `5` (numeric enums are weakly checked against `number`). Union-of-strings rejects `"actve"` typos AND rejects `5`.
4. **Two ways to write the same thing** — enums and unions overlap, so teams pick one. Unions match how JS actually works at runtime and how JSON looks on the wire.

## Where it's used in a real project

- **API payloads / DB columns:** `status: "active" | "inactive"` — matches the JSON exactly, no translation layer.
- **UI state machines:** `type View = "loading" | "error" | "ready"` — used with `switch` + `never` for exhaustive handling.
- **Feature flags / config keys:** `const Flags = { NewCheckout: "new_checkout" } as const`.
- **The one place enums still appear:** interop with libraries that already use them (e.g., some older Angular/React codebases, `tslib` output).

## Diagram

```
enum Status { Active, Inactive }        type Status = "active" | "inactive"
            │                                        │
            ▼ tsc                                    ▼ tsc
  ┌─────────────────────────┐              ┌────────────────────┐
  │ EMITTED JS OBJECT:      │              │ EMITS NOTHING      │
  │ { 0:"Active",           │              │ (type erased)      │
  │   1:"Inactive",         │              │                    │
  │   Active:0,             │              │ runtime value is   │
  │   Inactive:1 }          │              │ just "active"      │
  └─────────────────────────┘              └────────────────────┘
   costs bytes, surprises            costs nothing, matches JSON
   isolatedModules, reverse map      typos caught, no magic
```

## Code — explained

```typescript
// --- The enum way ---
enum Role { Admin, User, Guest }                 // (1)

function canDelete(r: Role) { return r === Role.Admin; }

canDelete(Role.Admin);   // ok                    // (2)
canDelete(99);           // ALSO ok — numeric enums leak!  // (3)

console.log(Object.keys(Role).length);           // (4)

// --- The union + const-object way ---
const RoleObj = {                                 // (5)
  Admin: "admin",
  User: "user",
  Guest: "guest",
} as const;                                       // (6)

type RoleU = (typeof RoleObj)[keyof typeof RoleObj];  // (7) "admin" | "user" | "guest"

function canDeleteU(r: RoleU) { return r === RoleObj.Admin; }

canDeleteU("admin");        // ok — plain string works
canDeleteU(RoleObj.Admin);  // ok — named access works too
// canDeleteU("admnin");    // ERROR: typo rejected
// canDeleteU(99);          // ERROR: numbers rejected
```

1. Declares a numeric enum — `Admin` = 0, `User` = 1, `Guest` = 2.
2. Normal usage looks identical to a union version.
3. **The leak:** `Role` is assignable from `number`, so `99` compiles. A string-literal union would reject it.
4. Prints `6`, not `3` — reverse mapping doubles the keys.
5. A plain object holds the runtime values.
6. `as const` freezes the types: `"admin"` stays the literal `"admin"` instead of widening to `string`, and the object becomes `readonly`.
7. `typeof RoleObj` gets the object's type; `keyof` gets `"Admin" | "User" | "Guest"`; indexing by that union produces the *values' types*: `"admin" | "user" | "guest"`. This pattern replaces `enum` completely.

## Problems

### Easy — Define a literal union
**Problem:** Define a type `OrderStatus` that allows only `"pending"`, `"shipped"`, `"delivered"`, and write `isFinal` returning `true` only for `"delivered"`.
**Try this input:** `isFinal("shipped")`, `isFinal("delivered")`, `isFinal("cancelled")`
**Expected output:** `false`, `true`, and a compile error: `Argument of type '"cancelled"' is not assignable to parameter of type 'OrderStatus'`.
**Solution:**
```typescript
type OrderStatus = "pending" | "shipped" | "delivered";

function isFinal(s: OrderStatus): boolean {
  return s === "delivered";
}

console.log(isFinal("shipped"));    // false
console.log(isFinal("delivered"));  // true
// isFinal("cancelled");            // compile error
```
**Logic explained:**
1. The union type lists every legal string — anything else is rejected at compile time.
2. `s === "delivered"` is just a normal string comparison; the type only exists at compile time.
3. `"cancelled"` is not in the union, so `tsc` flags it before the code ever runs.

### Medium — Replace an enum with a const object
**Problem:** This enum exists: `enum HttpMethod { Get = "GET", Post = "POST" }`. Replace it with a `const` object + derived union type, and write `send(method, url)` that only accepts those methods.
**Try this input:** `send(HttpMethodObj.Post, "/api")`, `send("GET", "/api")`, `send("DELETE", "/api")`
**Expected output:** first two compile and print `POST /api` and `GET /api`; `"DELETE"` is a compile error.
**Solution:**
```typescript
const HttpMethodObj = {
  Get: "GET",
  Post: "POST",
} as const;

type HttpMethod = (typeof HttpMethodObj)[keyof typeof HttpMethodObj];
// = "GET" | "POST"

function send(method: HttpMethod, url: string): void {
  console.log(method, url);
}

send(HttpMethodObj.Post, "/api");  // POST /api
send("GET", "/api");               // GET /api — plain literals work!
// send("DELETE", "/api");         // compile error
```
**Logic explained:**
1. `as const` makes the object's property types the literals `"GET"`/`"POST"` (readonly).
2. `keyof typeof HttpMethodObj` = `"Get" | "Post"` (the keys).
3. `typeof HttpMethodObj[those keys]` = `"GET" | "POST"` (the value types) — this is your union.
4. Unlike `enum`, callers can pass the raw string `"GET"` — no import needed, matches what goes on the wire.

### Hard — Show the numeric-enum leak and fix it
**Problem:** Demonstrate that a function typed with a numeric enum accepts an out-of-range number, then rewrite it so the bad call is a compile error. Also print the enum's keys to show the reverse mapping.
**Try this input:** `setLevel(4)` with `enum Level { Low, Med, High }`
**Expected output:** `setLevel(4)` compiles and prints `level = 4` (silently wrong); after the fix it fails with `Argument of type '4' is not assignable...`; `Object.keys` prints 6 entries.
**Solution:**
```typescript
// --- broken version ---
enum Level { Low, Med, High }

function setLevel(l: Level) { console.log("level =", l); }
setLevel(4);                              // compiles! prints: level = 4
console.log(Object.keys(Level));          // ["0","1","2","Low","Med","High"]

// --- fixed version ---
const LevelObj = { Low: 0, Med: 1, High: 2 } as const;
type LevelT = (typeof LevelObj)[keyof typeof LevelObj];  // 0 | 1 | 2

function setLevelFixed(l: LevelT) { console.log("level =", l); }
setLevelFixed(LevelObj.High);             // ok
setLevelFixed(1);                         // ok — 1 is a valid member
// setLevelFixed(4);                      // compile error: 4 not in 0|1|2
```
**Logic explained:**
1. TS treats a numeric enum type as compatible with *any* `number`, so `4` slides through.
2. `Object.keys` reveals both directions of the mapping — `0→"Low"` and `"Low"→0` — six keys for three members.
3. The `as const` object + derived union produces the type `0 | 1 | 2` exactly, so `4` is rejected.
4. If you truly need numeric flags, this pattern keeps the strictness; otherwise prefer string literals.

## The 30-second interview answer

"A union of string literals gives me the same compile-time safety as an enum with zero emitted code, and it matches what the data actually looks like in JSON at runtime. Enums emit a real object — numeric enums even add a reverse mapping, which doubles `Object.keys` output, and they're loosely checked so a raw `number` like `99` can sneak into a `Status` parameter. `const enum` breaks under `isolatedModules`/esbuild. If I need named runtime values, I use a `const` object with `as const` and derive the union type from it. That's why many style guides — including the TypeScript team's own caveats — steer you away from `enum`."

## Follow-up trap

**"So are enums ever the right choice?"** Don't say "never" — that sounds dogmatic. Good answers: interop with a library/framework that already uses enums, cases where you *want* the runtime object and reverse lookup (rare), or `const enum` inside a monorepo where you control the whole toolchain. Also be ready for: *"what does `as const` actually do?"* — it makes the inferred type readonly and keeps literal types instead of widening to `string`/`number`.
