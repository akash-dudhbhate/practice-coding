# 34 — `declare`, ambient types, and `.d.ts` files

> **Interview question:** "What does `declare` do in TypeScript, and what is a `.d.ts` file?"
> **What the interviewer is really testing:** Whether you understand `declare` means *"trust me, this exists at runtime — emit nothing"* — it's how TypeScript describes JavaScript that already exists (browser globals, JS libraries, env vars) without generating code. `.d.ts` files are just declarations collected into a file.

## Theory — what it is

`declare` tells the compiler: **"a value/type with this name exists at runtime; I'm only describing its shape — do not emit any JavaScript for it."**

```typescript
declare const VERSION: string;        // "a global const exists — trust me"
declare function gtag(cmd: string, ...args: any[]): void;
declare class Chart { render(): void }
declare module "*.png";               // "importing a .png is allowed"
```

Rules that matter:

- **Zero output.** `declare` produces no JS — if the thing *doesn't* actually exist at runtime, you get a runtime crash despite clean compilation. It's an unchecked promise you're making to the compiler.
- **`.d.ts` = a file of only declarations.** No implementations allowed (`declare` is implied — you write `function f(): void` not `declare function`). It's the standard way to ship types for JS code.
- **Ambient context:** inside `.d.ts` (or a `declare global`/`declare module` block), everything is a description, not code.
- **`declare module "x"`** types an entire import — either for an untyped npm package or for non-code assets (`*.css`, `*.svg`).
- **`declare global`** adds to the global scope from inside a module — used for `process.env`, `window.myApp`, etc.
- **`/// <reference types="..." />`** or tsconfig `types`/`typeRoots` pull `.d.ts` files into the compilation.
- **Types-only or values:** `declare` can declare types (`declare type X = ...` — rarely needed since `.d.ts` files are ambient anyway), values, classes, namespaces, and enums.

## Why it was needed

TypeScript's whole job is describing JavaScript — but most JavaScript was written *without* types. When you `npm i lodash`, TS has no idea what `_.debounce` is. Rewriting every JS library in TS wasn't feasible, so `.d.ts` files became the bridge: **DefinitelyTyped** (`@types/lodash`) is a giant repo of declaration files describing JS libraries, shipped as separate packages.

Same story for things that exist but were never in your code at all: `window`, `document`, `process.env`, a global injected by a `<script>` tag, a webpack `DefinePlugin` constant, images/CSS imports handled by the bundler. All of these need a way to say "this exists, here's its shape, don't emit code" — that's `declare`.

## Where it's used in a real project

- **`@types/*` packages:** every `@types/lodash`, `@types/express` install is just `.d.ts` files.
- **Asset imports:** `vite/client` or a local `globals.d.ts` declares `declare module "*.svg" { ... }` so `import logo from "./logo.svg"` compiles.
- **Env vars:** `declare global { namespace NodeJS { interface ProcessEnv { API_URL: string } } }` — typed `process.env`.
- **Library authors shipping types:** write `lib.js`, ship `lib.d.ts` alongside (or generate it with `tsc --declaration`).
- **Third-party script tags:** analytics libs that set `window.dataLayer` — `declare const dataLayer: unknown[]`.
- **Generated `.d.ts`:** `tsc --emitDeclarationOnly` produces `.d.ts` from your TS for consumers.

## Diagram

```
YOUR CODE                          WHAT ACTUALLY EXISTS AT RUNTIME
─────────                          ────────────────────────────────

import _ from "lodash";    ──►     node_modules/lodash/... .js files
        │
        └─ needs types ─► @types/lodash/index.d.ts
                          declare function debounce(fn, ms): ...;
                          (descriptions only — zero JS emitted)

import logo from "./a.svg" ──►     bundler serves a URL string
        │
        └─ needs types ─► globals.d.ts:
                          declare module "*.svg" {
                            const src: string;
                            export default src;
                          }

process.env.API_KEY        ──►     Node's process.env object
        │
        └─ needs types ─► declare global {
                            namespace NodeJS {
                              interface ProcessEnv { API_KEY: string }
                            }
                          }

declare = "trust me, it exists"    .d.ts = a file full of those promises
If the promise is a lie -> clean compile, crash at runtime.
```

