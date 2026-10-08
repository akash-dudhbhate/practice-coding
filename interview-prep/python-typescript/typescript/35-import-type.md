# 35 — `import type` — type-only imports and why they exist

> **Interview question:** "Why does TypeScript have `import type` — isn't a normal import good enough?"
> **What the interviewer is really testing:** Whether you know `import type` guarantees the import is *fully erased* at compile — which matters for `isolatedModules`, bundlers, circular dependencies, and tools that transform files one-at-a-time without knowing the type context.

## Theory — what it is

`import type` imports **types only** — the entire import is erased during compile, so no JS `import` statement is emitted at all:

```typescript
import type { User } from "./user";     // gone after compile — no runtime import
import { helper, type Config } from "./x";  // mixed: value + inline type import
```

Rules that matter:

- **The imported name can't be used as a value.** `new User()`, `User.create()`, `typeof User` (as a value-position use) — all errors. It's purely a type.
- **Erased unconditionally.** A normal `import { User }` *also* gets erased if TS can prove `User` is only used in type positions — but whether the compiler can see that depends on the tooling. `import type` makes the guarantee explicit.
- **Three forms:** `import type { A }`, `import type * as ns`, and the inline `import { a, type B }` (TS 4.5+).
- **`verbatimModuleSyntax` (TS 5+)** makes the old "elide unused type imports" behavior explicit: with it on, imports are kept exactly as written — `import type` is the *required* way to mark type imports.
- **`import type` works where values don't:** it's the only way to import types in contexts where the file is transpiled without type info (esbuild, Babel, SWC — they strip types without understanding them).

## Why it was needed

The root problem: **TypeScript is compiled file-by-file, but imports have side effects.**

A single-file transpiler (esbuild, Babel, `isolatedModules` mode) looks at `import { User } from "./user"` in isolation and must decide: emit `import "./user"` or drop it? If `User` is a type it should be dropped — but a single-file transpiler *can't tell* whether `User` is a type or a class without looking at `./user.ts`. If it guesses wrong:

- Keeping it → a runtime `import` for a file that may not exist at runtime (`.d.ts`-only modules) or introduces a circular dependency.
- Dropping it → a real class import silently deleted.

`import type` removes the guesswork: the developer declares "this is only types, always drop it" so the transpiler doesn't need type information. That's the entire motivation — it's not about style, it's about *correctness under single-file transpilation*.

Bonus reason: `isolatedModules` (required by many bundler pipelines) *requires* this explicitness for type re-exports, and circular-dependency bugs often vanish when an accidental runtime import becomes `import type`.

## Where it's used in a real project

- **Everywhere in bundler/Vite/esbuild projects:** importing `type { User }` for annotations — the standard habit.
- **Fixing circular imports:** `a.ts` imports `type { B }` from `b.ts` — no runtime edge, cycle broken at the module-graph level.
- **Node-specific types in shared code:** `import type { Request } from "express"` in a file bundled for the browser — the import disappears, express never gets bundled.
- **`verbatimModuleSyntax` codebases:** enforced explicitly — every import is either `import type` (erased) or a real import (kept). No ambiguity.
- **`.d.ts` files and type re-exports:** `export type { X } from "./x"` — re-exporting types without creating a runtime edge.

## Diagram

```
// user.ts
export interface User { name: string }     <- type only, no value
export class UserRepo {...}                <- real value

// app.ts
import type { User } from "./user";   ──►  ERASED completely
import { UserRepo } from "./user";    ──►  kept: import "./user"

EMITTED JS for app.ts:
  import { UserRepo } from "./user";      // User gone — file never imported
                                          //   just for a type

WHY single-file transpilers need it:
  import { Foo } from "./x";              <- esbuild sees ONE file
      │  Is Foo a type? a class? Can't know without ./x
      ├── guess "keep" -> runtime import of a maybe-type-only module
      └── guess "drop" -> real value silently missing

  import type { Foo } from "./x";         <- NO GUESSING: always drop
```

## Code — explained

```typescript
// ---- user.ts
export interface User { id: string; name: string }
export const DEFAULT_USER: User = { id: "0", name: "anon" };

// ---- app.ts
import type { User } from "./user";            // (1) type-only, erased
import { DEFAULT_USER } from "./user";         // (2) real value import

function label(u: User): string {              // (3) User usable in types
  return u.name;
}

console.log(label(DEFAULT_USER));              // anon

// 4. Trying to use a type-only import as a value:
// const u = new User();                        // Error: 'User' is a type

// 5. Inline type imports (TS 4.5+) — mix in one statement:
import { someFn, type Options } from "./util";

// 6. Re-exporting types — explicit type re-export
export type { User } from "./user";            // no runtime edge created

// 7. Under verbatimModuleSyntax this distinction is ENFORCED:
// import { User } from "./user" would ERROR if User is only a type —
// the compiler makes you write import type so the emit is predictable.
```

1. `import type` promises: erase this completely — no `import "./user"` will appear in the output. That means `user.ts` doesn't even need to exist at runtime (it could be types-only).
2. `DEFAULT_USER` is a `const` — a real value — so this import *is* emitted.
3. Type positions are the only place a type-only import can appear — annotations, generics, `extends` clauses.
4. Value positions are rejected: `new User()`, `User.prototype`, passing `User` as an argument — all errors, because there *is* no `User` at runtime.
5. `import { type X, y }` lets one import statement do both — the cleanest style when you need values *and* types from one module.
6. `export type` is the re-export version — forwarding types without creating a runtime module dependency.
7. `verbatimModuleSyntax` is the "strict mode" for this: whatever you write is what gets emitted — `import type` = erase, plain `import` = keep. No compiler magic guessing.

