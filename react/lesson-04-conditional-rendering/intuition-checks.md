# Lesson 04 — Intuition Checks

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
