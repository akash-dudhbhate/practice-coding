# 04 — Union vs intersection

> **Interview question:** "What's the difference between `A | B` and `A & B` in TypeScript?"
> **What the interviewer is really testing:** Whether you can read the operators the right way — `|` is "one of these" (value satisfies *either*), `&` is "all of these" (value satisfies *both simultaneously*) — with real examples, not just definitions.

## Theory — what it is

A **union** `A | B` means "a value of this type is an `A` *or* a `B` (or both)." The set of allowed values is the *sum* of both sets — it gets **bigger**. Inside your code you can only safely use what *all* members share (e.g. a common field), unless you **narrow** first with `if`, `switch`, `typeof`, `in`, or `instanceof`.

An **intersection** `A & B` means "a value of this type must satisfy `A` *and* `B` at the same time." For object types it behaves like merging the members — the result has every field of `A` *and* every field of `B`. The set of allowed values gets **smaller** (fewer objects qualify), but the type's *capabilities* grow — you can use members of both without narrowing.

The counterintuitive bit that interviewers love: union = more possible values, fewer guaranteed properties; intersection = fewer possible values, more guaranteed properties. And on primitives they invert intuition: `string | number` accepts `"x"` or `5`; `string & number` is **impossible** — it collapses to `never`, because no value is both.

Jargon: a **discriminated union** is a union of object types sharing a literal "tag" field (like `kind`) that lets the compiler narrow. **Narrowing** is the compiler refining a union to one member inside a branch.

## Why it was needed

Real data is polymorphic in both directions:

- "This is **one of** several shapes" — an API response is `Success | Failure`; a payment is `Card | Cash | Crypto`. Modeling that with classes or `any` loses the guarantee that you handled every case. Unions + narrowing make the compiler enforce handling.
- "This must be **all of** these" — a function needs a value that's both `Timestamped` and `Identifiable`; a config combines `BaseConfig` with env-specific overrides. Before intersections, you'd hand-copy fields into a new interface or misuse inheritance (`class`/`extends` couples implementation, not just shape).

What breaks without them: unions get replaced by optional-field soup (`{ email?: string, total?: number, kind: string }`) where every field "might not exist" and nothing tells you which combinations are legal. Intersections get replaced by duplicated interfaces that drift out of sync.

## Where it's used in a real project

- **Discriminated unions for state machines:** `type Req = { status: "loading" } | { status: "ok"; data: T } | { status: "err"; message: string }` — Redux states, fetch results, form statuses.
- **Unions for parameter flexibility:** `formatId(id: string | number)` — one function, two accepted inputs; inside, `typeof` narrows.
- **Intersections for mixins/composition:** `type AuditedEntity = Entity & { createdAt: Date; updatedAt: Date }` — layering orthogonal concerns without inheritance.
- **Intersections for "with" patterns:** `WithUser<T> = T & { user: User }` — HOCs and middleware that attach context.
- **Union literals for enums-that-aren't:** `type Env = "dev" | "staging" | "prod"` — lighter than `enum`, and the compiler checks exhaustiveness.

## Diagram

```
   UNION  A | B                      INTERSECTION  A & B
   "either"                          "both at once"

   ┌────────┐   ┌────────┐           ┌────────┐
   │  A     │   │   B    │           │  A  ┌──┼─────────┐
   │ {a:1}  │   │ {b:2}  │           │     │∩│   B     │
   └────────┘   └────────┘           └─────┼──┘         │
        values: {a:1} OR {b:2}             └───────────┘
        (more values allowed)         value must satisfy BOTH
        (fewer shared props)          {a:1, b:2} — more props

   primitives:
   string | number  -> accepts "x" or 5          (bigger)
   string & number  -> NEVER (impossible)        (empty)

   narrowing a union:                 using an intersection:
   if (x.kind === "card") {           x.a  // OK
     x.cardField  // OK only here     x.b  // OK — no narrowing needed
   }
```

## Code — explained

```typescript
// ---------- UNION: value is ONE OF ----------
type Card   = { kind: "card"; last4: string };
type Cash   = { kind: "cash" };
type Payment = Card | Cash;              // a Payment is a Card OR a Cash

function describe(p: Payment): string {
  // p.last4       // ERROR here — Cash has no last4; must narrow first
  if (p.kind === "card") {
    return `card •••• ${p.last4}`;     // narrowed to Card inside the branch
  }
  return "cash";                        // narrowed to Cash (only option left)
}

// ---------- INTERSECTION: value is ALL OF ----------
type HasId   = { id: number };
type HasName = { name: string };
type Entity  = HasId & HasName;          // must have id AND name

const e: Entity = { id: 1, name: "Ada" }; // both fields required
// const bad: Entity = { id: 1 };         // ERROR: missing 'name'

// ---------- the trap: impossible intersection ----------
type Impossible = string & number;        // = never — nothing satisfies both
```

1. `Card | Cash` declares "one of." Notice each member carries a `kind` literal — the discriminant that makes narrowing work.
2. Accessing `p.last4` before narrowing is an error: the compiler only guarantees members common to *every* union constituent (here just `kind`).
3. `p.kind === "card"` narrows `p` to `Card` inside the block — now `last4` is legal.
4. `HasId & HasName` requires *both* fields — no narrowing needed to use `id` or `name` because they're guaranteed on every value.
5. `string & number` collapses to `never`: intersections shrink the value set; when it shrinks to empty you get the impossible type.

## Problems

### Easy — accept either

**Problem:** Write `formatId` that accepts a user ID as `string | number` and always returns a string like `"ID: 42"`. Handle both inputs safely.

