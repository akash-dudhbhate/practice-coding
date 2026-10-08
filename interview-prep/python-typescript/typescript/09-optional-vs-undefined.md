# 09 — `name?: string` vs `name: string | undefined`

> **Interview question:** "Is `name?: string` the same as `name: string | undefined`?"
> **What the interviewer is really testing:** Whether you know `?` controls *key presence* while `| undefined` controls the *value* — and whether you've hit `exactOptionalPropertyTypes`, the flag that makes the difference a compile error instead of trivia.

## Theory — what it is

They look interchangeable because **reading** is identical — `obj.name` is `string | undefined` either way. They differ on **writing**:

- **`name?: string`** — the key may be **absent**. `{ }` and `{name: "x"}` are both legal.
- **`name: string | undefined`** — the key is **required**; only its *value* may be `undefined`. `{ }` is an error; you must write `{name: undefined}` or `{name: "x"}`.

Now the nuance that makes this interview-worthy: **`exactOptionalPropertyTypes`** (a separate tsconfig flag — *not* enabled by `strict`, a common misconception). With it **off**, `{name: undefined}` is also accepted for `name?: string` — TS treats "absent" and "present-but-undefined" as the same. With it **on**, `name?: string` means "if the key exists, its value is `string` — period" — so `{name: undefined}` is a **compile error**.

Why care? At runtime, absent and present-undefined are observably different: `"name" in obj`, `Object.keys(obj)`, spreads, and `Object.assign` all distinguish them. `exactOptionalPropertyTypes` makes the *types* match that reality — critical for libraries and codebases where `in` checks or merges are meaningful (React props, config merging, PATCH bodies).

## Why it was needed

Pre-flag, `name?: string` silently accepted `{name: undefined}` — and that hole produced real bugs:

- **Spread overrides:** `{...defaults, ...overrides}` where `overrides.name` is explicitly `undefined` *wipes* the default — the resulting object has the key with an `undefined` value, breaking `"name" in result` checks downstream.
- **Assignability lies:** a function returning `{timeout?: number}` could return `{timeout: undefined}`; a caller doing `if ("timeout" in cfg)` branches wrong.
- **Library contracts:** types like React's props or Node's options interfaces want "absent = use default," and an explicit `undefined` sneaking in defeated that.

`exactOptionalPropertyTypes` (TS 4.4) tightened `?` to mean exactly "may be absent." If you *want* "present-or-undefined," you now write it honestly: `name?: string | undefined` — which is the union of both syntaxes and accepts all three forms.

## Where it's used in a real project

- **Library/framework types:** many published types enable `exactOptionalPropertyTypes` internally; consumers passing `{...base, timeout: maybe}` get errors until they stop smuggling `undefined` keys.
- **Options bags:** `opts?: { retries?: number; timeout?: number }` — absent means default; callers building options via spread must avoid explicit `undefined`.
- **API types:** `{middleName: string | null}` (server always sends it) vs `{middleName?: string}` (server may omit it) — pick based on the real contract.
- **Class fields:** `name?: string` vs `name: string | undefined` changes whether constructors must initialize — `strictPropertyInitialization` cares.
- **`Partial<T>` results:** `Partial<User>` makes every key optional — combined with exactOptionalPropertyTypes, merging partials is where the errors surface.

## Diagram

```
                 key absent     key=undefined    key="x"
                 ----------     -------------    --------
name?: string       yes       off:yes / on:NO      yes
name: string|undef   NO            yes             yes
name?: string|undef yes            yes             yes   <- accepts all three

runtime sees the difference (regardless of types):
  { }                "name" in o -> false   Object.keys -> []
  { name: undefined } "name" in o -> TRUE    Object.keys -> ["name"]
  both: o.name -> undefined        JSON.stringify drops both

the classic bug without the flag:
  {...{name:"dflt"}, ...{name:undefined}}  ->  {name: undefined}
  looks like "name provided" to `in` / Object.keys, but value is gone
```

## Code — explained

