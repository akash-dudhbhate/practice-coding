# 02 — pydantic vs zod: parsing untrusted data into typed shapes

> **Interview question:** "How does pydantic compare to zod — are they doing the same job?"
> **What the interviewer is really testing:** Do you understand *runtime schema validation* as a language-agnostic concept, not just a library you imported once?

## Theory — what it is

**pydantic** (Python) and **zod** (TypeScript) are both *runtime schema validators*. You declare the shape you expect — field names, types, constraints — as a **schema**. Then you feed it untrusted data (usually `dict`/`Any` or `unknown`/`JSON`), and it either returns a clean, correctly-typed object or raises a detailed error listing every violation.

Both do two things at once:

1. **Validation** — reject bad data with precise errors (`"age must be a number"`).
2. **Coercion/parsing** — fix what's fixable (pydantic turns `"36"` into `36`; zod does it only when you opt in with `z.coerce.number()`).

The killer feature on both sides: the schema *is* the source of truth for the static type. `z.infer<typeof Schema>` gives you a TypeScript type; a pydantic `BaseModel` *is* both schema and type. Write the contract once, get runtime checking and compile-time checking from the same definition.

## Why it was needed

Static types can't help with data that doesn't exist at compile time. `JSON.parse()` returns `any`; `json.loads()` returns `dict` — the compiler trusts whatever you claim it is. Before these libraries, people wrote hand-rolled `if "age" in body and isinstance(body["age"], int): ...` pyramids that were verbose, inconsistent, and drifted from the documented API shape.

A schema library centralizes the contract in one declarative place, produces human-readable error responses (which your API should return as `400`s/`422`s), and keeps runtime truth and static types in sync automatically.

## Where it's used in a real project

1. **FastAPI request/response models** — FastAPI is built on pydantic: declare a `BaseModel` as your endpoint's body type and validation + OpenAPI docs come free.
2. **Express/Nest request validation** — `Schema.parse(req.body)` in middleware or a pipe; catch `ZodError` and return a 400 with `error.issues`.
3. **Environment/config validation** — crash fast at startup if `DATABASE_URL` is missing instead of failing on first DB call.
4. **Message queues & third-party webhooks** — validate payloads from Kafka/webhooks where the producer might silently change shape.

## Diagram

```
untrusted input              schema                 trusted output
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│ req.body (any)  │───▶│  z.object({...}) │───▶│ typed Order      │
│ json.loads(...) │    │  BaseModel       │    │ or raises:       │
│ env vars        │    │  .parse()        │    │ ZodError /       │
│ webhook payload │    │  .model_validate │    │ ValidationError  │
└─────────────────┘    └──────────────────┘    └──────────────────┘
         fail path: collect ALL violations → 400/422 error response
```

## Code — explained

Equivalent schemas, side by side:

```python
# ---------- PYTHON: pydantic v2 ----------
from pydantic import BaseModel, Field, field_validator
from typing import Literal

class UserIn(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=0, le=150)
    role: Literal["admin", "member"] = "member"   # default value
    email: str

    @field_validator("email")
    @classmethod
    def must_have_at(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("invalid email")
        return v

# .model_validate -> clean object or ValidationError (collects ALL errors)
user = UserIn.model_validate({"name": "Ada", "age": "36", "email": "a@b.c"})
# age coerced "36" -> 36, role defaults to "member"

# .model_dump -> back to plain dict for JSON responses
user.model_dump()
```

```typescript
// ---------- TYPESCRIPT: zod ----------
import { z } from "zod";

const UserIn = z.object({
  name: z.string().min(1),
  age: z.number().int().min(0).max(150),   // strict: "36" fails unless z.coerce.number()
  role: z.enum(["admin", "member"]).default("member"),
  email: z.string().refine((v) => v.includes("@"), "invalid email"),
  // or simply: z.email() in zod v4
});

type UserIn = z.infer<typeof UserIn>; // static type derived from schema

const user = UserIn.parse({ name: "Ada", age: 36, email: "a@b.c" });
// throws ZodError with ALL issues; role defaults to "member"

// Non-throwing variant — great for request handlers:
const result = UserIn.safeParse(req.body);
if (!result.success) return res.status(400).json(result.error.issues);
```

Three differences worth naming in the interview:

| | pydantic | zod |
|---|---|---|
| Coercion | Eager by default (`"36"` → `36`) | Strict by default; opt in via `z.coerce.*` |
| Static type | The class IS the type | `z.infer<typeof Schema>` derives it |
| Errors | `ValidationError` | `ZodError` (`.issues` array) / `safeParse` |

## Problems

### Easy — Translate a schema
**Problem:** Translate this zod schema to pydantic.

