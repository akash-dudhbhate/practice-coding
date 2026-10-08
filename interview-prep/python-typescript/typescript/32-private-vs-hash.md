# 32 — `private` vs `#private` — compile-time vs real runtime privacy

> **Interview question:** "What's the difference between TypeScript's `private` keyword and JavaScript's `#private` fields?"
> **What the interviewer is really testing:** Whether you know `private` is *erased at compile time* (anyone can reach the field at runtime or via bracket access), while `#field` is a *real JavaScript* feature enforced by the engine — inaccessible even with casts or bracket notation.

## Theory — what it is

Two different privacy mechanisms that look similar but work in different universes:

```typescript
class A {
  private tsSecret = "only type-checked";   // TS keyword — erased on compile
  #jsSecret = "really private";             // JS feature — enforced at runtime
}
```

Rules that matter:

- **`private` (TypeScript keyword):** only exists during type-checking. Compiled JS has a normal property. Escapes: `a["tsSecret"]` compiles fine, `(a as any).tsSecret` works, plain JS consumers see it. Same story for `protected` — also compile-time only.
- **`#field` (ECMAScript private fields, ES2022):** part of JavaScript itself. The field lives in a hidden slot, not as a normal property. `a.#jsSecret` outside the class is a **syntax error** (hard failure, not just a type error), `a["#jsSecret"]` is `undefined`, `Object.keys`/`JSON.stringify`/`Object.getOwnPropertyNames` don't see it.
- **Access rules differ:** `private` members are accessible in *other instances of the same class* (`other.x` inside a method is allowed). `#` fields behave the same — but only within the class body, enforced at runtime.
- **Construction differs:** `#` fields must be declared in the class body and exist before the constructor runs; `private` is just an annotation on a normal property.
- **`in` check:** `obj instanceof` doesn't reveal `private` fields, but `#jsSecret in obj` is a real runtime test for the brand — a feature unique to `#` fields.
- **Compatibility:** `#` fields require `target: ES2015+` in tsconfig (TS errors otherwise). Older runtimes can't run them at all.

## Why it was needed

TypeScript's `private` shipped in 2011, *years* before JavaScript had real private fields. It solved the practical problem of 90% of encapsulation — "stop teammates from touching internals" — with zero runtime cost.

But library authors kept hitting the leaks: `obj["privateThing"]` bypassed it, external JS code could overwrite internals, and reflection exposed everything. When TC39 finally standardized `#` fields (ES2022), TypeScript adopted the syntax — now you pick per-field: `private` for convention-level privacy, `#` for walls that actually hold at runtime (important for library internals, security-sensitive fields, and guaranteeing invariants).

## Where it's used in a real project

