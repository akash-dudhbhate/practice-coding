# 05 — `strict` mode

> **Interview question:** "What does `"strict": true` in tsconfig actually turn on, and which of those flags matters most?"
> **What the interviewer is really testing:** Whether you can name the flags beyond "it makes things stricter" — especially `strictNullChecks` and `noImplicitAny` — and whether you'd enable it on a real project (yes) and know the migration story.

## Theory — what it is

`"strict": true` in `tsconfig.json` is a **master switch** that enables a family of stricter type-checking flags at once. It's the default in `tsc --init` and every serious project template, and it keeps growing — new TS versions may add flags under the `strict` umbrella, so upgrading TS can surface new errors.

The flags it turns on (the ones worth naming in an interview):

- **`strictNullChecks`** — the big one. Without it, `null` and `undefined` are assignable to *everything* (`const s: string = null` compiles!). With it, `null`/`undefined` are their own types and you must handle them — this single flag eliminates the "cannot read property of undefined" bug class at compile time.
- **`noImplicitAny`** — when the compiler can't infer a type, it errors instead of silently using `any`. Function parameters with no annotation and no context are the classic trigger.
- **`strictFunctionTypes`** — checks function parameter types *contravariantly* (prevents assigning a handler that takes `Dog` where one taking `Animal` is expected).
- **`strictBindCallApply`** — type-checks `.bind()`, `.call()`, `.apply()` arguments.
- **`strictPropertyInitialization`** — class properties must be initialized in the constructor or at declaration (unless `!` or `| undefined`).
- **`noImplicitThis`** — `this` inside a function must have a known type; errors on `this: any` contexts.
- **`useUnknownInCatchVariables`** — `catch (e)` gives `e: unknown` instead of `any`, forcing you to check before `e.message`.
- **`alwaysStrict`** — emits `"use strict"` and parses files in ES strict mode.

You can also turn `strict` on and selectively opt flags *out* (`"strict": true, "strictPropertyInitialization": false`) — common during migrations.

## Why it was needed

TypeScript's original defaults were chosen for *adoptability*: a 2012-era JS codebase could be renamed `.ts` and compile, because anything unchecked silently became `any` and `null` fit anywhere. The cost: a huge slice of real bugs passed right through. The two most expensive:

- **Unchecked nulls** — Tony Hoare called `null` his "billion-dollar mistake." Without `strictNullChecks`, `user.address.city` where `address` can be `null` compiles fine and crashes for users.
- **Silent `any`** — every un-inferrable parameter becoming `any` means errors you *think* are checked aren't. `any` is contagious: one `any` in a chain poisons everything downstream.

`strict` bundles the fixes so teams don't have to discover the flags one by one. The migration path exists because flipping it on a legacy codebase produces hundreds of errors at once — hence the per-flag opt-outs, and the convention of enabling strict only for new code (`strict` in a child tsconfig) while migrating incrementally.

## Where it's used in a real project

- **Every new project's tsconfig:** `"strict": true` is the baseline — non-negotiable on most professional teams.
- **Null-safety at boundaries:** `strictNullChecks` forces `find`/`Map.get`/optional JSON fields to be handled: `users.get(id)?.name`.
- **Catching `any` leaks in reviews:** `noImplicitAny` means a forgotten parameter type is a build error, not a silent hole.
- **Class initialization contracts:** `strictPropertyInitialization` catches "property used before the constructor set it" — a real prod-crash pattern.
- **Safer error handling:** `useUnknownInCatchVariables` forces `if (e instanceof Error)` before reading `e.message`.
- **Incremental adoption:** `strict: true` + `"strictNullChecks": false` on a legacy app, then ratcheting flags back on directory by directory.

## Diagram

```
                    "strict": true
                          |
   +----------+-----------+-----------+----------+---------+
   |          |           |           |          |         |
   v          v           v           v          v         v
strict    noImplicit  strict     strict     useUnknown alwaysStrict
Null      Any         Function   Property   InCatch    ("use strict"
Checks    (no silent  Types      Init       (e:unknown  emitted)
(null ≠   any)                   (class     in catch)
string)                          fields)
   |
   +-- the flag that kills "Cannot read property 'x' of undefined"
```

