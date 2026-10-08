# 13 — Discriminated unions: `{kind:"circle",r} | {kind:"rect",w,h}` + exhaustive switch

> **Interview question:** "What is a discriminated union? Model a `Shape` and write an `area` function that handles every case."
> **What the interviewer is really testing:** Can you model real "one of several shapes" data AND prove to the compiler you've handled every case — so adding a new case later becomes a compile error, not a runtime bug?

## Theory — what it is

A **discriminated union** (a.k.a. *tagged union* or *algebraic data type*) is a union of object types that all share one common property — the **discriminant** (or *tag*) — whose type is a different literal in each member:

```typescript
type Shape =
  | { kind: "circle"; radius: number }
  | { kind: "rect"; width: number; height: number }
  | { kind: "triangle"; base: number; height: number };
```

Here `kind` is the discriminant. Checking `shape.kind === "circle"` narrows `shape` to exactly the circle member — so `shape.radius` compiles, while `shape.width` would be an error. A `switch (shape.kind)` narrows per `case`.

The killer feature is **exhaustiveness checking**: after handling every `kind`, the remaining type is `never`. If you later add `{ kind: "hexagon" }` to the union, every switch that didn't handle it fails to compile — the compiler becomes your TODO list.

The standard trick for the "impossible" default case:

```typescript
function assertNever(x: never): never {
  throw new Error(`Unhandled case: ${JSON.stringify(x)}`);
}
```

Passing a value to a `never` parameter is an error *unless* the value is truly impossible — which is exactly the check you want.

## Why it was needed

Real data is constantly "one of these shapes": API responses (`success | error`), UI state (`loading | ready | failed`), events (`click | scroll | keypress`), AST nodes. Without a discriminant you get the classic problems:

1. **Optional-everything soup:** `{ kind: string; radius?: number; width?: number; ... }` — every field optional, nothing checked, `shape.radius * shape.width` compiles while both are `undefined`. The type says nothing true.
2. **Silent gaps:** adding a new `kind` breaks no code — every consumer keeps silently doing the wrong thing.
3. **Narrowing that doesn't work:** `typeof`/`instanceof` can't distinguish two plain object literals. The shared literal tag gives TypeScript a cheap, runtime-checkable handle.

The discriminated union makes illegal states unrepresentable (`{kind:"circle"}` MUST have `radius`, CANNOT have `width`) and makes the compiler enforce total handling.

## Where it's used in a real project

- **API responses:** `type Result = { status: "ok"; data: T } | { status: "err"; message: string }` — forces you to check status before touching `data`.
- **Redux/React reducers:** `type Action = { type: "inc" } | { type: "set"; value: number }` — the `type` field is the discriminant; this is *the* canonical Redux pattern.
- **State machines / UI:** `type FetchState = {s:"idle"} | {s:"loading"} | {s:"ok";data:T} | {s:"err";e:Error}` — impossible combos (loading + data) can't exist.
- **WebSocket/event streams:** one socket, many message shapes, switched on `type`.

## Diagram

```
            type Shape = ─────────┬──────────┬──────────
                    ┌─────────────▼──┐  ┌────▼────────┐  ┌──────────────▼─┐
                    │ kind:"circle"  │  │ kind:"rect" │  │ kind:"triangle"│
                    │ radius: number │  │ w, h        │  │ base, height   │
                    └───────┬────────┘  └──────┬──────┘  └───────┬────────┘
                            │                  │                 │
        switch (shape.kind) ▼                  ▼                 ▼
                      case "circle"      case "rect"      case "triangle"
                      shape: Circle      shape: Rect      shape: Triangle
                            │                  │                 │
                      default: shape: never  ◄── unreachable if all handled
                      assertNever(shape) ──► compile ERROR when a new
                                           kind is added & unhandled
```

## Code — explained

```typescript
type Shape =
  | { kind: "circle"; radius: number }                          // (1)
  | { kind: "rect"; width: number; height: number }
  | { kind: "triangle"; base: number; height: number };

function assertNever(x: never): never {                         // (2)
  throw new Error(`Unhandled: ${JSON.stringify(x)}`);
}

function area(shape: Shape): number {
  switch (shape.kind) {                                         // (3)
    case "circle":
      return Math.PI * shape.radius ** 2;                       // (4)
    case "rect":
      return shape.width * shape.height;                        // (5)
    case "triangle":
      return (shape.base * shape.height) / 2;
    default:
      return assertNever(shape);                                // (6)
  }
}

console.log(area({ kind: "circle", radius: 2 }));               // (7)
```

1. Each member is a full object type: the tag `kind` plus only the fields that shape needs. `{kind:"circle"}` *cannot* have `width` — illegal states are unrepresentable.
2. `assertNever` accepts only `never`. Calling it with anything else is a compile error.
3. `switch` on the discriminant — TypeScript narrows `shape` inside each `case`.
4. Here `shape` is `{kind:"circle"; radius:number}` — `radius` is legal, `width` would error.
5. `height` is `number` in both rect and triangle, but each branch still sees only its own member.
6. If all kinds are handled, `shape` is `never` here — call compiles. Add `{kind:"hexagon"}` to `Shape` and this line instantly errors: `Argument of type '{kind:"hexagon"...}' is not assignable to parameter of type 'never'`. That's exhaustiveness for free.
7. `12.566370614359172`.

## Problems

