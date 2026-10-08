# 14 — `satisfies` vs plain annotation — keeps literal inference

> **Interview question:** "What does `satisfies` do that a plain type annotation doesn't?"
> **What the interviewer is really testing:** Do you understand the widening-vs-checking tradeoff — annotation *changes* the inferred type, `satisfies` only *validates* it?

## Theory — what it is

`satisfies` (added in TypeScript 4.9) is an operator you put on a value: `expr satisfies SomeType`. It checks that the expression is assignable to `SomeType` — a compile error if not — **but leaves the expression's inferred type unchanged**.

Compare the three ways to declare the same object:

```typescript
const config = { port: 3000, mode: "dev" };                    // inferred
const config: Config = { port: 3000, mode: "dev" };            // annotated
const config = { port: 3000, mode: "dev" } satisfies Config;   // satisfied
```

- **Plain inference:** no checking at all — a typo'd shape slips through.
- **Annotation:** checks the value AND *widens* the variable's type to `Config`. `config.mode` becomes `Config["mode"]` (say `"dev" | "prod"`), forgetting the literal `"dev"`. You also lose excess-property knowledge — `config` is now exactly `Config`, nothing more.
- **`satisfies`:** checks the value AND *keeps* the precise inferred type. `config.mode` stays `"dev"`. Typos and missing keys still error.

Think of it as: annotation says "this variable **is** a Config"; `satisfies` says "this value **must fit** Config, but remember what it literally was."

## Why it was needed

The classic pain: you annotate a config map to get checking, and the annotation *destroys* the literal information you needed downstream.

```typescript
type Color = "red" | "green" | "blue";
const palette: Record<Color, string> = { red: "#f00", green: "#0f0", blue: "#00f" };
palette.red.toUpperCase();   // fine
palette.pink;                // ERROR — good
```

But with `Record<Color, string | number[]>` (mixed value types), annotation makes every value `string | number[]`, so `palette.red.toUpperCase()` errors even though `red` is plainly a string. Before `satisfies` your options were ugly: drop the annotation (lose checking), or write `as const` casts, or maintain the type by hand. `satisfies` gives you both: **validate against the contract, keep the literal type.**

## Where it's used in a real project

- **Config objects:** `export default { plugins: [...] } satisfies Config` — checked against the library's `Config` type, but the exact plugin names stay inferred for downstream typing.
- **Exhaustive lookup maps:** `{ red: ..., green: ... } satisfies Record<Color, X>` — missing a key or adding a bogus key is a compile error, while `Object.keys(map)` gives the precise literal keys.
- **Route/endpoint tables:** satisfy `Record<string, Handler>` so a wrong-shaped handler errors, but each route keeps its specific param types.
- **Component props presets:** `const props = {...} satisfies ButtonProps` — validates without losing literal `"primary"` for `variant`.

## Diagram

```
const p = { red: "#f00", green: [0,255,0] }

  ── inferred only ────────────► p.red: "#f00", p.green: number[]
                                 ✗ no checking — typos pass

  ── : Record<Color, string|number[]> ──► p.red: string|number[]
                                 ✓ checked   ✗ literal info lost
                                 p.red.toUpperCase() = ERROR

  ── satisfies Record<Color, string|number[]> ──► p.red: "#f00"
                                 ✓ checked   ✓ literal info kept
                                 p.red.toUpperCase() = OK
                                 p.pink = ERROR (not a key)
                                 missing "blue" = ERROR
```

## Code — explained

```typescript
type Color = "red" | "green" | "blue";

// (1) satisfies: validate the shape, keep the literals
const palette = {
  red: [255, 0, 0],
  green: "#00ff00",
  blue: [0, 0, 255],
} satisfies Record<Color, number[] | string>;

palette.red.map((v) => v * 2);      // (2) red is number[] — works
palette.green.toUpperCase();        // (3) green is "#00ff00" — works
// palette.pink;                    // (4) ERROR — pink isn't a key
// palette.red = "oops";            // (5) "oops" is a string... but red
                                    //     must be number[] — ERROR

// (2b) compare with the annotated version:
const palette2: Record<Color, number[] | string> = {
  red: [255, 0, 0], green: "#00ff00", blue: [0, 0, 255],
};
// palette2.red.map(v => v * 2);    // (6) ERROR — string|number[] has no map
```

1. `satisfies` checks the object against `Record<Color, number[] | string>`: all three keys required, each value must be `number[] | string`.
2. The inferred type of `palette.red` stays `number[]` (its literal inferred type), so `.map` is legal.
3. `palette.green` stays `"#00ff00"` — a `string` — so `.toUpperCase()` is legal.
4. Excess/unknown keys: `pink` isn't in the object, error; and if you'd *written* a `pink` key, `satisfies` would flag it as not in `Record<Color, ...>` — actually it would be an excess property error since the record only allows the three keys.
5. `palette.red` keeps type `number[]`, so assigning a string fails — the *narrow* inferred type still guards you.
6. The annotated `palette2` widened everything to the union — the method call that worked before is now an error. This is the exact problem `satisfies` solves.

## Problems

