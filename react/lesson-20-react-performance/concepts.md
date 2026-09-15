# Lesson 20 — Concepts Explained (React Performance Optimization)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## The React Render Cycle

**What:** When state or props change, React re-renders the component and all its children (unless memoized).

```jsx
function Parent() {
    const [count, setCount] = useState(0);
    const [text, setText] = useState("");

    return (
        <>
            <input value={text} onChange={e => setText(e.target.value)} />
            <button onClick={() => setCount(c => c + 1)}>Count: {count}</button>
            <ExpensiveChild />  {/* re-renders when count OR text changes */}
        </>
    );
}
```

**Why it exists:** Understanding the render cycle is the foundation of performance. Every state change re-renders the component tree → if children are expensive → slow. Knowing this helps you decide what to optimize.

**Where it's used:** Every React app — understanding renders is essential for performance.

**What goes wrong without it:**
- Assuming React "knows" what changed → it doesn't. It re-renders the entire subtree by default.
- Optimizing before measuring → premature optimization → complex code, no benefit.
- Not knowing which state change triggers which re-render → can't optimize effectively.

---

## React.memo (Preventing Re-renders)

**What:** `React.memo` prevents a component from re-rendering if its props haven't changed.

```jsx
const ExpensiveChild = React.memo(({ data }) => {
    console.log("ExpensiveChild rendered");
    return <div>{data.name}</div>;
});

function Parent() {
    const [count, setCount] = useState(0);
    const [data] = useState({ name: "Akash" });

    return (
        <>
            <button onClick={() => setCount(c => c + 1)}>Count: {count}</button>
            <ExpensiveChild data={data} />  {/* doesn't re-render when count changes */}
        </>
    );
}
```

**Why it exists:** Without `React.memo`, every parent re-render re-renders all children → unnecessary work if props are the same. `React.memo` does a shallow comparison → skips re-render if props are unchanged.

**Where it's used:** Expensive components, list items, components that receive stable props.

**What goes wrong without it:**
- `React.memo` with object/function props → new reference every render → re-renders anyway. Use `useMemo` for objects, `useCallback` for functions.
- `React.memo` does SHALLOW comparison → `{a: 1}` !== `{a: 1}` (different reference). Use a custom comparator: `React.memo(Component, (prev, next) => prev.data.id === next.data.id)`.
- Overusing `React.memo` → memoization overhead on every component → slower than just re-rendering. Only memoize expensive components.

---

## useMemo and useCallback (Stable References)

**What:** `useMemo` caches values, `useCallback` caches functions → stable references for `React.memo` children.

```jsx
function Parent() {
    const [count, setCount] = useState(0);
    const [items, setItems] = useState([1, 2, 3]);

    // Without useMemo: new array every render → Child re-renders
    // const processedItems = items.map(i => i * 2);

    // With useMemo: stable reference unless items change
    const processedItems = useMemo(() => items.map(i => i * 2), [items]);

    // Without useCallback: new function every render → Child re-renders
    // const handleClick = (id) => console.log(id);

    // With useCallback: stable function reference
    const handleClick = useCallback((id) => {
        console.log(id);
    }, []);

    return (
        <>
            <button onClick={() => setCount(c => c + 1)}>Count: {count}</button>
            <MemoizedChild items={processedItems} onClick={handleClick} />
        </>
    );
}
```

**Why it exists:** `React.memo` only works if props are stable. Without `useMemo`/`useCallback`, new objects/functions are created every render → `React.memo` sees "new" props → re-renders → memoization is useless.

**Where it's used:** When passing objects, arrays, or functions to `React.memo` children.

**What goes wrong without it:**
- `useMemo`/`useCallback` for everything → overhead (storing deps, comparing) → slower for cheap operations. Only memoize expensive calculations and functions passed to memoized children.
- Forgetting a dependency → stale value (uses old data). Always include all values used inside.
- Memoizing a value that's only used in the same component → no benefit (no child needs a stable reference).

---

## Virtualization (Large Lists)

**What:** Only render the items visible in the viewport, not the entire list.

```jsx
import { FixedSizeList as List } from 'react-window';

function LargeList({ items }) {
    const Row = ({ index, style }) => (
        <div style={style}>
            {items[index].name}
        </div>
    );

    return (
        <List
            height={600}
            itemCount={items.length}
            itemSize={50}
            width="100%"
        >
            {Row}
        </List>
    );
}
// Renders 10,000 items but only ~12 DOM nodes (visible ones)
```

**Why it exists:** Without virtualization, 10,000 items → 10,000 DOM nodes → slow initial render, high memory, janky scroll. Virtualization renders only visible items → fast, smooth scrolling.

**Where it's used:** Large lists, tables, feeds, any list with 100+ items.

**What goes wrong without it:**
- Search/filtering with virtualization → must filter the data array, not the DOM. The list re-renders with the filtered array.
- Dynamic item heights → `FixedSizeList` doesn't work. Use `VariableSizeList` or `react-virtualized`.
- Scroll restoration → virtualized lists don't keep off-screen items in DOM → scroll position needs manual restoration.

---

## Code Splitting (Lazy Loading)

**What:** Split the bundle into chunks → load only what's needed.

```jsx
import { lazy, Suspense } from 'react';

// Lazy load heavy components
const Chart = lazy(() => import('./Chart'));
const Dashboard = lazy(() => import('./Dashboard'));

function App() {
    return (
        <Suspense fallback={<Loading />}>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/chart" element={<Chart />} />
                <Route path="/dashboard" element={<Dashboard />} />
            </Routes>
        </Suspense>
    );
}
// Home loads immediately. Chart and Dashboard load when navigated to.
```

