# Interactive Todo List (Vanilla JS) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-04-interactive-todo/
├── index.html, styles.css, script.js
└── README.md
```

---

## Implementation Steps

### Step 1: HTML Structure

Input field, add button, todo list (ul), filter buttons (all/active/completed), count.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: CSS Styling

Clean card-based design. Checkbox styling, delete button hover, completed strikethrough.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: JS: Add Todo

Function to create todo object {id, text, done}. Render to DOM. Enter key + button.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: JS: Toggle Todo

Click checkbox → toggle done state. Update DOM + strikethrough.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: JS: Delete Todo

Delete button → remove from array + DOM. Confirmation for completed todos.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: JS: Filter

All/Active/Completed filter buttons. Show/hide todos based on filter.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: JS: Counter

Show remaining count: 'X items left'. Update on every change.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: JS: Persistence

Save todos to localStorage. Load on page refresh.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: JS: Edit Todo

Double-click to edit. Input field replaces text. Enter to save, Esc to cancel.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] Add todo (input + button + Enter key)
- [ ] Toggle complete (checkbox)
- [ ] Delete todo (button)
- [ ] Filter (all/active/completed)
- [ ] Item counter
- [ ] localStorage persistence
- [ ] Edit todo (double-click)
- [ ] Clean, responsive UI

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
