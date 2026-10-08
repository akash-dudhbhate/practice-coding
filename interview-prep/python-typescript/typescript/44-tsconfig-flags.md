# 44 — tsconfig flags: `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`, `verbatimModuleSyntax`

> **Interview question:** "Which tsconfig strict flags do you enable, and what does each one actually catch?"
> **What the interviewer is really testing:** Whether you know what each flag *does* beyond "makes things stricter" — `strict` is a bundle of sub-flags, `noUncheckedIndexedAccess` adds `| undefined` to index lookups, `exactOptionalPropertyTypes` separates "absent" from "`undefined`", and `verbatimModuleSyntax` controls import emit.

## Theory — what it is

**`strict: true`** — a bundle flag enabling ~8 sub-flags at once. The ones that matter most:

- `noImplicitAny` — params/returns with no inferable type error instead of silently `any`
- `strictNullChecks` — `null`/`undefined` become distinct types, can't flow into `string`
- `strictFunctionTypes`, `strictBindCallApply`, `strictPropertyInitialization`, `noImplicitThis`, `alwaysStrict`, `useUnknownInCatchVariables`

**`noUncheckedIndexedAccess`** — indexing (`obj[key]`, `arr[i]`) returns `T | undefined` — because `arr[10]` on a 3-element array *is* `undefined` at runtime, and previously TS lied about it.

**`exactOptionalPropertyTypes`** — `prop?: T` means "may be *absent*" — NOT "may be `undefined`". `{ prop: undefined }` becomes an error; you must write `prop?: T | undefined` to allow explicitly passing `undefined`.

**`verbatimModuleSyntax`** — imports/exports are emitted *as written*: `import type` erased, plain `import` kept. No compiler guessing about whether an import is type-only (see file 35).

## Why it was needed

- **`strict`** — TypeScript launched permissive so JS devs could adopt it; `strict` was added (2.x-3.x) as the "actually safe" mode. `strictNullChecks` alone killed the "billion-dollar mistake" class of bugs. It's the baseline; disabling sub-flags is the exception.
- **`noUncheckedIndexedAccess`** — `arr[i]` was typed `T` even when `i` is out of bounds — a lie that produced `undefined`-crashes. This flag makes index access honest; the `| undefined` forces a check.
- **`exactOptionalPropertyTypes`** — `{ name?: string }` used to accept `{ name: undefined }`, blurring "absent" vs "present but undefined." When `Object.keys`/`in` checks distinguish the two, the blur matters. This flag separates them — required for certain type-level gymnastics (e.g. `Partial`-adaptive APIs).
- **`verbatimModuleSyntax`** — import elision ("does the compiler drop this import?") was invisible magic that broke under single-file transpilers (esbuild, Babel). This flag makes the rule explicit: `import type` = erase, `import` = keep — what's written is what's emitted.

## Where it's used in a real project

- **`strict` catches:** reading `.name` on `User | undefined` after a failed lookup; implicit `any` params creeping in; `this` being `undefined` in callbacks.
- **`noUncheckedIndexedAccess` catches:** `items[i].name` where `i` is a loop index or user input — forces `items[i]?.name` or a bounds check; `Record<string, T>` lookups where the key might not exist.
- **`exactOptionalPropertyTypes` catches:** spreading `{ opts: undefined }` into a function expecting `{ opts?: Opts }` — under the flag, passing *explicit* `undefined` errors where "absent" wouldn't.
- **`verbatimModuleSyntax` catches:** type-only imports that single-file transpilers would mis-emit; makes `.cts`/`.mts` ESM-vs-CJS emit predictable.

## Diagram

```
strictNullChecks:
  const u: User | undefined = find(id);
  u.name        ❌ must narrow first   | off: compiles, crashes at runtime

noUncheckedIndexedAccess:
  const arr: string[] = ["a"];
  arr[5]               : string         | flag ON:  string | undefined
  arr[5].toUpperCase() ❌ must handle undefined
  obj["key"]           : T | undefined  — Record lookups too

exactOptionalPropertyTypes:
  interface Cfg { debug?: boolean }
  const c: Cfg = {}              ✅ absent is fine
  const c: Cfg = { debug: undefined }
                     OFF: ✅   |   ON: ❌ — must be debug?: boolean | undefined
  "absent" ≠ "present-but-undefined" — Object.keys sees the difference

verbatimModuleSyntax:
  import { A } from "./x"   -> KEPT in emit  (you wrote a real import)
  import type { A } from "./x" -> ERASED     (you wrote 'type')
  no compiler guessing — what you wrote is what's emitted
```

