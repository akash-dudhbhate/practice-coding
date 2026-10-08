# 08 — `void` vs `undefined` vs `null`

> **Interview question:** "When should a value be `null` vs `undefined`, and where does `void` fit in?"
> **What the interviewer is really testing:** Whether you know the convention — `undefined` means "the language didn't put anything there," `null` means "someone deliberately emptied it," `void` means "the return value doesn't matter" — and the famous `() => void` assignability quirk.

## Theory — what it is

Three different "nothing" that answer three different questions:

- **`undefined`** — *absence produced by the language*. You get it for free: declared-but-unassigned variables, missing object properties, missing function arguments, functions that `return` nothing, `arr[99]`, `map.get(missing)`. You rarely *write* `undefined` deliberately — it's what shows up when nothing was provided.
- **`null`** — *absence chosen by a programmer*. Someone explicitly wrote `null` to mean "this field is empty on purpose": `middleName: null`, a cleared selection, a JSON API field set to `null`. It's a value you assign, not a default the language gives you.
- **`void`** — not really a *value* type; it's a **return-type annotation** meaning "this function's return value should be ignored." `function log(msg): void` may internally return `undefined`, but callers promise not to use whatever comes back.

With `strictNullChecks` on, `undefined` and `null` are distinct types and neither is assignable to `string`/`number`/etc. without a union — that's the flag that makes this distinction enforceable.

## Why it was needed

JavaScript itself created the split: `undefined` is baked into the runtime (every "missing" slot holds it), while `null` only exists because a program put it there. The practical consequences are why you must distinguish them:

- `null == undefined` is `true` (loose equality groups them); `null === undefined` is `false`. `??` and `?.` treat both as "nullish."
- `typeof null === "object"` — a 1995 bug JS can't fix without breaking the web. `typeof undefined === "undefined"`.
- **JSON has `null` but no `undefined`**: `JSON.stringify({a: undefined, b: null})` produces `'{"b":null}'` — the `undefined` key silently *vanishes*. API payloads therefore use `null`; `undefined` means "not present."
- `void` exists because "returns nothing" needed a type that *also* describes callbacks whose return is ignored — leading to the quirk that `() => 42` is assignable to `() => void` but **not** to `() => undefined`.

## Where it's used in a real project

- **API/domain models:** `null` = "user cleared this field"; absent/`undefined` = "not provided." PATCH semantics live on this difference: `{email: null}` clears the email, a missing `email` key leaves it alone.
- **Optional properties & params:** `name?: string` reads as `string | undefined` — the language produces `undefined` for absent keys.
- **Callbacks:** `onDone: () => void` — the standard annotation; it deliberately accepts handlers that happen to return values (`() => fetchDone()`), because the caller ignores them.
- **Lookups:** `Map.get` returns `V | undefined`; with `noUncheckedIndexedAccess`, `arr[i]` is `T | undefined`.
- **React props:** optional props are `| undefined`; `null` is often used for "explicitly render nothing" slots.

## Diagram

```
"where did the nothing come from?"

   language gave it            you chose it            return-type slot
   (missing/absent)            (deliberate empty)      (ignore the result)
        |                          |                        |
        v                          v                        v
    undefined                    null                      void
   var x;                     middleName: null        f(): void
   obj.missing                selected = null          |
   f(noArg)                   JSON: {"email":null}     accepts () => 42
   arr[99]                                               but NOT as
   return;                          |                  () => undefined
        |                           |                        |
        +--------- both are "nullish" for ?? / ?. / == null   |
                  but === tells them apart:                   |
                  null === undefined  -> false                |
        JSON.stringify({a: undefined, b: null}) -> '{"b":null}'
```

## Code — explained

