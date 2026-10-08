# 16 — Type assertion vs type guard — which survives refactoring and why

> **Interview question:** "What's the difference between a type assertion and a type guard — and which one survives refactoring?"
> **What the interviewer is really testing:** Do you know an assertion is an unchecked compile-time claim that silently rots as code changes, while a guard is a runtime test that fails loudly — and do you reach for guards at boundaries?

## Theory — what it is

A **type assertion** — `x as T` — is a *claim*: "compiler, trust me, this is a `T`." It emits zero JavaScript and performs zero checks. A **type guard** is a *test*: runtime code that inspects the value, whose boolean result TypeScript wires back into the type system. Built-in guards are `typeof`, `instanceof`, `in`, equality, and truthiness; a **custom guard** is a function returning a *type predicate*, `x is T`.

```typescript
function isDog(pet: Cat | Dog): pet is Dog {
  return "bark" in pet;   // a real runtime check
}
```

The asymmetry that matters for refactoring:

- **`as` duplicates an unchecked claim at every site.** If `Dog` gains a required field, or a union gains a member, every `pet as Dog` still compiles — the assertion never re-verifies the shape — and malformed values flow downstream to crash far from the lie.
- **A guard concentrates the check in one place.** When the shape changes, you fix one tested function; and when the check fails at runtime, you land in an `else` branch — a visible, handleable outcome — instead of a `TypeError` three calls deep.
- **Narrowing stays honest automatically.** `typeof`, `instanceof`, discriminant checks on tagged unions, and `switch` + `never` exhaustiveness are re-analyzed by the compiler on every change. Add a union member and the `never` check becomes a compile error, *forcing* you to handle the new case.

Honesty caveat: a hand-rolled `x is T` predicate is still code the compiler trusts — the body can be wrong too. But "one wrong check function" beats "fifty wrong claims scattered across the codebase," and a guard's failure mode is a testable boolean, not silence.

## Why it was needed

TypeScript must bridge compile-time types and runtime values the compiler can't see — network responses, DOM lookups, user input. It offers two bridges: assertions (cheap, silent) and guards (one extra function, but honest). Codebases learn the hard way: `as` is a bet that's never re-checked; a guard is a bet tested on every call. Refactoring is where the bill comes due — assertions accumulate drift, guards accumulate correctness.

## Where it's used in a real project

- **Assertions (legit):** DOM lookups you control (`querySelector("#app") as HTMLDivElement`), `as const`, test fixtures, narrowing `unknown` after a check the compiler can't track.
- **Assertions (rot):** `resp as ApiUser`, `JSON.parse(x) as Config` at boundaries — each one a stale claim waiting for a schema change.
- **Guards:** `typeof x === "string"` before string methods; `e instanceof HttpError` in catch blocks; discriminant narrowing `if (msg.type === "click")`; custom guards `isUser`/`isConfig` at every JSON boundary; exhaustive `switch` over discriminated unions with a `never` default — the gold standard for refactor-safe code.

## Diagram

```
value arrives typed Cat | Dog
        │
   ┌────┴──────────┐
   ▼               ▼
 pet as Dog    isDog(pet)
 "trust me"    "check it"
   │               │
   │          ┌────┴────┐
   │       true        false
   │          │          │
   ▼          ▼          ▼
 compiler   compiler   compiler
 sees Dog   sees Dog   sees Cat
   │          │          │
   ▼          ▼          ▼
 runtime:   runtime:   runtime:
 UNCHECKED  proven Dog proven Cat
   │
   └── after refactor (Dog changes / union grows):
       as Dog        → still compiles → malformed value → crash later
       isDog         → fix ONE check fn / returns false → handled path
       switch+never  → compile error at the switch → forced fix
```

## Code — explained

