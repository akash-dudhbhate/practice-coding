# Lesson 05 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01-solve.jsx (Fruit List)
- [ ] Uses `.map()` on the fruits array.
- [ ] Each `<li>` has `key={fruit.id}` (NOT index).
- [ ] Renders fruit name inside `<li>`.
- [ ] Test: 5 fruits → 5 `<li>` elements render.
- [ ] Test: No console warning about missing keys.

### p02-solve.jsx (Number List)
- [ ] Uses `.map()` on an array of numbers 1-10.
- [ ] Uses `key={index}` (acceptable for static list).
- [ ] Test: Numbers 1-10 render in order.
- [ ] Test: No console warning about missing keys.
- [ ] Test: Each number is in its own `<li>`.

### p03-solve.jsx (User Cards from Array)
- [ ] Uses `.map()` on users array.
- [ ] Each card has `key={user.id}`.
- [ ] Card shows `user.name` and `user.email`.
- [ ] Test: 3 users → 3 cards render with correct data.
- [ ] Test: No console warning about missing keys.
- [ ] Test: Each card shows the correct name and email (not all showing the same data).

## Medium

### p01-solve.jsx (Dynamic Todo List)
- [ ] Each todo has a unique `id` (using `Date.now()` or a counter).
- [ ] Add creates new array: `setTodos([...todos, newTodo])`.
- [ ] Remove uses `.filter()`: `setTodos(todos.filter(t => t.id !== id))`.
- [ ] Each `<li>` has `key={todo.id}` (NOT index).
- [ ] Test: Add 3 todos → all 3 appear with correct text.
- [ ] Test: Remove middle todo → other two remain with correct state.
- [ ] Test: Add after remove → new todo appears at the end.
- [ ] Test: No key warnings in console.

### p02-solve.jsx (Searchable List)
- [ ] Has a search input with `onChange` handler.
- [ ] Filters items: `items.filter(item => item.name.toLowerCase().includes(query.toLowerCase()))`.
- [ ] Shows "No results" when filtered list is empty.
- [ ] Does NOT modify the original items array.
- [ ] Test: Type "app" → only items containing "app" show (case-insensitive).
- [ ] Test: Type "xyz" → "No results" shows.
- [ ] Test: Clear search → all items show again.
- [ ] Test: Keys remain stable during filtering (use item.id, not index).

### p03-solve.jsx (Sortable List)
- [ ] Sorts a COPY: `[...items].sort(...)`, NOT `items.sort()`.
- [ ] Toggle button switches between ascending and descending.
- [ ] Uses `.localeCompare()` for string sorting or `(a, b) => a - b` for numbers.
- [ ] Test: Click sort ascending → items in A-Z order.
- [ ] Test: Click sort descending → items in Z-A order.
- [ ] Test: Original state array is NOT mutated (check that re-sorting works both ways).
- [ ] Test: Keys remain stable after sorting (use item.id, not index).

## Hard

### p01-solve.jsx (Nested Category List)
- [ ] Outer `.map()` on categories with `key={category.id}`.
- [ ] Inner `.map()` on `category.items` with `key={item.id}`.
- [ ] Category name shows in a heading (`<h3>` or similar).
- [ ] Items show in a nested `<ul>`.
- [ ] Test: 2 categories with 2 items each → 2 headings, 4 total items.
- [ ] Test: No key warnings for either level.
- [ ] Test: Items appear under the correct category heading.

### p02-solve.jsx (Todo List with Item Components)
- [ ] `TodoItem` is a separate component that accepts `todo`, `onToggle`, `onRemove` props.
- [ ] `key={todo.id}` is on `<TodoItem>` in the `.map()`, NOT inside `TodoItem`.
- [ ] `TodoItem` renders checkbox, text, and delete button.
- [ ] Test: 3 todos → 3 `TodoItem` components render.
- [ ] Test: Click checkbox → toggles done state for that todo only.
- [ ] Test: Click delete → removes only that todo.
- [ ] Test: No key warnings (key is on the component, not inside it).

### p03-solve.jsx (Reorderable List with State)
- [ ] Each item has a stable `id` used as key (NOT index).
- [ ] Up/Down buttons move items within the array.
- [ ] Moving items uses immutable updates (creates new array).
- [ ] Each item has some internal state (e.g., a text input or checkbox).
- [ ] Test: Move item 2 up → item 2 is now first, item 1 is second.
- [ ] Test: Type in item 1's input, then move it down → the typed text moves WITH the item (state follows the key).
- [ ] Test: Check item 2's checkbox, move item 2 up → checkbox stays checked on the same item.
- [ ] Test: No state jumping to wrong items after reordering.
