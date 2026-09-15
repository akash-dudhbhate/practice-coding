# React Todo App — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-05-react-todo/
├── src/App.jsx, src/components/TodoInput.jsx, src/components/TodoList.jsx, src/components/TodoItem.jsx, src/components/Filters.jsx, src/hooks/useTodos.js
└── README.md
```

---

## Implementation Steps

### Step 1: Setup

npx create-vite app --template react. Install. Clean App.jsx.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: useTodos Hook

Custom hook: todos state, addTodo, toggleTodo, deleteTodo, filter, localStorage sync.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: TodoInput Component

Input + button. useState for input. Call addTodo on submit. Enter key support.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: TodoItem Component

Props: todo, onToggle, onDelete, onEdit. Checkbox, text, delete button. Edit mode.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: TodoList Component

Map filtered todos to TodoItem. Empty state message.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Filters Component

All/Active/Completed buttons. Active state styling.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: App Component

Compose all components. useTodos hook. Pass props down.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Styling

CSS modules or Tailwind. Clean, modern design. Responsive.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Testing

Write basic tests: add, toggle, delete, filter. Use vitest + testing-library.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] useTodos custom hook with localStorage
- [ ] Add todo (input + Enter)
- [ ] Toggle complete
- [ ] Delete todo
- [ ] Filter (all/active/completed)
- [ ] Edit todo (double-click)
- [ ] Item counter
- [ ] Responsive design
- [ ] Basic tests

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