```typescript
interface Cat { meow(): string }
interface Dog { bark(): string }

// --- Assertion: compiles, lies, crashes ---
function speakUnsafe(pet: Cat | Dog): string {
  return (pet as Dog).bark();              // (1)
}
// speakUnsafe({ meow: () => "mew" });     // (2) compiles → TypeError at runtime

// --- Guard: check, then trust ---
function isDog(pet: Cat | Dog): pet is Dog {   // (3)
  return "bark" in pet;
}

function speakSafe(pet: Cat | Dog): string {
  if (isDog(pet)) return pet.bark();       // (4) pet: Dog — proven
  return pet.meow();                       // (5) pet: Cat — proven by exclusion
}

console.log(speakSafe({ bark: () => "woof" }));  // woof
console.log(speakSafe({ meow: () => "mew" }));   // mew

// --- The refactor test: add a Bird member to the union ---
// speakUnsafe compiles unchanged — the as-claim never re-checks.
// speakSafe routes Birds to the else — and an exhaustive switch
// would ERROR at compile time, pointing at the exact place to fix.
```

1. `(pet as Dog)` relabels the union as `Dog`. Emits nothing; on a `Cat`, `.bark` is `undefined` and calling it throws — the compiler approved the whole path.
2. This call compiles: `pet` is `Cat | Dog`, a `Cat` literal is legal, and the assertion inside suppresses any doubt.
3. `pet is Dog` is a **type predicate** — the signature promises: "when this returns `true`, treat `pet` as `Dog`." The body is ordinary runtime code (`in` checks the property exists).
4. Inside the `if`, control-flow analysis narrows `pet` to `Dog` *because the runtime check passed*.
5. The `else` narrows to `Cat` — `Cat | Dog` minus `Dog`. Every path is backed by a real test.

## Problems

### Easy — Replace `as` with `instanceof`
**Problem:** `function errMsg(e: unknown) { return (e as Error).message; }` returns `undefined` for non-Errors instead of a fallback. Fix it without `as`.
**Try this input:** `errMsg(new Error("boom"))`, `errMsg("plain string")`
**Expected output:** before fix — `boom`, then `undefined` (silently wrong); after fix — `boom`, then `plain string`.
**Solution:**
```typescript
function errMsg(e: unknown): string {
  if (e instanceof Error) return e.message;   // narrowed honestly
  return String(e);                            // anything → string fallback
}

console.log(errMsg(new Error("boom")));   // boom
console.log(errMsg("plain string"));      // plain string
console.log(errMsg(42));                  // 42
```
**Logic explained:**
1. `(e as Error).message` claims `e` is an `Error`; on a string, `.message` is `undefined` — a silent wrong answer, not even a crash.
2. `instanceof` is a real runtime check: inside the `if`, `e` is `Error` because the test proved it.
3. The fallback `String(e)` makes "not an Error" an explicit, handled outcome — the signature `string` never lies.

### Medium — Guard at the JSON boundary
**Problem:** `const u = JSON.parse(text) as User` compiles with malformed JSON and crashes later. Write `parseUser` using a guard that returns `User | null`.
**Try this input:** `{"id":1,"name":"Amy"}` and `{"id":1}`
**Expected output:** `{ id: 1, name: 'Amy' }`, then `null` — no crash.
**Solution:**
```typescript
interface User { id: number; name: string }

function isUser(x: unknown): x is User {
  if (typeof x !== "object" || x === null) return false;
  const o = x as Record<string, unknown>;
  return typeof o.id === "number" && typeof o.name === "string";
}

function parseUser(text: string): User | null {
  const data: unknown = JSON.parse(text);
  return isUser(data) ? data : null;   // guard-verified or honestly absent
}

console.log(parseUser(`{"id":1,"name":"Amy"}`));   // { id: 1, name: 'Amy' }
console.log(parseUser(`{"id":1}`));                // null
```
**Logic explained:**
1. `as User` relabels whatever `JSON.parse` produced — missing `name` compiles fine and crashes at the first `.name.toUpperCase()` downstream.
2. `isUser` checks both fields with `typeof` — a real proof, run on every call.
3. `User | null` makes "bad payload" a first-class outcome in the signature; callers must handle `null`, so the failure is visible at the boundary instead of exploding three files away.
4. When `User` gains a field, you update `isUser` — one place — versus hunting every `as User` in the repo.

