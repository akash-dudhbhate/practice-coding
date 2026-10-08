# 03 — mypy/pyright vs tsc: strict mode and CI

> **Interview question:** "How do Python type checkers compare to the TypeScript compiler — and how do you run them strictly in a real project?"
> **What the interviewer is really testing:** Whether you've actually wired type checking into CI, and whether you know what "strict" turns on.

## Theory — what it is

**`tsc`** is the TypeScript *compiler*. It does two jobs: type-check your `.ts` files and emit runnable `.js`. In CI you usually run `tsc --noEmit` — check types only, let a bundler (esbuild/vite/tsup) handle the emit. `strict: true` in `tsconfig.json` turns on a bundle of checks, the big ones being `noImplicitAny` (unannotated params can't silently be `any`) and `strictNullChecks` (`null`/`undefined` are distinct types you must handle).

**`mypy`** and **`pyright`** are Python *type checkers only* — they never run or emit your code; they just read the hints and report. `mypy` is the original; `pyright` (Microsoft) is faster, powers VS Code's Pylance, and is stricter about inference in places. `strict = true` in `mypy` config enables things like `disallow_untyped_defs` (every function must be fully annotated) and `warn_return_any`.

The asymmetry to name: `tsc` is *one* official checker with `strict` as a recommended flag; Python has *two mainstream checkers* that can disagree, and strictness is more opt-in and incremental (`follow_imports`, per-module overrides) because most real Python codebases started untyped.

## Why it was needed

Without a checker, type annotations are decorative. A hint that says `-> int` but returns `None` is a bug that neither Python nor erased TS types will catch at runtime — it explodes three calls later. Checkers turn annotations into a verified contract.

Strict mode exists because *partial* typing creates a false sense of safety: one `Any`/`any` leaks in and infects everything it touches (`Any` is "contagious" — `x: Any` makes everything derived from it unchecked). Strict flags exist mainly to **hunt down implicit `Any`s and unhandled `None`s/nulls**, which are the two biggest sources of runtime type bugs.

## Where it's used in a real project

1. **CI gate** — `tsc --noEmit` and `mypy src/` (or `pyright`) run on every PR; a type error blocks merge like a failing test.
2. **Pre-commit hooks** — run the checker (via `pre-commit`/`lint-staged`) so errors surface before push, not in CI.
3. **Editor feedback** — pyright powers Pylance in VS Code; tsc powers TS IntelliSense. Same checker locally and in CI = no surprises.
4. **Gradual adoption** — on a legacy codebase, enable strict per-module (`[[tool.mypy.overrides]]` / per-directory `tsconfig`) instead of boiling the ocean.

## Diagram

```
        developer writes code
               │
   ┌───────────▼────────────┐
   │ editor: pyright / tsc  │  instant red squiggles
   └───────────┬────────────┘
               │ git push
   ┌───────────▼────────────┐
   │ CI job:                │
   │  tsc --noEmit          │  TS: check only, no output files
   │  mypy src/  (strict)   │  PY: check only, always
   │  + ruff/eslint, tests  │
   └───────────┬────────────┘
          pass │        fail
               ▼            ▼
          merge OK      block PR
```

## Code — explained

Strict configuration, side by side:

```jsonc
// ---------- TYPESCRIPT: tsconfig.json ----------
{
  "compilerOptions": {
    "strict": true,               // bundle: noImplicitAny, strictNullChecks, ...
    "noUncheckedIndexedAccess": true, // arr[i] is T | undefined — forces checks
    "noEmit": true,               // type-check only; bundler emits
    "target": "ES2022",
    "module": "NodeNext"
  }
}
// CI step:  npx tsc --noEmit
```

```ini
# ---------- PYTHON: mypy (in pyproject.toml or mypy.ini) ----------
[tool.mypy]
strict = true                 # disallow_untyped_defs, warn_return_any, ...
python_version = "3.12"
# gradual adoption: loosen rules for legacy dirs only
[[tool.mypy.overrides]]
module = "legacy.*"
disallow_untyped_defs = false
# CI step:  mypy src/        (or: pyright)
```

```python
# What strict actually catches — none of these raise at runtime-check time:
def get_user(uid):            # strict: error — missing param & return types
    return db.find(uid)       # returns Any -> silently infects callers

def head(xs: list[int]) -> int:
    return xs[0]              # strict: error — could IndexError; also xs may be []
```

```typescript
// Same bugs under strict tsc:
function getUser(uid) {       // strict: error — implicit any parameter
  return db.find(uid);
}

function head(xs: number[]): number {
  return xs[0];               // noUncheckedIndexedAccess: xs[0] is number|undefined
}
```

The deep similarity: both checkers' strict modes are mostly about **eliminating `Any`/`any` and forcing null/None handling**. The deep difference: `tsc` also emits JS (so "compile" and "check" are the same tool), while Python checkers are purely advisory — which is exactly why file 01's runtime-validation point matters.

## Problems

### Easy — Read the error
**Problem:** mypy reports `error: Function is missing a return type annotation  [no-untyped-def]` on `def normalize(name: str):`. Fix it.

**Try this input:** `normalize("  Ada ")` should return `"ada"`.
**Expected output:** mypy clean; function returns lowercase trimmed name.
**Solution:**

```python
def normalize(name: str) -> str:
    return name.strip().lower()
```

**Logic explained:**
1. `strict` enables `disallow_untyped_defs` — every parameter AND return needs an annotation.
2. If the function can return nothing, annotate `-> None`; if it might fail, return `str | None` honestly.
3. `no-untyped-def` errors are the most common blocker when enabling strict on old code.

### Medium — Kill the Any leak
**Problem:** This passes loose mypy but is unsafe. Find the `Any` leak and fix it.

```python
import json

def total(raw: str) -> float:
    data = json.loads(raw)      # data: Any
    return data["price"] * 2    # Any * 2 -> Any -> return type lies
```

**Try this input:** `'{"price": "abc"}'` — returns `"abcabc"`-style garbage or crashes, no type error.
**Expected output:** a `ValidationError` or a correct `float`.
**Solution:**

```python
from pydantic import BaseModel

class Cart(BaseModel):
    price: float

def total(raw: str) -> float:
    return Cart.model_validate_json(raw).price * 2
```

**Logic explained:**
1. `json.loads` returns `Any` — under strict, `warn_return_any` and `disallow_any_expr` flag the leak.
2. `Any` is contagious: `data["price"]` is `Any`, so the multiplication and return are unchecked.
3. Parsing through a pydantic model converts `Any` into a verified `float` — the runtime check produces the static guarantee.

### Hard — Strictness that fights back
**Problem:** Under `strict` + `noUncheckedIndexedAccess`, this fails to compile. Fix it *without* a non-null assertion (`!`), and give the Python equivalent treatment.

```typescript
const counts: Record<string, number> = { a: 1 };
const first = Object.keys(counts)[0];
const v = counts[first];      // number | undefined
return v + 1;                 // error: possibly undefined
```

**Try this input:** `counts = {}`.
**Expected output:** function returns `undefined` (or a default) rather than `NaN` — safely.
**Solution:**

```typescript
const counts: Record<string, number> = { a: 1 };
const first = Object.keys(counts)[0];
if (first === undefined) return undefined;
const v = counts[first];
if (v === undefined) return undefined;   // key existed but... be honest
return v + 1;
// or simpler: return (counts[first ?? ""] ?? 0) + 1 — explicit default
```

```python
counts: dict[str, int] = {"a": 1}
v = counts.get("a")          # int | None — honest lookup
if v is None:
    return None
return v + 1
```

**Logic explained:**
1. `noUncheckedIndexedAccess` makes every index access `T | undefined` — mirroring Python where `dict.get` returns `Optional`.
2. The strict fix is *narrowing* (`if v === undefined return`), not `v!` — `!` is another `as`, a claim not a check.
3. In Python the parallel is `counts["a"]` (KeyError risk) vs `counts.get("a")` + a `None` check. Strict checkers push both languages toward explicit handling.

## The 30-second interview answer

"`tsc` is TypeScript's compiler — it type-checks and emits JS, so in CI you run `tsc --noEmit` and let the bundler emit. Python has no compile step, so `mypy` or `pyright` are separate check-only tools; pyright also powers VS Code's IntelliSense. On both sides, `strict: true` mostly hunts the same two bugs: implicit `Any`s — which are contagious and silently disable checking — and unhandled `null`/`None` (`strictNullChecks`, `noUncheckedIndexedAccess`; `disallow_untyped_defs` in mypy). In CI both are blocking gates next to lint and tests, run identically locally via pre-commit. On a legacy codebase I'd enable strict incrementally per-module rather than all at once."

## Follow-up trap

"mypy passes but the code crashes at runtime — how?" — Strong answer: the checker only sees what you *declared*. A `cast(int, x)`, an `Any` leaking from `json.loads`, a `type: ignore` comment, or untyped third-party stubs all create blind spots. Static checking verifies consistency of your claims, not truth of the data — which is why boundary validation (pydantic/zod) is still required even with a green mypy run.
