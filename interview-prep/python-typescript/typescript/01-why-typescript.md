# 01 — Why TypeScript?

> **Interview question:** "What is TypeScript, and why would you use it over plain JavaScript?"
> **What the interviewer is really testing:** Do you understand that types are a *compile-time* safety net and a tooling layer — not a runtime feature — and can you name concrete payoffs: earlier bug-catching, safe refactors, and IDE autocomplete.

## Theory — what it is

TypeScript is JavaScript plus a **static type system** — a layer that describes what shape your data has (this variable is a `string`, this function returns a `User`, this object has a `name` field). TypeScript files (`.ts`) are fed to the TypeScript compiler (`tsc`), which does two things: it **type-checks** the code (reports errors like "you called `.toUpperCase()` on a number") and then **emits plain JavaScript** that runs anywhere JS runs — browser, Node, Deno, etc.

The crucial point: **types are erased at runtime**. After compilation there are no types left — the emitted JS is what actually executes. TypeScript cannot change what happens at runtime; it can only refuse to compile (or warn about) code that is *probably* wrong. That's why it's called "static" typing: the checking happens before the program runs, not during it.

In exchange for writing annotations like `name: string`, you get three big things: (1) **earlier errors** — bugs surface as red squiggles in your editor or as `tsc` failures in CI instead of as `undefined is not a function` in production; (2) **tooling** — your editor knows every property on an object, so autocomplete, "go to definition", and "rename symbol" actually work; (3) **safe refactoring** — rename a field or change a function signature and the compiler lists every place you broke, which is what makes large codebases maintainable.

Jargon check: a **type annotation** is the `: string`-style label you write; **type inference** is TypeScript figuring out types you didn't write; **transpilation** is the `.ts` → `.js` emit step (TypeScript is often called a transpiler rather than a compiler for this reason).

## Why it was needed

JavaScript is dynamically typed: a variable can hold anything, and mistakes are only discovered when that exact line executes. The classic failure modes:

- `user.emial` instead of `user.email` → returns `undefined`, which then explodes three functions later (or silently renders a blank email). Nothing warns you.
- Calling `formatPrice("12.99")` when the function expects a number → `"12.99".toFixed is not a function` at runtime, or worse, silent string math like `"5" + 1 === "51"`.
- Renaming a field in a 200-file codebase → you grep, miss two call sites, and find out via a bug report.

Without TypeScript, the only safety nets are tests (which must cover the buggy path), code review, and luck. TypeScript moves an entire class of bugs — typos, wrong argument shapes, impossible states — from "found by a user" to "found by the compiler in milliseconds." On a team, the type annotations also act as always-up-to-date documentation: `function checkout(cart: Cart, coupon?: Coupon): Receipt` tells the next engineer the contract without opening the function body.

## Where it's used in a real project

- **API boundaries:** typing the JSON your backend returns (`interface UserDto { id: number; email: string }`) so a renamed field on the server breaks the frontend build instead of breaking the page silently.
- **Refactoring:** renaming `user.name` to `user.fullName` across 40 files — `tsc` prints every broken call site instead of you grepping.
- **Modeling state:** `type RequestState = "idle" | "loading" | "success" | "error"` makes illegal states unrepresentable — you can't accidentally write `state === "loadign"`.
- **Library authoring:** typed packages ship `.d.ts` files so consumers get autocomplete and inline docs (this is why React/Express feel "smart" in your editor).
- **Gradual adoption:** `allowJs` lets a JS codebase migrate file by file — you don't rewrite everything on day one.

## Diagram

```
   you write                tsc                       runtime
+------------------+   +---------------------+   +-------------------+
|  app.ts          |   |  1. type-check       |   |  app.js (plain JS)|
|  name: string    |-->|     errors? --> STOP |-->|  types ERASED     |
|  greet(u: User)  |   |  2. emit .js         |   |  node / browser   |
+------------------+   +---------------------+   +-------------------+

   feedback loops:

   editor (VS Code)  <-- reads the same type info -->  autocomplete,
   hover docs, rename-symbol, red squiggles as you type

   CI pipeline:  tsc --noEmit   --> build fails before bad code ships
```

## Code — explained

```typescript
interface User {
  id: number;
  name: string;
  email: string;
}

function sendWelcomeEmail(user: User): void {
  console.log(`Sending to ${user.name} <${user.email}>`);
}

const ada = { id: 1, name: "Ada", email: "ada@example.com" };

sendWelcomeEmail(ada);                                        // OK
sendWelcomeEmail({ id: 2, name: "Bob", email: "b@x.com" });   // OK
// sendWelcomeEmail({ id: 3, name: "Cat" });                  // ERROR: missing 'email'
// sendWelcomeEmail(ada.email);                               // ERROR: string is not a User
// console.log(ada.emial);                                    // ERROR: 'emial' doesn't exist
```

1. `interface User` declares a *shape*: any value used as a `User` must have a numeric `id` and string `name`/`email`. This is the contract.
2. `sendWelcomeEmail(user: User)` annotates the parameter — the compiler will now check every call site against `User`.
3. `: void` is the return type — the function returns nothing useful.
4. `const ada = {...}` — TypeScript *infers* ada's type from the object literal; you don't have to write `: User` for the call to be checked.
5. Both valid calls compile because the argument's shape matches `User` (TypeScript is *structurally* typed — it's about shape, not class names).
6. The commented-out lines are the payoff: the missing `email`, the wrong argument type, and the `emial` typo are all compile errors — caught before the code ever runs. In plain JS all three would sail through and fail (or silently misbehave) at runtime.

