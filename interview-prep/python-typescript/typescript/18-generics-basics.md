# 18 — Generics basics: `function identity<T>(x: T): T` — why not just `any`

> **Interview question:** "Why write `function identity<T>(x: T): T` instead of `function identity(x: any): any`?"
> **What the interviewer is really testing:** Do you understand that generics *preserve and connect* type information — the input type flows to the output — while `any` severs the link and disables checking entirely?

## Theory — what it is

A generic function declares a **type parameter** `T` — a placeholder bound *per call*. `identity(5)` binds `T = number`, so the return is `number`; `identity("hi")` binds `T = string`. One function, infinitely many typed instantiations — `T` is like a function parameter, but for types.

The magic is the **link**: `x: T` and `: T` are the *same* slot, so "whatever goes in comes out" is a compile-time fact. Compare:

```typescript
function identity<T>(x: T): T { return x; }
function identityAny(x: any): any { return x; }

const n = identity(5);        // n: number  — type flows through
const a = identityAny(5);     // a: any     — information destroyed
// n.toUpperCase();           // compile error — good, it's a number!
// a.toUpperCase();           // compiles — crashes at runtime
```

Two more basics:

- **Inference** — you rarely write `identity<number>(5)`; `T` is inferred from the argument. Explicit `<>` is for when inference needs help or has nothing to see (`useState<User>(null)`).
- **Generics are universally quantified** — inside the body, `T` is opaque: you can't call `x.toUpperCase()` because `T` might be `number`. The body must type-check for *every* possible `T`. (Constraining `T` — `T extends string` — is file 19.)

Worth one line on `unknown`: `identity(x: unknown): unknown` also accepts anything, but the *return* stays `unknown` — callers can't use it without narrowing. `T` captures the specific type; `unknown` captures nothing about it.

## Why it was needed

Without generics, reusable code has three bad options:

1. **Duplicate per type** — `numberIdentity`, `stringIdentity`, `userIdentity` — twenty copies that drift apart.
2. **`any`** — compiles everywhere, checks nothing: typos pass, autocomplete dies, refactors break silently.
3. **`unknown`** — safe but useless at the output: every caller must re-narrow.

Generics give the fourth option: write the *shape* of the logic once (`x` in, same `x` out; `T[]` in, `T` out; `Promise<T>`), and let each call site supply the concrete type. It's the difference between a function that *accepts* anything and a function that *remembers* what it accepted.

## Where it's used in a real project

- `Array<T>`, `Promise<T>`, `Map<K, V>`, `Set<T>` — the entire standard library is generic.
- `useState<T>()`, `useRef<T>()` — React hooks preserve your state type.
- `function get<T>(url: string): Promise<T>` — typed fetch wrappers; `axios.get<User>(...)`.
- `Array.prototype.map<U>`, `filter`, `reduce`, `Promise.all` — element types flow through transforms.
- `first<T>(arr: T[]): T | undefined`, `groupBy`, `pluck` — every utility library.
- `Emitter<Events>` where `emit<K extends keyof Events>(k: K, payload: Events[K])` — typed event maps.

## Diagram

```
function identity<T>(x: T): T
                     ▲        ▲
                     └────────┘  same slot — input type flows to output

  identity(5)          identity("hi")        identity({ id: 1 })
  T = number           T = string            T = { id: number }
  → returns number     → returns string      → returns { id: number }
  → n.toFixed() OK     → s.toUpperCase() OK  → u.id OK, u.name errors

  identityAny(5) : any
  → a.toUpperCase() compiles → runtime TypeError
  → any = "I remember nothing about this value"
```

## Code — explained

```typescript
// 1. The canonical generic
function identity<T>(x: T): T {
  return x;                            // (1) T is opaque here — `return x` is provably safe
}

const n = identity(5);                 // (2) T inferred = number
const s = identity("hi");              // (3) T inferred = string
const explicit = identity<number>(5);  // (4) explicit argument — usually unnecessary

console.log(n + 1);                    // 6
console.log(s.toUpperCase());          // HI
// n.toUpperCase();                    // compile error — number has no toUpperCase

// 2. Generics over containers — the pattern everywhere
function first<T>(arr: T[]): T | undefined {
  return arr[0];                       // (5) T[] in, T out — no any
}
console.log(first([1, 2, 3]));         // 1   — T = number
console.log(first(["a", "b"]));        // a   — T = string

// 3. The link survives nesting
function wrap<T>(x: T): { value: T } {
  return { value: x };
}
const w = wrap({ id: 7 });             // T = { id: number }
console.log(w.value.id);               // 7 — inner shape preserved
console.log(explicit);                 // 5
```

1. Inside the body, `T` is a black box — the only thing provably safe is returning `x` itself. That constraint is the *point*: the function can't accidentally assume too much.
2. `T` is inferred from the argument — `5` binds `T = number`, so `n: number` with full checking.
3. Same function, `T = string` — one definition, two precise instantiations.
4. Explicit type arguments exist for cases inference can't cover (empty arrays, `useState<User>(null)`); here it's redundant but legal.
5. `first` shows generics over containers: `arr[0]` keeps the element type — `first([1,2,3])` returns `number | undefined`, never `any`. `wrap` proves the link survives structure: `T` inside an object literal still tracks the input.

