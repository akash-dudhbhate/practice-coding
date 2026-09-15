# Lesson 04 — Approach Comparison

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