## Code — explained

```typescript
// ---- assets.d.ts — a "script" .d.ts (no top-level imports/exports)
declare module "*.svg" {
  const src: string;                // (1) importing an svg gives a string
  export default src;
}

// ---- globals.d.ts — a "module" .d.ts (has import/export)
declare global {                    // (2) add to global scope from a module
  namespace NodeJS {
    interface ProcessEnv {
      API_URL: string;              // (3) now process.env.API_URL: string
    }
  }
}

export {};                          // (4) makes the file a module so
                                    //     `declare global` is allowed

// ---- app.ts
import logo from "./logo.svg";      // (5) compiles thanks to "*.svg" decl
const url = process.env.API_URL;    // (6) string — not string | undefined
                                    //     (whether that's wise: see below)

// 7. declare in a normal .ts file — describing an injected global
declare const __BUILD_TIME__: string;   // webpack DefinePlugin sets this
console.log(__BUILD_TIME__);            // compiles — emits nothing for it

// ---- legacy.d.ts — describes an untyped JS module
declare module "legacy-lib" {
  export function init(opts: { debug?: boolean }): void;
}
```

1. The `"*.svg"` wildcard module declaration says: *any* import matching that pattern yields a module whose default export is a string. Now the bundler's behavior is type-described.
2. `declare global` is the way to augment globals when your `.d.ts` file is a module (has imports/exports). `namespace NodeJS { interface ProcessEnv }` merges into the existing `ProcessEnv` interface — declaration merging doing the work.
3. After this, `process.env.API_URL` is typed `string`. Note the trade-off: this *asserts* the var exists — if it's missing at runtime you get `undefined` typed as `string`. Safer: `API_URL: string | undefined` or validate at startup.
4. A file with no imports/exports is a *script*, not a module — `declare global` is only legal in modules, so `export {}` is the idiom. This split matters: in a *module* `.d.ts`, `declare module "*.svg"` would be treated as a *module augmentation* of a module that doesn't exist — an error. Wildcard/ambient module declarations belong in a *script* `.d.ts` (like `assets.d.ts` here), where `declare module` creates rather than augments.
5. Without the declaration, `import logo` errors: "Cannot find module './logo.svg'". With it, `logo: string`.
6. `ProcessEnv` merging gives you a typed env — a hugely common real-world pattern.
7. `declare const __BUILD_TIME__` in a `.ts` file works identically — it emits nothing; if the build tool doesn't actually define it, `console.log` prints `undefined` or crashes, and TypeScript won't warn you.
8. Library declarations can be as precise as you want — function signatures, classes, generics. This is exactly how `@types/*` packages are written.

## Problems

### Easy — type an injected global
**Problem:** A third-party script sets `window.analytics = { track(name: string, props?: object): void }`. Write the declaration so `analytics.track("signup")` compiles in any file — no implementation needed.
**Try this input:** `analytics.track("signup", { plan: "pro" })`.
**Expected output:** compiles cleanly; at runtime the real `window.analytics` is called.
**Solution:**
```typescript
// globals.d.ts
declare global {
  interface Window {
    analytics: {
      track: (name: string, props?: Record<string, unknown>) => void;
    };
  }
}
export {};

// app.ts
window.analytics.track("signup", { plan: "pro" });   // compiles
// window.analytics.track(123);                      // Error: number ≠ string
```
**Logic explained:**
1. `interface Window` inside `declare global` merges with the DOM lib's `Window` interface — you're adding a property, not replacing the interface.
2. Declaration merging is why this works: two `Window` interfaces in scope combine their members.
3. The `export {}` makes the `.d.ts` a module, which is what unlocks `declare global`.

