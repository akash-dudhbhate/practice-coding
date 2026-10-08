# 07 — `never`

> **Interview question:** "What is the `never` type, and where have you actually used it?"
> **What the interviewer is really testing:** Whether you know `never` is the *bottom* type — "no value can ever be this" — and that its killer use is **exhaustiveness checking**: code that fails to compile the moment someone adds a case you forgot to handle.

## Theory — what it is

`never` is the type of **something that can never happen / never produce a value**. Three places it appears:

1. **Functions that never return** — they `throw` or loop forever. `function fail(msg: string): never { throw new Error(msg); }`. The return type is `never`, not `void`, because control never comes back to the caller.
2. **Unreachable narrowing** — after you've checked every variant of a union, the "leftover" type in the `default` branch is `never`: `type Left = string | number` → after `typeof x === "string"` and `typeof x === "number"`, `x` is `never`.
3. **Conditional-type filtering** — `T extends U ? never : T` removes members from a union; `never` in a union evaporates (`string | never` is just `string`). This is how `Exclude`, `NonNullable`, `Omit`-style utilities work internally.

Type-system position: `never` is the **bottom type** — assignable *to* every type (`const s: string = unreachable()` compiles), but *nothing* is assignable to `never` except `never` itself. `any` sits at the top and disables checking; `never` sits at the bottom and proves impossibility.

## Why it was needed

TypeScript needed a way to express "this branch is dead" so the compiler could *verify* exhaustiveness instead of trusting comments. Without `never`, adding a new variant to a union — `{ kind: "triangle" }` joining `circle | square` — compiles silently, and every `switch` that forgot a case falls through to a `default` that returns `undefined` or does nothing. That's a real production bug class: "added a status enum value, one reducer didn't handle it, orders stuck."

With `never` you turn it around: assign the leftover to `never` in `default`, and the *compiler* enumerates every place that needs updating. The day someone adds `"triangle"`, the build breaks at the unhandled switch — the type system does the code review.

It also gives throwing functions an honest signature: `assertIsString(x): asserts x is string` and `fail(): never` let code *after* the call narrow correctly, because TS knows a `never`-returning call can't be followed by normal flow.

## Where it's used in a real project

- **Exhaustive switch over discriminated unions** — reducers, event handlers, state machines, renderers per `kind`. The `assertNever` helper is the standard pattern.
- **`fail`/`invariant`/`unreachable` helpers** — `throw` wrappers typed `never` so `const v = maybe() ?? fail("required")` types `v` as non-nullable.
- **Type-level filtering** — `type NonNull<T> = T extends null | undefined ? never : T`; extracting function-property names with `T[K] extends Function ? K : never`.
- **Impossible states** — typing props so two options can't coexist, or `process.exit` / ` Deno.exit` wrappers that never return.

## Diagram

```
the type lattice:                 exhaustive switch:

        any  <- top, checking off   type Shape = Circle | Square | (new) Triangle
       / | \
  string number Dog                  switch (s.kind) {
       \ | /                          case "circle":  ...
        unknown                       case "square":  ...
          |                    +----> default:
       narrowed unions         |        const _e: never = s
          |                    |        //  ^ compiles: s is never
        NEVER <- bottom        |        //  add Triangle -> s is Triangle here
        nothing is a never     |        //  ERROR: Type 'Triangle' is not
        never is everything    |        //  assignable to 'never'  <== build
                               |        //  breaks AT the missed case
                               +---- the compiler reviews the diff for you
```

## Code — explained

```typescript
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "square"; side: number };

function assertNever(x: never): never {                    // 1
  throw new Error(`Unhandled variant: ${JSON.stringify(x)}`);
}

function area(s: Shape): number {
  switch (s.kind) {
    case "circle": return Math.PI * s.radius ** 2;          // 2
    case "square": return s.side ** 2;
    default:
      return assertNever(s);                               // 3
  }
}

// never for functions that can't return:                    // 4
function fail(msg: string): never {
  throw new Error(msg);
}

function requireName(u: { name?: string }): string {
  return u.name ?? fail("name is required");                // 5
}

// never in conditional types — filtering a union:           // 6
type MyExclude<T, U> = T extends U ? never : T;
type NoNulls = MyExclude<string | null | number, null>;     // string | number

const total = area({ kind: "circle", radius: 2 })           // 7
            + area({ kind: "square", side: 3 });
console.log(total.toFixed(2));                              // 21.57
```