**Why it exists:** Without code splitting, the entire app is one JS bundle → slow initial load. Splitting → user downloads only the code for the current page → faster initial load.

**Where it's used:** Route-level splitting, heavy components (charts, editors), admin sections.

**What goes wrong without it:**
- Too many small chunks → many HTTP requests → overhead. Find a balance.
- Lazy loading without Suspense → error. Always wrap in `<Suspense>`.
- Lazy loading without ErrorBoundary → failed import → blank page. Wrap in ErrorBoundary.

---

## Bundle Analysis

**What:** Analyze the bundle to find large dependencies.

```bash
# Install bundle analyzer
npm install --save-dev webpack-bundle-analyzer

# Or for Vite
npm install --save-dev rollup-plugin-visualizer

# Build with analysis
npm run build -- --analyze
```

**Why it exists:** Without analysis, you don't know what's making the bundle large → can't optimize effectively. The analyzer shows a visual tree of every module and its size → identify the largest dependencies.

**Where it's used:** Before performance optimization → find what to split or replace.

**What goes wrong without it:**
- Importing entire libraries when you need one function: `import _ from 'lodash'` → 70KB. Use `import debounce from 'lodash/debounce'` → 2KB.
- Not analyzing → guessing what's large → optimizing the wrong thing.
- Forgetting to analyze after changes → new dependency might bloat the bundle unnoticed.

---

## Profiling with React DevTools

**What:** Use the React DevTools Profiler to identify slow renders.

```jsx
// Wrap components in Profiler to measure render times
import { Profiler } from 'react';

<Profiler id="App" onRender={(id, phase, actualDuration) => {
    console.log(`${id} ${phase}: ${actualDuration}ms`);
}}>
    <App />
</Profiler>
```

**Why it exists:** Without profiling, you guess what's slow → optimize the wrong thing. The Profiler shows exactly which components take long to render → optimize those.

**Where it's used:** Performance debugging, verifying optimizations work.

**What goes wrong without it:**
- Profiling in production → different performance characteristics. Profile in development but test in production.
- Profiling with React Strict Mode → double-renders → misleading timings. Disable Strict Mode during profiling.
- One-off profiling → performance varies. Profile multiple interactions and average.

---

## useTransition (Non-urgent Updates)

**What:** Mark state updates as "non-urgent" → React can interrupt them to handle urgent updates (typing, clicking).

```jsx
import { useTransition, useState } from 'react';

function Search() {
    const [isPending, startTransition] = useTransition();
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);

    const handleSearch = (e) => {
        setQuery(e.target.value);  // urgent: update input immediately
        startTransition(() => {
            setResults(filterHugeList(e.target.value));  // non-urgent: can be interrupted
        });
    };

    return (
        <>
            <input value={query} onChange={handleSearch} />
            {isPending && <p>Filtering...</p>}
            <ul>{results.map(r => <li key={r.id}>{r.name}</li>)}</ul>
        </>
    );
}
```

**Why it exists:** Without `useTransition`, filtering a large list blocks the main thread → typing feels laggy. With `useTransition`, the input updates immediately (urgent) while filtering happens in the background (non-urgent) → smooth typing.

**Where it's used:** Search filtering, sorting large lists, any expensive update that shouldn't block user input.

**What goes wrong without it:**
- `startTransition` doesn't make the update async — it makes it interruptible. The work still happens on the main thread.
- `isPending` → shows a pending state while the transition is in progress → good UX indicator.
- Overusing `useTransition` for quick updates → no benefit (they're already fast). Use for expensive updates only.

---

## useDeferredValue

**What:** Defer a value's update → similar to debounce but integrated with React's rendering.

```jsx
import { useDeferredValue, useMemo, useState } from 'react';

function Search({ items }) {
    const [query, setQuery] = useState("");
    const deferredQuery = useDeferredValue(query);  // lags behind `query`

    // Filter uses the deferred value → doesn't block typing
    const results = useMemo(() => {
        return items.filter(item => item.name.includes(deferredQuery));
    }, [items, deferredQuery]);

    return (
        <>
            <input value={query} onChange={e => setQuery(e.target.value)} />
            <ul>
                {results.map(r => <li key={r.id}>{r.name}</li>)}
            </ul>
        </>
    );
}
```

**Why it exists:** Similar to `useTransition` but for values instead of updates. The input updates immediately (urgent), the list updates with the deferred value (non-urgent) → smooth typing.

**Where it's used:** Search inputs, real-time filtering, any value that drives an expensive computation.

**What goes wrong without it:**
- `useDeferredValue` doesn't delay the value by a fixed time → it defers based on React's rendering priority → more responsive than debounce.
- The deferred value lags behind → for a moment, the list shows results for the old query → acceptable for search, not for critical data.
- Combining with `useMemo` → the memo recalculates when the deferred value changes → efficient.

---

## Key Performance Rules

**What:** Summary of when to optimize:

1. **Measure first** — use Profiler before optimizing.
2. **Memoize only expensive components** — not everything.
3. **Stabilize props** — `useMemo`/`useCallback` for `React.memo` children.
4. **Virtualize large lists** — 100+ items.
5. **Code split** — lazy load routes and heavy components.
6. **Defer non-urgent updates** — `useTransition`/`useDeferredValue`.
7. **Avoid inline objects/functions** — in props (creates new reference every render).

**Why it exists:** Without rules, developers optimize randomly → wasted effort. These rules prioritize the highest-impact optimizations.

**Where it's used:** Every React app — apply rules when performance issues arise.

**What goes wrong without it:**
- Premature optimization → complex code, no measurable benefit.
- Optimizing the wrong thing → "I think this is slow" → no improvement.
- Rule: measure → identify bottleneck → optimize → measure again → verify improvement.