## Problems

### Easy — convert to type-only import
**Problem:** `import { User } from "./models"` is only ever used in type positions, and your bundler warns it's creating an unnecessary runtime import. Fix it so the import is fully erased.
**Try this input:** `function save(u: User)` + `import type { User }`.
**Expected output:** compiles the same; emitted JS contains *no* `import "./models"`.
**Solution:**
```typescript
// models.ts
export interface User { id: string }

// app.ts
// before: import { User } from "./models";   — ambiguous, maybe emitted
// after:
import type { User } from "./models";         // guaranteed erased

function save(u: User): void {
  console.log(`saving ${u.id}`);
}

save({ id: "u1" });    // saving u1
```
**Logic explained:**
1. `User` never appears in a value position — it's pure annotation — so the runtime edge to `./models` was never needed.
2. `import type` makes the erasure explicit rather than trusting the compiler to notice: emitted JS simply has no import.
3. Why it matters: if `models.ts` imports other heavy modules, this prevents pulling them into the bundle for a mere type.

### Medium — break a circular dependency with `import type`
**Problem:** `order.ts` and `customer.ts` import each other's classes — a cycle causing `undefined` at runtime when one module loads first. The `Customer` type is only needed for annotations in `order.ts`. Fix the cycle.
**Try this input:** `new Order("o1", customer)` where `Order` needs `Customer` only as a type.
**Expected output:** compiles and runs — the `order -> customer` runtime edge is gone.
**Solution:**
```typescript
// customer.ts
export class Customer {
  constructor(public name: string) {}
}

// order.ts — was: import { Customer } from "./customer";  (runtime edge -> cycle)
import type { Customer } from "./customer";               // type only -> erased

export class Order {
  constructor(
    public id: string,
    public customer: Customer,      // annotation only — no runtime need
  ) {}
}

// main.ts
import { Customer } from "./customer";
import { Order } from "./order";
const o = new Order("o1", new Customer("Ana"));
console.log(o.customer.name);       // Ana
```
**Logic explained:**
1. The cycle existed because `order.ts` *ran* `import "./customer"` just to get a type. At runtime that's a real module edge, and whoever loads first sees a half-initialized module.
2. `import type` removes the runtime edge entirely — `order.js` never imports `customer.js`. Cycle gone.
3. The parameter type still works at compile time — `customer: Customer` type-checks exactly as before.
4. This is one of `import type`'s most practical uses: cycles caused purely by type imports evaporate for free.

### Hard — `verbatimModuleSyntax` and re-exports
**Problem:** With `verbatimModuleSyntax: true`, `import { User } from "./a"; export { User };` fails — you're re-exporting what might be a type as if it's a value. Write a barrel file (`index.ts`) that re-exports a class, a const, and an interface correctly.
**Try this input:** consumers do `import { Repo, TYPES, type Entity } from "./index"`.
**Expected output:** compiles under `verbatimModuleSyntax`; `Entity` is a type, `Repo`/`TYPES` are values.
**Solution:**
```typescript
// store.ts
export interface Entity { id: string }
export const TYPES = { user: "u" } as const;
export class Repo {
  save(e: Entity) { console.log("saved", e.id); }
}

// index.ts — the barrel
export { Repo, TYPES } from "./store";        // values: real re-export
export type { Entity } from "./store";        // type: export type — no edge

// consumer.ts
import { Repo, TYPES, type Entity } from "./index";

const e: Entity = { id: "e1" };
new Repo().save(e);                            // saved e1
console.log(TYPES.user);                       // u
```
**Logic explained:**
1. `verbatimModuleSyntax` makes emit literal: `export { Entity }` would emit a *value* re-export of a thing that doesn't exist at runtime — so it must be `export type`.
2. `export type { X }` is erased completely; `export { X }` emits a real re-export. The barrel now precisely mirrors what's a value vs what's a type.
3. Consumers use `import { Repo, TYPES, type Entity }` — the inline `type` marker keeps the same explicitness at the use site.
4. Interview point: `verbatimModuleSyntax` exists because "let the compiler guess" broke down under single-file transpilers — this flag turns implicit import elision into a rule you can see in the source.

## The 30-second interview answer

"`import type` marks an import as types-only — it's completely erased at compile, so no `import` statement is emitted and no runtime module edge is created. It exists because single-file transpilers like esbuild and Babel can't tell whether `import { Foo }` refers to a type or a value without type information — `import type` removes the guesswork. That's why `isolatedModules` and `verbatimModuleSyntax` push you toward it: under `verbatimModuleSyntax`, `import type` is erased and plain `import` is kept, exactly as written — no implicit elision. Practically I use it to avoid pulling heavy modules into a bundle for a mere annotation, to break circular dependencies where the cycle was only ever a type-level dependency, and to re-export types with `export type`. The rule of thumb: if you only use a name in type positions, `import type` makes that fact explicit and guaranteed."

## Follow-up trap

**"If TS already erases unused type imports, why bother?"** — Because "the compiler notices it's only used as a type" only works when the compiler *sees the whole program*. esbuild/Babel/`isolatedModules` compile file-by-file and can't know — `import type` is the developer *asserting* the answer so the tool doesn't have to guess. Second trap: **"can you use an `import type` name in a value position — e.g. `import type { Foo }` then `new Foo()`?"** — No: "`Foo` cannot be used as a value because it was imported using 'import type'". Third: **"does `import type` prevent the module from being bundled?"** — It prevents your *import statement* from creating a runtime edge; if something else imports the module for real, it still gets bundled. And a classic gotcha: **`import { type X, Y }` inline syntax vs `import type { X }`** — same erasure guarantee, the inline form just mixes value and type imports in one statement (TS 4.5+).