1. `assertNever` takes `x: never` and returns `never` — it can only be *called* with a value that is provably impossible. This is the standard exhaustiveness helper.
2. Each `case` narrows `s` to one variant — `s.radius` only exists inside `"circle"`.
3. In `default`, every handled variant is removed from `Shape`, so `s: never`. If someone later adds `{ kind: "triangle" }` to the union, `s` in `default` is `Triangle` — and `assertNever(s)` becomes `error TS2345: Argument of type 'Triangle' is not assignable to parameter of type 'never'`. The build breaks exactly where handling is missing.
4. `fail` returns `never` — honest: it throws, control never returns. Typing it `void` would be wrong in a subtle way (next line).
5. Because `fail` returns `never`, `u.name ?? fail(...)` types as `string`: `never` in a union disappears. If `fail` were `void`, the expression would be `string | undefined` and the function wouldn't compile — `never` is what makes `?? fail()` a valid idiom.
6. `T extends U ? never : T` distributes over unions: each member matching `U` maps to `never`, and `never` unions evaporate — so `null` is filtered out. This is literally how the built-in `Exclude` and `NonNullable` are written.
7. `toFixed(2)`: `12.566...` + `9` = `21.566...` → `"21.57"`.

## Problems

### Easy — never vs void
**Problem:** What's the correct return type for this, and why not `void`?

```typescript
function panic(reason: string) {
  throw new Error(reason);
}
```

**Try this input:** `pick(maybeName)` where `maybeName` may be `undefined` — does it compile if `panic` is typed `void`? If `never`?
**Expected output:** With `void`, the `??` expression is `string | void` → error assigning to `string`. With `never`, it's `string` — compiles.
**Solution:**

```typescript
function panic(reason: string): never {   // never returns, not "returns nothing"
  throw new Error(reason);
}

function pick(input: string | undefined): string {
  return input ?? panic("no");            // string | never collapses to string
}

console.log(pick("x"));                   // "x"
console.log(pick(undefined));             // throws Error: no
```

**Logic explained:**
1. `void` means "returns a value you shouldn't use" — `panic` returns *no* value ever; `never` is the honest type.
2. In `A ?? B`, the result type is `string | typeof B`. `string | void` keeps `void` in the union — breaking assignment to `string`. `string | never` collapses to `string`, because `never` unions vanish.
3. Practical payoff: `?? panic(...)`, `x || panic(...)`, and `return panic(...)` all type-check correctly only when `panic` is `never`.

### Medium — exhaustive reducer
**Problem:** Write `applyDiscount(state, action)` over `Action = {type:"add",item:number} | {type:"clear"} | {type:"tax",rate:number}` using a switch with an `assertNever` default. Then show what happens when `{type:"undo"}` is added to `Action` without touching the reducer.
**Try this input:** `applyDiscount(10, {type:"tax", rate:0.2})`; then add the `undo` variant.
**Expected output:** `12` for the tax call; after adding `undo`: `error TS2345: Argument of type '{ type: "undo" }' is not assignable to parameter of type 'never'`.
**Solution:**

```typescript
type Action =
  | { type: "add"; item: number }
  | { type: "clear" }
  | { type: "tax"; rate: number };
// | { type: "undo" }        // <- uncomment: assertNever errors

function assertNever(x: never): never {
  throw new Error(`Unhandled action: ${JSON.stringify(x)}`);
}

function applyDiscount(state: number, action: Action): number {
  switch (action.type) {
    case "add":   return state + action.item;
    case "clear": return 0;
    case "tax":   return state + state * action.rate;
    default:      return assertNever(action);   // compiles only when exhausted
  }
}

console.log(applyDiscount(10, { type: "tax", rate: 0.2 }));  // 12
console.log(applyDiscount(10, { type: "add", item: 5 }));    // 15
```

