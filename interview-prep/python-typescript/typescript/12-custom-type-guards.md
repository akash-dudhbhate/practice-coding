# 12 — Custom type guards: `function isCat(x: Animal): x is Cat`

> **Interview question:** "Write a custom type guard — what does `x is Cat` mean in a return type?"
> **What the interviewer is really testing:** Can you teach the compiler something it can't figure out on its own — and do you know a guard is a *promise* it will trust blindly?

## Theory — what it is

A **custom type guard** is a function that returns a `boolean` at runtime but whose declared return type is a **type predicate**: `x is Cat`. Inside an `if (isCat(pet))` block, TypeScript treats `pet` as `Cat` — even though it could never prove that itself.

```typescript
function isCat(x: Animal): x is Cat {
  return x.kind === "cat";
}
```

The signature means: "When this function returns `true`, you may treat `x` as `Cat`." It works anywhere a boolean check works — `if`, ternaries, `.filter()`, `&&` chains.

Two critical rules:

1. **The predicate type must be assignable to the parameter type.** `x is Cat` only compiles if `Cat` is a subtype of `Animal` (the parameter's type). You can't write `x is Date` for an `Animal` param.
2. **TypeScript trusts you completely.** If the function body lies (returns `true` when it's not a `Cat`), the compiler will happily let you call `.meow()` on a dog. The check must be *real* — a guard is runtime code plus an honest claim.

For validating `unknown` data (e.g., JSON), the parameter is usually `unknown` and the predicate claims the checked shape: `function isUser(x: unknown): x is User`.

## Why it was needed

Built-in narrowing (`typeof`, `instanceof`, `in`) can only check *one thing at a time*. Real code asks questions like "is this object a valid `User`?" — which means checking several properties at once. Without custom guards you'd inline that logic everywhere and TypeScript would lose the narrowing the moment you extract it into a helper:

```typescript
// Inline check narrows, but extracting it breaks narrowing:
function hasKind(x: Animal): boolean { return x.kind === "cat"; }
if (hasKind(pet)) { pet.meow(); } // ERROR — boolean doesn't narrow!
```

Change the return type to `x is Cat` and the extracted function narrows perfectly. Custom guards also compose: `isCat(a) && isKitten(a)`, and they power `.filter(isPresent)` to turn `(string | undefined)[]` into `string[]`.

## Where it's used in a real project

- **Validating API/JSON data:** `function isUser(x: unknown): x is User` checks every required field before trusting the payload.
- **Filtering nulls:** `list.filter(isDefined)` where `isDefined = <T,>(x: T): x is NonNullable<T> => x != null`.
- **Domain logic:** `isAdmin(user)`, `isRetryable(err)`, `isPaidOrder(order)` — readable checks that also narrow.
- **Library internals:** `.filter(Boolean)` famously doesn't narrow; libraries ship `(x): x is T` helpers instead.

## Diagram

```
pet: Animal = Cat | Dog

   if (isCat(pet))                if (!isCat(pet))
        │                              │
   ┌────▼─────┐                   ┌────▼─────┐
   │ pet: Cat │                   │ pet: Dog │   <- else branch narrows too!
   │ .meow()✓ │                   │ .bark()✓ │
   └──────────┘                   └──────────┘

   The 'x is Cat' return type is the bridge:
   runtime boolean ──► compile-time narrowing
```

## Code — explained

```typescript
interface Cat { kind: "cat"; meow(): void }
interface Dog { kind: "dog"; bark(): void }
type Animal = Cat | Dog;

// (1) The predicate return type is the whole trick.
function isCat(x: Animal): x is Cat {
  return x.kind === "cat";   // (2) a REAL runtime check
}

function greet(pet: Animal): string {
  if (isCat(pet)) {
    return pet.meow ? "meow!" : "?"; // (3) pet: Cat here
  }
  pet.bark();                        // (4) pet: Dog in the else
  return "woof!";
}

// (5) Guards also upgrade .filter:
const animals: Animal[] = [
  { kind: "cat", meow: () => console.log("m") },
  { kind: "dog", bark: () => console.log("w") },
];
const cats: Cat[] = animals.filter(isCat); // (6) Cat[] — not Animal[]!
```

1. `x is Cat` is a type predicate — it tells the compiler "trust my boolean; `true` means `x` is a `Cat`."
2. The body must contain a check that's actually true iff `x` is a `Cat` — here, the `kind` discriminant.
3. Inside the `if`, `pet` is narrowed to `Cat`; `.meow` is accessible.
4. The `else` branch narrows to `Dog` — predicates narrow both ways.
5. Passing the guard to `.filter` is a killer feature: `Array<T>.filter` has an overload for type predicates.
6. Result type is `Cat[]` — the guard *changed the type of the filtered array*, something `filter(a => a.kind === "cat")` also does (inline predicates are inferred since TS 5.5) but named guards keep it explicit and reusable.

## Problems

### Easy — Guard for a primitive union member
**Problem:** Write `isString(x: unknown): x is string`, then use it in `shoutAll(items: unknown[])` to uppercase only the strings.
**Try this input:** `shoutAll(["hi", 3, "yo", null])`
**Expected output:** prints `HI` then `YO`.
**Solution:**
```typescript
function isString(x: unknown): x is string {
  return typeof x === "string";
}

function shoutAll(items: unknown[]): void {
  for (const item of items) {
    if (isString(item)) console.log(item.toUpperCase()); // item: string
  }
}

shoutAll(["hi", 3, "yo", null]); // HI / YO
```
**Logic explained:**
1. `x is string` is legal because `string` is assignable to `unknown` (everything is).
2. Inside the `if`, `item` is `string`, so `.toUpperCase()` compiles.
3. Non-strings fall through to the `else` (skipped).

### Medium — Guard + filter
**Problem:** `type Job = { status: "done"; result: number } | { status: "pending" }`. Write `isDone` and use `.filter` to collect all results into `number[]`, then sum them.
**Try this input:** `[{status:"done",result:10},{status:"pending"},{status:"done",result:5}]`
**Expected output:** `15`.
**Solution:**
```typescript
type Job = { status: "done"; result: number } | { status: "pending" };

function isDone(j: Job): j is { status: "done"; result: number } {
  return j.status === "done";
}

function sumResults(jobs: Job[]): number {
  return jobs
    .filter(isDone)                       // {status:"done";result:number}[]
    .reduce((acc, j) => acc + j.result, 0);
}

console.log(sumResults([
  { status: "done", result: 10 },
  { status: "pending" },
  { status: "done", result: 5 },
])); // 15
```
**Logic explained:**
1. `j is {status:"done"...}` narrows the union member — the predicate names the *subtype*.
2. `filter(isDone)` uses the predicate overload, so the result is the done-variant array.
3. `.result` is accessible post-filter; `.reduce` sums it.

### Hard — Validate unknown JSON with a shape guard
**Problem:** Write `isUser(x: unknown): x is User` where `interface User { id: number; name: string; email?: string }`. It must return `false` for `{}`, `null`, `{id:"1",name:"a"}` (wrong type), and `true` for `{id:1,name:"a"}` and `{id:1,name:"a",email:"e@x.com"}`. Use it on `JSON.parse` output.
**Try this input:** `isUser({id: 1, name: "a"})`, `isUser({id: "1", name: "a"})`, `isUser(null)`
**Expected output:** `true`, `false`, `false`.
**Solution:**
```typescript
interface User { id: number; name: string; email?: string }

function isUser(x: unknown): x is User {
  if (typeof x !== "object" || x === null) return false;   // (a)
  const o = x as Record<string, unknown>;                  // (b)
  if (typeof o.id !== "number") return false;
  if (typeof o.name !== "string") return false;
  if ("email" in o && o.email !== undefined && typeof o.email !== "string") {
    return false;                                          // (c) optional field
  }
  return true;
}

function parseUser(json: string): User {
  const data: unknown = JSON.parse(json);
  if (!isUser(data)) throw new Error("bad user payload");
  return data;                                             // data: User
}

console.log(isUser({ id: 1, name: "a" }));                  // true
console.log(isUser({ id: "1", name: "a" }));                // false
console.log(isUser(null));                                  // false
```
**Logic explained:**
1. (a) `typeof null === "object"`, so the `x === null` guard is mandatory before property access.
2. (b) `x` is `object` now; casting to `Record<string, unknown>` lets us index fields while each value stays `unknown` and must be checked.
3. (c) `email` is optional — check it only when present and not `undefined`.
4. `parseUser` turns untrusted text into a `User` — the guard makes the `unknown` → `User` transition *honest* instead of an `as` cast lie.
5. This is the hand-rolled version of what Zod/io-ts do automatically.

## The 30-second interview answer

"A custom type guard is a function returning a type predicate — `x is Cat` — instead of plain `boolean`. It lets me extract a runtime check into a named function while keeping the narrowing: inside `if (isCat(pet))`, `pet` is `Cat`, and in the `else` it's `Dog`. The predicate type has to be a subtype of the parameter type, and TypeScript trusts the body completely, so the check must be truthful. I use them for validating `unknown` JSON, for `.filter` calls that change the element type, and for readable domain checks like `isAdmin`."

## Follow-up trap

**"What happens if your guard lies?"** — TypeScript does NOT verify the body against the predicate. `function isCat(x: Animal): x is Cat { return true; }` compiles fine and will let you `.meow()` a dog at runtime. So the follow-up is really "how do you keep guards honest?" — answer: keep them tiny (one discriminant check or a field-by-field shape check), test them against real payloads, and prefer generated validators (Zod schemas can *infer* the type so the check and the type can never drift apart). Also expect: *"can a guard narrow `this`?"* — yes: `this is Cat` works in class/interface methods.
