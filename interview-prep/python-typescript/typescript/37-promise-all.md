# 37 — Typing `Promise.all` — `Promise<[User, Post[]]>` tuple results

> **Interview question:** "How is `Promise.all` typed, and why does awaiting several different promises give you a tuple like `[User, Post[]]` instead of `any[]`?"
> **What the interviewer is really testing:** Whether you understand tuple inference vs array inference — and that `Promise.all` preserves each slot's type.

## Theory — what it is

A `Promise<T>` is an object representing "a `T` that will exist later." `Promise<User>` resolves to a `User`; `Promise<Post[]>` resolves to an array of `Post`s. `Promise.all` takes a group of promises and returns a single promise that resolves once *every* input resolves — the results arrive in an array in the same order you passed them.

The typing trick is that `Promise.all` has two "personalities" depending on what you pass:

1. **Tuple literal** — `[p1, p2]` written inline. TypeScript uses a generic signature built on *variadic tuple types* (a type that maps over each position of a tuple) and infers `Promise<[User, Post[]]>`. Slot 0 is a `User`, slot 1 is a `Post[]`. Destructuring `const [user, posts] = await ...` gives each variable its correct type.
2. **Regular array** — `Promise<User>[]`. TypeScript falls back to the array overload and infers `Promise<User[]>`. Every element is the same type — fine for `ids.map(fetchUser)`, wrong when the promises are heterogeneous.

A **tuple** is a fixed-length array where each position has its own declared type — `[string, number]` means "exactly two elements: a string, then a number." Losing the tuple (getting `(User | Post[])[]` instead) means `user.name` no longer type-checks, because element 0 might be a `Post[]`.

If the array is built separately in a variable, TypeScript widens it to `Promise<X>[]` and you lose the tuple. Adding `as const` tells the compiler "treat this as a readonly tuple, not a growing array," and `Promise.all` accepts readonly tuples.

## Why it was needed

Without tuple inference, `Promise.all` results collapse to `any[]` or a union array. Then `const [user, posts] = await Promise.all([getUser(), getPosts()])` types `user` as `User | Post[]` — every property access needs a manual narrow, defeating the point of types. In non-strict code it silently degrades to `any`, and a typo like `user.emial` ships to production.

It also matters for correctness: `Promise.all` rejects as soon as *any* input rejects — the first error wins and the rest are abandoned. If you need "wait for all and keep partial results," you want `Promise.allSettled`, which is typed differently: each slot is a union `{ status: "fulfilled"; value: T } | { status: "rejected"; reason: any }`.

## Where it's used in a real project

- **Parallel page loads:** fetch user + posts + settings in one `await` on a dashboard.
- **Batch API calls:** `Promise.all(ids.map(fetchUser))` — the homogeneous-array case, `Promise<User[]>`.
- **Startup checks:** await DB ping + cache ping + config load together instead of serially.
- **React/SSR data fetching:** loaders that resolve multiple resources before rendering.

## Diagram

```
getUser()  ── Promise<User> ────┐
                                ├── Promise.all ──► Promise<[User, Post[]]>
getPosts() ── Promise<Post[]> ──┘                          │
                                               await ──► [user, posts]
                                               slot 0: User   slot 1: Post[]

passed as [p1, p2] literal  ──► tuple type   Promise<[A, B]>
passed as Promise<T>[]      ──► array type   Promise<T[]>
any input rejects           ──► whole Promise.all rejects (first error wins)
```

## Code — explained

```typescript
interface User { id: number; name: string }
interface Post { id: number; title: string }

declare function getUser(id: number): Promise<User>;
declare function getPosts(userId: number): Promise<Post[]>;

async function loadDashboard(userId: number) {
  // tuple literal -> Promise<[User, Post[]]>
  const [user, posts] = await Promise.all([
    getUser(userId),
    getPosts(userId),
  ]);
  console.log(user.name);      // string — slot 0 keeps its type
  console.log(posts.length);   // number — slot 1 keeps its type

  // homogeneous array -> Promise<User[]>
  const friends = await Promise.all([1, 2, 3].map(getUser));
  // friends: User[] — every element is User, fine here

  // built in a variable? use `as const` to keep the tuple
  const work = [getUser(1), getPosts(1)] as const;
  const [u2, p2] = await Promise.all(work);   // [User, Post[]]
}
```

1. `interface` declares object shapes; `declare function` says "this exists at runtime" so we can specify its return type.
2. `Promise.all([a, b])` on a tuple literal matches the variadic-tuple signature; the result is `Promise<[User, Post[]]>`.
3. Array destructuring `const [user, posts]` assigns slot 0 → `user: User`, slot 1 → `posts: Post[]`.
4. `[1, 2, 3].map(getUser)` produces `Promise<User>[]` — the array overload — so `friends` is `User[]`.
5. `as const` freezes the array into a `readonly [Promise<User>, Promise<Post[]>]` tuple, so `Promise.all` still returns a tuple.

