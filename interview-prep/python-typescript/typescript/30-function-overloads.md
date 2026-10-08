# 30 — Function overloads vs union parameters — when overloads are worth it

> **Interview question:** "When would you write function overloads instead of just union parameter types?"
> **What the interviewer is really testing:** Do you understand that a union parameter can't express *correlation* — "string in → string out, number in → number out" — and that overloads exist to tie input type to output type?

## Theory — what it is

A union parameter gives every caller **one** signature:

```typescript
function wrap(x: string | number): (string | number)[]
```

Pass a `string`, get back `(string | number)[]` — the correlation between what went in and what comes out is lost. Overloads fix that by declaring **multiple call signatures** over a single implementation:

```typescript
function wrap(x: string): string[];      // call signature 1
function wrap(x: number): number[];      // call signature 2
function wrap(x: string | number) {      // implementation signature
  return [x];
}
```

Rules that matter:

- **Callers only see the overloads.** `wrap("a")` → `string[]`, `wrap(1)` → `number[]`. The implementation signature (`string | number` → `(string|number)[]` inferred) is *not* callable — `wrap(true)` errors even though the impl body might handle it.
- The implementation must be **compatible with every overload** (its params/return broad enough to cover them all).
- Overloads are checked **top to bottom, first match wins** — order specific cases before general ones.
- Overloads live in signatures, not bodies: inside the impl you still write `x: string | number` and narrow manually. The types are for callers; the body is plain JS.

**When overloads are worth it:** return type depends on argument type; different arities (`f(a)` vs `f(a, b)` with different returns); literal-level dispatch (`on("click", …)` vs `on("submit", …)`); string-key → result-type maps like DOM `createElement`.

**When a union is better:** the return type is the same regardless of input — `format(x: string | number): string`. One signature, less machinery. And when correlation is the only goal, a generic often beats overloads: `function wrap<T extends string | number>(x: T): T[]` does the same job in one signature.

## Why it was needed

JavaScript functions routinely behave polymorphically — `document.createElement("div")` returns `HTMLDivElement`, `createElement("canvas")` returns `HTMLCanvasElement`. One signature can't express that; a union parameter loses the correlation; a generic needs the arg itself to carry the type, which works (`<T extends …>`) until the mapping is a *lookup* rather than identity — `"div"` isn't `HTMLDivElement`, it's a string key that maps to it.

Overloads let library authors write a *table of signatures*. TypeScript checks calls against the table; the single JavaScript implementation underneath stays dynamic, exactly as it always was. Zero runtime cost — overloads are erased.

## Where it's used in a real project

- **DOM typing:** `createElement`, `querySelector`, `addEventListener("click", e => …)` — the event name picks the event object's type. This is the textbook overload table.
- **Flag-driven returns:** `fetchData(url, { parse: true }): Parsed` vs `{ parse: false }`: string — booleans in, different types out.
- **Currying/arity:** `pipe(f)` → unary, `pipe(f, g)` → composed — arity changes meaning.
- **String-key dispatch:** `store.get("user"): User` vs `store.get("cart"): Cart` — a map from literal keys to types (though an object-type map + generics often does this cleaner).
- **Backward-compatible APIs:** old signature + new signature both listed as overloads while the impl handles both.

## Diagram

```
UNION PARAM — one signature, correlation LOST
  wrap(x: string | number): (string | number)[]
     "a" ──► (string | number)[]   caller can't count on element type
     1  ──► (string | number)[]

OVERLOADS — a table of signatures, correlation KEPT
  function wrap(x: string): string[];
  function wrap(x: number): number[];
  function wrap(x: string | number) { return [x]; }
            ▲
            └── implementation signature: invisible to callers,
                must be broad enough to cover every overload
     "a" ──► matches sig 1 ──► string[]
     1  ──► matches sig 2 ──► number[]
     true ──► NO match ──► compile error (impl sig is hidden)

GENERIC alternative — correlation via inference
  function wrap<T extends string | number>(x: T): T[]
     "a" ──► T = "a"  ──► string[]   (often simpler when it fits)
```

## Code — explained