```typescript
// tsconfig: { "strict": true, "exactOptionalPropertyTypes": true }

type A = { name?: string };                 // 1: key may be absent
type B = { name: string | undefined };      // 2: key required, value may be undefined

const a1: A = {};                           // 3 OK — absent allowed
const a2: A = { name: "Ada" };              //   OK
// const a3: A = { name: undefined };       // 4 ERROR with exactOptionalPropertyTypes
                                            //   (compiles without the flag!)
// const b1: B = {};                        // 5 ERROR — name is REQUIRED
const b2: B = { name: undefined };          //   OK — present with undefined value

function readName(x: A | B): string | undefined {
  return x.name;                            // 6 reading is identical either way
}

// the "accept everything" spelling:                                       // 7
type C = { name?: string | undefined };
const c1: C = {}; const c2: C = { name: undefined }; const c3: C = { name: "Ada" };

// runtime: absent vs present-undefined are DIFFERENT objects               // 8
const empty = {};
const explicit: { name?: string | undefined } = { name: undefined };
console.log("name" in empty, "name" in explicit);   // false true
console.log(Object.keys(explicit));                  // ["name"]
console.log(JSON.stringify(explicit));               // '{}' — both drop on the wire
```

1. `name?: string` — the `?` governs *presence*. With `exactOptionalPropertyTypes`, presence implies a real `string`.
2. `name: string | undefined` — `| undefined` on a *required* key only widens the value, not the presence. The object literal must contain the key.
3. `{}` is valid for `A` — absent is the whole point of `?`.
4. `a3` is the trap line: without the flag it compiles (absent ≈ undefined-valued); with the flag it's `error TS2375` — "Type '{ name: undefined }' is not assignable… 'undefined' is not a valid value for 'name'."
5. `b1` fails because required keys must be written, even if only to hold `undefined`. This spelling is rare — useful when the contract says "the sender must consciously decide."
6. `readName` doesn't care which spelling built the object — the *read* type is `string | undefined` both ways. The difference is purely in what you're allowed to construct.
7. `name?: string | undefined` is the union of both meanings — the fix when you genuinely want to accept explicit `undefined` under `exactOptionalPropertyTypes`.
8. `in` and `Object.keys` distinguish presence at runtime; `JSON.stringify` does not preserve it (both serialize to `{}` — the wire can't carry "present but undefined").

## Problems

### Easy — which literals compile?
**Problem:** With `exactOptionalPropertyTypes` on, which of these compile?

```typescript
type Cfg = { retries?: number; label: string | undefined };
const c1: Cfg = { label: undefined };
const c2: Cfg = { retries: undefined, label: "x" };
const c3: Cfg = { retries: 3, label: undefined };
```

**Try this input:** each assignment under `"exactOptionalPropertyTypes": true`.
**Expected output:** `c1` OK; `c2` ERROR (`retries` can't be explicitly `undefined`); `c3` OK.
**Solution:**

```typescript
// c1: OK — retries absent (allowed), label present-as-undefined (required key, allowed value)
// c2: ERROR TS2375 — retries?: number rejects an explicit undefined under the flag
// c3: OK — retries present with a real number; label present with undefined
// Fix for c2's intent: { label: "x" } (omit retries) — or change the type to
// retries?: number | undefined if explicit undefined should be legal.
```

**Logic explained:**
1. `retries?: number` — `?` permits absence only; under `exactOptionalPropertyTypes`, a *present* `retries` must be a `number`.
2. `label: string | undefined` — required key: must appear, but `undefined` is a legal value. `c1` and `c3` both satisfy it.
3. Takeaway: `?` answers "may the key be missing?"; `| undefined` answers "may the value be undefined?" — orthogonal questions.

### Medium — the spread that breaks under the flag
**Problem:** This helper compiles without `exactOptionalPropertyTypes` but errors with it on. Explain why and fix it so `timeout` is only present when defined.

```typescript
interface Options { url: string; timeout?: number }
function build(url: string, timeout?: number): Options {
  return { url, timeout };            // ERROR under exactOptionalPropertyTypes
}
```

**Try this input:** `build("/api", undefined)` vs `build("/api", 3000)`.
**Expected output:** `error TS2375: Type 'number | undefined' is not assignable…` on the literal — because `{timeout: undefined}` is being constructed. Fixed: `{url: "/api"}` and `{url:"/api", timeout:3000}`.
**Solution:**

```typescript
interface Options { url: string; timeout?: number }

function build(url: string, timeout?: number): Options {
  // conditional spread: key only exists when timeout is a real number
  return { url, ...(timeout !== undefined && { timeout }) };
}

console.log(build("/api", undefined));   // { url: '/api' }      — no timeout key!
console.log(build("/api", 3000));        // { url: '/api', timeout: 3000 }
console.log("timeout" in build("/api")); // false
```

**Logic explained:**
1. `{ url, timeout }` shorthand always emits the key — with `timeout: undefined` when absent. Under the flag, `timeout?: number` rejects that literal, surfacing the latent bug.
2. `...(cond && { timeout })` — `&&` yields `false` (spreading `false` adds nothing) or `{timeout}`; the key exists *iff* the value is real. Idiomatic fix; alternatives: build then `if (timeout !== undefined) o.timeout = timeout`, or loosen the type to `timeout?: number | undefined`.
3. Why it matters beyond compiling: `Object.assign(defaults, build(...))` — an explicit `undefined` key would *overwrite* a default; omitting the key preserves it. The flag makes the types honest about merge semantics.

### Hard — strip undefined keys, correctly typed
**Problem:** Write `compact<T>` that removes every key whose value is `undefined` at runtime, and whose *return type* marks every key optional-without-undefined — so the result is assignable under `exactOptionalPropertyTypes`. `compact({a: 1, b: undefined, c: "x"})` → `{a: 1, c: "x"}` typed `{a?: number; b?: never... }`— actually: `b` must not linger as `number | undefined`.
**Try this input:** `{url: "/x", timeout: undefined as number | undefined, tag: "t"}`.
**Expected output:** `{url: "/x", tag: "t"}` — and assignable to `{url?: string; timeout?: number; tag?: string}` under the flag.
**Solution:**

```typescript
// every key becomes optional AND its value loses `undefined`:
type Compact<T> = { [K in keyof T]?: Exclude<T[K], undefined> };

function compact<T extends object>(obj: T): Compact<T> {
  const out: Record<string, unknown> = {};
  for (const [k, v] of Object.entries(obj)) {
    if (v !== undefined) out[k] = v;     // drop undefined-valued keys entirely
  }
  return out as Compact<T>;
}

interface RequestCfg { url?: string; timeout?: number; tag?: string }

const raw = { url: "/x", timeout: undefined as number | undefined, tag: "t" };
const cfg: RequestCfg = compact(raw);    // compiles under exactOptionalPropertyTypes
console.log(cfg);                        // { url: '/x', tag: 't' }
console.log("timeout" in cfg);           // false — key truly absent
```

**Logic explained:**
1. `Exclude<T[K], undefined>` removes `undefined` from each value's type — `number | undefined` → `number`, so no key may hold `undefined`, satisfying `exactOptionalPropertyTypes`.
2. `[K in keyof T]?` — every key becomes optional because *any* key could have been stripped; that's the honest type for the runtime behavior (you can't know statically which were removed).
3. `v !== undefined` inside `Object.entries` drops the *key*, not just the value — this is the "present-but-undefined" cleanup that spread/`Object.assign` pipelines need.
4. The `as Compact<T>` cast is justified: we've proven at runtime that no `undefined` values survive — the same "narrow cast after proof" discipline as `unknown` validation.
5. Real-world slot: sanitizing objects before APIs whose types enable `exactOptionalPropertyTypes` (a growing set of libraries), or before `Object.assign` merges where explicit `undefined` would clobber defaults.

## The 30-second interview answer

"Not the same. `name?: string` means the key may be *absent* — `{}` is legal. `name: string | undefined` means the key is *required* but its value may be undefined — you must write `{name: undefined}`. Reading is identical — `string | undefined` either way — the difference is in construction. And it only bites with `exactOptionalPropertyTypes` — a separate flag, *not* part of `strict` — under which `{name: undefined}` no longer satisfies `name?: string`. It matters because absent and present-undefined differ at runtime: `"name" in obj`, `Object.keys`, spreads. The fix when you hit the error is either conditional spread `...(x !== undefined && {x})` or the honest type `name?: string | undefined`."

## Follow-up trap

**"Is `exactOptionalPropertyTypes` part of `strict`?"** — No — that's the trap answer. `strict` is a fixed umbrella (strictNullChecks, noImplicitAny, …); `exactOptionalPropertyTypes` is opt-in separately, which is why plenty of strict codebases still get bitten when a *dependency* enables it in its own types. Second trap: **"why does `JSON.stringify` not help distinguish these?"** — both `{a: undefined}` and `{}` serialize to `{}`; the wire can't carry "present-but-undefined," so the distinction is compile-time + in-memory only (`in`, `Object.keys`, spread, `Object.assign`). If an API needs to express "explicitly empty," it must use `null` — which is exactly why domain types pair `?` (absent) with `| null` (cleared) rather than relying on `undefined` semantics.
