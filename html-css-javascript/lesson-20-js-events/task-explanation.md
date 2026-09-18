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

   ```
   WHAT IT SHOULD LOOK LIKE:
   BEFORE click:            AFTER click:
   [ Click me ]             [ Clicked! ]   <- same button,
                                             text swapped
   ```
2. `easy/p02-solve.html` — Create an input field that prints its value in real-time as you type. Use the `input` event and `event.target.value`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Input: [ hello______ ]
   You typed: hello         <- paragraph mirrors the input
                               on EVERY keystroke (input event)
   ```
3. `easy/p03-solve.html` — Create a link (`<a href="https://google.com">`) that DOESN'T navigate when clicked. Use `preventDefault()` and show an alert instead.

   ```
   WHAT IT SHOULD LOOK LIKE:
   link: https://google.com  <- click it...
           |
           v
   +----------------------------+
   | alert("Navigation blocked")|   <- alert pops instead;
   +----------------------------+      the page never navigates
   ```

### Medium
4. `medium/p01-solve.html` — Create a list of 5 items. Use event delegation: ONE listener on the `<ul>` that logs which `<li>` was clicked. Use `event.target` or `closest()`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   - Item 1
   - Item 2
   - Item 3   <- click any li...
   - Item 4        console logs:  "Clicked: Item 3"
   - Item 5        (ONE listener on the <ul>, via delegation)
   ```
5. `medium/p02-solve.html` — Create a form with name and email. On submit: prevent default, validate (both fields required), show success or error message. No page reload.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Name:  [__________]
   Email: [__________]
   [ Submit ]
   empty fields -> "Both fields are required"   (red error)
   both filled  -> "Submitted successfully!"    (green success)
                   -- the page never reloads
   ```
6. `medium/p03-solve.html` — Create a keyboard shortcut: pressing Ctrl+K focuses a search input. Pressing Escape clears it. Use `keydown` event with `e.ctrlKey` and `e.key`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Search: [____________]
   Ctrl+K pressed anywhere -> cursor jumps into the field
   Esc pressed in the field -> text cleared, focus dropped
   ```

### Hard
7. `hard/p01-solve.html` — Build a dropdown menu: click to open, click outside to close. Use event delegation and `stopPropagation()`. Add keyboard support (Escape to close).

   ```
   WHAT IT SHOULD LOOK LIKE:
   CLOSED:                 OPEN (after click):
   [ Menu  v ]             [ Menu  ^ ]
                           +-----------+
                           | Profile   |   <- closes on outside click
                           | Settings  |      or the Escape key
                           | Logout    |
                           +-----------+
   ```
8. `hard/p02-solve.html` — Build a draggable element: mousedown starts drag, mousemove updates position, mouseup ends drag. Track position with `event.clientX/clientY`. Add a "dropped" custom event.

   ```
   WHAT IT SHOULD LOOK LIKE:
   BEFORE drag:                 WHILE dragging:
                                 (cursor) --->   +---+
   +---+                                       |box|   <- follows the
   |box|                                       +---+      cursor
   +---+
   mouseup -> "dropped" custom event logs final x, y coords
   ```
9. `hard/p03-solve.html` — Build an infinite scroll page: listen to `scroll` event, detect when user is near the bottom (scrollY + innerHeight >= documentHeight - 100), load more content (simulate with setTimeout). Use `removeEventListener` to clean up when done.

   ```
   WHAT IT SHOULD LOOK LIKE:
   - item 1
   - item 2
      ... (scroll toward the bottom) ...
   - item 20
   [ Loading more... ]   <- appears near the bottom,
   - item 21                  then new items append
   - item 22
   ```

### How to work
- Write your complete HTML + CSS + JS solution.
- Remove the TODO comment when done.
- Open in browser to test.