### Easy — Basic discriminated switch
**Problem:** Define `Animal = {type:"dog"; barkVolume:number} | {type:"cat"; lives:number}` and write `describe(a)` returning `"WOOF xN"` or `"N lives left"`.
**Try this input:** `describe({type:"dog",barkVolume:3})`, `describe({type:"cat",lives:9})`
**Expected output:** `WOOF x3`, `9 lives left`.
**Solution:**
```typescript
type Animal =
  | { type: "dog"; barkVolume: number }
  | { type: "cat"; lives: number };

function describe(a: Animal): string {
  switch (a.type) {
    case "dog":  return `WOOF x${a.barkVolume}`;
    case "cat":  return `${a.lives} lives left`;
  }
}

console.log(describe({ type: "dog", barkVolume: 3 })); // WOOF x3
console.log(describe({ type: "cat", lives: 9 }));      // 9 lives left
```
**Logic explained:**
1. `type` is the discriminant — a different string literal per member.
2. `switch (a.type)` narrows: in `case "dog"`, `a` is the dog member, so `barkVolume` exists.
3. No `default` needed — every case returns, and the union has exactly two members; TS knows the function can't fall through.

### Medium — Exhaustive handling of an API result
**Problem:** Model `ApiResult = {status:"ok"; data:string} | {status:"err"; code:number} | {status:"loading"}` and write `render(r)` covering all three, with `assertNever` in `default`.
**Try this input:** all three variants
**Expected output:** `Data: hello`, `Error 500`, `Spinner...`.
**Solution:**
```typescript
type ApiResult =
  | { status: "ok"; data: string }
  | { status: "err"; code: number }
  | { status: "loading" };

function assertNever(x: never): never {
  throw new Error(`Unhandled: ${JSON.stringify(x)}`);
}

function render(r: ApiResult): string {
  switch (r.status) {
    case "ok":      return `Data: ${r.data}`;
    case "err":     return `Error ${r.code}`;
    case "loading": return "Spinner...";
    default:        return assertNever(r);
  }
}

console.log(render({ status: "ok", data: "hello" })); // Data: hello
console.log(render({ status: "err", code: 500 }));    // Error 500
console.log(render({ status: "loading" }));           // Spinner...
```
**Logic explained:**
1. `status` discriminates three members; `loading` carries no extra fields at all.
2. Each `case` narrows `r`, so `.data` only appears where it exists — you *can't* accidentally read `r.data` when status is `"err"`.
3. `default` is provably unreachable, so `r: never` and `assertNever` compiles.
4. Add a `{status:"cancelled"}` member tomorrow and `render` stops compiling until you handle it — the bug becomes visible at build time.

### Hard — Refactor-proof event handler
**Problem:** You're handling `AppEvent = {name:"click";x:number;y:number} | {name:"keypress";key:string} | {name:"scroll";deltaY:number}`. Write `handle(e)` that logs each. Then, without looking, explain what happens in the file when a PM asks to add `{name:"resize";w:number;h:number}` — and write the smallest possible `Shape`-style proof (a compile-failing line) showing it.
**Try this input:** add the resize member to `AppEvent` but don't touch `handle`
**Expected output:** `tsc` error at the `assertNever(e)` line: `Argument of type '{ name: "resize"; w: number; h: number }' is not assignable to parameter of type 'never'`.
**Solution:**
```typescript
type AppEvent =
  | { name: "click"; x: number; y: number }
  | { name: "keypress"; key: string }
  | { name: "scroll"; deltaY: number }
  // | { name: "resize"; w: number; h: number }   // <-- uncomment: handle() breaks to compile-error
  ;

function assertNever(x: never): never {
  throw new Error(`Unhandled: ${JSON.stringify(x)}`);
}

function handle(e: AppEvent): void {
  switch (e.name) {
    case "click":    console.log(`clicked ${e.x},${e.y}`); break;
    case "keypress": console.log(`key ${e.key}`);          break;
    case "scroll":   console.log(`scrolled ${e.deltaY}`);  break;
    default:         assertNever(e); // compile error once "resize" exists
  }
}

handle({ name: "click", x: 10, y: 20 });      // clicked 10,20
handle({ name: "keypress", key: "Enter" });   // key Enter
handle({ name: "scroll", deltaY: -5 });       // scrolled -5
```
**Logic explained:**
1. `assertNever(e)` in `default` is the tripwire: reachable only when a member is unhandled.
2. Adding `"resize"` to the union makes `e` possibly `{name:"resize"...}` at `default` — not `never` — so `tsc` fails with the assignability error shown.
3. This turns "did I update every switch in the codebase?" from a grep-and-pray exercise into a compiler-enforced checklist.
4. Bonus: this is exactly how Redux reducers stay correct when new action types are added.

## The 30-second interview answer

"A discriminated union is a union of object types that share one literal-typed tag property — like `kind` — with a different literal per member. Checking the tag with `if` or `switch` narrows to that member, so only its fields are accessible. The big win is exhaustiveness: I put `assertNever` in the `default`, which only accepts `never`, so if anyone adds a variant later, every switch that doesn't handle it fails to compile. It's how I model API results, Redux actions, and UI state — it makes illegal states unrepresentable and missing cases compile-time errors instead of production bugs."

## Follow-up trap

**"Why not just use optional fields or subclasses?"** Optional fields (`radius?: number; width?: number`) let `{kind:"circle"}` exist with NO radius — the type permits states that are meaningless, and nothing forces you to check `kind` first. Subclasses + `instanceof` work but tie you to classes, don't serialize to plain JSON cleanly, and can't express "exactly these three, closed set" — anyone can subclass. Also expect: *"does the tag have to be a string?"* — no: numbers, booleans, even `null`/`undefined` literals work as discriminants. And *"what if a member doesn't need extra fields?"* — fine: `{status:"loading"}` with just the tag is perfectly valid.
