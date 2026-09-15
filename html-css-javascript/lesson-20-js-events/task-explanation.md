# Lesson 20 — JS Events & Interactivity

## What you'll learn
- addEventListener (attaching event handlers)
- Event object (target, currentTarget, key, clientX)
- Common event types (mouse, keyboard, form, scroll)
- Event bubbling and capturing
- Event delegation (one listener for many children)
- preventDefault (stopping default behavior)
- Keyboard events and shortcuts
- removeEventListener (cleanup)
- DOMContentLoaded vs load
- Custom events

## Lesson

### Basic event
```javascript
button.addEventListener("click", (e) => {
    console.log("Clicked!", e.target);
});
```

### Event delegation
```javascript
list.addEventListener("click", (e) => {
    const item = e.target.closest(".item");
    if (item) item.classList.toggle("done");
});
```

### Prevent default
```javascript
form.addEventListener("submit", (e) => {
    e.preventDefault();
    // handle with JS
});
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.html` — Create a button that changes its own text to "Clicked!" when clicked. Use `addEventListener` and `event.target`.
2. `easy/p02-solve.html` — Create an input field that prints its value in real-time as you type. Use the `input` event and `event.target.value`.
3. `easy/p03-solve.html` — Create a link (`<a href="https://google.com">`) that DOESN'T navigate when clicked. Use `preventDefault()` and show an alert instead.

### Medium
4. `medium/p01-solve.html` — Create a list of 5 items. Use event delegation: ONE listener on the `<ul>` that logs which `<li>` was clicked. Use `event.target` or `closest()`.
5. `medium/p02-solve.html` — Create a form with name and email. On submit: prevent default, validate (both fields required), show success or error message. No page reload.
6. `medium/p03-solve.html` — Create a keyboard shortcut: pressing Ctrl+K focuses a search input. Pressing Escape clears it. Use `keydown` event with `e.ctrlKey` and `e.key`.

### Hard
7. `hard/p01-solve.html` — Build a dropdown menu: click to open, click outside to close. Use event delegation and `stopPropagation()`. Add keyboard support (Escape to close).
8. `hard/p02-solve.html` — Build a draggable element: mousedown starts drag, mousemove updates position, mouseup ends drag. Track position with `event.clientX/clientY`. Add a "dropped" custom event.
9. `hard/p03-solve.html` — Build an infinite scroll page: listen to `scroll` event, detect when user is near the bottom (scrollY + innerHeight >= documentHeight - 100), load more content (simulate with setTimeout). Use `removeEventListener` to clean up when done.

### How to work
- Write your complete HTML + CSS + JS solution.
- Remove the TODO comment when done.
- Open in browser to test.