## Problems

### Easy — `last<T>`
**Problem:** Write `last` that returns the final element of any array, fully typed.
**Try this input:** `last([10, 20, 30])`, `last(["x", "y"])`, `last([])`
**Expected output:** `30`, `y`, `undefined`.
**Solution:**
```typescript
function last<T>(arr: T[]): T | undefined {
  return arr[arr.length - 1];
}

console.log(last([10, 20, 30]));   // 30
console.log(last(["x", "y"]));     // y
console.log(last([]));             // undefined
```
**Logic explained:**
1. `T[]` in, `T | undefined` out — the element type flows to the caller.
2. Empty array returns `undefined`, and the union in the return type is *honest* — callers must handle it (or use `??`).
3. With `any` plumbing, `last([])` would type as `any` — no signal that `undefined` is possible, and `last(nums).toFixed()` on an empty array compiles then crashes.

### Medium — `map<T, U>`: two independent parameters
**Problem:** Write `map(arr, f)` yourself — array of `T`, callback `T → U`, returns `U[]`. Use it to turn numbers into labels.
**Try this input:** `map([1, 2], (n) => "#" + n)`
**Expected output:** `[ '#1', '#2' ]` — and the result is `string[]`, not `any[]`.
**Solution:**
```typescript
function map<T, U>(arr: T[], f: (x: T) => U): U[] {
  const out: U[] = [];
  for (const x of arr) out.push(f(x));
  return out;
}

const labels = map([1, 2], (n) => "#" + n);   // T = number, U = string — both inferred
console.log(labels);                          // [ '#1', '#2' ]
console.log(labels[0].toUpperCase());         // #1 — string methods available
```
**Logic explained:**
1. `T` and `U` are independent slots: `T` is inferred from the array, `U` from the callback's return type.
2. Inference handles both — no explicit type arguments needed.
3. The payoff: `labels` is `string[]`, so `toUpperCase` type-checks. With `any` you'd get `any[]` and lose everything.
4. This is literally `Array.prototype.map`'s signature — `map<U>(f: (x: T) => U): U[]`.

### Hard — A typed `Stack<T>`
**Problem:** Implement `class Stack<T>` with `push(item: T)`, `pop(): T | undefined`, `peek(): T | undefined`, and a `size` getter — so `new Stack<number>()` rejects strings and `pop()` returns `number | undefined`.
**Try this input:** push `1`, `2`; then `peek`, `pop`, `pop`, `pop`.
**Expected output:** `2`, `2`, `1`, `undefined`.
**Solution:**
```typescript
class Stack<T> {
  private items: T[] = [];

  push(item: T): void {
    this.items.push(item);
  }
  pop(): T | undefined {
    return this.items.pop();
  }
  peek(): T | undefined {
    return this.items[this.items.length - 1];
  }
  get size(): number {
    return this.items.length;
  }
}

const s = new Stack<number>();
s.push(1);
s.push(2);
// s.push("x");          // compile error — T is locked to number
console.log(s.peek());  // 2
console.log(s.pop());   // 2
console.log(s.pop());   // 1
console.log(s.pop());   // undefined
```
**Logic explained:**
1. Generics work on classes too — `Stack<T>` declares `T` once; every method signature shares it.
2. `new Stack<number>()` binds `T` for the whole instance: `push("x")` is a compile error, `pop()` returns `number | undefined`.
3. `items: T[]` internally keeps storage honest — zero `any`, yet the class works for any element type.
4. `new Stack<string>()` gives a parallel string stack from the same code — one implementation, N type-checked uses. This is exactly how `Map<K, V>` and `Promise<T>` work.

## The 30-second interview answer

"`identity<T>(x: T): T` declares a type parameter bound per call — `identity(5)` gives `number`, `identity("hi")` gives `string` — and crucially the *same* `T` links input to output, so the type flows through instead of being discarded. `any` accepts anything but forgets everything: the return is `any`, so `result.toUpperCase()` compiles on a number and crashes at runtime. Generics are how you write reusable logic once without losing checking — the same idea behind `Array<T>`, `Promise<T>`, `useState<T>`, and typed fetch wrappers. Inference usually fills in `T` from the argument; you write `<T>` explicitly only when inference has nothing to work with. And versus `unknown`: `unknown` accepts anything but the return stays `unknown` — `T` remembers the concrete type."

## Follow-up trap

**"Inside `identity`, why can't you call `x.toUpperCase()`?"** — because `T` is *universally* quantified: the body must compile for every possible `T`, including `number`. If you want string methods, constrain it — `function f<T extends string>(x: T): T` — or don't use a generic. Inverse trap: **"if `T` could be anything, why does `return x` compile?"** — because `x: T` is returned where `T` is expected; identity is the one operation valid for all types. Third: **"generic `T` vs union `x: string | number`?"** — a union forces every caller to narrow the *return* (`identity(5)` would be `string | number`, so `n.toFixed()` needs a check), while `T` preserves the exact type each caller passed in.
