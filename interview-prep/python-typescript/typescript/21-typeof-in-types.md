# 21 — `typeof` in type position: `const config = {...}; type Config = typeof config`

> **Interview question:** "What does `typeof` do inside a type annotation — e.g. `type Config = typeof config` — and how is it different from JavaScript's runtime `typeof`?"
> **What the interviewer is really testing:** Do you know TypeScript has *two* `typeof`s living in different worlds — one inspects a value at runtime, the other captures a value's type at compile time — and why the type-level one exists?

## Theory — what it is

JavaScript already has a `typeof` operator: `typeof 5` evaluates to the string `"number"` **at runtime**. TypeScript reuses the same keyword in a completely different context: when `typeof` appears *inside a type* (a "type position" — after `:` in an annotation, inside `type X = ...`, in `<>` generic brackets, in `as` casts), it means "give me the **type** that TypeScript has inferred for this **value**."

So `const config = { env: "dev", retries: 3 }` followed by `type Config = typeof config` produces `Config = { env: string; retries: number }`. You wrote the value once; the type is *derived* from it for free. No duplicated interface, no drift between the object and its type.

The critical detail: **type-position `typeof` reads the variable's declared/inferred type, not its runtime value.** `typeof` in a type position works on *identifiers and property accesses* (`typeof config`, `typeof config.env`, `typeof window.location`) — you can't put arbitrary expressions there. And since types are erased at compile time, `type Config = typeof config` emits zero JavaScript.

One subtlety interviewers probe: `typeof` captures the *widened* type, not literal types, unless the value is `as const`. `const x = "dev"` has type `"dev"` (a literal — const never changes), but `typeof { env: "dev" }` gives `{ env: string }` because object properties are mutable and TypeScript widens them.

## Why it was needed

Real code is full of objects that already exist — config files, constants tables, mock data, library defaults. Without type-position `typeof`, you face duplication:

```typescript
const config = { env: "dev", retries: 3 };   // the value
interface Config { env: string; retries: number }  // the same thing, retyped
```

Now add `timeout` to `config` — and `Config` silently goes stale. Type-position `typeof` makes the value the **single source of truth**: `type Config = typeof config` always mirrors reality. It also enables patterns impossible otherwise — `ReturnType<typeof fetch>`, `Parameters<typeof myFunc>`, and `keyof typeof CONSTANTS` all pull types out of *values*, which is essential when the value came from a library and you can't edit its source.

## Where it's used in a real project

- **Config modules:** `export const config = { apiUrl: "...", timeout: 5000 }` then `type Config = typeof config` — consumers type their functions against `Config` while the object stays authoritative.
- **Redux/state stores:** `type RootState = ReturnType<typeof store.getState>` — the canonical Redux typing pattern; the store's actual shape drives the type.
- **Constants as enums:** `const ROLES = { ADMIN: "admin", USER: "user" } as const; type Role = typeof ROLES[keyof typeof ROLES]` gives `"admin" | "user"` — a union generated from real values.
- **Wrapping third-party functions:** `function myFetch(...args: Parameters<typeof fetch>): ReturnType<typeof fetch>` — you reuse the library's signature without copying it.

## Diagram

```
Two different operators, same spelling:

VALUE WORLD (runtime JS)              TYPE WORLD (compile-time TS)
------------------------              ---------------------------
typeof 5            -> "number"       const config = { env: "dev" }
typeof "hi"         -> "string"       type Config = typeof config
typeof user         -> "object"           = { env: string }
runs in the browser                   erased before JS is emitted

How "value -> type" flows:

  const ROLES = { ADMIN: "admin", USER: "user" } as const;
        |                    (real object — source of truth)
        | typeof ROLES
        v
  { readonly ADMIN: "admin"; readonly USER: "user" }
        | keyof
        v
  "ADMIN" | "USER"                    (the keys)
        | typeof ROLES[...]
        v
  "admin" | "user"                    (the values — type Role)
```

## Code — explained

```typescript
// 1. The basic pattern: value first, type derived second
const config = {
  env: "dev",
  retries: 3,
  features: { beta: true },
};

type Config = typeof config;
// = { env: string; retries: number; features: { beta: boolean } }

// Config can now type other things — always in sync with the object
function printConfig(c: Config): void {
  console.log(c.env, c.retries, c.features.beta);
}
printConfig(config);                      // dev 3 true

// 2. as const freezes literal types BEFORE typeof reads them
const ROUTES = {
  home: "/",
  dashboard: "/dash",
} as const;

type Route = typeof ROUTES[keyof typeof ROUTES];
// keyof typeof ROUTES  = "home" | "dashboard"
// typeof ROUTES[...]   = "/" | "/dash"          (literal union!)

function navigate(r: Route): void {
  console.log("going to", r);
}
navigate("/");            // OK
// navigate("/nope");     // ERROR: '"/nope"' is not assignable to 'Route'

// 3. typeof on a function reads its signature
function greet(name: string, punct = "!"): string {
  return `hi ${name}${punct}`;
}
type GreetFn = typeof greet;              // (name: string, punct?: string) => string
const alsoGreet: GreetFn = greet;
console.log(alsoGreet("amy", "?"));       // hi amy?

// 4. Runtime typeof still exists — different world, don't confuse them
const n = 42;
if (typeof n === "number") {              // runtime check, returns "number"
  console.log("really a number");         // really a number
}
```