- **`private` everywhere:** normal application code — `private readonly repo: UserRepo`, `private cache = new Map()`. Convention is enough; the type error stops teammates.
- **`#` fields in libraries/SDKs:** published packages where consumers are untyped JS — `#token` can't be sniffed or monkey-patched.
- **`#` for true invariants:** a class whose correctness breaks if outsiders mutate a field — e.g. a `#balance` on an account object.
- **`private` when subclass-friendly visibility matters:** `protected` has no `#` equivalent (there's no `protected` in JS private fields — `#` is strictly class-only).
- **Detection:** `#field in obj` brand-checks without exposing the value — used for "was this made by my factory?" checks.

## Diagram

```
class Account {
  private tsBalance = 100;     <- annotation only
  #jsBalance = 100;            <- real runtime slot
}

COMPILED JS (conceptually):
  class Account {
    tsBalance = 100;           <- PLAIN PROPERTY, fully reachable
    #jsBalance = 100;          <- engine-managed, unreachable outside
  }

REACHABILITY TEST on `const a = new Account()`:

  a.tsBalance              ❌ TS error        | ✅ works in plain JS!
  a["tsBalance"]           ✅ compiles!!      | ✅ runtime works
  (a as any).tsBalance     ✅ compiles        | ✅ runtime works
  a.#jsBalance             ❌ syntax error    | ❌ syntax error
  a["#jsBalance"]          undefined          | undefined (not found)
  JSON.stringify(a)        {"tsBalance":100}  | #field invisible

  private = a sign saying "staff only"     (you can still walk in)
  #field  = a locked door                   (no key outside the class)
```

## Code — explained

```typescript
class Wallet {
  private tsPin = "1234";          // (1) compile-time privacy only
  #jsPin = "1234";                 // (2) runtime-enforced privacy

  verifyPin(pin: string): boolean {
    return pin === this.#jsPin;    // (3) class body can read both
  }

  // (4) both kinds are reachable on OTHER instances of same class
  samePinAs(other: Wallet): boolean {
    return this.#jsPin === other.#jsPin;      // legal
    // this.tsPin === other.tsPin             // also legal
  }
}

const w = new Wallet();

// 5. private blocks direct access — but only at compile time
// w.tsPin;               // Error: 'tsPin' is private

// 6. The escape hatches — private is a suggestion, not a wall
const leak1 = (w as unknown as { tsPin: string }).tsPin;  // cast works
console.log(leak1);              // 1234 — private field exposed!

const leak2 = (w as any)["tsPin"];                        // bracket access
console.log(leak2);              // 1234

// 7. #jsPin has NO escape hatch from outside
// w.#jsPin;               // SyntaxError — not even a type error, a parse error
// (w as any).#jsPin;      // still a syntax error — casts don't help
console.log((w as any)["#jsPin"]); // undefined — it's not a property key

// 8. Reflection can't see # fields either
console.log(JSON.stringify(w));    // {"tsPin":"1234"} — the "private" one leaks!
console.log(w.verifyPin("1234"));  // true — the real one stays hidden
```

1. `private` on `tsPin` tells the compiler "reject outside access" — and it does — but the emitted JS is a plain property.
2. `#jsPin` is declared with the `#` prefix and accessed as `this.#jsPin` — the `#` is part of the name, mandatory at every use.
3. Inside the class body both are reachable; the difference is what happens *outside*.
4. Privacy is class-scoped, not instance-scoped — methods can touch other `Wallet` instances' private members, for both mechanisms.
5. This is the illusion most people rely on: the compile error makes `private` *feel* safe.
6. Casts and bracket access walk right past it — TypeScript can't protect you at runtime because the keyword simply isn't there anymore.
7. `#` fields are parsed by the JS engine as private-slot access; there's no property to reach, so no cast or bracket trick works — `w["#jsPin"]` looks up a *normal property literally named* `#jsPin`, which doesn't exist.
8. The practical consequence: `JSON.stringify`, `Object.keys`, `for...in`, spread — all of them see `tsPin` but not `#jsPin`. If you're serializing an object for logs, `private` fields leak into the output while `#` fields don't.

## Problems

### Easy — spot the leak
**Problem:** `class Doc { private body: string }` is serialized with `JSON.stringify` for logging. Which fields leak into the log output — `private` fields, `#` fields, or both?
**Try this input:** `new Doc()` with `private body = "secret"` and `#sig = "abc"`, then `JSON.stringify(doc)`.
**Expected output:** `{"body":"secret"}` — the `private` field serializes, the `#` field doesn't appear at all.
**Solution:**
```typescript
class Doc {
  private body = "secret";    // compiles to a normal property -> leaks
  #sig = "abc";               // private slot -> invisible to stringify
}

const doc = new Doc();
console.log(JSON.stringify(doc));   // {"body":"secret"}
console.log(Object.keys(doc));      // ["body"] — #sig isn't a property
```
**Logic explained:**
1. `private` is erased at compile time — `body` becomes an ordinary own-property, and `JSON.stringify` serializes own enumerable properties.
2. `#sig` lives in a private slot, not in the object's property list — so `Object.keys`, spread, and stringify all miss it.
3. Interview takeaway: "private" in TS does not mean "hidden from serialization/logging" — if leaking internals to logs matters, use `#`.

### Medium — bypass `private`, fail on `#`
**Problem:** Show two ways to read a `private` field from outside a class, and show the equivalent attempts on a `#` field failing.
**Try this input:** `new Vault()` with `private code = "open"` and `#key = "gold"`.
**Expected output:** two `open` logs (cast + bracket), then `undefined` for the `#key` bracket attempt.
**Solution:**
```typescript
class Vault {
  private code = "open";
  #key = "gold";
}

const v = new Vault();

// bypass 1: cast to a matching shape
console.log((v as unknown as { code: string }).code);  // open
// bypass 2: bracket access via any — the property is just sitting there
console.log((v as any)["code"]);                         // open
// bypass 3 (most common): (v as any).code — any disables all checks

// #key attempts:
console.log((v as any)["#key"]);   // undefined — no such property
// v.#key                          // SyntaxError: can't even parse it
// (v as any).#key                 // still SyntaxError — parser-level, not types
```
**Logic explained:**
1. A cast retypes the object to `{ code: string }` — no `private` exists in that shape, so access compiles. The property is right there at runtime.
2. Bracket access `v["code"]` historically bypassed TS's private checks; `as any` does it trivially — `private` is a lint rule in disguise.
3. `#key` can't be reached by *any* of these: `#` access is syntax the parser handles before types, and `["#key"]` looks up a property that literally doesn't exist.

### Hard — brand-check with `#field in obj`
**Problem:** A factory produces `Session` objects. Write `isSession(x: unknown)` that returns `true` only for objects built by the class — surviving casts, clones, and lookalike objects — using a `#` field.
**Try this input:** `isSession(new Session())`, `isSession({ userId: "u1" } as Session)`, `isSession({})`.
**Expected output:** `true`, `false`, `false` — the imposter with a cast is correctly rejected.
**Solution:**
```typescript
class Session {
  #brand = true;                       // real private field = unforgeable brand
  userId: string;

  constructor(userId: string) {
    this.userId = userId;
  }

  static isSession(x: unknown): x is Session {
    return typeof x === "object" && x !== null && #brand in x;
  }
}

const real = new Session("u1");
const fake = { userId: "u1" } as Session;          // lookalike + cast
const fake2 = { userId: "u1", "#brand": true };    // even faking the name fails

console.log(Session.isSession(real));   // true
console.log(Session.isSession(fake));   // false — shape matches, brand doesn't
console.log(Session.isSession(fake2));  // false — "#brand" property ≠ #brand slot
console.log(Session.isSession({}));     // false
```
**Logic explained:**
1. `#brand in x` is a real operator on private fields — true only if `x` was constructed by this class (the private slot actually exists on it).
2. `{ userId: "u1" } as Session` silences the compiler but can't forge the private slot — the `in` check correctly rejects it, where a shape-check would pass.
3. Even naming a normal property `"#brand"` doesn't work: `"#brand" in obj` checks the *property*, `#brand in obj` checks the *private slot* — different namespaces.
4. This is something `private` fundamentally cannot do — there's no runtime trace of a `private` field to check for. `in`-brand-checks are the standard pattern for "is this one of mine?" in libraries.

## The 30-second interview answer

"TypeScript `private` is a compile-time annotation — it gets erased, so at runtime it's a plain property. Anyone can bypass it with bracket access, an `as` cast, or just by consuming the compiled JS, and it shows up in `JSON.stringify` and `Object.keys`. `#field` is real JavaScript private state from ES2022 — the field lives in an engine-managed private slot, so outside access is a *syntax error*, reflection can't see it, and no cast reaches it. Private fields even support `#field in obj` brand checks — the only unforgeable way to test 'was this made by my class?' So: `private` is fine for internal app code where a compile error stops teammates; `#` is what you use for library internals, invariants that must hold at runtime, or fields you don't want leaking into serialization."

## Follow-up trap

**"So `private` is useless — always use `#`?"** — No, three catches: `#` fields can't be `protected` (subclasses can't see them — there's no protected-`#` hybrid), they require `target: ES2015+`, and they're a *hard* boundary — a subclass that needs the field forces awkward redesign, where `protected` would have just worked. Second trap: **"can a subclass access a parent's `#` field?"** — No. `#` fields are per-class-body, not per-hierarchy — the subclass literally can't name the parent's private name. Third: **"does `private` on a constructor parameter property (`constructor(private x: number)`) behave differently?"** — no, it's still compile-time only; it's just sugar for declaring + assigning a normal property. And a bonus: mixing both is legal — `private #x` is meaningless, but `private x` + `#y` on the same class is fine.
