# Lesson 04 — Refactoring Challenges

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
