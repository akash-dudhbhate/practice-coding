# 29 — `as const` — freezing literals at the type level

> **Interview question:** "What does `as const` do to a literal or an object?"
> **What the interviewer is really testing:** Do you understand *widening* — that object/array properties widen to `string`/`number` unless you stop it — and that `as const` gives you literal types + deep `readonly` in one move?

## Theory — what it is

`as const` is a **const assertion**: it tells TypeScript "infer the narrowest possible type for this expression, and make it readonly." Two effects:

1. **Literal types are kept.** `"dark" as const` has type `"dark"`, not `string`. `[1, 2] as const` is the tuple `readonly [1, 2]`, not `number[]`.
2. **Everything becomes deeply `readonly`.** `{ theme: "dark" } as const` gets type `{ readonly theme: "dark" }` — recursively, through nested objects and arrays.

Why is it needed at all? Because TypeScript **widens**. `const x = "dark"` gets type `"dark"` (a `const` can't be reassigned, so the narrow type is safe). But `const obj = { theme: "dark" }` gets `{ theme: string }` — the *property* could be reassigned later, so TS widens `theme` to `string` to stay honest. `as const` says "I promise nothing here changes — keep the literals."

```typescript
const a = "dark";                    // "dark"          (const → literal already)
const b = { theme: "dark" };         // { theme: string }   (property widened!)
const c = { theme: "dark" } as const;// { readonly theme: "dark" }
const d = ["red", "blue"] as const;  // readonly ["red", "blue"] — a tuple
```

Critical: `as const` is **compile-time only** — it emits nothing. It does *not* call `Object.freeze`; the runtime object is still mutable. It's a type-level freeze, not a real one.

The classic payoff pattern — extracting a union of values from a config object:

```typescript
const ROUTES = { home: "/", user: "/u/:id" } as const;
type Route = (typeof ROUTES)[keyof typeof ROUTES];   // "/" | "/u/:id"
```

## Why it was needed

Before `as const` (TS 3.4), getting literal types out of an object meant annotating every field by hand (`{ theme: "dark" as "dark" }`) or duplicating a union next to the object and praying they stayed in sync. Codebases needed "the exact values in this object, as a type" for action types, route tables, and exhaustiveness checks — `as const` made it one keyword.

The deeper reason: union-of-literals is TypeScript's favorite modeling tool (file 10's enum alternative), and `as const` is the bridge between "a runtime lookup table" and "a compile-time union." One object, both uses.

## Where it's used in a real project

- **Redux/action constants:** `const ACTIONS = { add: "cart/add", rm: "cart/rm" } as const` — action types stay literal and discriminated-union-friendly.
- **Route/URL maps:** one `ROUTES` object powers both `navigate(ROUTES.user)` and `type Route = typeof ROUTES[keyof typeof ROUTES]`.
- **Exhaustive `switch`:** a `STATUS` object `as const` + `type Status = typeof STATUS[keyof typeof STATUS]` — add a key and every switch flags the missing case.
- **Function args that must be literals:** `setMode("readonly")` errors on `"read-only"` typos only if `"readonly"` wasn't widened — `as const` on the options array preserves the check.
- **With `satisfies`:** `{ a: 1 } as const satisfies Record<string, number>` — validated *and* literal.

## Diagram

```
expression                 inferred WITHOUT as const   WITH as const
──────────                 ─────────────────────────   ──────────────
"dark"                     "dark"  (const: no widen)   "dark"
{ theme: "dark" }          { theme: string }           { readonly theme: "dark" }
[ "a", "b" ]               string[]                    readonly ["a", "b"]  ← tuple!
{ n: 1, s: "x" }           { n: number; s: string }    { readonly n: 1; readonly s: "x" }

Value → type extraction:

const STATUS = { idle: "idle", busy: "busy" } as const
                    │                        │
                    │ typeof STATUS          │ keys stay literal,
                    ▼                        ▼ readonly + deep-frozen
          { readonly idle: "idle"; readonly busy: "busy" }
                    │
                    ▼  keyof typeof STATUS = "idle" | "busy"
   type Status = (typeof STATUS)[keyof typeof STATUS]
              = "idle" | "busy"        ← the union you wanted
```

## Code — explained