## Code — explained

```typescript
// 1. strictNullChecks — the big sub-flag of strict
function findUser(id: string): { name: string } | undefined {
  return id === "u1" ? { name: "Ana" } : undefined;
}
const u = findUser("u9");
// u.name;                     // ❌ Error: u is possibly 'undefined'
if (u) console.log(u.name);    // ✅ narrowed

// 2. noUncheckedIndexedAccess — honest indexing
const scores = [10, 20, 30];
const s = scores[10];          // type: number | undefined  (flag ON)
// s.toFixed();                // ❌ Error: possibly undefined
console.log(s ?? "missing");   // ✅ handle it

const dict: Record<string, number> = { a: 1 };
const v = dict["nope"];        // number | undefined — the key might not exist

// 3. exactOptionalPropertyTypes — absent vs explicit-undefined
interface Config {
  debug?: boolean;
  // to allow explicit undefined you'd write:  debug?: boolean | undefined;
}
const ok: Config = {};                          // ✅ absent — fine
// const bad: Config = { debug: undefined };    // ❌ under the flag: not assignable
const ok2: Config = { debug: false };           // ✅ real value

// 4. verbatimModuleSyntax — emit mirrors source
//    import type { X } -> erased    import { X } -> kept
//    (covered in depth in file 35)
```

1. `strictNullChecks` makes `undefined` a real, tracked type — `findUser` must return `| undefined`, and the caller must narrow. Without it, `u.name` compiles and crashes.
2. `scores[10]` — index access was `number` before; with the flag it's `number | undefined`, forcing `??`/`?.`. Same for `Record` lookups — the most common new-error source when enabling it on legacy code.
3. `exactOptionalPropertyTypes`: `{}` assigns fine (absent allowed); `{ debug: undefined }` errors — the property's *type* is `boolean`, optionality is about presence. To accept explicit `undefined`, opt in: `debug?: boolean | undefined`.
4. `verbatimModuleSyntax`: turns implicit import-elision into a visible rule — `import type` erases, `import` stays, no surprises under esbuild/Babel.

## Problems

### Easy — read a possibly-undefined array element
**Problem:** `const first = arr[0]` — under `noUncheckedIndexedAccess`, `first` is `T | undefined`. Fix code that calls `first.toUpperCase()` so it compiles and is safe.
**Try this input:** `["a","b"]` and `[]`.
**Expected output:** `A` then `empty`.
**Solution:**
```typescript
function firstUpper(arr: string[]): string {
  const first = arr[0];                  // string | undefined under the flag
  if (first === undefined) return "empty";
  return first.toUpperCase();            // narrowed to string
}

console.log(firstUpper(["a", "b"]));   // A
console.log(firstUpper([]));           // empty
```
**Logic explained:**
1. `arr[0]` isn't safe just because it's index 0 — empty arrays make it `undefined`; the flag makes the type reflect that.
2. The `=== undefined` check narrows `string | undefined` → `string` — `first.toUpperCase()` is now provably safe.
3. Alternatives: `arr[0]?.toUpperCase()` (returns `string | undefined`), `arr.at(0)` (same honest typing), or a `for` loop/index bound check.

### Medium — exactOptionalPropertyTypes and config objects
**Problem:** `interface Opts { retries?: number; verbose?: boolean }`. A caller does `build({ retries: maybeNumber })` where `maybeNumber: number | undefined`. Under `exactOptionalPropertyTypes` this errors — show the two correct fixes.
**Try this input:** `maybeNumber = undefined` then `= 3`.
**Expected output:** both compile-fix paths shown; `{}` and `{retries:3}` built.
**Solution:**
```typescript
interface Opts {
  retries?: number;            // absent OK; explicit undefined NOT ok
  verbose?: boolean | undefined;  // absent AND explicit-undefined both ok
}

function build(o: Opts) { console.log(o); }

const maybeNum: number | undefined = undefined;

// Fix 1: widen the property to include undefined
build({ verbose: maybeNum === undefined ? undefined : true });

// Fix 2: only include the key when defined (spread)
build({
  ...(maybeNum !== undefined ? { retries: maybeNum } : {}),
});
//  -> {} when undefined; { retries: 3 } when set
```
**Logic explained:**
1. `retries?: number` under the flag means "key may be absent, but if present must be `number`" — `{ retries: undefined }` violates that.
2. Fix 1 adds `| undefined` to the type — `verbose?: boolean | undefined` means "absent or explicitly undefined, both fine."
3. Fix 2 uses conditional spread — the key is only *present* when defined, so "absent" is what the type sees.
4. Why the flag exists: `Object.keys`/`"k" in obj` distinguish absent from undefined — types now match that runtime distinction.