### Hard — Exhaustiveness: the refactor-proof switch
**Problem:** Two versions of `area`: one asserts, one narrows a discriminated union with a `never` exhaustiveness check. Show what happens when `| { kind: "triangle"; base: number; height: number }` is added to `Shape`.
**Try this input:** `areaUnsafe({ kind: "square", side: 2 })` today; then add the `triangle` member and recompile.
**Expected output:** today — `NaN` (silent wrong answer!) then `4`. After adding `triangle` — `areaSafe` fails to compile (`Type '{ kind: "triangle"; ... }' is not assignable to type 'never'`) pointing at the default branch; `areaUnsafe` still compiles and returns `NaN` for triangles.
**Solution:**
```typescript
type Shape =
  | { kind: "circle"; r: number }
  | { kind: "square"; side: number };

// assertion version — "handles" circles, lies about everything else
function areaUnsafe(s: Shape): number {
  const c = s as { kind: "circle"; r: number };
  return Math.PI * c.r ** 2;
}

// guard version — discriminant narrowing + exhaustiveness
function areaSafe(s: Shape): number {
  switch (s.kind) {
    case "circle":
      return Math.PI * s.r ** 2;
    case "square":
      return s.side ** 2;
    default:
      const _exhaustive: never = s;   // compile error if a member is unhandled
      return _exhaustive;
  }
}

console.log(areaUnsafe({ kind: "square", side: 2 }));  // NaN — silently wrong
console.log(areaSafe({ kind: "square", side: 2 }));    // 4
```
**Logic explained:**
1. `s as {kind:"circle"; r:number}` compiles for a square — asserting a union member is always allowed — so `c.r` is `undefined` and `Math.PI * undefined` is `NaN`. Not even a crash: a silent wrong number propagating through your code.
2. `switch (s.kind)` narrows on the discriminant: each `case` knows the exact member, with `s.r`/`s.side` type-checked.
3. `const _exhaustive: never = s` is the refactor tripwire: `s` in `default` is `never` only when every member is handled. Add `triangle` → `s` narrows to the triangle member → compile error *at the exact line that needs a new case*.
4. This is "survives refactoring" in code: the assertion version compiles forever while rotting; the guard version refuses to compile until the new reality is handled.

## The 30-second interview answer

"An assertion — `x as T` — is a compile-time-only claim: it emits no code and nothing verifies it, so when the shape drifts it keeps compiling and produces malformed values that crash downstream. A type guard is a runtime test wired into the type system — `typeof`, `instanceof`, `in`, or a function returning `x is T` — so a wrong guess lands in an `else` branch instead of a crash. The refactoring answer: assertions rot silently because the unchecked claim is duplicated at every site and never re-verified; guards survive because the check lives in one tested function, discriminant narrowing stays honest under union changes, and `switch` + `never` exhaustiveness turns 'you forgot a case' into a compile error. My rule: `as` for things the compiler genuinely can't know and I can prove otherwise; guards at every boundary and every union."

## Follow-up trap

**"A custom `x is T` guard can lie too — so why is it better than `as`?"** — true: the compiler trusts the predicate's declared return without verifying the body, so `isDog` can be wrong. The difference is surface area and failure mode: a guard is *one* function you can unit-test and fix when the shape changes; assertions are N scattered claims with no single place to correct. A wrong guard also fails at its check site; a wrong `as` fails arbitrarily far downstream. Second trap: **"does `isDog` protect you if `Dog` itself changes?"** — only partially: `"bark" in pet` keeps checking the *old* shape, so you must still update the guard. What auto-protects you is checking the compiler can re-derive — discriminants, `typeof`, `instanceof`, `never`-exhaustive switches. The strongest refactor-safety comes from putting the tag in the *type* (discriminated unions), not in a hand-maintained function.
