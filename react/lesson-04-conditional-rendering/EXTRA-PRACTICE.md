# lesson-04-conditional-rendering — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: && rendering
```jsx
{true && <div>A</div>}
{false && <div>B</div>}
```
<details><summary>Answer</summary>
Renders `<div>A</div>`. The second renders nothing (false is ignored by React). But `0 && ...` renders `0`!
</details>

## Check 02: Ternary
```jsx
{status === "loading" ? <Spinner /> : <Content />}
```
<details><summary>Answer</summary>
If/else in JSX. Renders Spinner if loading, Content otherwise. Most common conditional pattern.
</details>

## Check 03: Early return
```jsx
function Component({ data }) {
  if (!data) return <Loading />;
  return <div>{data.name}</div>;
}
```
<details><summary>Answer</summary>
Return early for guard clauses. Cleaner than nested ternaries. Can't use inside JSX — must be before return.
</details>

## Check 04: IIFE
```jsx
{(() => {
  if (x === 1) return <A />;
  if (x === 2) return <B />;
  return <C />;
})()}
```
<details><summary>Answer</summary>
Immediately Invoked Function Expression — allows if/else in JSX. But it's ugly. Prefer extracting to a variable or sub-component.
</details>

## Check 05: Enum object
```jsx
const components = { loading: Spinner, error: Error, success: Content };
const Component = components[status];
return <Component />;
```
<details><summary>Answer</summary>
Map status to component. Clean for multiple mutually exclusive states.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): && with 0
```jsx
{count && <div>{count}</div>}
```
<details><summary>Answer</summary>
**Bug:** When count is 0, `0 && <div>` renders `0` (falsy but rendered).
**Fix:** `{count > 0 && <div>{count}</div>}` or `{Boolean(count) && ...}`.
</details>

## Debug 02 (Medium): Ternary Returning undefined
```jsx
{isLoggedIn ? <Dashboard /> : null}
```
<details><summary>Answer</summary>
Works but verbose. Can use `&&`: `{isLoggedIn && <Dashboard />}`.
</details>

## Debug 03 (Hard): Condition in Wrong Place
```jsx
function App() {
  if (loading) return <Spinner />;
  return <div>Data: {data}</div>;
  if (error) return <Error />;
}
```
<details><summary>Answer</summary>
**Bug:** `if (error)` is unreachable — after return statement.
**Fix:** Move error check before the data return.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: && with falsy values
```jsx
// WRONG — renders 0
{count && <div>{count}</div>}
// CORRECT
{count > 0 && <div>{count}</div>}
```

## Mistake 02: Nested ternaries
```jsx
// HARD TO READ
{a ? x ? "A" : "B" : "C"}
// BETTER
{a ? (x ? "A" : "B") : "C"}
// BEST — extract to variable or component
```

## Mistake 03: Unreachable code
```jsx
// WRONG — error check after return
if (loading) return <Spinner />;
return <Data />;
if (error) return <Error />; // never reached
```

## Mistake 04: Condition in render body
```jsx
// Can't use if inside JSX {}
// Use ternary or extract
```

## Mistake 05: Not extracting complex conditions
```jsx
// WRONG — complex inline
{user && user.profile && user.profile.name ? user.profile.name : "Guest"}
// BETTER — extract variable
const name = user?.profile?.name ?? "Guest";
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Ternary for Simple Show/Hide
### Before
```jsx
{isVisible ? <div>Content</div> : null}
```
### After
```jsx
{isVisible && <div>Content</div>}
```

## Refactor 02 (Medium): Nested Ternaries
### Before
```jsx
{status === "loading" ? <Spinner /> : status === "error" ? <Error /> : <Data />}
```
### After
```jsx
const components = { loading: <Spinner />, error: <Error /> };
{components[status] || <Data />}
```

## Refactor 03 (Hard): If/Else in JSX
### Before
```jsx
function renderContent() {
  if (loading) return <Spinner />;
  if (error) return <Error />;
  return <Data />;
}
return <div>{renderContent()}</div>;
```
### After
```jsx
return <div>
  {loading && <Spinner />}
  {error && <Error />}
  {!loading && !error && <Data />}
</div>;
```

---

## Approach Comparison — different ways to solve it

## Problem: Show Loading or Content

### Approach 1: Ternary
```jsx
{isLoading ? <Spinner /> : <Content data={data} />}
```

### Approach 2: Early return
```jsx
if (isLoading) return <Spinner />;
return <Content data={data} />;
```

**Winner:** Approach 2 for simple cases. Approach 1 when both need to render in same position.

---

## Problem: Multiple States

### Approach 1: Nested ternaries
```jsx
{loading ? <Spinner /> : error ? <Error /> : <Content />}
```

### Approach 2: Enum
```jsx
const views = { loading: Spinner, error: Error, success: Content };
const View = views[status];
return <View />;
```

**Winner:** Approach 2 — cleaner for 3+ states.