```typescript
// 1. Widening: properties widen because objects are mutable
const settings = { theme: "dark", retry: 3 };
//    type: { theme: string; retry: number }

// 2. as const: literals kept, everything readonly, deeply
const frozen = { theme: "dark", retry: 3 } as const;
//    type: { readonly theme: "dark"; readonly retry: 3 }
// frozen.theme = "light";   // Error: Cannot assign to 'theme' (read-only)

// 3. Arrays become readonly TUPLES — position matters
const pair = ["a", "b"] as const;        // readonly ["a", "b"]
// pair.push("c");                       // Error: 'push' doesn't exist on readonly tuple
const first: "a" = pair[0];              // (4) pair[0] is literally "a"

// 5. The value-union pattern — one object powers value AND type
const STATUS = {
  idle: "idle",
  busy: "busy",
  done: "done",
} as const;
type Status = (typeof STATUS)[keyof typeof STATUS];   // "idle" | "busy" | "done"

function setStatus(s: Status) { return `-> ${s}`; }
console.log(setStatus(STATUS.busy));     // (6) -> busy
// setStatus("bussy");                   // (7) Error: typo caught at compile time

// 8. Nested readonly — as const is DEEP
const cfg = { db: { host: "h", ports: [80, 443] } } as const;
// cfg.db.ports[0] = 81;                 // Error: readonly all the way down
console.log(cfg.db.ports.length, first); // 2 a
```

1. Without `as const`, `settings.theme` widens to `string` — TS assumes you might reassign it, so it keeps the type honest (and useless for literal checks).
2. `as const` rewrites the inferred type: literal `"dark"` instead of `string`, `readonly` on every property, recursively.
3. On arrays the effect is bigger than people expect: not `readonly string[]` but `readonly ["a", "b"]` — a fixed-length tuple with literal elements.
4. `pair[0]` has type `"a"` — you can assign it to a `"a"`-typed variable. Without `as const`, `pair[0]` would be `string`.
5. `typeof STATUS[keyof typeof STATUS]` — index the object's type by all its keys → union of all value types. The single most-used `as const` idiom.
6. `STATUS.busy` is the literal `"busy"`, which satisfies `Status` — the runtime value and the type came from the same source of truth.
7. `"bussy"` isn't in the union — the typo is a compile error, not a silent runtime no-op.
8. Deep freeze at the type level: `cfg.db.ports` is `readonly [80, 443]`; even index writes are rejected. (At runtime, though, `cfg.db.ports[0] = 81` would still mutate — `as const` emitted no `Object.freeze`.)

## Problems

### Easy — fix the widening
**Problem:** `function setMode(m: "dev" | "prod")` works, but `const opts = { mode: "dev" }; setMode(opts.mode)` errors. Fix it with `as const`.
**Try this input:** `setMode(opts.mode)`.
**Expected output:** compiles and logs `mode: dev`; without `as const`, the compiler says `Argument of type 'string' is not assignable to parameter of type '"dev" | "prod"'`.
**Solution:**
```typescript
function setMode(m: "dev" | "prod") {
  console.log("mode:", m);
}

const opts = { mode: "dev" } as const;   // mode: "dev", not string
setMode(opts.mode);                       // OK — "dev" is assignable to "dev" | "prod"
```
**Logic explained:**
1. `{ mode: "dev" }` widens `mode` to `string` — a `string` can't go into `"dev" | "prod"`, so the call fails. Nothing was wrong at runtime; the *type* lied about precision.
2. `as const` keeps `mode: "dev"` — a literal is assignable to any union containing it.
3. Same fix applies to arrays of options, nested config — anywhere a literal must survive inference.

