# Lesson 09 — useMemo & useCallback

## What you'll learn
- useMemo (caching computed values)
- useCallback (caching function references)
- useMemo vs useCallback (value vs function)
- React.memo (preventing child re-renders)
- Dependency arrays (when to recalculate)
- When to use memoization (and when NOT to)
- Common memoization patterns
- Performance measurement with Profiler

## Lesson

### useMemo
```jsx
const filtered = useMemo(() => items.filter(i => i.active), [items]);
```

### useCallback
```jsx
const handleClick = useCallback((id) => deleteItem(id), [deleteItem]);
```

### React.memo + useCallback
```jsx
const Child = React.memo(({ onClick }) => <button onClick={onClick}>X</button>);
const handle = useCallback(() => {}, []);
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create a component with a list of numbers and a text input. Use `useMemo` to compute the sum of numbers. Typing in the input should NOT recompute the sum.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Sum: 15                         <- stays fixed while typing
   +------------------+
   | type here...     |            <- re-renders but NO recompute
   +------------------+
   ```
2. `easy/p02-solve.jsx` — Create a parent with a counter and a `React.memo` child. Pass a `useCallback`-wrapped handler to the child. Incrementing the counter should NOT re-render the child.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Count: 2                        <- parent state
   [ Increment ]
   +------------------+
   |  Child  [Click]  |            <- memo child; console logs
   +------------------+               "Child rendered" only once
   ```
3. `easy/p03-solve.jsx` — Create a component that sorts an array of 1000 random numbers using `useMemo`. Add a button to regenerate the array (should re-sort) and a text input (should NOT re-sort).

   WHAT IT SHOULD LOOK LIKE:
   ```
   First 5 sorted: 3, 17, 22, 48, 91
   [ Regenerate ]                  <- new array -> re-sorts
   +------------------+
   | type here...     |            <- typing does NOT re-sort
   +------------------+
   ```

### Medium
4. `medium/p01-solve.jsx` — Create a `SearchFilter` component: large list of items (100+), search input. Use `useMemo` to filter items. Verify that unrelated state changes don't trigger re-filtering.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------+
   | app              |            <- search input
   +------------------+
   Unrelated clicks: 3 [ + ]       <- re-render, no re-filter
   * Apple
   * Pineapple                     <- filtered <ul>
   ```
5. `medium/p02-solve.jsx` — Create a `TodoList` with `React.memo` todo items. Each item has a delete button. Use `useCallback` for the delete handler. Adding a new todo should NOT re-render existing items.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------+ +-----+
   | new task       | | Add |
   +----------------+ +-----+
   * Buy milk      [x]    <- memoized <TodoItem>; adding does
   * Walk the dog  [x]       NOT re-render existing items
   ```
6. `medium/p03-solve.jsx` — Create a `Dashboard` with 3 widgets (stats, chart, table). Each widget is `React.memo`-wrapped. Use `useMemo` for computed data and `useCallback` for handlers. Only the changed widget should re-render.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-----------+ +-----------+ +-----------+
   |  Stats    | |  Chart    | |  Table    |   <- 3 memo widgets
   |  42 users | |  #####    | |  6 rows   |
   +-----------+ +-----------+ +-----------+
   [ Update Table ]   <- only Table re-renders
   ```

### Hard
7. `hard/p01-solve.jsx` — Build a `DataTable` component: 1000 rows, sortable by column, filterable by search. Use `useMemo` for sorting and filtering. Add a "render count" display to verify memoization works.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Renders: 1   [ Re-render ]      <- count proves memoization
   +------------------+
   | search...        |
   +------------------+
   [ Sort: name ] [ Sort: age ]
   +-----+-------+-----+
   | ID  | Name  | Age |           <- <table>, 20 visible rows
   +-----+-------+-----+
   |  1  | Amy   | 30  |
   | ... | ...   | ... |
   +-----+-------+-----+
   ```
8. `hard/p02-solve.jsx` — Build a `Form` with multiple fields. Each field is a `React.memo` component with `useCallback` change handlers. Typing in one field should NOT re-render other fields. Use a ref or state wisely.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Name:  [ Ada_______________ ]   <- only this <Field> re-renders
   Email: [ _________________ ]       while typing in it
   Phone: [ _________________ ]
   (console: only "Name rendered" logs)
   ```
9. `hard/p03-solve.jsx` — Build a `PerformanceDemo` that shows the difference between memoized and non-memoized rendering. Include a toggle to enable/disable memoization, a render counter for each mode, and a Profiler wrapper to measure actual render times.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [x] Memoized        [ Recompute ]   <- checkbox + button
   Preview: 1000 items computed        <- wrapped in <Profiler>
   CONSOLE:
   list render: 12.3ms   (memoized)
   list render: 48.7ms   (non-memoized)
   ```

### How to work
- Write your complete React component solution.
- Remove the TODO comment when done.
- Test by importing into a React app or using a sandbox.