```typescript
// 1. The overload table — what callers can see
function parse(input: string): number;            // "42" -> number
function parse(input: number): string;            // 42   -> string
// 2. The implementation signature — broad, hidden from callers
function parse(input: string | number): string | number {
  if (typeof input === "string") return Number(input);
  return String(input);
}

const n = parse("42");    // (3) n: number — matched sig 1
const s = parse(42);      // (4) s: string — matched sig 2
// parse(true);           // (5) Error: no overload matches — impl sig is NOT callable

// 6. Arity overloads — different argument counts, different returns
function range(stop: number): number[];
function range(start: number, stop: number): number[];
function range(a: number, b?: number): number[] {
  const [start, stop] = b === undefined ? [0, a] : [a, b];
  return Array.from({ length: stop - start }, (_, i) => start + i);
}
console.log(range(3));       // [0, 1, 2]      — one arg: 0..n
console.log(range(2, 5));    // [2, 3, 4]      — two args: start..stop

// 7. Inside the impl you still narrow — overloads don't narrow for you
function stringify(x: string): `str:${string}`;
function stringify(x: number): `num:${number}`;
function stringify(x: string | number): string {
  return typeof x === "string" ? `str:${x}` : `num:${x}`;   // (8)
}
console.log(stringify("a"), stringify(9));   // str:a num:9
```

