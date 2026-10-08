# 25 — `Record<K, V>` vs `{ [key: string]: V }` — when each

> **Interview question:** "`Record<string, number>` vs `{ [key: string]: number }` — same thing? When do they differ?"
> **What the interviewer is really testing:** Do you know `Record` is a mapped type over a *key union* — so it can demand an exact, exhaustive key set — while an index signature means "any string key, none required," with the famous "typed `V`, actually `undefined`" lookup trap?

## Theory — what it is

`Record<K, V>` is a built-in mapped type: `type Record<K extends keyof any, V> = { [P in K]: V }`. `K` can be any key-ish type — and crucially, a *finite union of literals*. `{ [key: string]: V }` is an **index signature**: "any string key maps to `V`."

For `Record<string, V>` the two are nearly identical. They diverge when `K` is narrower than `string`:

```typescript
type Status = "idle" | "loading" | "done";

const a: Record<Status, string> = {
  idle: "waiting", loading: "working", done: "finished",
};                                   // ALL three required; extras error

const b: { [k: string]: string } = {};   // zero keys fine; any key fine
```

- **Exhaustiveness:** `Record<Status, V>` *requires* every union member — add `"failed"` to `Status` and every such `Record` errors until handled. Index signatures can't express that.
- **Exactness:** extra keys on a literal `Record<Status, V>` error too — the key set is closed.
- **The lookup trap:** `b["anything"]` types as `string`, but at runtime it's `undefined` for missing keys — TypeScript trusts the signature. (`noUncheckedIndexedAccess` types it `string | undefined` honestly.) `Record<string, V>` has the identical trap.
- **Sparse maps over known keys:** `Partial<Record<Status, V>>` — lookups still keyed by `Status`, not arbitrary strings.
- `Record` composes cleanly: `Record<Status, { label: string; color: string }>`, or skip it and map directly: `{ [K in Status]: ... }`.

## Why it was needed

Two real shapes recur: **closed maps** — a value for each member of a finite set (labels per status, colors per theme, handlers per event type) — and **open dictionaries** — word counts, caches keyed by arbitrary ids, parsed JSON objects. Index signatures only express the second. `Record` expresses both, and for the first it turns "you forgot a case" into a compile error — the same favor discriminated unions do for `switch` statements.

## Where it's used in a real project

- `Record<Locale, Dictionary>` — i18n: add a locale, every dictionary must provide it.
- `Record<Status, () => void>` — state machines: exhaustive handler tables instead of if-chains.
- `Record<string, User>` / `{ [id: string]: User }` — caches and normalized store slices (`entities` in Redux/Normalizr).
- `Record<EnvVar, string>` — required env config that must name every variable.
- `Partial<Record<K, V>>` — feature flags and overrides where keys are known but sparse.
- `Record<keyof Form, string | null>` — per-field error bags that can't drift from the form shape.

## Diagram

```
Record<"dark" | "light", Theme>          { [key: string]: Theme }
┌─────────────────────────────┐          ┌────────────────────────────┐
│ keys: EXACTLY these two     │          │ keys: any string, or none  │
│ missing key → compile ERR   │          │ {} is valid                │
│ extra key   → compile ERR   │          │ any extra key fine         │
│ lookup by Theme-key → Theme │          │ lookup by "anything"       │
│                             │          │   typed Theme — actually   │
│ add "system" to the union → │          │   undefined at runtime!    │
│ every Record must update    │          │ (noUncheckedIndexedAccess  │
└─────────────────────────────┘          │  types it Theme|undefined) │
        CLOSED MAP                       └────────────────────────────┘
        "one per member"                        OPEN DICTIONARY
                                              "bag of string → V"
```

## Code — explained

```typescript
type Status = "idle" | "loading" | "done";

// 1. Record over a union — exhaustive, closed
const labels: Record<Status, string> = {
  idle: "waiting",
  loading: "working",
  done: "finished",
};                                     // (1) all three required; a 4th errors
console.log(labels.loading);           // working

// 2. Index signature — open dictionary
const counts: { [word: string]: number } = {};   // (2) zero keys is fine
counts["hello"] = 1;
counts["hello"] += 1;
console.log(counts["hello"]);          // 2

// 3. The lookup trap
const cache: Record<string, number> = {};
const v: number = cache["missing"];    // (3) typed number — runtime undefined!
console.log(v);                        // undefined — no error, silent lie
console.log(v + 1);                    // NaN

// 4. Record catches drift
const handlers: Record<Status, () => string> = {
  idle: () => "i",
  loading: () => "l",
  done: () => "d",
};
// add "failed" to Status → `handlers` errors until you add its handler
console.log(handlers.done());          // d
```

1. Every `Status` member must be a key, and no others — miss one or typo `lodging` and it's a compile error.
2. Index signature: `{}` is valid, `counts["whatever"]` is valid — openness is the point (and the danger).
3. `cache["missing"]` is *declared* `number` but is `undefined` at runtime — `v + 1` becomes `NaN` with no error anywhere. `Record<string, V>` has the same trap; `noUncheckedIndexedAccess` or `Partial<Record<...>>` makes it honest.
4. The closed-map payoff: extend the union and every `Record<Status, ...>` in the codebase lights up red — exhaustiveness enforced by the compiler.

## Problems