1. `const config = {...}` is a normal object; `typeof config` in `type Config = ...` lifts its inferred type. Adding `timeout: 10` to `config` automatically updates `Config` — zero drift.
2. Without `as const`, `typeof { env: "dev" }` widens to `{ env: string }`. `as const` tells TypeScript "treat everything as literal and readonly," so `typeof ROUTES[...]` yields the literal union `"/" | "/dash"` — the enum-like pattern.
3. `typeof ROUTES[keyof typeof ROUTES]` reads left to right: `keyof` gets the keys `"home" | "dashboard"`, then indexing the object type by that union collects the *value* types.
4. `typeof greet` captures the full function signature — `(name: string, punct?: string) => string` — letting other functions adopt it exactly. This composes with `Parameters`/`ReturnType` (file 26).
5. Line `if (typeof n === "number")` is the *runtime* `typeof` — it returns a string like `"number"` and survives in the emitted JS. Same word, different universe: inside `type`/`:` it's compile-time; in an expression it's runtime.

## Problems

### Easy — derive a type from a constant
**Problem:** Given `const settings = { theme: "dark", fontSize: 14 }`, create a type `Settings` from it and write a function `applySettings` that accepts it.
**Try this input:** `applySettings({ theme: "light", fontSize: 16 })`
**Expected output:** function compiles and runs; passing `{ theme: "light" }` (missing `fontSize`) is a compile error.
**Solution:**
```typescript
const settings = { theme: "dark", fontSize: 14 };
type Settings = typeof settings;

function applySettings(s: Settings): void {
  console.log(`${s.theme} @ ${s.fontSize}`);
}
applySettings({ theme: "light", fontSize: 16 });   // light @ 16
// applySettings({ theme: "light" });              // ERROR: missing fontSize
```
**Logic explained:**
1. `typeof settings` captures `{ theme: string; fontSize: number }`.
2. The function parameter uses that derived type — no duplicated interface.
3. If `settings` gains a property later, `applySettings` callers are forced to provide it — the type follows the value automatically.

### Medium — enum-free role union
**Problem:** Without using `enum`, create a `Role` type with values `"admin" | "editor" | "viewer"` derived from a `ROLES` constant object, so the constant and the type can never disagree.
**Try this input:** `assign("admin")`, then `assign("superuser")`
**Expected output:** first call compiles; second errors: `'"superuser"' is not assignable to parameter of type 'Role'`.
**Solution:**
```typescript
const ROLES = {
  ADMIN: "admin",
  EDITOR: "editor",
  VIEWER: "viewer",
} as const;

type Role = typeof ROLES[keyof typeof ROLES];   // "admin" | "editor" | "viewer"

function assign(role: Role): void {
  console.log("assigned", role);
}
assign("admin");          // OK
// assign("superuser");   // ERROR
```
**Logic explained:**
1. `as const` keeps values as literals (`"admin"`, not `string`) and adds `readonly`.
2. `keyof typeof ROLES` = `"ADMIN" | "EDITOR" | "VIEWER"` — the property names.
3. Indexing `typeof ROLES` by that union collects the value types — the idiomatic `typeof X[keyof typeof X]` recipe for "union of this constant object's values."

### Hard — `satisfies` + `typeof` for validated config
**Problem:** Write a `defineConfig` function that validates an object against a required shape at compile time but *preserves the caller's literal types*, so `typeof` on the result gives precise literals — e.g. mode `"production"` not `string`.
**Try this input:**
```typescript
const cfg = defineConfig({ mode: "production", debug: false });
type Mode = typeof cfg.mode;
```
**Expected output:** `Mode` is `"production"` (literal). And `defineConfig({ debug: false })` errors — missing `mode`.
**Solution:**
```typescript
interface AppConfig {
  mode: string;
  debug: boolean;
}

function defineConfig<C extends AppConfig>(c: C): C {
  return c;
}

const cfg = defineConfig({ mode: "production", debug: false });
type Mode = typeof cfg.mode;        // "production" — literal preserved
console.log(cfg.mode);              // production

// defineConfig({ debug: false });  // ERROR: missing 'mode'
// defineConfig({ mode: "prod", debug: "no" }); // ERROR: debug not boolean
```
**Logic explained:**
1. `C extends AppConfig` validates the argument — missing or wrong-typed properties are compile errors.
2. Returning `C` (the inferred type) instead of `AppConfig` keeps the literal `"production"`; if the signature were `(c: AppConfig): AppConfig`, `typeof cfg.mode` would widen to plain `string`.
3. `satisfies` (TS 4.9) achieves the same inline: `const cfg = { mode: "production", debug: false } satisfies AppConfig` — checked *and* literal-preserving. Worth naming in an interview.

## The 30-second interview answer

"TypeScript reuses `typeof` in two worlds. In an expression it's plain JavaScript — `typeof x` returns a string like `"number"` at runtime. But in *type position* — inside `type X = ...`, after a colon, in a generic argument — it means 'the type TypeScript inferred for this value.' So `type Config = typeof config` derives a type from an existing object, making the value the single source of truth: change the object and the type follows automatically. It composes into the `keyof typeof` idiom for turning constant objects into unions, and into `ReturnType<typeof fn>`/`Parameters<typeof fn>` for reusing function signatures. One gotcha: it captures widened types unless the value is `as const`, which is why the constants-as-enum pattern always pairs `as const` with `typeof`."

## Follow-up trap

**"Why does `type Config = typeof config` give `env: string` and not `env: "dev"`?"** Because `typeof` reads the *inferred type*, and TypeScript widens mutable properties: object fields can be reassigned (`config.env = "prod"`), so their honest type is `string`, not the literal. `const` *variables* keep literals (`const x = "dev"` is type `"dev"` because it can't be reassigned) — but object *properties* widen. The fix is `as const`, which asserts literals and `readonly`. Second common probe: **"can you `typeof` an expression like `typeof (a + b)`?"** No — type-position `typeof` only accepts an identifier or a property-access chain (`typeof config.features.beta`), never arbitrary expressions. If you need the type of an expression, compute it into a `const` first — or use `ReturnType<typeof fn>` for call results.
