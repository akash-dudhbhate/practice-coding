# Lesson 03 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01-solve.jsx (Click Counter)
- [ ] Uses `onClick` on a `<button>`.
- [ ] Handler is a function reference or arrow function, NOT called: `onClick={() => setCount(count + 1)}`.
- [ ] Count displays inside the button or in a `<p>`.
- [ ] Test: Click 5 times → count shows 5.
- [ ] Test: No page reload on click.

### p02-solve.jsx (Text Echo)
- [ ] Input has `onChange` handler.
- [ ] Handler uses `e.target.value` to update state.
- [ ] Paragraph below shows the current text in real time.
- [ ] Test: Type "Hello" → "Hello" appears below on each keystroke.
- [ ] Test: Clear input → paragraph clears.

### p03-solve.jsx (Double-Click Alert)
- [ ] Box has both `onClick` and `onDoubleClick` handlers.
- [ ] Single click changes color (toggles between two colors).
- [ ] Double click shows a message (alert or text on screen).
- [ ] Test: Single click → color changes.
- [ ] Test: Double click → message appears.
- [ ] Test: Single click doesn't trigger the double-click message.

## Medium

### p01-solve.jsx (Login Form)
- [ ] Uses `<form onSubmit={handleSubmit}>` (NOT `onClick` on the button).
- [ ] `handleSubmit` calls `e.preventDefault()` as the first line.
- [ ] Email and password inputs are controlled with state.
- [ ] Submit button has `type="submit"`.
- [ ] Test: Fill form and press Enter → form submits, no page reload.
- [ ] Test: Fill form and click Submit button → form submits.
- [ ] Test: Credentials display on screen after submit.

### p02-solve.jsx (Todo with Delete Buttons)
- [ ] Each todo item has a delete button with `onClick={() => handleDelete(item.id)}`.
- [ ] Delete button uses arrow function wrapper (NOT `onClick={handleDelete(item.id)}`).
- [ ] `handleDelete` filters the todo by id.
- [ ] Test: Add 3 items → all appear.
- [ ] Test: Click delete on item 2 → items 1 and 3 remain, item 2 is gone.
- [ ] Test: Delete doesn't trigger any parent handler or page reload.

### p03-solve.jsx (Search with Enter Key)
- [ ] Input has `onKeyDown` handler.
- [ ] Handler checks `e.key === "Enter"` to trigger search.
- [ ] Handler checks `e.key === "Escape"` to clear the input.
- [ ] Search results or a search message displays when Enter is pressed.
- [ ] Test: Type "react" and press Enter → search triggers with "react".
- [ ] Test: Press Escape → input clears.
- [ ] Test: Pressing other keys does NOT trigger search.

## Hard

### p01-solve.jsx (Clickable Card with Inner Button)
- [ ] Card div has `onClick` that logs "Card clicked".
- [ ] Inner button has `onClick` that logs "Details" and calls `e.stopPropagation()`.
- [ ] `stopPropagation` is called BEFORE the button's action.
- [ ] Test: Click the card (not the button) → only "Card clicked" logs.
- [ ] Test: Click the "Details" button → only "Details" logs, "Card clicked" does NOT log.
- [ ] Test: No console errors or warnings.

### p02-solve.jsx (Multi-Input Form with Validation)
- [ ] Form has `onSubmit` handler with `e.preventDefault()`.
- [ ] Three controlled inputs: name, email, password.
- [ ] Validation: all fields required (show error if empty).
- [ ] Validation: email must contain "@".
- [ ] Errors display inline next to each field.
- [ ] Test: Submit empty form → all three fields show errors.
- [ ] Test: Submit with name only → email and password show errors.
- [ ] Test: Submit email without "@" → email error shows.
- [ ] Test: Submit all valid → success message shows, no errors.
- [ ] Test: No page reload on any submit.

### p03-solve.jsx (Keyboard-Navigable Dropdown)
- [ ] Dropdown button opens/closes menu on click.
- [ ] Pressing Enter when focused opens the dropdown.
- [ ] Arrow Down/Up navigates between items (highlighted item changes).
- [ ] Escape closes the dropdown.
- [ ] Enter selects the highlighted item and closes dropdown.
- [ ] Test: Click button → dropdown opens.
- [ ] Test: Press Arrow Down → second item highlighted.
- [ ] Test: Press Arrow Down again → third item highlighted (wraps or stops).
- [ ] Test: Press Escape → dropdown closes.
- [ ] Test: Press Enter on highlighted item → item selected, dropdown closes.
