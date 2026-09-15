# Lesson 03 — Approach Comparison

## Problem: Click Handler with Parameter

### Approach 1: Arrow function
```jsx
<button onClick={() => deleteItem(id)}>Delete</button>
```

### Approach 2: bind
```jsx
<button onClick={deleteItem.bind(null, id)}>Delete</button>
```

**Winner:** Approach 1 — more readable, more common.

---

## Problem: Form Submission

### Approach 1: Button onClick
```jsx
<button onClick={handleSubmit}>Submit</button>
```
**Cons:** Doesn't handle Enter key.

### Approach 2: Form onSubmit
```jsx
<form onSubmit={handleSubmit}>
  <button type="submit">Submit</button>
</form>
```

**Winner:** Approach 2 — handles all submission methods.
