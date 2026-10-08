# 11 — Type narrowing: `typeof`, `instanceof`, `in`, custom guards

> **Interview question:** "What is type narrowing? Show me `typeof`, `instanceof`, `in`, and a custom type guard."
> **What the interviewer is really testing:** Can you take a union/`unknown` value and safely get to the specific type you need — at runtime AND in the type system?

## Theory — what it is

A **union type** like `string | number` says "this value is one of these." **Narrowing** is TypeScript refining that broad type down to one member inside a block of code, based on a runtime check you wrote. The check runs in real JavaScript; the narrowing is the compiler *following along* with what the check proves.

The built-in narrowing tools:

- **`typeof`** — checks primitive types. `typeof x` returns one of `"string" | "number" | "boolean" | "object" | "function" | "undefined" | "symbol" | "bigint"`. Watch out: `typeof null === "object"` (an ancient JS bug you can't fix), and arrays/functions are `"object"`/`"function"`, not `"array"`.
- **`instanceof`** — checks whether an object was built by a class (walks the prototype chain). Works for `Date`, `Error`, your own classes — not for plain object literals or interfaces.
- **`in`** — checks whether a property name exists on an object: `"radius" in shape`. Works on plain objects and narrows unions of object types.
- **`Array.isArray`** — narrows `T[] | something` (because `typeof [] === "object"` won't help).
- **Equality / truthiness** — `if (x === "a")`, `if (x)` drops `null`/`undefined`/`""`/`0`.
- **Custom type guards** — your own function returning a *type predicate* `x is T` (covered in file 12).
- **Discriminated unions** — switching on a shared literal tag like `kind` (file 13).

## Why it was needed

Without narrowing, union types would be unusable: if `x: string | number`, you can't call `x.toUpperCase()` because numbers don't have it — but the code is perfectly safe *if* you've checked. Narrowing is how the compiler rewards you for doing the runtime check: inside `if (typeof x === "string")`, it knows `x` is `string` and unlocks string methods. It's the bridge between TypeScript's static world and JavaScript's dynamic reality — you must prove something at runtime before the compiler will believe it.

## Where it's used in a real project

- **API/route handlers:** `req.body.id` might be `string | string[] | undefined` — narrow before use.
- **Error handling:** `catch (e)` gives `unknown` — `e instanceof Error` unlocks `.message`.
- **Parsing external data:** `JSON.parse` gives `any`/`unknown` — narrow field by field.
- **Rendering logic:** `props.value: string | number | null` — narrow to decide what to render.

## Diagram

```
let x: string | number | Date
        │
        ├─ typeof x === "string" ──► x: string     (primitives)
        ├─ typeof x === "number" ──► x: number     (primitives)
        ├─ x instanceof Date     ──► x: Date       (class instances)
        ├─ "prop" in x           ──► x: HasProp    (object shapes)
        ├─ Array.isArray(x)      ──► x: any[]      (arrays)
        ├─ x.kind === "circle"   ──► x: Circle     (discriminated union)
        └─ isCat(x) /*x is Cat*/ ──► x: Cat        (custom guard)
```

## Code — explained

```typescript
function describe(x: string | number | Date | string[] | null): string {
  if (x === null) return "nothing";                    // (1)
  if (typeof x === "string") return x.toUpperCase();   // (2)
  if (typeof x === "number") return x.toFixed(2);      // (3)
  if (x instanceof Date) return x.toISOString();       // (4)
  if (Array.isArray(x)) return x.join(", ");           // (5)
  return x;                                            // (6)
}

interface Fish { swim(): void }
interface Bird { fly(): void }

function move(pet: Fish | Bird): void {
  if ("swim" in pet) pet.swim();                       // (7)
  else pet.fly();                                      // (8)
}
```

1. `=== null` removes `null` — inside the return, `x` is `null`; after it, `x` can't be `null` anymore.
2. `typeof` narrows to `string`, so `.toUpperCase()` is legal.
3. After the two returns, `x` is `number | Date | string[]`; `typeof` picks out `number`.
4. `instanceof` works because `Date` is a class — narrows to `Date`.
5. `Array.isArray` narrows `string[]`; `typeof` alone couldn't (arrays are `"object"`).
6. TS can prove `x` is `never` here — every union member was handled. Returning it still compiles because `never` is assignable to everything.
7. `"swim" in pet` narrows to `Fish` — the `in` operator checks the property exists.
8. `else` branch: TS knows it's `Bird`, so `.fly()` is safe.

## Problems

### Easy — Narrow `string | number`
**Problem:** Write `format(value: string | number): string` that returns strings wrapped in quotes and numbers rounded to 2 decimals.
**Try this input:** `format("hi")`, `format(3.14159)`
**Expected output:** `"hi"` (with quotes: `"hi"`) and `3.14`.
**Solution:**
```typescript
function format(value: string | number): string {
  if (typeof value === "string") {
    return `"${value}"`;   // value: string here
  }
  return value.toFixed(2); // value: number here
}

console.log(format("hi"));     // "hi"
console.log(format(3.14159));  // 3.14
```
**Logic explained:**
1. `typeof value === "string"` narrows the union to `string` inside the `if`.
2. In the implicit `else`, TS knows it must be `number`, so `.toFixed` is allowed.
3. Both branches return `string`, matching the signature.

### Medium — Narrow with `in` and `instanceof`
**Problem:** Given `type Input = { kind: "text"; text: string } | { kind: "file"; file: File }`, write `sizeOf(input)` returning `text.length` for text or `file.size` for files. Then write `printError(e: unknown)` that prints `e.message` only if `e` is an `Error`, else `"unknown error"`.
**Try this input:** `sizeOf({kind:"text",text:"hello"})`, `printError(new Error("boom"))`, `printError(42)`
**Expected output:** `5`, `boom`, `unknown error`.
**Solution:**
```typescript
type Input =
  | { kind: "text"; text: string }
  | { kind: "file"; file: File };

function sizeOf(input: Input): number {
  if ("text" in input) return input.text.length;  // narrowed to text variant
  return input.file.size;                          // narrowed to file variant
}

function printError(e: unknown): void {
  if (e instanceof Error) console.log(e.message);  // e: Error here
  else console.log("unknown error");
}

console.log(sizeOf({ kind: "text", text: "hello" })); // 5
printError(new Error("boom"));                        // boom
printError(42);                                       // unknown error
```
**Logic explained:**
1. `"text" in input` is true only for the first variant — TS narrows to it.
2. The `else` must be the file variant, so `.file.size` compiles.
3. `unknown` accepts anything, so `e` must be narrowed before touching `.message`.
4. `instanceof Error` is the idiomatic check in `catch` blocks (`catch (e: unknown)` under strict mode).

### Hard — Narrow a messy real-world value
**Problem:** Write `totalLength(x: string | string[] | null | undefined): number` — `null`/`undefined` → 0, string → its length, array → sum of element lengths. Do it with truthiness + `Array.isArray`. Then explain why `typeof x === "object"` would NOT have worked for the array check.
**Try this input:** `totalLength(null)`, `totalLength("abc")`, `totalLength(["a","bc"])` 
**Expected output:** `0`, `3`, `3`.
**Solution:**
```typescript
function totalLength(x: string | string[] | null | undefined): number {
  if (!x) return 0;                    // removes null, undefined, AND ""
  if (Array.isArray(x)) {
    return x.reduce((sum, s) => sum + s.length, 0); // x: string[]
  }
  return x.length;                     // x: string
}

console.log(totalLength(null));        // 0
console.log(totalLength("abc"));       // 3
console.log(totalLength(["a", "bc"])); // 3
```
**Logic explained:**
1. `!x` is true for `null`, `undefined`, and `""` — all return 0. (If empty string should count differently, check `x == null` first — `== null` matches both `null` and `undefined` only.)
2. `Array.isArray` is the only reliable array check: `typeof [] === "object"` can't distinguish `[]` from `{}` or `null`.
3. After both guards, `x` is a non-empty `string`, so `.length` is safe.
4. Note the trap: `typeof null === "object"`, so `typeof x === "object"` would be true for BOTH `null` and arrays — always check `null` first.

## The 30-second interview answer

"Narrowing is TypeScript refining a union type inside a block based on a runtime check. `typeof` handles primitives — with the famous caveat that `typeof null` is `"object"`. `instanceof` checks class instances via the prototype chain. The `in` operator narrows object unions by property presence, `Array.isArray` handles arrays, and truthiness/equality drops `null` and `undefined`. For anything more complex — like validating an object's whole shape — I write a custom type guard returning `x is T`. The key idea: the check is real runtime code; the compiler just tracks what it proves."

## Follow-up trap

**"Why can't you use `instanceof` on an interface?"** Because interfaces are erased at compile time — there's no constructor/prototype at runtime to check against. That's exactly why the `in` operator and discriminated-union `kind` tags exist: they check *shape*, which is what survives to runtime. Related trap: *"what's `typeof null`?"* — `"object"`. And *"how do you narrow `unknown`?"* — you must; `unknown` forces a check before any use, unlike `any`.
