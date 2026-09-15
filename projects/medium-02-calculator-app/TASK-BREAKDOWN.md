# Calculator App (Vanilla JS) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
medium-02-calculator-app/
├── index.html, styles.css, script.js
└── README.md
```

---

## Implementation Steps

### Step 1: HTML Structure

Display, number pad (0-9), operators (+, -, *, /), functions (C, =, +/-, %).

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: CSS Grid Layout

Grid for button layout. Display at top. Responsive sizing.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: JS: Input Handling

Click button → update display. Handle numbers, operators, decimals.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: JS: Calculation

Evaluate expression. Handle order of operations. Prevent invalid input.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Keyboard Support

Map keys: 0-9, +, -, *, /, Enter (=), Escape (C), Backspace.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: History

Store last 10 calculations. Show in a dropdown or side panel. Click to reuse.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Theme Toggle

Light/dark theme. CSS variables. Persist to localStorage.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Edge Cases

Division by zero, max digits, consecutive operators, leading zeros.

**Checkpoint:** Step 8 is complete when the described functionality works.

---

## Final Checklist

- [ ] Number pad (0-9)
- [ ] Operators (+, -, *, /)
- [ ] Clear and equals
- [ ] Keyboard support
- [ ] Calculation history
- [ ] Light/dark theme
- [ ] Division by zero handling
- [ ] Responsive design

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
