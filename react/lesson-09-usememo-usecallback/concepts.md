# Lesson 09 — Concepts Explained (useMemo & useCallback)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## useMemo

**What:** `useMemo` caches (memoizes) a computed value so it's not recalculated on every render. Only recalculates when dependencies change.

```jsx
import { useMemo, useState } from 'react';

function ProductList({ products, searchTerm }) {
    // WITHOUT useMemo: filters on EVERY render (even if searchTerm didn't change)
    const filtered = products.filter(p => p.name.includes(searchTerm));

    // WITH useMemo: only filters when products or searchTerm change
    const filtered = useMemo(() => {
        return products.filter(p => p.name.includes(searchTerm));
    }, [products, searchTerm]);

    return <div>{filtered.map(p => <p key={p.id}>{p.name}</p>)}</div>;
}
```

**Why it exists:** Without `useMemo`, expensive calculations run on every render → slow. If sorting 10,000 items, you don't want to re-sort every time an unrelated state changes. `useMemo` caches the result → only recalculates when inputs change.

**Where it's used:** Expensive calculations (sorting, filtering large lists), complex object creation, preventing unnecessary re-renders of child components.

**What goes wrong without it:**
- Overusing `useMemo` for cheap calculations → the memoization overhead (storing deps, comparing) is more expensive than the calculation itself. Only memoize expensive operations.
- Forgetting a dependency → stale result (uses old value). Always include all values used inside the memo.
- `useMemo` doesn't guarantee the cached value is kept — React may discard it to free memory. Don't rely on it for side effects.

---

## useCallback

**What:** `useCallback` caches a function reference so it doesn't change on every render. Only creates a new function when dependencies change.

```jsx
import { useCallback, useState } from 'react';

function Parent() {
    const [count, setCount] = useState(0);
    const [text, setText] = useState("");

    // WITHOUT useCallback: new function every render → Child re-renders
    const handleClick = () => console.log("Clicked", count);

    // WITH useCallback: same function reference unless count changes
    const handleClick = useCallback(() => {
        console.log("Clicked", count);
    }, [count]);

    return (
        <>
            <input value={text} onChange={e => setText(e.target.value)} />
            <Child onClick={handleClick} />
        </>
    );
}

const Child = React.memo(({ onClick }) => {
    console.log("Child rendered");
    return <button onClick={onClick}>Click me</button>;
});
```

**Why it exists:** Without `useCallback`, every render creates a new function → passing it to a memoized child (`React.memo`) → the child sees a "new" prop → re-renders anyway → memoization is useless. `useCallback` keeps the function reference stable → child doesn't re-render.

**Where it's used:** Passing callbacks to memoized children, event handlers in dependency arrays of `useEffect`, stable references for custom hooks.

**What goes wrong without it:**
- `useCallback` without `React.memo` on the child → useless. The child re-renders anyway because parent re-renders. Both must be used together.
- Forgetting a dependency → stale closure (function uses old state). Always include all values used inside the callback.
- Overusing `useCallback` → wrapping every function → overhead. Only use when passing to memoized children or in effect deps.

---

## useMemo vs useCallback

**What:**
- `useMemo` → caches a VALUE (result of a computation).
- `useCallback` → caches a FUNCTION (the function itself, not its result).

```jsx
// useMemo: cache the computed value
const sortedList = useMemo(() => items.sort(), [items]);

// useCallback: cache the function reference
const handleClick = useCallback(() => doSomething(id), [id]);

// useCallback is equivalent to useMemo for functions:
const handleClick = useMemo(() => () => doSomething(id), [id]);
```

**Why it exists:** They serve different purposes. `useMemo` is for expensive calculations. `useCallback` is for stable function references. Understanding the difference prevents confusion.

**Where it's used:** `useMemo` for computed values. `useCallback` for event handlers passed to children.

**What goes wrong without it:**
- Using `useMemo` for a function: `useMemo(() => handleClick, [id])` → returns the function, but it's confusing. Use `useCallback` for functions.
- Using `useCallback` for a value: `useCallback(() => expensiveCalc(), [deps])` → returns the function, not the result. Use `useMemo` for values.
- Rule: `useMemo` = "remember this VALUE". `useCallback` = "remember this FUNCTION".

---

## React.memo

**What:** `React.memo` prevents a component from re-rendering if its props haven't changed.

```jsx
const ExpensiveChild = React.memo(({ data, onClick }) => {
    console.log("ExpensiveChild rendered");
    return <div>{data.name}</div>;
});

// Parent re-renders → ExpensiveChild only re-renders if `data` or `onClick` changes
```

**Why it exists:** Without `React.memo`, every parent re-render re-renders all children → unnecessary work if props are the same. `React.memo` does a shallow comparison of props → skips re-render if unchanged.

**Where it's used:** Expensive child components, list items in large lists, components that receive stable props.