## Code — explained

```typescript
// tsconfig: { "strict": true }

// --- strictNullChecks ---
function getLength(s: string | null): number {
  // return s.length;            // ERROR: 's' is possibly 'null'
  return s === null ? 0 : s.length; // narrowed: s is string inside
}

// --- noImplicitAny ---
// function logIt(msg) {}        // ERROR: Parameter 'msg' implicitly has an 'any' type
function logIt(msg: string): void { console.log(msg); }

// --- strictPropertyInitialization ---
class UserService {
  private repo: UserRepo;             // must be assigned in constructor
  // private cache: Map<string, User>;  // ERROR: not initialized
  constructor(repo: UserRepo) { this.repo = repo; }
}

// --- useUnknownInCatchVariables ---
try {
  JSON.parse("{}");
} catch (e) {
  // console.log(e.message);     // ERROR: 'e' is of type 'unknown'
  if (e instanceof Error) console.log(e.message); // OK after narrowing
}

interface UserRepo { find(id: string): User }
interface User { id: string }
```

1. `s: string | null` makes the nullability *explicit* — and `strictNullChecks` then refuses `s.length` until the `=== null` branch rules it out.
2. `noImplicitAny` — `msg` has no annotation and no inference source, so instead of silently being `any` (a hole), it's a compile error demanding a type.
3. `strictPropertyInitialization` — `cache` would error because nothing guarantees it's set before use; `repo` is fine because the constructor assigns it unconditionally.
4. `useUnknownInCatchVariables` — thrown values can be anything (`throw "oops"` is legal JS), so `e` is `unknown` and must be narrowed before reading `.message`.
5. Every error above was a real-world production crash pattern; strict mode moves them all to compile time.

## Problems

### Easy — strictNullChecks fix

**Problem:** With `strictNullChecks` on, this fails to compile. Fix it in the idiomatic way.

```typescript
function firstChar(s: string | null): string {
  return s[0];
}
```

**Try this input:** `firstChar("abc")` and `firstChar(null)`.
**Expected output:** Without a fix: `error TS18047: 's' is possibly 'null'`. Fixed version prints `a` for `"abc"` and returns `""` for `null`.
**Solution:**

```typescript
function firstChar(s: string | null): string {
  return s?.[0] ?? ""; // optional chain -> string|undefined, ?? supplies default
}

console.log(firstChar("abc")); // "a"
console.log(firstChar(null));  // ""
```

**Logic explained:**
1. `s[0]` on `string | null` errors because indexing `null` is the exact crash the flag exists to prevent.
2. `s?.[0]` short-circuits to `undefined` when `s` is null — so the result type is `string | undefined`.
3. `?? ""` replaces nullish (`null`/`undefined`) results with a default — the idiomatic "handle or default" one-liner strictNullChecks pushes you toward.

### Medium — strictPropertyInitialization

**Problem:** Under `strict`, this class errors on `engine`. Fix it *three* different ways and know when each is appropriate.

```typescript
class Car {
  engine: Engine; // ERROR: not initialized
}
```

**Try this input:** `new Car()` then `car.engine.start()`.
**Expected output:** Each fix compiles; the wrong choice (e.g. `!` when the field is never set) still compiles but crashes at runtime — that's the trap.
**Solution:**

```typescript
interface Engine { start(): string }
const defaultEngine: Engine = { start: () => "vroom" };

// Fix 1 — assign in constructor (preferred: real guarantee)
class CarA {
  constructor(private engine: Engine) {}
  go() { return this.engine.start(); }
}

// Fix 2 — initialize at declaration (when there's a sane default)
class CarB {
  private engine: Engine = defaultEngine;
  go() { return this.engine.start(); }
}

// Fix 3 — definite-assignment assertion (only when YOU guarantee it:
// e.g. a framework/DI container injects it, or a lifecycle method sets it)
class CarC {
  private engine!: Engine;
  init(e: Engine) { this.engine = e; }
  go() { return this.engine.start(); }
}

console.log(new CarA(defaultEngine).go()); // "vroom"
console.log(new CarB().go());              // "vroom"
const c = new CarC(); c.init(defaultEngine);
console.log(c.go());                       // "vroom" — but c.go() BEFORE init() would crash
```