```typescript
const Product = z.object({ sku: z.string(), price: z.number().positive() });
```

**Try this input:** `{"sku": "A1", "price": 9.99}` and `{"sku": "A1", "price": -1}`.
**Expected output:** first passes; second fails with a "greater than 0" error.
**Solution:**

```python
from pydantic import BaseModel, PositiveFloat

class Product(BaseModel):
    sku: str
    price: PositiveFloat
```

**Logic explained:**
1. `z.object` ↔ `BaseModel` subclass — fields become class attributes with annotations.
2. `z.number().positive()` ↔ `PositiveFloat` (a constrained type pydantic ships with).
3. Both reject `-1`; pydantic's error is a `ValidationError`, zod's a `ZodError`.

### Medium — Partial update endpoint
**Problem:** Build a PATCH handler schema where every field is optional but at least one must be present, in both languages. Input: `{"name": "New"}` OK, `{}` must fail.

**Try this input:** `{"name": "New"}`, `{}`, `{"name": 5}`.
**Expected output:** pass, fail ("at least one field"), fail ("name must be string").
**Solution:**

```typescript
const Patch = z
  .object({ name: z.string().min(1), age: z.number().int().min(0) })
  .partial()
  .refine((o) => Object.keys(o).length > 0, "at least one field required");
```

```python
from pydantic import BaseModel, Field, model_validator

class Patch(BaseModel):
    name: str | None = Field(default=None, min_length=1)
    age: int | None = Field(default=None, ge=0)

    @model_validator(mode="after")
    def at_least_one(self):
        if self.name is None and self.age is None:
            raise ValueError("at least one field required")
        return self
```

**Logic explained:**
1. `.partial()` / `| None = None` makes each field optional.
2. "At least one" is a *cross-field* rule — zod uses `.refine` on the object, pydantic uses a `mode="after"` model validator that sees the whole instance.
3. Note the asymmetry: in pydantic a provided-but-invalid `name: 5` fails at the field level before the model validator runs.

### Hard — Discriminated union payloads
**Problem:** A webhook sends events shaped `{type: "created", id: str}` or `{type: "deleted", id: str, reason: str}`. Model it so invalid combinations are rejected, in both languages, and show how to dispatch on the parsed type.

**Try this input:** `{"type":"created","id":"1"}`, `{"type":"deleted","id":"1"}`, `{"type":"deleted","id":"1","reason":"spam"}`.
**Expected output:** pass, fail (missing `reason`), pass.
**Solution:**

```typescript
const Event = z.discriminatedUnion("type", [
  z.object({ type: z.literal("created"), id: z.string() }),
  z.object({ type: z.literal("deleted"), id: z.string(), reason: z.string() }),
]);
type Event = z.infer<typeof Event>;

function handle(e: Event) {
  if (e.type === "deleted") console.log(e.reason); // TS narrows on e.type
}
```

```python
from typing import Annotated, Literal, Union
from pydantic import BaseModel, Field

class Created(BaseModel):
    type: Literal["created"]
    id: str

class Deleted(BaseModel):
    type: Literal["deleted"]
    id: str
    reason: str

Event = Annotated[Union[Created, Deleted], Field(discriminator="type")]

def handle(e: Event) -> None:
    if isinstance(e, Deleted):
        print(e.reason)
```

**Logic explained:**
1. The `type` field is the *discriminator* — it selects which variant schema applies.
2. zod's `discriminatedUnion` and pydantic's `Field(discriminator=...)` both use it for fast, precise matching (and better errors than a plain union).
3. After parsing, `e.type === "deleted"` narrows the TS type; in Python you narrow with `isinstance`.
4. This is THE answer for polymorphic payloads — much better than "all fields optional."

## The 30-second interview answer

"They're the same idea in two ecosystems: declarative runtime schemas that turn untrusted data into typed objects or produce detailed errors. In Python it's pydantic — a `BaseModel` subclass where the class is both schema and type; FastAPI is built on it. In TypeScript it's zod — `z.object({...})` schemas, and `z.infer` derives the static type from the schema so the two can't drift. The main differences: pydantic coerces eagerly (`"36"` becomes `36`) while zod is strict unless you opt into `z.coerce`; and zod offers a non-throwing `safeParse`. I use them at every trust boundary — request bodies, env vars, webhook payloads — because static types alone can't check data that arrives at runtime."

## Follow-up trap

"What happens to validation errors — do they reach the client?" — Strong answer: catch them centrally and map to a structured 400/422 response (`error.issues` in zod, `e.errors()` in pydantic — FastAPI does this automatically). Never leak raw internals; return field-level messages the caller can act on. Bonus points: mention that `safeParse`/`model_validate` inside a try lets you log-and-reject rather than crash.
