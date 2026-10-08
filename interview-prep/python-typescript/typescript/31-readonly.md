# 31 — `readonly` properties and `ReadonlyArray` — immutability at the type level

> **Interview question:** "What does `readonly` do in TypeScript, and how is `ReadonlyArray<T>` different from `T[]`?"
> **What the interviewer is really testing:** Whether you understand `readonly` is a *compile-time contract* — it blocks mutation through that reference but is erased at runtime, so it neither freezes the object nor makes other aliases safe.

## Theory — what it is

`readonly` can appear in three places, all meaning "you may read but not assign/mutate **through this reference**":

```typescript
interface Config {
  readonly host: string;                    // readonly property
  readonly tags: readonly string[];         // readonly array (syntax sugar)
}

const xs: ReadonlyArray<number> = [1, 2];   // readonly array type
```

Rules that matter:

- **`readonly` property:** `cfg.host = "x"` is a compile error. But `readonly` is *shallow* — `cfg.tags.push("x")` would be legal if `tags` were a plain `string[]`. You need `readonly` on the *array itself* to block `.push`.
- **`readonly T[]` / `ReadonlyArray<T>`:** same thing, two spellings. The array type hides mutating methods — no `push`, `pop`, `sort`, `splice`, no index assignment `xs[0] = 9`. Reading (`xs[0]`, `.map`, `.length`) is fine.
- **It's assignable one way only:** a mutable `number[]` can be passed where `readonly number[]` is expected, but a `readonly number[]` can **not** be assigned to `number[]` — widening immutability away would defeat it.
- **Erased at runtime:** compiled JS has no trace of `readonly`. It's not `Object.freeze`; another reference to the same object can still mutate it, and a cast can bypass it entirely.
- **`Readonly<T>` mapped type** wraps an object: `Readonly<Config>` makes every top-level property readonly (still shallow — nested objects need `Readonly` applied recursively or a `DeepReadonly` helper).

## Why it was needed

JavaScript has no immutable collections or immutable fields — `const` only locks the *binding*, not the contents. Teams were writing defensive copies everywhere, or relying on conventions like `Object.freeze` that return the same mutable type anyway.

`readonly` gives you the *intent* "this function won't mutate your data" as a checkable contract instead of a comment. A signature like `sort(xs: readonly number[])` tells callers "I won't reorder your array" and lets the compiler enforce it — without paying for `Object.freeze` calls or copying at runtime.

## Where it's used in a real project

- **Function parameters that promise not to mutate:** `renderItems(items: readonly Item[])` — callers can pass frozen or shared arrays without fear.
- **Class state that shouldn't be reassigned:** `private readonly id = crypto.randomUUID()` — set once in the constructor, never again.
- **Redux-style state:** `Readonly<State>` prevents accidental `state.count++` outside reducers.
- **Shared constants/config:** `const routes: readonly Route[] = [...]` — nobody can `.push` a route at runtime by accident.
- **`as const` output:** `const modes = ["dev", "prod"] as const` produces `readonly ["dev", "prod"]` — readonly tuple with literal types.

## Diagram

```
const xs: number[] = [1, 2, 3];
      │
      ▼  assign to readonly view (ALLOWED — mutability is a capability you can drop)
const ro: readonly number[] = xs;

ro[0]        ✅ read fine
ro.map(...)  ✅ read fine
ro.push(4)   ❌ compile error — push doesn't exist on readonly arrays
xs.push(4)   ✅ legal! — xs is another alias to the SAME array;
             ro[3] is now 4 at runtime. readonly ≠ frozen.

ro -> number[] assignment   ❌ compile error (can't widen away immutability)
xs -> readonly number[]     ✅ allowed

One object, two views:
  xs (mutable) ──┐
                 ├──► [1, 2, 3]   one array in memory
  ro (readonly) ─┘
  readonly blocks mutation THROUGH ro only — the data isn't frozen
```

## Code — explained

