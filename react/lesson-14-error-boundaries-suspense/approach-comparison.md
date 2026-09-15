# Lesson 14 — Approach Comparison

## Problem: Handle Errors

### Approach 1: try/catch in render
```jsx
try { return <Component />; }
catch (e) { return <Error />; }
```
**Cons:** Can't catch render errors in children.

### Approach 2: Error boundary
```jsx
<ErrorBoundary><Component /></ErrorBoundary>
```

**Winner:** Approach 2 — catches errors in entire subtree.

---

## Problem: Code Splitting

### Approach 1: React.lazy + Suspense
```jsx
const Page = React.lazy(() => import("./Page"));
<Suspense fallback={<Spinner />}><Page /></Suspense>
```

### Approach 2: Manual dynamic import
```jsx
const [Page, setPage] = useState(null);
useEffect(() => { import("./Page").then(m => setPage(m.default)); }, []);
if (!Page) return <Spinner />;
return <Page />;
```

**Winner:** Approach 1 — declarative, cleaner.