**Logic explained:**
1. `switch (action.type)` on the discriminant — each case narrows `action` to the matching variant, so `action.item`/`action.rate` are safe inside their cases.
2. `default: assertNever(action)` — when all variants are handled, `action` is `never` here; the call compiles. Add `undo` to the union and `action` is `{type:"undo"}` in `default` — compile error at exactly the forgotten case.
3. This is the pattern Redux-style reducers, state machines, and event routers use: the union is the contract, `never` enforces it across every consumer at compile time.

### Hard — build the utilities yourself
**Problem:** Without using built-ins, write `MyNonNullable<T>` and `FunctionKeys<T>` — the keys of `T` whose values are functions. `type K = FunctionKeys<{a:number; b:()=>void; c:string}>` should be `"b"`.
**Try this input:** `type K = FunctionKeys<{a: number; b: () => void; c: string}>`; `type N = MyNonNullable<string | null | undefined>`.
**Expected output:** `K = "b"`, `N = string`. (Check: assign `const k: K = "b"` compiles, `const k: K = "a"` errors.)
**Solution:**

```typescript
// never removes union members:
type MyNonNullable<T> = T extends null | undefined ? never : T;
type N = MyNonNullable<string | null | undefined>;   // string

// never filters keys via a mapped type:
type FunctionKeys<T> = {
  [K in keyof T]: T[K] extends (...args: never[]) => unknown ? K : never
}[keyof T];
type K = FunctionKeys<{ a: number; b: () => void; c: string }>;  // "b"

const good: K = "b";          // OK
// const bad: K = "a";        // ERROR: '"a"' not assignable to '"b"'
const nn: N = "hi";           // OK — null/undefined removed
```

**Logic explained:**
1. `T extends null | undefined ? never : T` — conditional types distribute over union members: `string→string`, `null→never`, `undefined→never`; `string | never | never` collapses to `string`. That collapse is the whole trick — `never` is how you *delete* from a union.
2. `FunctionKeys` maps every key to either itself (`K`) if its value is a function type, or `never`; then `[keyof T]` indexes the object by all keys, yielding the union of values — `number-key` and `c` became `never`, so only `"b"` survives.
3. `(...args: never[]) => unknown` is the most general function type — any function is assignable to it, so the check means "is `T[K]` some kind of function."
4. Same machinery powers `Omit`, `Pick` filters, and `keyof`-based event maps — `never` is the type-level "drop this."

## The 30-second interview answer

"`never` is the bottom type — the type of values that can't exist. Three real uses: functions that never return, like a `fail` that throws — `never` not `void`, so `x ?? fail()` still types as `string`; exhaustiveness — assign the leftover to `never` in a switch's `default` via `assertNever`, so adding a union variant breaks the build at every missed case; and type-level filtering — conditional types map unwanted union members to `never`, which evaporates from unions, which is literally how `Exclude` and `NonNullable` are implemented. The big win is the exhaustive switch: it turns 'forgot to handle the new case' from a runtime bug into a compile error."

## Follow-up trap

**"Why does `string | never` collapse but `string | void` doesn't?"** — `never` is the empty union member: a union with `never` is a union over zero extra possibilities, so it disappears. `void` is a real inhabitant (functions returning nothing), so it stays. That's also why `?? fail()` works only with `never`. Second trap: **"What's wrong with `if (x) {...} else { const n: never = x }`?"** — nothing, *if* the else is truly unreachable; but people slap `assertNever` where `x` can legitimately survive narrowing (e.g., `x` typed `any` upstream, or a union widened by a broad check). `never` in `default` is only as strong as the union's honesty — if your API type is `any`, the exhaustiveness check is theater. Also: `assertNever` must *throw* (return `never`) — a version returning `void` compiles the same check but silently no-ops at runtime if types were bypassed.