```typescript
interface User {
  readonly id: string;              // (1) can't be reassigned
  name: string;                     // (2) still mutable
  readonly roles: readonly string[];// (3) property AND array are readonly
}

const u: User = { id: "u1", name: "Ana", roles: ["admin"] };

// u.id = "u2";            // (4) Error: Cannot assign to 'id' — readonly property
u.name = "Ana Maria";      // (5) fine — name isn't readonly
// u.roles.push("dev");    // (6) Error: 'push' doesn't exist on readonly string[]

// 7. Function promising not to mutate its argument
function total(nums: readonly number[]): number {
  // nums.push(0);        // Error: no push on readonly arrays
  return nums.reduce((a, b) => a + b, 0);
}

const scores = [10, 20, 30];          // plain number[]
console.log(total(scores));           // 60 — mutable array fits readonly param

// 8. The escape hatch: another alias can still mutate
function sneaky(xs: number[]) { xs.push(99); }
sneaky(scores);
console.log(scores.length);           // 4 — readonly didn't freeze anything

// 9. Readonly<T> — every property readonly, still shallow
type FrozenUser = Readonly<User>;
const f: FrozenUser = u;
// f.name = "x";           // Error: name is now readonly too
```

1. `readonly id` — after the object literal is created, `id` can't be reassigned. Note it *can* be set at creation; `readonly` allows initialization, not later assignment.
2. Properties without `readonly` stay normal — readonly is per-property, not per-object.
3. `readonly string[]` on the property value means the *array itself* can't be mutated through `u.roles` — two different readonys: the property slot and the array's methods.
4. Compile error — the property is locked to its initial value.
5. Regular assignment, no restriction.
6. `ReadonlyArray` simply doesn't declare mutating methods — `push`, `pop`, `sort`, `splice`, `fill`, `copyWithin` are all missing from the type.
7. `total` advertises "read-only access," so callers can safely pass arrays they still own — and arrays they got as `readonly` from elsewhere.
8. The key gotcha: `readonly` is a view, not a vault. `scores` is a mutable alias to the same array, so mutation still happens — `ro.length` would change underneath the readonly reference.
9. `Readonly<T>` applies readonly to all top-level properties — handy for config/state snapshots, but `f.roles` is still only as readonly as its own type says.

## Problems

### Easy — stop the push
**Problem:** `function first(arr: number[])` should promise callers it won't modify their array. Change the signature so `arr.push(0)` inside the body is a compile error, then make it return the first element.
**Try this input:** `first([7, 8, 9])`
**Expected output:** `7` logged; `arr.push(0)` inside the function fails with `Property 'push' does not exist on type 'readonly number[]'`.
**Solution:**
```typescript
function first(arr: readonly number[]): number | undefined {
  // arr.push(0);            // Error: 'push' does not exist on readonly number[]
  return arr[0];
}

console.log(first([7, 8, 9]));   // 7
console.log(first([]));          // undefined
```
**Logic explained:**
1. Changing `number[]` to `readonly number[]` removes all mutating methods from the type inside the function.
2. `number[]` is assignable to `readonly number[]`, so existing callers pass arrays unchanged — the contract only restricts the callee.
3. Return type is `number | undefined` because `arr[0]` on an empty array is `undefined` — a nice bonus of thinking about edge cases (with `noUncheckedIndexedAccess` the compiler forces this).

### Medium — a class with readonly state
**Problem:** Write a `Counter` class: `readonly id: string` set once in the constructor, a private mutable `count`, and a `readonly history: readonly number[]` that callers can read but never mutate — while the class internally pushes to it.
**Try this input:** `c.increment(); c.increment(); console.log(c.history)`
**Expected output:** `[1, 2]` — and `c.history.push(5)` outside the class is a compile error.
**Solution:**
```typescript
class Counter {
  readonly id: string;
  private count = 0;
  private readonly _history: number[] = [];   // private mutable store

  constructor(id: string) {
    this.id = id;                              // readonly: assignable in ctor
  }

  get history(): readonly number[] {
    return this._history;                      // expose read-only view
  }

  increment(): void {
    this.count++;
    this._history.push(this.count);            // mutate via private alias
  }
}

const c = new Counter("c1");
c.increment();
c.increment();
console.log(c.history);        // [1, 2]
// c.id = "c2";                // Error: readonly property
// c.history.push(5);          // Error: no push on readonly array
```
**Logic explained:**
1. `readonly id` can be assigned exactly once — inside the constructor. After that, `c.id = "c2"` is a compile error.
2. `_history` is `private` and mutable so the class can push; the public `history` getter returns it as `readonly number[]`, stripping mutating methods for outsiders.
3. This is the canonical real-world pattern: *mutate internally through one reference, expose a readonly view through another.* Same array, two capabilities.
4. It also shows why readonly isn't `Object.freeze` — the underlying array genuinely changes; callers just can't change it themselves.

