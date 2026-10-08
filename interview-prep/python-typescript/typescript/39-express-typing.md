# 39 — Typing an Express handler — `Request<Params, ResBody, ReqBody, ReqQuery>`

> **Interview question:** "How do you type a route handler in Express (or Fastify) so `req.params`, `req.body`, and `req.query` aren't `any`?"
> **What the interviewer is really testing:** Whether you know Express's `Request` takes four generics in a weird order — **Params, ResponseBody, RequestBody, Query** — and that typed handlers are how you stop `req.body.email` from being a typo away from a runtime `undefined`.

## Theory — what it is

Express's core types are generic interfaces. The signature you must memorize:

```typescript
Request<P, ResBody, ReqBody, ReqQuery>
```

Mapped to what they control inside the handler:

| Generic | Fills | Default |
|---|---|---|
| `P` | `req.params` | `ParamsDictionary` (`{ [k: string]: string }`) |
| `ResBody` | what `res.send()` / `res.json()` accept | `any` |
| `ReqBody` | `req.body` | `any` |
| `ReqQuery` | `req.query` | `ParsedQs` (`{ [k: string]: ... }`) |

**The trap:** `ResBody` (response) sits at position **2**, *before* `ReqBody` (request) at position **3**. People constantly write `Request<Params, Body>` expecting body typing and end up typing the *response*. Mnemonic: **P**ath, **Res**ponse, **Req**uest body, **Q**uery — "Params-Res-Req-Query."

There's also a matching handler type, `RequestHandler<P, ResBody, ReqBody, ReqQuery>` — same generics, same order — for typing a standalone function instead of an inline callback.

**Fastify** does it differently: you pass *one* object generic to the route method, keyed by which part you're typing:

```typescript
app.post<{ Body: CreateUserBody; Params: { id: string } }>("/users/:id", handler);
```

Inside, `request.body` is `CreateUserBody` and `request.params.id` is `string` — no positional generics to mis-order, which is why many teams prefer it.

## Why it was needed

Without generics, `req.body` is `any` (Express can't know what a client will POST), `req.params` is `ParamsDictionary` (every param a `string`, which is true — URLs are strings — but you can't see *which* keys exist), and `req.query` is a grab-bag. So `req.body.emial` compiles fine and explodes at runtime; `parseInt(req.params.id)` works, but nobody stops you reading `req.params.userId` on a route declared `/users/:id`.

Typed generics fix three things at once: **autocomplete** (`req.body.` shows real fields), **typo-checking** (`emial` is a compile error), and **response contracts** (`res.json()` rejects shapes that aren't `ResBody`, so a handler can't accidentally leak `{ passwordHash }`). It also forces honesty about the URL: `req.params.id` is still a `string` — the type reflects that path params are always strings, never numbers.

## Where it's used in a real project

- **CRUD routes:** `app.get("/users/:id", (req: Request<{ id: string }>, res) => ...)`.
- **POST/PUT handlers:** `RequestHandler<{}, User, CreateUserBody>` — read `req.body.name` with full autocomplete.
- **Paginated list endpoints:** `Request<{}, User[], {}, { page?: string; limit?: string }>` — query params are strings, so `req.query.page` needs `parseInt`.
- **Middleware chains:** `RequestHandler` lets a shared `validateBody` middleware be typed once and reused.
- **Fastify services:** route-level `RouteShorthandOptions` generics or JSON Schema that *derives* the types.

## Diagram

```
app.post("/users/:id/orders", handler)
                  │              │
                  │              v
                  │   Request<{ id: string },          <- P:    req.params.id: string
                  │          Order,                     <- ResBody: res.json(order)
                  │          CreateOrderBody,           <- ReqBody: req.body.item
                  │          { rush?: string }>         <- ReqQuery: req.query.rush
                  v
   URL parts come in as STRINGS — always:
   /users/42/orders?rush=true
        └─> req.params.id === "42"   (string! parseInt if you need a number)
        └─> req.query.rush === "true" (string!)

Type flow inside the handler:
   req.params  <- P
   req.body    <- ReqBody        res.send / res.json <- must match ResBody
   req.query   <- ReqQuery
```

