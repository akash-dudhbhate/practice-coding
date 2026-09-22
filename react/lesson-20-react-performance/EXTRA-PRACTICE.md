# lesson-20-react-performance — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

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

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: React.memo Without Stable Props
```jsx
const MemoChild = React.memo(Child);
<MemoChild onClick={() => handleClick()} style={{ color: "red" }} />
```
<details><summary>Answer</summary>
**Bug:** New function and object every render → memo is useless (props always "change").
**Fix:** `useCallback` for onClick, `useMemo` for style.
</details>

## Debug 02 (Medium): Large Bundle
```jsx
import _ from "lodash"; // imports entire lodash
```
<details><summary>Answer</summary>
**Bug:** Imports entire lodash (~70KB). Most of it unused.
**Fix:** `import debounce from "lodash/debounce";` — imports only what's needed.
</details>

## Debug 03 (Hard): Unnecessary Re-renders
```jsx
function Parent() {
  const [count, setCount] = useState(0);
  return <div><ExpensiveChild /><button onClick={() => setCount(c => c + 1)}>{count}</button></div>;
}
```
<details><summary>Answer</summary>
**Bug:** ExpensiveChild re-renders when count changes (Parent re-renders).
**Fix:** Wrap ExpensiveChild in `React.memo`, or move count state to the button component.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Premature optimization
```jsx
// Don't wrap everything in React.memo
// Measure first, optimize what's actually slow
```

## Mistake 02: memo without stable props
```jsx
// WRONG — new props every render
<MemoChild onClick={() => {}} style={{}} />
// CORRECT
const onClick = useCallback(() => {}, []);
const style = useMemo(() => ({}), []);
<MemoChild onClick={onClick} style={style} />
```

## Mistake 03: Importing entire libraries
```jsx
// WRONG — 70KB
import _ from "lodash";
// CORRECT — tree-shakeable
import debounce from "lodash/debounce";
```

## Mistake 04: Not code splitting
```jsx
// WRONG — one huge bundle
import Heavy from "./Heavy";
// CORRECT — load on demand
const Heavy = React.lazy(() => import("./Heavy"));
```

## Mistake 05: Rendering huge lists
```jsx
// WRONG — renders all 10,000 items
{items.map(item => <Row key={item.id} />)}
// CORRECT — virtualize
<FixedSizeList itemCount={items.length}>...</FixedSizeList>
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): No Memo on Expensive List
### Before
```jsx
function List({ items }) {
  const sorted = items.sort((a, b) => a.name.localeCompare(b.name));
  return sorted.map(i => <Item key={i.id} item={i} />);
}
```
### After
```jsx
const sorted = useMemo(() => [...items].sort((a, b) => a.name.localeCompare(b.name)), [items]);
```

## Refactor 02 (Medium): No React.memo
### Before
```jsx
function Item({ item }) { return <div>{item.name}</div>; }
// re-renders even if item prop same
```
### After
```jsx
const Item = React.memo(({ item }) => <div>{item.name}</div>);
```

## Refactor 03 (Hard: Inline Object Props
### Before
```jsx
<Child style={{ color: 'red' }} config={{ timeout: 1000 }} />
```
### After
```jsx
const style = useMemo(() => ({ color: 'red' }), []);
const config = useMemo(() => ({ timeout: 1000 }), []);
<Child style={style} config={config} />
```

---

## Approach Comparison — different ways to solve it

## Problem: Prevent Unnecessary Re-renders

### Approach 1: React.memo
```jsx
const MemoChild = React.memo(Child);
```

### Approach 2: Move state down
```jsx
// Instead of state in parent, put it in a small component
function Button() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(c => c + 1)}>{count}</button>;
}
// Parent doesn't re-render when count changes
```

**Winner:** Approach 2 — often simpler than memo. Only memo when you can't restructure.

---

## Problem: Large List

### Approach 1: Render all
```jsx
{items.map(item => <Row key={item.id} />)}
```
**Cons:** Slow for 1000+ items.

### Approach 2: Pagination
```jsx
{items.slice(0, page * 20).map(...)}
```

### Approach 3: Virtualization
```jsx
<FixedSizeList itemCount={items.length} itemSize={50}>...</FixedSizeList>
```

**Winner:** Approach 3 for 1000+ items. Approach 2 for moderate lists.