### Medium — union of values from a const map
**Problem:** Given `const METHODS = { get: "GET", post: "POST", del: "DELETE" } as const`, write a type `Method` that is the union of its *values*, and a `call(m: Method, url: string)` that rejects `"PUT"`.
**Try this input:** `call(METHODS.post, "/api")` and `call("PUT", "/api")`.
**Expected output:** first logs `POST /api`; second is a compile error (`"PUT"` not in the union).
**Solution:**
```typescript
const METHODS = {
  get: "GET",
  post: "POST",
  del: "DELETE",
} as const;

type Method = (typeof METHODS)[keyof typeof METHODS];   // "GET" | "POST" | "DELETE"

function call(m: Method, url: string) {
  console.log(`${m} ${url}`);
}

call(METHODS.post, "/api");   // POST /api
call("GET", "/api");          // GET /api — literal works too
// call("PUT", "/api");       // Error: '"PUT"' not assignable to 'Method'
```
**Logic explained:**
1. `keyof typeof METHODS` = `"get" | "post" | "del"` — the *keys*.
2. Indexing `typeof METHODS` by that union yields the *value* types: `"GET" | "POST" | "DELETE"`.
3. Both the map entry (`METHODS.post`) and the raw literal (`"GET"`) satisfy `Method`; `"PUT"` doesn't exist in the map, so it's a compile error. Add `put: "PUT"` to the object and the union updates automatically — one source of truth.

### Hard — `as const` + `satisfies`: validated config that keeps literals
**Problem:** Build a `routes` table where every value must match `interface Route { path: string; auth: boolean }`, but keys/values must stay literal for `type RouteKey`/`type RoutePath` unions — and one entry with a missing `auth` must fail to compile.
**Try this input:** `const routes = { home: {...}, admin: { path: "/a" /* missing auth */ } }`.
**Expected output:** the `admin` entry errors (`Property 'auth' is missing`); with `auth` added, `RoutePath` = `"/" | "/a"` and `routes.home.path` is `"/"`, not `string`.
**Solution:**
```typescript
interface Route {
  path: string;
  auth: boolean;
}

const routes = {
  home: { path: "/", auth: false },
  admin: { path: "/a", auth: true },
  // bad: { path: "/x" },            // Error: 'auth' is missing in type '{ path: string; }'
} as const satisfies Record<string, Route>;

type RouteKey = keyof typeof routes;                      // "home" | "admin"
type RoutePath = (typeof routes)[keyof typeof routes]["path"]; // "/" | "/a"

function goto(k: RouteKey) {
  const r: Route = routes[k];
  console.log(r.path, r.auth);
}
goto("admin");    // /a true
const p: RoutePath = "/";   // literal, not string
console.log(p);             // /
```
**Logic explained:**
1. `satisfies Record<string, Route>` *checks* each entry against `Route` — missing `auth` is caught — without widening the inferred type. (Annotating `: Record<string, Route>` instead would widen `path` to `string` and lose the literals.)
2. `as const` keeps every value literal and readonly; `satisfies` keeps it honest. They compose: `as const satisfies X` is the modern "validate my constant" idiom.
3. `keyof typeof routes` gives `"home" | "admin"` — keys as a union, usable for `goto`.
4. Indexing by `["path"]` after the value-union extracts `"/" | "/a"` — the exact paths, as a type. Change the table and both unions follow.

## The 30-second interview answer

"`as const` is a const assertion — it tells TypeScript to infer the narrowest possible type: literals stay literals, and everything becomes deeply readonly. Without it, `{ theme: 'dark' }` widens to `{ theme: string }` because properties are mutable; with it you get `{ readonly theme: 'dark' }`. On arrays it's even stronger — `['a','b'] as const` is the tuple `readonly ['a','b']`. It emits zero JavaScript — it's not `Object.freeze`, the runtime object is still mutable. The big use is extracting unions from data: `type Status = typeof STATUS[keyof typeof STATUS]` turns a lookup object into a compile-time union, so routes, action types, and status enums live in one place. And it composes with `satisfies` — `as const satisfies Config` validates the shape while preserving literals."

## Follow-up trap

**"Does `as const` freeze the object at runtime?"** — No. It's erased like every type assertion; `obj.field = x` would still mutate the real object if bypassed through `any`. For runtime immutability you need `Object.freeze` — and note `Object.freeze`'s *type* is `Readonly<T>`, shallow, while `as const`'s readonly is deep at the type level. Second trap: **"`as const` vs `const` variable declaration?"** — `const` only stops rebinding the variable; properties still widen (`const o = {a:1}` → `a: number`). `as const` narrows the *type* of the expression. Third: **"why did my `readonly [1,2]` break when passed to a function taking `number[]`?"** — a readonly tuple isn't assignable to a mutable array (the callee could push); the function should take `readonly number[]` — which leads straight into file 31.