```typescript
// --- undefined: the language produces it ---                  // 1
let notAssigned;                          // undefined
function noReturn(): void {}              // returns undefined implicitly
const bag: { a?: number } = {};
console.log(bag.a);                       // undefined — key never existed

// --- null: a programmer chose it ---                          // 2
interface Profile { middleName: string | null }
const p: Profile = { middleName: null };  // deliberate: "has none"

// --- void: the return-ignoring contract ---                   // 3
type Callback = () => void;
const cb: Callback = () => 42;            // OK — return value discarded
// const bad: () => undefined = () => 42; // ERROR: number not assignable to undefined

// --- telling them apart ---                                   // 4
console.log(null == undefined);           // true  (loose: both "nullish")
console.log(null === undefined);          // false (strict: different types)
console.log(typeof null, typeof undefined);        // "object" "undefined"
console.log(JSON.stringify({ a: undefined, b: null }));        // '{"b":null}'

// --- void can't smuggle a value out ---                       // 5
function ignored(): void {
  // return 42;                          // ERROR: void can't return a value
  return;                                 // bare return is fine
}
ignored();
```

1. `undefined` appears without you writing it: uninitialized `let`, absent optional key, missing arg. Convention: let the language produce it; annotate optionality with `?` rather than writing `= undefined` everywhere.
2. `null` is a decision: `middleName: string | null` says the API *will* send this field, and `null` is meaningful data ("user has no middle name"), different from the field being absent.
3. The signature `() => void` promises "callers ignore the return" — so a function returning `42` is a perfectly good `Callback`. Reversing it fails: `() => undefined` demands the callee literally return `undefined`, so `() => 42` errors. This is why event handlers, `forEach` callbacks, and `setTimeout` are all typed `=> void`.
4. `== null` is the one sanctioned loose-equal: `x == null` catches both `null` and `undefined` in one check (equivalent to `x === null || x === undefined`). `typeof null === "object"` is the legacy bug — never test for null with `typeof`.
5. `void` functions may `return;` or fall off the end, but `return 42` errors — the annotation means the value is meaningless, not that any value is allowed out.

## Problems

### Easy — predict the output
**Problem:** Without running it, what does this print — and why?

```typescript
const user = { name: "Ada", nickname: undefined, age: null };
console.log(JSON.stringify(user));
console.log("nickname" in user, user.age == null, user.missing === undefined);
```

**Try this input:** the object above.
**Expected output:** `'{"name":"Ada","age":null}'` · `true true true`
**Solution:**

```typescript
// '{"name":"Ada","age":null}' — undefined-valued keys are DROPPED by JSON
// true  — the key exists even though its value is undefined
// true  — age is null, and null == null
// true  — missing property reads as undefined
```

**Logic explained:**
1. `JSON.stringify` omits `undefined` values entirely — `nickname` vanishes; `null` survives as `null`. That's the JSON boundary rule: APIs can't send `undefined`, so `null` is the wire format's "empty."
2. `"nickname" in user` is `true` — key presence and value are separate questions; the key exists, its value is `undefined`.
3. `user.age == null` — the idiom that checks both nothings at once; `user.missing === undefined` — reading an absent key yields `undefined` (not an error), which is why `?.` exists for deeper paths.

### Medium — the `() => void` trap
**Problem:** Explain why line A compiles but line B errors, then fix `saveDraft` so `handle` accepts it without changing `handle`'s type.

```typescript
const handle: () => void = () => 5;              // A — compiles
const handle2: () => undefined = () => 5;        // B — ERROR
const saveDraft = (): number => persist();       // returns a row id
```

**Try this input:** assign `saveDraft` to a `() => void` slot vs a `() => undefined` slot.
**Expected output:** `() => void` accepts `saveDraft`; `() => undefined` rejects it. Fix: `() => { saveDraft(); }` or change the slot type.
**Solution:**

```typescript
declare function persist(): number;
const saveDraft = (): number => persist();

const handle: () => void = () => 5;                    // A: OK — caller ignores returns
// const handle2: () => undefined = () => 5;           // B: ERROR — must return undefined

const ok: () => void = saveDraft;                      // fine — id discarded by callers
const wrapped: () => undefined = () => { saveDraft(); return undefined; };
// or: const wrapped = () => undefined as undefined;
console.log(typeof ok, typeof wrapped);                // "function" "function"
```

