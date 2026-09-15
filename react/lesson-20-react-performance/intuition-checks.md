# Lesson 20 — Intuition Checks

## Check 01: React.memo
What does React.memo do?
<details><summary>Answer</summary>
Memoizes a component — skips re-render if props are the same (shallow compare). Use for components that re-render often with same props.
</details>

## Check 02: When does React re-render?
<details><summary>Answer</summary>
When: state changes, parent re-renders (children re-render), context value changes. NOT when: props are same AND wrapped in React.memo.
</details>

## Check 03: Virtualization
```jsx
import { FixedSizeList } from "react-window";
<FixedSizeList height={600} itemCount={10000} itemSize={50}>
```
<details><summary>Answer</summary>
Only renders visible items + buffer. Handles 10,000+ items smoothly. Essential for large lists.
</details>

## Check 04: Code splitting
```jsx
const Lazy = React.lazy(() => import("./Heavy"));
<Suspense fallback={<Spinner />}><Lazy /></Suspense>
```
<details><summary>Answer</summary>
Loads component on demand (separate chunk). Reduces initial bundle size. Use for routes, modals, heavy components.
</details>

## Check 05: useDeferredValue
```jsx
const deferredQuery = useDeferredValue(query);
```
<details><summary>Answer</summary>
Defers updating a value — lets urgent updates (typing) happen first, expensive computation (filtering) later. Keeps UI responsive.
</details>
