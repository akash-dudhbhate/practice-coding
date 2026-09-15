# Lesson 04 — Common Mistakes

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