## Code — explained

```typescript
import { Request, Response, RequestHandler } from "express";

interface CreateUserBody {
  name: string;
  email: string;
  age?: number;
}

// 1. Inline handler — annotate req/res yourself
const createUser = (
  req: Request<{}, { id: number }, CreateUserBody>,
  res: Response<{ id: number }>
) => {
  const name: string = req.body.name;      // typed — autocomplete works
  const email = req.body.email;            // string
  // req.body.emial;                       // ❌ compile error: no such field
  res.status(201).json({ id: 42 });        // matches ResBody { id: number }
  // res.json({ id: "x" });               // ❌ compile error: wrong ResBody
};

// 2. Params — positional generic #1
const getUser: RequestHandler<{ id: string }, { name: string }> = (req, res) => {
  const id: string = req.params.id;        // string — path params always are
  res.json({ name: `user-${id}` });
};

// 3. Query — positional generic #4 (skip with {} for body)
type ListQuery = { page?: string; limit?: string };
const listUsers: RequestHandler<{}, { names: string[] }, {}, ListQuery> =
  (req, res) => {
    const page = parseInt(req.query.page ?? "1", 10);  // string | undefined -> number
    res.json({ names: [], });
  };

// 4. Fastify equivalent — one object generic, self-documenting keys
// fastify.post<{ Params: { id: string }; Body: CreateUserBody }>(
//   "/users/:id", async (request, reply) => {
//     request.params.id;   // string
//     request.body.email;  // string
//   });
```

1. Positional generics mean `{}` placeholders: to type only the body you still write `Request<{}, {}, CreateUserBody>` — you can't skip positions.
2. `res.json()` is checked against `ResBody` — that's how the compiler enforces "this endpoint returns `{ id: number }`."
3. `req.params.id` is `string`, not `number`. If your type says `id: number` you're lying — Express hands you the raw URL segment. Parse it: `parseInt(req.params.id, 10)`.
4. `req.query` values are `string | undefined` (or arrays) — never trust them as numbers without parsing, and mark optional ones `?` in the type.
5. `RequestHandler<...>` is the same four generics — use it for extracted handlers; for inline handlers annotate `req: Request<...>` directly.
6. Fastify swaps positional generics for a named object (`{ Params, Body, Querystring, Reply }`) — same idea, friendlier ergonomics.

## Problems

### Easy — type a GET handler's params
**Problem:** Route `GET /products/:sku` returns `{ sku: string; price: number }`. Write the handler so `req.params.sku` is `string` and `res.json` rejects wrong shapes.
**Try this input:** request `GET /products/A1`
**Expected output:** `{"sku":"A1","price":9}` — and `res.json({ sku: "A1" })` (missing `price`) is a compile error.
**Solution:**
```typescript
import { RequestHandler } from "express";

interface Product {
  sku: string;
  price: number;
}

const getProduct: RequestHandler<{ sku: string }, Product> = (req, res) => {
  const sku: string = req.params.sku;
  res.json({ sku, price: 9 });
  // res.json({ sku });               // ❌ missing `price` in ResBody
  // res.json({ sku, price: "9" });   // ❌ price must be number
};
```
**Logic explained:**
1. `P = { sku: string }` gives `req.params.sku` type `string`.
2. `ResBody = Product` makes `res.json(...)` accept only `Product` shapes.
3. Positional order means `Product` lands on `ResBody` (slot 2) — the response, not the request body.