### Hard — enabling noUncheckedIndexedAccess on a Record-based lookup
**Problem:** `const handlers: Record<string, () => string>` maps route → handler. `handlers[route]()` compiles without the flag but `route` may be unknown. Make it safe under `noUncheckedIndexedAccess` — handle the miss without casting.
**Try this input:** `route = "home"` (exists) and `route = "bogus"`.
**Expected output:** `HOME PAGE` then `404`.
**Solution:**
```typescript
const handlers: Record<string, () => string> = {
  home: () => "HOME PAGE",
  about: () => "ABOUT PAGE",
};

function route(path: string): string {
  const h = handlers[path];            // (() => string) | undefined
  if (h === undefined) return "404";   // handle the miss
  return h();                          // h: () => string — narrowed
}

console.log(route("home"));    // HOME PAGE
console.log(route("bogus"));   // 404
```
**Logic explained:**
1. `handlers[path]` under the flag is `(() => string) | undefined` — `Record<string, X>` claims every string maps to `X`, but most keys don't exist; `| undefined` is the truth.
2. The `=== undefined` check narrows the call-site — `h()` is provably callable after it.
3. Without the flag, `handlers["bogus"]()` compiles and crashes `h is not a function` at runtime — this flag turns that class of bug into a compile error.
4. Alternative worth mentioning: `handlers[path]?.()` returning `string | undefined`, or `Map.get` which already returns `V | undefined` — the flag brings `Record` lookups in line with `Map`'s honesty.

## The 30-second interview answer

"`strict` is a bundle — the big ones being `strictNullChecks` (null/undefined become tracked types) and `noImplicitAny` (no silent `any`). I always enable it — it's the baseline for real safety. `noUncheckedIndexedAccess` adds `| undefined` to index access — `arr[i]` and `record[key]` honestly reflect that the index/key might not exist, forcing a check instead of a runtime crash; it's noisy on legacy code but catches real bugs. `exactOptionalPropertyTypes` separates 'property absent' from 'property present-but-undefined' — `prop?: T` means absent-or-T, and explicitly passing `undefined` errors unless you write `prop?: T | undefined`; it matters because `Object.keys` and `in` can distinguish the two at runtime. `verbatimModuleSyntax` makes import emit literal — `import type` erases, `import` stays — which is what single-file transpilers like esbuild need, since they can't infer whether an import is type-only. I enable strict plus the first two on new projects; the last two depend on whether the codebase's semantics actually distinguish the cases they protect."

## Follow-up trap

**"Is `strict` just `strictNullChecks`?"** — No — it's ~8 flags: `noImplicitAny`, `strictNullChecks`, `strictFunctionTypes`, `strictBindCallApply`, `strictPropertyInitialization`, `noImplicitThis`, `alwaysStrict`, `useUnknownInCatchVariables`. `strictNullChecks` is the biggest but not the whole bundle — and `strict` auto-includes new flags as they're added, so `strict: true` is "strictest current default." Second trap: **"does `noUncheckedIndexedAccess` affect `.at()` / tuple access?"** — `.at(i)` already returns `T | undefined` even without the flag; tuples (`arr: [string, number]`) are unaffected for *in-range* indices since length is known — `t[0]` is `string`, `t[5]` errors as out-of-range. Third: **"why would anyone *not* enable `exactOptionalPropertyTypes`?"** — it breaks a lot of real code that passes `{ opt: undefined }` meaning "not set"; `JSON.parse`-adjacent and spread-heavy codebases get noisy. And a classic: **`verbatimModuleSyntax` vs `importsNotUsedAsValues`/`preserveValueImports`** — the latter were the older, confusing knobs; `verbatimModuleSyntax` (TS 5+) replaces them with one clear rule.