## Problems

### Easy — parallel fetch, typed destructure
**Problem:** Given `getUser` and `getPosts` (declared above), fetch both for user 7 and print `"<name> has <n> posts"`.
**Try this input:** user resolves to `{ id: 7, name: "Ada" }`, posts resolve to `[{id:1,title:"x"},{id:2,title:"y"}]`
**Expected output:** `Ada has 2 posts`
**Solution:**
```typescript
async function main() {
  const [user, posts] = await Promise.all([getUser(7), getPosts(7)]);
  console.log(`${user.name} has ${posts.length} posts`);
}
main();
// Ada has 2 posts
```
**Logic explained:**
1. `Promise.all` on a tuple literal returns `Promise<[User, Post[]]>`.
2. Destructuring types `user: User` and `posts: Post[]` — `user.name` and `posts.length` both compile with no casts.
3. Both requests run concurrently; total wait ≈ the slower of the two, not the sum.

### Medium — allSettled result typing
**Problem:** Fetch users 1, 2, 3 with `Promise.allSettled`; print each user's name, or `"failed"` if that request rejected. `allSettled` never rejects — it waits for everything and reports each outcome.
**Try this input:** users 1 and 3 resolve (`"Ana"`, `"Cid"`); user 2 rejects.
**Expected output:**
```
Ana
failed
Cid
```
**Solution:**
```typescript
const results = await Promise.allSettled([1, 2, 3].map(getUser));
for (const r of results) {
  if (r.status === "fulfilled") console.log(r.value.name);
  else console.log("failed");
}
// Ana
// failed
// Cid
```
**Logic explained:**
1. `Promise<User>[]` in → `Promise<PromiseSettledResult<User>[]>` out.
2. `PromiseSettledResult<User>` is the union `{ status:"fulfilled"; value: User } | { status:"rejected"; reason: any }`.
3. Checking `r.status === "fulfilled"` narrows the union, so `r.value.name` is safe. In the `else` branch you could read `r.reason` (typed `any` in the standard lib — treat it as `unknown` and narrow before using).

### Hard — implement your own typed `all`
**Problem:** Write `myAll` so `myAll([getUser(1), getPosts(1)])` returns `Promise<[User, Post[]]>` — one type parameter must capture the whole tuple and unwrap each `Promise` inside it.
**Try this input:** `await myAll([getUser(1), getPosts(1)])`
**Expected output:** the value is typed `[User, Post[]]` — `r[0].name` and `r[1].length` compile; `r[0].length` is a compile error.
**Solution:**
```typescript
type AwaitedAll<T extends readonly unknown[]> = {
  -readonly [K in keyof T]: Awaited<T[K]>;
};

async function myAll<T extends readonly unknown[]>(
  promises: T,
): Promise<AwaitedAll<T>> {
  return Promise.all(promises) as Promise<AwaitedAll<T>>;
}

const r = await myAll([getUser(1), getPosts(1)]);
//    r: [User, Post[]]
```
**Logic explained:**
1. `T extends readonly unknown[]` lets `T` capture the whole tuple `[Promise<User>, Promise<Post[]>]` in one parameter.
2. A *mapped type* `{ [K in keyof T]: ... }` over a tuple/array produces a tuple/array — it maps each index individually instead of flattening to one element type.
3. `Awaited<T[K]>` unwraps `Promise<X>` → `X` — the built-in "one level of await" utility type.
4. `-readonly` strips `readonly` so callers can pass `as const` arrays and still get a mutable tuple back.
5. The `as` cast inside is honest bookkeeping: `Promise.all` already returns exactly this at runtime; we re-declared the type to learn how the real signature works.

## The 30-second interview answer

"`Promise.all` is generic over the input tuple — TypeScript maps each position through `Awaited`, so `[Promise<User>, Promise<Post[]>]` comes out as `Promise<[User, Post[]]>` and destructuring gives each variable its own type. That tuple inference only kicks in for a tuple literal or an `as const` array; a `Promise<T>[]` array gives `Promise<T[]>`, which is right for homogeneous batches like `ids.map(fetch)`. It fails fast — the first rejection rejects the whole call — so when I need partial results I use `allSettled`, whose slots are a fulfilled/rejected union I narrow on `status`."

## Follow-up trap

**"How do you keep tuple types when the promise array is built in a variable first?"** Two answers: add `as const` so it becomes `readonly [Promise<User>, Promise<Post[]>]` (`Promise.all` accepts readonly tuples), or inline the array in the call. Bonus trap: *"What if one promise can legitimately resolve to two different shapes?"* — that's not `Promise.all`'s problem; model it as `Promise<A | B>` at the source and narrow after awaiting. And *"why not always use allSettled?"* — because it swallows rejections into data; use it only when partial failure is acceptable.