### Medium — declare a module for an untyped import
**Problem:** You import `import { cn } from "classnames-legacy"` but it ships no types, and there is no `@types` package. Write a declaration file so `cn("a", "b", cond && "c")` is typed — accepting strings/falsy values, returning `string`.
**Try this input:** `cn("btn", isActive && "active", undefined)`.
**Expected output:** returns `string`; `cn(123)` is a compile error.
**Solution:**
```typescript
// classnames-legacy.d.ts
declare module "classnames-legacy" {
  type ClassValue = string | number | false | null | undefined;
  export function cn(...args: ClassValue[]): string;
}

// app.ts — usage
import { cn } from "classnames-legacy";
const cls = cn("btn", true && "active", undefined);   // string
// cn({ foo: 1 });                                    // Error: object not allowed
```
**Logic explained:**
1. `declare module "name"` describes the whole module — everything inside is ambient, so `export function cn(...)` needs no body.
2. `ClassValue` mirrors the runtime contract: strings/numbers join, falsy values are skipped — so the type accepts exactly what the function can handle.
3. The file doesn't need `declare` on the inner items — inside `declare module`, everything is already ambient.
4. Alternative worth mentioning: `declare module "classnames-legacy";` (no body) types the whole module as `any` — quick escape hatch, but you lose the safety.

### Hard — typed env vars via declaration merging
**Problem:** Make `process.env` fully typed for your app: `DATABASE_URL` required `string`, `PORT` optional `string`, `NODE_ENV` restricted to `"development" | "production" | "test"`. Then show a safe accessor that parses `PORT` to a number.
**Try this input:** `process.env.PORT` set to `"3000"`, `process.env.NODE_ENV` read.
**Expected output:** `3000` as a number; assigning `process.env.NODE_ENV = "banana"` is a compile error.
**Solution:**
```typescript
// env.d.ts
declare global {
  namespace NodeJS {
    interface ProcessEnv {
      DATABASE_URL: string;
      PORT?: string;
      NODE_ENV: "development" | "production" | "test";
    }
  }
}
export {};

// app.ts
function getPort(): number {
  const raw = process.env.PORT;              // string | undefined
  const port = raw === undefined ? 8080 : Number(raw);
  if (Number.isNaN(port)) throw new Error("PORT must be a number");
  return port;
}

const env = process.env.NODE_ENV;            // "dev"|"prod"|"test" literal
// process.env.NODE_ENV = "banana";          // Error: not assignable
console.log(getPort(), env);
```
**Logic explained:**
1. `ProcessEnv` is an existing interface in `@types/node` — `declare global` + `namespace NodeJS` merges your members into it.
2. `PORT?: string` keeps it `string | undefined` — honest typing that forces the `Number()`/fallback handling instead of pretending it's always set.
3. `NODE_ENV` as a string-literal union gives autocomplete and rejects `"banana"` at assignment — the type encodes the deployment contract.
4. The caveat to say out loud: this is still a *promise* — env vars are all strings at runtime and might be missing entirely. Types here document intent; a startup validation (or a schema lib) is the real guard.

## The 30-second interview answer

"`declare` means 'this exists at runtime, I'm only describing its shape — emit no JavaScript.' It lets TypeScript type-check code that references things it didn't write: browser globals, libraries without types, bundler-injected constants, asset imports. `.d.ts` files are just collections of declarations — they contain shapes, no implementations — and they're how the whole ecosystem gets types: every `@types/*` package is `.d.ts` files, and `tsc --declaration` generates them for your own libraries. The key mechanisms are `declare module` for imports — including wildcard modules like `*.svg` — and `declare global` for augmenting globals like `process.env`. The catch: `declare` is an *unchecked promise* — the compiler trusts you completely, so a declaration describing something that doesn't exist compiles fine and explodes at runtime."

## Follow-up trap

**"What's the difference between `.d.ts` and `.ts`?"** — A `.d.ts` can only contain declarations — no function bodies, no `const x = 1` — and emits zero JavaScript. A `.ts` file emits code. Also: `.d.ts` files aren't compiled *into* your program; they're consumed during type-checking. Second trap: **"if `declare` emits nothing, what happens if you `declare const x` that's never actually defined?"** — Clean compile, runtime `ReferenceError` (or `undefined`). The compiler takes you at your word; that's why `declare` blocks describing reality are a documentation burden, not a safety net. Third: **"why does `import logo from './logo.svg'` error even though webpack handles it fine?"** — TypeScript's module resolution doesn't know what the bundler does; the `declare module "*.svg"` declaration is how you teach it. And a sneaky one: **in a `.d.ts` *script* file (no imports/exports) you don't need `declare global` — top-level declarations are already global; the `export {}` is only needed when the file is a module.**