1. Two call signatures: callers see a *menu*, not a union. Each describes one input→output correlation.
2. The impl signature `input: string | number` is the union of the overload domains — it must cover all of them. Its return type annotation is required here because TS won't check it's covered by the overloads' returns (a known footgun: it can be sloppier than the overloads claim).
3. `parse("42")` matches sig 1 → declared `number`. The compiler doesn't verify the impl actually returns a number for strings — overloads are *trusted*, which is why sloppy impls can lie.
4. `parse(42)` skips sig 1 (`number` isn't `string`), matches sig 2 → `string`.
5. `parse(true)` matches nothing — and `boolean` isn't in the impl signature anyway. The impl signature being non-callable is a feature: it can't be invoked "loosely."
6. Arity overloads: `range(3)` and `range(2, 5)` mean different things. One union signature `range(a: number, b?: number)` would *also* compile — but then `range()` alone would be illegal… actually the union handles arity fine too. The real overload win in this example is clarity; the *type-level* win shows up when arity changes the return type.
7. Overloads are caller-facing only — inside the body `x` is still `string | number` and you narrow with `typeof` as usual.
8. Template-literal return types (`str:${string}`) show overloads carrying literal-precision types a union signature couldn't.

## Problems

### Easy — add a second overload
**Problem:** `function double(x: number): number` exists. Add overloads so `double("hi")` returns `"hihi"` (string) while `double(2)` still returns `number`, and `double(true)` is a compile error.
**Try this input:** `double("hi")`, `double(2)`, `double(true)`.
**Expected output:** `hihi` and `4` logged; the `boolean` call fails with `No overload matches this call`.
**Solution:**
```typescript
function double(x: string): string;
function double(x: number): number;
function double(x: string | number): string | number {
  return typeof x === "string" ? x + x : x * 2;
}

console.log(double("hi"));   // hihi
console.log(double(2));      // 4
// double(true);             // Error: No overload matches this call
```
**Logic explained:**
1. Two overloads declare the correlation: string→string, number→number. A union signature `x: string | number` could only promise `string | number` back.
2. The impl covers both domains and narrows with `typeof` — the overloads don't do the dispatch, your code does.
3. `double(true)` has no matching overload → compile error. If you'd written one union signature you'd have had to either accept `boolean` (wrong) or add `boolean` and return a nonsense union type.

### Medium — correlated key→value lookup
**Problem:** A config store: `getConfig("theme")` must return `string`, `getConfig("retries")` must return `number`, `getConfig("verbose")` must return `boolean`. Write it with overloads so `getConfig("retries") + 1` is a `number` operation.
**Try this input:** `getConfig("retries") + 1`, `getConfig("theme").toUpperCase()`, `getConfig("missing")`.
**Expected output:** `4` and `"DARK"` logged; `"missing"` is a compile error — no overload for it.
**Solution:**
```typescript
function getConfig(key: "theme"): string;
function getConfig(key: "retries"): number;
function getConfig(key: "verbose"): boolean;
function getConfig(key: string): string | number | boolean {
  const store: Record<string, string | number | boolean> = {
    theme: "dark",
    retries: 3,
    verbose: false,
  };
  return store[key];
}

console.log(getConfig("retries") + 1);      // 4 — number
console.log(getConfig("theme").toUpperCase()); // DARK — string
// getConfig("missing");                     // Error: no overload matches
```
**Logic explained:**
1. Literal-typed overload params turn each key into its own signature — `"retries"` maps to `number`. This is a manual key→type table.
2. Inside the impl the key is just `string` and the return is the full union — the precision lives in the overloads, not the body.
3. `getConfig("retries") + 1` type-checks as number arithmetic; `getConfig("theme").toUpperCase()` as a string op. With a union return both would error.
4. Cleaner alternative worth mentioning in an interview: `interface ConfigMap { theme: string; retries: number; verbose: boolean }` + `function getConfig<K extends keyof ConfigMap>(k: K): ConfigMap[K]` — one generic signature, same precision, auto-extends when keys are added.

### Hard — boolean flag changes the return type
**Problem:** `fetchText(url)` returns `Promise<string>`; `fetchText(url, { json: true })` must return `Promise<Record<string, unknown>>`. Add overloads, implement with a union/optional impl signature, and show a call where the flag picks the type.
**Try this input:** `await fetchText("/api", { json: true })` then `.data`, vs without the flag `.toUpperCase()`.
**Expected output:** json-flag call logs a key from the object; plain call logs `HELLO`; calling `.toUpperCase()` on the json-flag result is a compile error.
**Solution:**
```typescript
interface Opts {
  json?: boolean;
}

async function fetchText(url: string): Promise<string>;
async function fetchText(url: string, opts: { json: true }): Promise<Record<string, unknown>>;
async function fetchText(url: string, opts?: Opts): Promise<string | Record<string, unknown>> {
  const res = await fetch(url);
  return opts?.json ? res.json() : res.text();
}

async function main() {
  const obj = await fetchText("/api", { json: true });   // Record<string, unknown>
  const txt = await fetchText("/api");                   // string
  console.log("keys:", Object.keys(obj));                // keys: [ 'id', 'name', ... ]
  console.log(txt.toUpperCase());                        // works — txt is string
  // obj.toUpperCase();                                  // Error: not on Record
}
```
**Logic explained:**
1. Overload 2's param `{ json: true }` is literal-typed — it only matches when the caller passes `json: true` specifically. `{ json: false }` matches neither overload → error, which is correct: we never defined what `false` returns.
2. The impl takes `opts?: Opts` (broad enough for both overloads) and returns the union `string | Record<...>` — again, precision lives in the overload table.
3. `opts?.json ? res.json() : res.text()` — the runtime branch mirrors the type branch; overloads don't do this dispatch for you.
4. The flag's literal type is the linchpin: `opts: { json: boolean }` in the overload would match `{ json: false }` too and wrongly claim `Record` comes back. Literal types in overload params are how you pin correlation.

## The 30-second interview answer

"Union parameters give every caller one signature — `f(x: string | number): string | number` loses the correlation between input and output. Overloads are a *table* of call signatures over a single implementation: `f(x: string): string` and `f(x: number): number` preserve it, so `f("a")` is known to return `string`. Callers only see the overloads — the implementation signature isn't callable — and inside the body you still narrow manually. They're worth it when return type depends on argument type, when arity changes meaning, or for literal-key dispatch like `addEventListener('click')`. If the return type is the same for all inputs, a union is simpler — and if the correlation is just 'same type in, same type out,' a generic like `<T extends string|number>(x: T): T` beats an overload table."

## Follow-up trap

**"Can callers use the implementation signature directly?"** — No. `function f(x: string): string; function f(x: string|number) {...}` — `f(1)` errors with "No overload matches this call." The impl signature exists only to type the body; that invisibility is by design. Second trap: **"Does TypeScript check that the implementation actually returns what each overload promises?"** — Only loosely. `function f(x: string): number; function f(x: any): any { return x }` compiles while returning a `string` for `f("a")`. Overloads are *trusted declarations* — sloppy impls lie, which is why some teams prefer generics. Third: **"overloads vs a generic + indexed access (`K extends keyof M => M[K]`)?"** — for key→type lookups the generic is usually better (auto-extends, no duplicated table); overloads win for genuinely different arities or flag-driven shapes.