**What goes wrong without it:**
- `React.memo` does SHALLOW comparison → `{name: "A"}` !== `{name: "A"}` (different object references) → re-renders anyway. Use `useMemo` for object props.
- `React.memo` with new function props every render → re-renders (function reference changes). Use `useCallback` for function props.
- Overusing `React.memo` → memoization overhead on every component → slower than just re-rendering. Only memoize expensive components.

---

## Dependency Arrays

**What:** The second argument to `useMemo`/`useCallback` — controls when the memoized value/function is recalculated.

```jsx
// Recalculate when `items` or `sortOrder` changes
const sorted = useMemo(() => sortItems(items, sortOrder), [items, sortOrder]);

// New function when `id` changes
const handler = useCallback(() => fetchUser(id), [id]);

// Empty array → calculate once, never update (value is fixed)
const initialData = useMemo(() => loadInitialData(), []);

// No array → recalculate every render (useless, same as no useMemo)
const value = useMemo(() => compute(x));  // DON'T DO THIS
```

**Why it exists:** Without dependency arrays, you'd have to manually decide when to recalculate. The array tells React "only recalculate when these values change."

**Where it's used:** Every `useMemo`, `useCallback`, and `useEffect` call.

**What goes wrong without it:**
- Missing a dependency → stale value (uses old data). React's exhaustive-deps ESLint rule catches this.
- Extra dependencies → unnecessary recalculations. Only include values used inside the memo/callback.
- Objects/functions as dependencies → new reference every render → recalculates every render. Memoize the dependency first, or use a primitive (string/number) as the dep.

---

## When to Use Memoization

**What:** Memoization is NOT free — it costs memory and comparison time. Use it only when the benefit outweighs the cost.

**USE memoization when:**
- Expensive calculations (> 1ms): sorting 1000+ items, complex math, large data processing
- Passing props to `React.memo` children: prevents unnecessary child re-renders
- Referential equality in `useEffect` deps: function/object used in effect dependency

**DON'T use memoization when:**
- Cheap calculations: `a + b`, `text.toUpperCase()`, simple array methods on small arrays
- Every component re-renders anyway: if parent always re-renders, memoizing children is useless
- The value is only used in the same component: no need to stabilize the reference

**Why it exists:** Understanding when NOT to memoize is as important as knowing when to. Premature optimization makes code complex without benefit.

**Where it's used:** Performance optimization — only after identifying actual performance issues (use React DevTools Profiler).

**What goes wrong without it:**
- Premature optimization → wrapping everything in `useMemo`/`useCallback` → complex code, no measurable benefit.
- Not memoizing when needed → slow app, janky UI. Use the Profiler to identify actual bottlenecks.
- Rule: measure first, optimize second. Don't guess what's slow.

---

## Common Patterns

**What:** Real-world memoization patterns:

```jsx
// 1. Filter + sort large lists
const processedData = useMemo(() => {
    return data
        .filter(item => item.active)
        .sort((a, b) => a.name.localeCompare(b.name));
}, [data]);

// 2. Stable callback for child component
const handleDelete = useCallback((id) => {
    setItems(prev => prev.filter(item => item.id !== id));
}, []);  // setItems is stable, no deps needed

// 3. Memoized child with memoized props
const Child = React.memo(({ data, onSelect }) => {
    return <div onClick={() => onSelect(data.id)}>{data.name}</div>;
});

// 4. Expensive derived state
const stats = useMemo(() => {
    return {
        total: items.length,
        active: items.filter(i => i.active).length,
        avgPrice: items.reduce((sum, i) => sum + i.price, 0) / items.length,
    };
}, [items]);
```

**Why it exists:** These patterns cover the most common use cases. Recognizing them helps you apply memoization correctly.

**Where it's used:** Data-heavy components, list rendering, dashboard widgets, any performance-sensitive UI.

**What goes wrong without it:**
- Pattern 1 without memo → re-filters and re-sorts on every render → slow for large lists.
- Pattern 2 without `useCallback` → `handleDelete` is a new function every render → `React.memo` child re-renders.
- Pattern 3: both `data` (useMemo) and `onSelect` (useCallback) must be stable for `React.memo` to work.

---

## Performance Measurement

**What:** Use React DevTools Profiler to identify actual performance issues before optimizing.

```jsx
// Wrap component in Profiler to measure render times
import { Profiler } from 'react';

<Profiler id="ProductList" onRender={(id, phase, actualDuration) => {
    console.log(`${id} ${phase} took ${actualDuration}ms`);
}}>
    <ProductList products={products} />
</Profiler>
```

**Why it exists:** Without measurement, you guess what's slow → optimize the wrong thing → no improvement. The Profiler shows exactly which components take long to render → optimize those.

**Where it's used:** Performance debugging, identifying bottlenecks, verifying that memoization actually helps.

**What goes wrong without it:**
- Optimizing without measuring → "I think this is slow" → add `useMemo` everywhere → no improvement → wasted time.
- Profiler in production → adds overhead. Use it in development only.
- Memoization that doesn't help → the Profiler shows the same render time → remove the memo → simpler code.