**Logic explained:**
1. `strictPropertyInitialization` requires every non-optional property be provably set before the constructor finishes — constructor assignment is the cleanest proof.
2. Declaration initializers work when a default exists (`= []`, `= new Map()`, `= defaultEngine`).
3. `!` (definite assignment assertion) tells the compiler "trust me" — right for dependency injection/frameworks (Angular, TypeORM entities); wrong as a silencer, because the crash just moves back to runtime.

### Hard — strictFunctionTypes in the wild

**Problem:** Explain why this breaks under `strictFunctionTypes` — it looks harmless:

```typescript
interface Animal { name: string }
interface Dog extends Animal { breed: string }
type Handler<T> = (x: T) => void;

const handleAnimal: Handler<Animal> = (a) => console.log(a.name);
const handleDog: Handler<Dog> = (d) => console.log(d.breed);

const h: Handler<Animal> = handleDog; // ERROR under strictFunctionTypes
```

**Try this input:** `h({ name: "cat" })` — passing a generic Animal (not a Dog) to a handler typed for Animals.
**Expected output:** `error TS2322` on the assignment — because if it compiled, `h({ name: "cat" })` would call `handleDog` with something that has no `breed`, and `d.breed` would be `undefined` at runtime.
**Solution:**

```typescript
interface Animal { name: string }
interface Dog extends Animal { breed: string }
type Handler<T> = (x: T) => void;

// Safe direction: a handler that accepts ANY Animal can stand in for
// a Dog handler (Dog IS an Animal). This assignment is legal:
const handleAnimal: Handler<Animal> = (a) => console.log(a.name);
const asDogHandler: Handler<Dog> = handleAnimal; // OK — contravariance

// The illegal one was the reverse: Handler<Dog> -> Handler<Animal>.
// Correct fix if you need both: keep the parameter type general.
const handleDog: Handler<Dog> = (d) => console.log(d.breed);
const safeGeneral: Handler<Animal> = (a: Animal) => {
  if ("breed" in a) console.log(a.breed); // narrow inside instead
};

asDogHandler({ name: "rex", breed: "lab" });      // "rex"
safeGeneral({ name: "rex", breed: "lab" });       // "lab"
```

**Logic explained:**
1. `strictFunctionTypes` checks parameter types **contravariantly**: `Handler<Dog>` is assignable to `Handler<Animal>` only if `Animal` is assignable to `Dog` — it's not (an arbitrary Animal has no `breed`).
2. The assignment direction that *is* safe — `Handler<Animal>` used as `Handler<Dog>` — works because every Dog is an Animal, so the handler can handle whatever it receives.
3. Why it matters: without this flag (and in method syntax, which is bivariantly checked for legacy reasons), the "harmless" assignment compiles and then `d.breed` reads `undefined` off a plain Animal — another runtime crash promoted to a compile error.

## The 30-second interview answer

"`strict` is a bundle of stricter checks: `strictNullChecks` makes null and undefined their own types instead of assignable to everything; `noImplicitAny` errors instead of silently inferring `any`; plus `strictFunctionTypes` for contravariant parameter checking, `strictPropertyInitialization`, `noImplicitThis`, `strictBindCallApply`, `useUnknownInCatchVariables`, and `alwaysStrict`. The two I'd name first are strictNullChecks — it eliminates the 'cannot read property of undefined' class — and noImplicitAny, because silent `any` is contagious. On new projects it's non-negotiable; on legacy codebases you migrate by enabling `strict` and opting flags out, then ratcheting them back on."

## Follow-up trap

**"Would you enable strict on an existing large JS/loose-TS codebase? How?"** — They want the pragmatic migration answer, not "always yes." Handle it: yes, but incrementally — `strict: true` with `"strictNullChecks": false` initially (it's the most disruptive flag), or a second tsconfig enforcing strict only on new directories; fix `noImplicitAny` first (usually mechanical annotations); use `--strict` error counts in CI as a ratchet that only goes down. And the counter-question they may add: "why not just leave it off?" — because every non-strict flag is a known hole where runtime crashes hide; the migration cost is paid once, the crash cost is paid forever.