### Easy — An exhaustive label map
**Problem:** `type Level = "info" | "warn" | "error"`. Write a `Record` mapping each level to a label, and show what the compiler says when one is missing.
**Try this input:** a map literal missing `"error"`.
**Expected output:** compile error — `Property 'error' is missing in type '{ info: string; warn: string; }' but required in type 'Record<Level, string>'`. With all three present, `console.log(map.error)` prints its label.
**Solution:**
```typescript
type Level = "info" | "warn" | "error";

const icon: Record<Level, string> = {
  info: "i",
  warn: "w",
  error: "e",
};
// missing "error" → error TS2741: Property 'error' is missing in type
// '{ info: string; warn: string; }' but required in type 'Record<Level, string>'

console.log(icon.error);   // e
```
**Logic explained:**
1. `Record<Level, string>` demands *exactly* the union members — no missing keys, no extras.
2. `{ [k: string]: string }` would happily accept a missing `"error"` and a nonsense `"erorr"` key — openness is wrong for a fixed set.
3. This is the dictionary version of an exhaustive `switch`: same "the compiler makes me handle every case" benefit.

### Medium — Word-frequency counter
**Problem:** Count word frequencies into `Record<string, number>`; demonstrate and fix the `undefined` increment trap (`counts[w] += 1` on a fresh key).
**Try this input:** `["a", "b", "a"]`
**Expected output:** `{ a: 2, b: 1 }` — and without the fix, `NaN` silently infects the counts.
**Solution:**
```typescript
function freq(words: string[]): Record<string, number> {
  const counts: Record<string, number> = {};
  for (const w of words) {
    counts[w] = (counts[w] ?? 0) + 1;   // ?? handles the undefined first hit
    // counts[w] += 1;                  // NaN! undefined + 1
  }
  return counts;
}

console.log(freq(["a", "b", "a"]));     // { a: 2, b: 1 }
```
**Logic explained:**
1. `counts[w]` is typed `number` but is `undefined` on first sight — `+=` produces `NaN` silently, and it poisons every later count for that word.
2. `?? 0` is the honest fix (`??` not `||` — `||` would also clobber a legitimate `0`, though harmless for counts; `??` is the precise habit). `noUncheckedIndexedAccess` would turn the trap into a compile error.
3. An open dictionary is the *right* choice here — the key set is data-driven and unknowable at compile time; `Record<union>` can't express "all possible words."

### Hard — `groupBy` into a sparse record
**Problem:** Write `groupBy<T, K extends string>(items: T[], key: (t: T) => K): Partial<Record<K, T[]>>`. Why `Partial` — and what does `groups["guest"]` do?
**Try this input:** users with `role: "admin" | "user"` — `[{name:"a",role:"admin"},{name:"b",role:"user"},{name:"c",role:"admin"}]`
**Expected output:** `groups["admin"]?.length` → `2`; `groups["user"]?.length` → `1`; `groups["guest"]` is a **compile error** — `"guest"` isn't a key of the union.
**Solution:**
```typescript
interface User { name: string; role: "admin" | "user" }

function groupBy<T, K extends string>(
  items: T[],
  key: (t: T) => K
): Partial<Record<K, T[]>> {
  const out: Partial<Record<K, T[]>> = {};
  for (const item of items) {
    const k = key(item);
    (out[k] ??= []).push(item);         // lazily create the bucket
  }
  return out;
}

const users: User[] = [
  { name: "a", role: "admin" },
  { name: "b", role: "user" },
  { name: "c", role: "admin" },
];
const groups = groupBy(users, (u) => u.role);   // K inferred = "admin" | "user"
console.log(groups["admin"]?.length);   // 2
console.log(groups["user"]?.length);    // 1
// console.log(groups["guest"]);        // compile error — not a key of the union
console.log(groups["admin"] === undefined);  // false — but the TYPE stays | undefined
```
**Logic explained:**
1. `Partial<Record<K, T[]>>` is the honest return type: keys *come from data*, so not every `K` is guaranteed present — `Partial` types each lookup `T[] | undefined` instead of lying.
2. `K extends string` lets the key function return a union; inference captures `"admin" | "user"`, so `groups["guest"]` is a compile error — closed-map key checking on a sparse map.
3. `(out[k] ??= [])` lazily creates buckets — `??=` papers over the `| undefined` reality one more time.
4. Plain `Record<K, T[]>` would *claim* every key exists — a worse lie than the index signature's, because `groups["admin"]` on empty input would type `T[]` while being `undefined` at runtime.

## The 30-second interview answer

"`Record<K, V>` is a mapped type over a key type `K`; `{[key: string]: V}` is an index signature meaning 'any string key.' They're equivalent when `K = string`, but `Record` shines when `K` is a union of literals: `Record<Status, string>` requires *exactly* those keys — miss one or add an extra and it won't compile — giving closed-map exhaustiveness an index signature can't express. Index signatures — equivalently `Record<string, V>` — are for open dictionaries: caches, word counts, normalized stores where keys are data-driven. The shared footgun: `map[someKey]` types as `V` even when the key is absent — it's `undefined` at runtime, hence `noUncheckedIndexedAccess` or `Partial<Record<K, V>>` for honesty. Rule: finite known key set → `Record<union>`; unbounded keys → index signature; data-driven subsets of known keys → `Partial<Record<union>>`."

## Follow-up trap

**"Does `Record<string, V>` protect you from missing keys on lookup?"** — no; `Record<string, number>` claims `m["anything"]` is `number` while it's `undefined` at runtime. Two fixes: enable `noUncheckedIndexedAccess` (adds `| undefined` to every indexed read) or type it `Partial<Record<K, V>>` / `Record<K, V | undefined>` yourself. Second trap: **"why can't `{[key: string]: V}` be exhaustive?"** — `string` is infinite; the compiler can't require 'all strings.' Only a finite union gives closed-set checking. Third: **"`Record` vs `Map`?"** — `Record` types a plain object (string-ish keys, prototype caveats, JSON-serializable); `Map` is a runtime class with keys of *any* type, insertion-order iteration, and no prototype pollution. Use `Record` for data shapes, `Map` for runtime key-value behavior — and notice `Map.get` honestly returns `V | undefined`.