## Problems

### Easy — the silent typo

**Problem:** This JavaScript ships to production and prints `Hello, undefined` because of a property typo. Add TypeScript types so the compiler catches it before it runs.

**Try this input:** `greet({ name: "Ada" })`
**Expected output:** `tsc` reports `error TS2551: Property 'nmae' does not exist on type 'User'. Did you mean 'name'?` — after fixing the typo, running the code prints `Hello, Ada`.
**Solution:**

```typescript
interface User {
  name: string;
}

// Buggy version — the compiler flags 'nmae' immediately:
// function greet(user: User): string {
//   return "Hello, " + user.nmae;
// }

// Fixed version:
function greet(user: User): string {
  return "Hello, " + user.name;
}

console.log(greet({ name: "Ada" })); // "Hello, Ada"
```

**Logic explained:**
1. Declaring `interface User { name: string }` gives the compiler a list of legal property names.
2. Annotating the parameter `user: User` means every `user.<something>` is checked against that list.
3. `nmae` isn't on the list, so `tsc` emits TS2551 (and even suggests `name`) — the bug is caught at compile time instead of printing `undefined` for a user.

### Medium — the safe rename

**Problem:** Product asks to rename `User.name` to `User.fullName`. The codebase has several call sites. In plain JS you'd `grep "name"` and pray — names like `username` and `fileName` flood the results. Show how the compiler becomes your checklist.

**Try this input:** change the interface field to `fullName` and run `tsc`.
**Expected output:** `tsc` reports an error at each still-broken call site, e.g. `error TS2339: Property 'name' does not exist on type 'User'` — a precise to-do list, no false positives.
**Solution:**

```typescript
interface User {
  id: number;
  fullName: string; // renamed from `name`
}

function label(u: User): string {
  return u.fullName; // fixed: was u.name — tsc pointed here
}

const users: User[] = [
  { id: 1, fullName: "Ada Lovelace" }, // fixed: object literals checked too
  { id: 2, fullName: "Grace Hopper" },
];

console.log(users.map(label)); // ["Ada Lovelace", "Grace Hopper"]
```

**Logic explained:**
1. The interface is the single source of truth — one edit changes the contract everywhere.
2. Every read (`u.name`), every object literal (`{ name: ... }`), and every function signature that used the old shape now produces a compile error.
3. You fix errors until `tsc` is silent — at that point the rename is *provably* complete, which grep can never guarantee.

### Hard — make illegal states unrepresentable

**Problem:** An app tracks fetch state with a string and a payload: `state` is `"loading" | "success" | "error"`. In JS, nothing stops you from reading `response.data` while `state === "loading"` — the classic `undefined` crash. Model it so the compiler *forces* you to handle each state before touching the data.

**Try this input:** `render({ status: "success", data: "hi" })` and `render({ status: "error", message: "boom" })`.
**Expected output:** `DATA: hi` then `ERR: boom`; meanwhile `resp.data` accessed outside the `"success"` branch is a compile error (`Property 'data' does not exist on type ...`).
**Solution:**

```typescript
type ApiResponse =
  | { status: "loading" }
  | { status: "success"; data: string }
  | { status: "error"; message: string };

function render(resp: ApiResponse): string {
  switch (resp.status) {
    case "loading":
      return "…";
    case "success":
      return `DATA: ${resp.data}`;      // data exists ONLY in this branch
    case "error":
      return `ERR: ${resp.message}`;    // message exists ONLY here
  }
}

console.log(render({ status: "success", data: "hi" }));   // "DATA: hi"
console.log(render({ status: "error", message: "boom" })); // "ERR: boom"
// render({ status: "success" });  // compile error: missing 'data'
// render({ status: "loadign" });  // compile error: typo in the literal
```

**Logic explained:**
1. This is a **discriminated union**: `status` is the "tag" that tells the compiler which variant it's looking at.
2. Inside `case "success"`, TypeScript *narrows* `resp` to the success variant — so `resp.data` type-checks; anywhere else it's an error because `data` doesn't exist on the other variants.
3. If you later add a `{ status: "cancelled" }` variant, `tsc` flags the switch as non-exhaustive at every call site that didn't handle it — the compiler drives the refactor, which is exactly why teams adopt TypeScript.

## The 30-second interview answer

"TypeScript is JavaScript with a static type system: you annotate or infer the shapes of your data, `tsc` checks the whole program before it runs, then erases the types and emits plain JS. The payoff is threefold — an entire class of bugs (typos, wrong argument shapes, impossible states) is caught at compile time instead of in production; editors get real autocomplete and go-to-definition; and large refactors become safe because the compiler lists every broken call site. It costs you annotations and a build step, and it's unsound at the edges, but on any codebase with more than one engineer the trade is overwhelmingly worth it."

## Follow-up trap

**"Doesn't TypeScript slow you down / isn't it just ceremony?"** — The expected follow-up probes whether you've felt the *costs*, not just read the pitch. Good handling: admit the real costs (generics can get hairy, type gymnastics in library code, `as any` escape hatches, a build step, third-party types sometimes lagging the library). Then land the punchline: those costs are front-loaded and fixed, while the JS costs — runtime type bugs, grep-driven refactors, stale docs — scale with codebase size and team size. Mentioning that types are erased at runtime (so zero runtime cost and zero runtime protection — you still validate external data at the boundary) shows you understand the model rather than the marketing.