### Hard — deep readonly for nested state
**Problem:** `Readonly<T>` is shallow — `state.user.name = "x"` still compiles under `Readonly<State>` because `user`'s properties aren't readonly. Write a `DeepReadonly<T>` that recursively makes objects and arrays readonly, and prove `state.user.name = "x"` fails.
**Try this input:** `const s: DeepReadonly<State>` then attempt `s.user.name = "x"`, `s.tags.push("x")`, and read `s.user.name`.
**Expected output:** `"Ana"` reads fine; both mutations are compile errors.
**Solution:**
```typescript
type DeepReadonly<T> = T extends (infer U)[]
  ? readonly U[]                                 // arrays -> readonly arrays
  : T extends object
    ? { readonly [K in keyof T]: DeepReadonly<T[K]> }
    : T;                                         // primitives pass through

interface State {
  user: { name: string; age: number };
  tags: string[];
}

const s: DeepReadonly<State> = {
  user: { name: "Ana", age: 30 },
  tags: ["a", "b"],
};

console.log(s.user.name);   // Ana — reads still work
// s.user.name = "x";       // Error: 'name' is readonly (deep!)
// s.tags.push("c");        // Error: 'push' doesn't exist on readonly array
```
**Logic explained:**
1. `DeepReadonly` is a recursive conditional type: arrays become `readonly` versions of their (recursively-processed) element type; objects get a mapped type that readonly-wraps every property *and* recurses into the values.
2. `s.user` is now `DeepReadonly<{name, age}>` → every nested property readonly — that's what shallow `Readonly<State>` missed.
3. The primitive arm `T` is essential: without it `string`/`number` would be treated as objects and mangled.
4. Worth saying in an interview: even `DeepReadonly` is still a compile-time view — it doesn't freeze the data and doesn't stop mutation through other aliases or casts.

## The 30-second interview answer

"`readonly` marks a property or array as read-only *through that reference* — `obj.prop = x` or `arr.push(x)` become compile errors. `readonly T[]` and `ReadonlyArray<T>` are the same type; it just doesn't declare mutating methods like `push`/`sort`, while reads like `map` and indexing still work. It's shallow — `readonly` on `user` doesn't make `user.name` readonly — and it's erased at runtime, so it's a contract, not `Object.freeze`: another mutable alias to the same data can still mutate it. Mutable arrays are assignable to `readonly` params but not back. The classic pattern is a class keeping a private mutable array while exposing it via a `readonly` getter — internal mutation allowed, external mutation blocked. For nested objects I'd use `Readonly<T>` for the top level, or a recursive `DeepReadonly` mapped type when I need it all the way down."

## Follow-up trap

**"Does `readonly` make the data immutable at runtime?"** — No. It's erased completely; the emitted JS has no readonly. `const ro: readonly number[] = xs; xs.push(4)` mutates the same array `ro` points at — readonly restricts *that reference*, not the object. If you want runtime immutability you need `Object.freeze` (which is also shallow). Second trap: **"can you assign a `readonly string[]` to `string[]`?"** — No, and that's the point: widening away readonly-ness would let anyone defeat the contract, so the assignability is one-directional (mutable → readonly OK, readonly → mutable error). Third: **"`readonly` vs `as const`?"** — `as const` goes further: it makes the whole literal deeply readonly *and* narrows every value to its literal type (`["dev","prod"]` becomes `readonly ["dev","prod"]`, `"dark"` becomes the literal `"dark"`).