**Try this input:** `formatId(42)` and `formatId("u-7")`.
**Expected output:** `ID: 42` and `ID: u-7`.
**Solution:**

```typescript
function formatId(id: string | number): string {
  if (typeof id === "number") {
    return `ID: ${id}`;   // id: number here
  }
  return `ID: ${id}`;     // id: string here
}

console.log(formatId(42));    // "ID: 42"
console.log(formatId("u-7")); // "ID: u-7"
// formatId(true);            // ERROR: boolean not assignable to string | number
```

**Logic explained:**
1. The union in the *parameter* position widens what callers may pass — both `42` and `"u-7"` are legal.
2. `typeof id === "number"` narrows the union to `number` in that branch (typeof narrowing works on primitives).
3. `formatId(true)` errors — unions widen the *accepted inputs* but still exclude everything outside the union.

### Medium — require both

**Problem:** You have `Timestamped = { createdAt: Date }` and `Identifiable = { id: string }`. Write a `logEntity` that accepts only values having *both* — objects missing either field must be rejected at compile time — then prove it.

**Try this input:** `logEntity({ id: "a", createdAt: new Date() })` vs `logEntity({ id: "a" })`.
**Expected output:** First prints the log line; second is a compile error (`Property 'createdAt' is missing`).
**Solution:**

```typescript
type Timestamped   = { createdAt: Date };
type Identifiable  = { id: string };
type AuditedEntity = Timestamped & Identifiable; // needs ALL members

function logEntity(e: AuditedEntity): string {
  // No narrowing needed — an intersection guarantees every member.
  return `[${e.createdAt.toISOString()}] entity ${e.id}`;
}

console.log(logEntity({ id: "a", createdAt: new Date("2024-01-01") }));
// "[2024-01-01T00:00:00.000Z] entity a"

// logEntity({ id: "a" });
// ERROR TS2345: Property 'createdAt' is missing in type '{ id: string; }'
// but required in type 'Timestamped'
```

**Logic explained:**
1. `&` composes the requirements: a valid `AuditedEntity` must satisfy *every* constituent — the accepted value set shrinks.
2. Because all members are guaranteed, you read `e.createdAt` and `e.id` directly — the opposite trade-off from unions (fewer legal values, more usable properties).
3. `{ id: "a" }` fails because it satisfies `Identifiable` but not `Timestamped` — "all of" is literal.

### Hard — design the right combinator

**Problem:** Model a notification system. Every notification has `id` and `createdAt` (shared infra). There are three kinds: `EmailNotif` (`to`, `subject`), `SmsNotif` (`phone`), `PushNotif` (`deviceToken`). Write `send(n)` that reads the right field per kind. Decide where `&` and `|` each belong — and explain why `Notification = Base & (Email | Sms | Push)` vs `(Base & Email) | (Base & Sms) | (Base & Push)` matters.

**Try this input:** `send({ id: "1", createdAt: d, kind: "sms", phone: "555" })`.
**Expected output:** Prints `SMS to 555`; reading `n.phone` outside the `"sms"` branch is a compile error.
**Solution:**

```typescript
type Base = { id: string; createdAt: Date };

// & distributes over | : Base & (A | B)  ===  (Base & A) | (Base & B)
type Notification = Base & (
  | { kind: "email"; to: string; subject: string }
  | { kind: "sms";   phone: string }
  | { kind: "push";  deviceToken: string }
);

function send(n: Notification): string {
  switch (n.kind) {
    case "email": return `EMAIL to ${n.to}: ${n.subject}`;
    case "sms":   return `SMS to ${n.phone}`;
    case "push":  return `PUSH to ${n.deviceToken}`;
  }
}

const d = new Date(0);
console.log(send({ id: "1", createdAt: d, kind: "sms", phone: "555" }));
// "SMS to 555"

// send({ id: "2", createdAt: d, kind: "sms" });
// ERROR: missing 'phone' — & forced the base fields, | kept the variants distinct
```

**Logic explained:**
1. `&` layers the *shared* requirement (every notification has `id`/`createdAt`) onto the `|` of *variants* — intersection for "all must have," union for "exactly one of."
2. `A & (B | C)` distributes to `(A & B) | (A & C)`, so the discriminant `kind` still narrows correctly — you get shared fields *and* per-variant narrowing.
3. The alternative — one flat type with all fields optional — would allow `{ kind: "sms" }` with no `phone` to compile and crash at runtime. Union-of-complete-variants makes each variant self-consistent: the kind tag and its required fields are glued together.

## The 30-second interview answer

"`A | B` is a union — the value is one of the two, so the set of legal values grows but you can only use members common to both unless you narrow first with `typeof`, `in`, or a discriminant check. `A & B` is an intersection — the value must satisfy both simultaneously, so for objects it's like merging the fields: fewer values qualify but every member is guaranteed without narrowing. Classic uses: discriminated unions for API results and state machines, intersections for composing orthogonal concerns like `Entity & Audited`. And the gotcha — intersecting primitives like `string & number` collapses to `never`, because no value can be both."

## Follow-up trap

**"What is `string & number`?"** — Answer instantly: `never`. Then show you know *why* (the intersection of two disjoint sets is empty) and the useful cousin: object intersections with a conflicting property don't always error at declaration — `{ a: string } & { a: number }` gives `a: never`, which compiles as a type but is unconstructable — so `interface X extends ...` (which errors eagerly) is often the safer way to combine object shapes. A second common trap: "how do you narrow a union of *non-object* types?" — `typeof`/`instanceof`/truthiness, or wrapping in tagged objects when there's no discriminant.