**Logic explained:**
1. `() => void` means "the return value will not be read" — so a callee returning `number` is *more* than compatible: extra information is safely discarded. TS models this with special void-return assignability.
2. `() => undefined` is a *value* contract: the function must return `undefined` itself — `() => 5` violates it. `void` ≠ `undefined` at the type level even though a `void` function returns `undefined` at runtime.
3. The real-world bite: `array.forEach(async x => await save(x))` — the async fn returns `Promise<void>`, assignable to `forEach`'s `void` callback, so `forEach` fires them without awaiting. Same "return ignored" machinery, surprising consequence.
4. When you must satisfy `() => undefined` (rare — e.g., a React `useEffect`-style slot), wrap: `() => { saveDraft(); }` — braces mean no implicit return value.

### Hard — PATCH semantics: absent vs null
**Problem:** Design an update type where a *missing* key means "don't touch" and `null` means "clear the field," then write `applyPatch`. `applyPatch({name:"A",email:"a@x"},{email:null})` must produce `{name:"A",email:null}`; `applyPatch(...,{})` must leave everything unchanged.
**Try this input:** `{name:"Ada",email:"a@x",phone:"1"}` patched with `{email:null}`, then `{}`, then `{name:"Grace"}`.
**Expected output:** `{name:"Ada",email:null,phone:"1"}` → unchanged → `{name:"Grace",email:null,phone:"1"}`.
**Solution:**

```typescript
interface User { name: string; email: string | null; phone: string }
type UserPatch = { name?: string; email?: string | null; phone?: string };
// each key optional (absent = skip); email's VALUE may be null (clear it)

function applyPatch(u: User, patch: UserPatch): User {
  const out = { ...u };
  for (const k of Object.keys(patch) as (keyof UserPatch)[]) {
    const v = patch[k];
    if (v !== undefined) {              // present key, non-undefined -> apply (null included)
      (out as Record<string, unknown>)[k] = v;
    }
  }
  return out;
}

const u: User = { name: "Ada", email: "a@x", phone: "1" };
console.log(applyPatch(u, { email: null }));
// { name: 'Ada', email: null, phone: '1' }   — cleared
console.log(applyPatch(u, {}));
// { name: 'Ada', email: 'a@x', phone: '1' }  — untouched
console.log(applyPatch(u, { name: "Grace" }));
// { name: 'Grace', email: 'a@x', phone: '1' }
```

**Logic explained:**
1. `email?: string | null` encodes three states in one field: absent (`undefined`, skip), `null` (clear), `string` (set). This is exactly how real PATCH APIs distinguish "not sent" from "emptied."
2. `v !== undefined` — not a truthiness check (`null` is falsy! `if (v)` would wrongly skip clears) and not `== null` (which groups null *with* undefined — the opposite of what we want).
3. `Object.keys` only lists keys that *exist* — an absent key never reaches the assignment; a key explicitly set to `undefined` is skipped by the `!== undefined` guard, matching "don't touch" semantics.
4. Design note for the interview: this is why `null` isn't redundant with `undefined` — `null` carries meaning through JSON; `undefined` can't survive `JSON.stringify` at all.

## The 30-second interview answer

"`undefined` is the language's 'nothing' — missing properties, missing args, functions that don't return. `null` is the programmer's 'nothing' — a deliberate empty value, and the only one JSON can carry. Convention: `null` from APIs means 'cleared,' `undefined` means 'not provided' — that's literally how PATCH semantics work. `void` is different in kind: it's a return-type annotation meaning 'ignore what this returns,' which is why `() => 42` is assignable to `() => void` but not to `() => undefined`. Practically: `x == null` checks both at once, `===` tells them apart, and `typeof null === 'object'` is a historic bug — never `typeof`-check for null."

## Follow-up trap

**"So are `void` and `undefined` interchangeable in return position?"** — No, and that's the trap. `function f(): void` returns `undefined` *at runtime*, but the *type contract* differs: `() => void` accepts any function because the caller discards the result; `() => undefined` demands the callee actually return `undefined`. Write `() => void` for callbacks; `| undefined` for *values* that may be absent. Second trap: **"why did `{nickname: undefined}` disappear after `res.json()`?"** — because JSON has no `undefined`; the key was dropped in transit, so `body.nickname === undefined` now means "absent" not "was set to undefined" — you cannot distinguish them on the wire. If the distinction matters, the API must send `null`. And a sneaky one: `let x: void = undefined` is legal but `let y: void = null` errors under `strictNullChecks` — `void`'s only inhabitant is `undefined`.