### Medium — a typed POST with body and query
**Problem:** Route `POST /users/:id/notify?channel=email` takes body `{ message: string }`, query `{ channel?: "email" | "sms" }`, returns `{ sent: boolean }`. Type all four slots as a `RequestHandler`.
**Try this input:** `req.body.message = "hi"`, `req.query.channel = "sms"`
**Expected output:** `sent=true via sms to user 7`
**Solution:**
```typescript
import { RequestHandler } from "express";

interface NotifyBody { message: string }
interface NotifyQuery { channel?: "email" | "sms" }
interface NotifyRes { sent: boolean }

const notify: RequestHandler<
  { id: string },   // P      -> req.params.id
  NotifyRes,        // ResBody-> res.json()
  NotifyBody,       // ReqBody-> req.body.message
  NotifyQuery       // ReqQuery-> req.query.channel
> = (req, res) => {
  const channel = req.query.channel ?? "email";   // "email" | "sms"
  const msg: string = req.body.message;
  console.log(`sent=true via ${channel} to user ${req.params.id} — "${msg}"`);
  res.json({ sent: true });
};
```
**Logic explained:**
1. All four generics used in order: params, response, body, query — the order is the whole quiz.
2. `channel` is optional in the query type, so `req.query.channel` is `"email" | "sms" | undefined` — `?? "email"` handles absence.
3. `res.json({ sent: true })` is checked against `NotifyRes`; `res.json({ sent: "yes" })` would fail to compile.

### Hard — a reusable typed middleware factory
**Problem:** Write `parseId<P>()` — Express middleware that converts `req.params.id` (a string) to a number, 400s if it's not numeric, and stores the number in `res.locals.userId` so downstream handlers read it typed.
**Try this input:** `GET /users/42/profile` then `GET /users/abc/profile`
**Expected output:** `42` → downstream sees `userId = 42` (number); `abc` → `400 invalid id`.
**Solution:**
```typescript
import { RequestHandler } from "express";

// Middleware: validate + transform at the boundary
const parseUserId: RequestHandler<{ id: string }> = (req, res, next) => {
  const n = parseInt(req.params.id, 10);
  if (Number.isNaN(n)) {
    res.status(400).json({ error: "invalid id" });
    return;                       // don't call next — stop the chain
  }
  res.locals.userId = n;          // stash parsed value for later handlers
  next();
};

// Downstream handler: params still string, locals carry the number
const profile: RequestHandler<{ id: string }> = (req, res) => {
  const userId: number = res.locals.userId;   // number, no re-parsing
  res.json({ userId, name: `user-${userId}` });
};

// app.get("/users/:id/profile", parseUserId, profile);
```
**Logic explained:**
1. `RequestHandler<{ id: string }>` types `req.params.id` — the middleware sees the same generic contract as the route.
2. `res.locals` is Express's per-request scratch space (`Record<string, any>` by default — a fifth generic `LocalsObj` can type it strictly: `RequestHandler<P, ResBody, ReqBody, ReqQuery, { userId: number }>`).
3. The pattern: **parse at the boundary once** (middleware), keep `string` params honest, hand downstream code a real `number` — this is the production version of "params are always strings."
4. `return` after `res.status(400)...` matters: Express won't stop the chain for you.

## The 30-second interview answer

"Express's `Request` is generic over four things in this order: **Params, ResponseBody, RequestBody, Query** — `Request<{ id: string }, User, CreateUserBody, { page?: string }>`. The response body at position 2 is the classic gotcha; I remember it as 'params, response, request body, query.' With those filled in, `req.params.id` is `string` — always a string, URLs don't have numbers — `req.body.email` autocompletes, and `res.json()` rejects anything that isn't `ResBody`, so the endpoint's contract is enforced at compile time. For extracted handlers I use `RequestHandler` with the same four generics. In Fastify it's nicer: one object generic like `{ Params, Body, Querystring }` on the route method, no positional ordering to get wrong. And since params/query arrive as strings, the real-world pattern is middleware that parses and validates once, then stashes typed values on `res.locals`."

## Follow-up trap

**"You wrote `Request<{ id: number }>` for `/users/:id` — what's wrong?"** Path params are always `string`s — Express gives you the raw URL segment, so `id: number` is a lie that will bite when `req.params.id + 1` produces `"421"`. Type it `string`, parse to number, validate. Second trap: **"Why is `req.body` still `any` even though you annotated the route?"** Because annotating `app.post("/x", handler)` doesn't type `handler` — Express's `post` accepts loosely-typed handlers. The generic goes on the *handler* (`RequestHandler<...>` or `req: Request<...>`), not the route registration. Third: the middleware-shared `res.locals` typing needs the fifth generic (`LocalsObj`) — most people don't know it exists.