### Easy — Keep the literal
**Problem:** Given `type Mode = "dev" | "prod"`, declare `settings` with `{ mode: "prod", retries: 3 }` so that `settings.mode` has type `"prod"` (not `Mode`), while still erroring if `mode` were `"staging"`.
**Try this input:** `settings.mode`, and try writing `mode: "staging"`
**Expected output:** `settings.mode: "prod"`; `"staging"` gives `Type '"staging"' is not assignable to type 'Mode'`.
**Solution:**
```typescript
type Mode = "dev" | "prod";
interface Settings { mode: Mode; retries: number }

const settings = {
  mode: "prod",
  retries: 3,
} satisfies Settings;

const m: "prod" = settings.mode;   // compiles — mode stayed "prod"

const bad = { mode: "staging", retries: 3 } satisfies Settings;
// ERROR: Type '"staging"' is not assignable to type 'Mode'
```
**Logic explained:**
1. `satisfies Settings` validates `mode` against `Mode` — `"staging"` fails.
2. But the inferred type of `settings` is `{ mode: "prod"; retries: number }` — the literal `"prod"`, not the widened `Mode`.
3. Assigning to `const m: "prod"` proves it — with a `: Settings` annotation, `settings.mode` would be `Mode` and that assignment would fail.

### Medium — Exhaustive map with literal keys
**Problem:** Build a `statusColor` map covering exactly `"ok" | "warn" | "err"` (a `Status` union), mapping each to a hex string. It must error if a status is missing AND if an extra key sneaks in — while letting you call `.toUpperCase()` on any entry.
**Try this input:** omit `"err"`, or add `pending: "#fff"`
**Expected output:** missing key → `Property 'err' is missing`; extra key → `Object literal may only specify known properties`.
**Solution:**
```typescript
type Status = "ok" | "warn" | "err";

const statusColor = {
  ok: "#22c55e",
  warn: "#eab308",
  err: "#ef4444",
} satisfies Record<Status, string>;

statusColor.warn.toUpperCase();   // "#EAB308" — values stayed string
const key: Status = "ok";
statusColor[key];                 // indexing by union member works

// { ok:"#0", warn:"#0" } satisfies Record<Status,string>
//   → ERROR: Property 'err' is missing
// { ok:"#0", warn:"#0", err:"#0", pending:"#0" } satisfies ...
//   → ERROR: 'pending' does not exist in type 'Record<Status, string>'
```
**Logic explained:**
1. `satisfies Record<Status, string>` enforces *exactly* the keys of `Status`: too few or too many = compile error.
2. Values keep their literal hex-string types, so all `string` methods work.
3. With plain `const m: Record<Status, string>`, you get the same checking — the `satisfies` payoff here is when values have *mixed* types (see Hard) or when you need the literal keys for `keyof typeof statusColor`.

### Hard — Mixed-type record (the classic TS 4.9 example)
**Problem:** Define `palette` where `red` is an RGB array, `green` is a hex string, `blue` is an RGB array — validated as `Record<Colors, string | number[]>` where `Colors = "red"|"green"|"blue"`. Then write `toHexOut` that calls `.map` on arrays and `.toUpperCase` on strings — WITHOUT narrowing, because satisfies kept each entry's type. Show the one-line annotated version that breaks it.
**Try this input:** `palette.red.map(v=>v+1)`, `palette.green.toUpperCase()`
**Expected output:** both compile; the `:`-annotated twin errors with `Property 'map' does not exist on type 'string | number[]'`.
**Solution:**
```typescript
type Colors = "red" | "green" | "blue";

const palette = {
  red: [255, 0, 0],
  green: "#00ff00",
  blue: [0, 0, 255],
} satisfies Record<Colors, string | number[]>;

// No narrowing needed — each entry kept its own type:
const doubled = palette.red.map((v) => v * 2);   // red: number[]
const loudGreen = palette.green.toUpperCase();   // green: "#00ff00"
console.log(doubled, loudGreen);                  // [510,0,0] "#00FF00"

// The breaking comparison:
const p2: Record<Colors, string | number[]> = { ...palette };
// p2.red.map(v => v * 2);      // ERROR: 'map' on 'string | number[]'
// p2.green.toUpperCase();      // ERROR: 'toUpperCase' on 'string | number[]'
```
**Logic explained:**
1. `satisfies` checks every value is `string | number[]` and every key of `Colors` is present — full contract checking.
2. The *inferred* type of `palette` is `{ red: number[]; green: string; blue: number[] }` — per-key precision.
3. Method calls pick the right overload per key with zero narrowing code — this is impossible with a plain annotation.
4. `p2` shows the alternative: correct checking, but every property is the union — you must narrow before any method call. `satisfies` = checked AND precise.

## The 30-second interview answer

"`satisfies` checks that a value matches a type without changing the value's inferred type — it validates instead of widens. A plain `const x: T = ...` annotation does check the value, but then `x` *is* `T`: literal types widen, per-property precision is lost, and mixed-type records force you to narrow before calling methods. With `satisfies`, `{ red: [255,0,0], green: '#0f0' } satisfies Record<Colors, string|number[]>` still knows `red` is `number[]` and `green` is a `string`. I use it for config objects and exhaustive lookup maps — I get the compiler checking completeness while keeping the literal types for downstream code. It shipped in TS 4.9."

## Follow-up trap

**"How is `satisfies` different from `as`?"** — `satisfies` *checks* assignability and errors if it doesn't hold; `as` *asserts* and can lie (`"x" as number` — well, that specific one errors, but `as` happily narrows `unknown` to anything). `satisfies` can never lie — it only rejects. Related: *"does `satisfies` change the runtime?"* — no, it's erased like all types. And *"`satisfies` vs `as const`?"* — they compose: `as const` makes everything readonly literals; `satisfies T` checks against `T`. `{...} as const satisfies Config` freezes AND validates.
