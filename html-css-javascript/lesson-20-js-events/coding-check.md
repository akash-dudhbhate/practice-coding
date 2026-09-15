# Lesson 20 — Coding Check

## Easy

### p01-solve.html — Button click
- [ ] Button exists in HTML
- [ ] `addEventListener("click", ...)` used
- [ ] Button text changes to "Clicked!" on click
- [ ] Uses `event.target` to reference the button

### p02-solve.html — Real-time input
- [ ] Input field exists
- [ ] `input` event listener attached (not `change`)
- [ ] Value printed in real-time as user types
- [ ] Uses `event.target.value`

### p03-solve.html — Prevent link navigation
- [ ] `<a>` tag with href exists
- [ ] `preventDefault()` called on click
- [ ] Link does NOT navigate
- [ ] Alert or message shown instead

## Medium

### p01-solve.html — Event delegation
- [ ] List with 5 `<li>` items
- [ ] ONE listener on `<ul>` (not on each `<li>`)
- [ ] Correct `<li>` identified when clicked
- [ ] Uses `event.target` or `closest()`
- [ ] Works even if new items are added dynamically

### p02-solve.html — Form validation
- [ ] Form with name and email inputs
- [ ] `submit` event listener with `preventDefault()`
- [ ] Validates both fields are required
- [ ] Shows success message if valid
- [ ] Shows error message if invalid
- [ ] No page reload on submit

### p03-solve.html — Keyboard shortcuts
- [ ] Ctrl+K focuses the search input
- [ ] Uses `keydown` event
- [ ] Checks `e.ctrlKey` and `e.key === "k"`
- [ ] Escape key clears the input
- [ ] Shortcuts don't interfere with normal typing

## Hard

### p01-solve.html — Dropdown menu
- [ ] Click on button opens dropdown
- [ ] Click outside closes dropdown
- [ ] Uses `stopPropagation()` on dropdown click
- [ ] Document click listener closes dropdown
- [ ] Escape key closes dropdown
- [ ] Only one dropdown open at a time

### p02-solve.html — Draggable element
- [ ] `mousedown` starts drag
- [ ] `mousemove` updates element position
- [ ] `mouseup` ends drag
- [ ] Uses `event.clientX` and `event.clientY`
- [ ] Element follows mouse smoothly
- [ ] Custom "dropped" event dispatched on release
- [ ] Custom event listener works

### p03-solve.html — Infinite scroll
- [ ] `scroll` event listener on window
- [ ] Detects when near bottom (within 100px)
- [ ] Loads more content (simulated with setTimeout)
- [ ] Content is actually added to the page
- [ ] No duplicate loads (guard against multiple triggers)
- [ ] Loading indicator shown while loading
- [ ] `removeEventListener` used for cleanup if needed
