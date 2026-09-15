# Lesson 20 — Concepts Explained (JS Events & Interactivity)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## addEventListener

**What:** `addEventListener` attaches a function that runs when an event occurs on an element.

```javascript
const button = document.querySelector("#myButton");

button.addEventListener("click", function(event) {
    console.log("Button clicked!");
    console.log(event.target);  // the element that was clicked
});

// Arrow function
button.addEventListener("click", (e) => {
    e.target.style.background = "blue";
});

// Multiple listeners on same element
button.addEventListener("click", handler1);
button.addEventListener("click", handler2);  // both run
```

**Why it exists:** Without `addEventListener`, you'd use `onclick` attributes in HTML (`<button onclick="doSomething()">`) → mixing HTML and JS → hard to maintain. `addEventListener` separates behavior from structure.

**Where it's used:** Every interactive web page — clicks, keypresses, form submissions, scrolls, hovers, drag-and-drop.

**What goes wrong without it:**
- `element.onclick = handler` → only allows ONE handler. `addEventListener` → multiple handlers on same event.
- Forgetting to remove listeners → memory leaks, especially for dynamically created elements.
- `addEventListener("click", handler())` → calls `handler` immediately (parentheses) instead of passing the function. Use `handler` without parentheses.

---

## Event Object

**What:** The event object contains information about the event.

```javascript
button.addEventListener("click", (event) => {
    event.target;          // element that triggered the event
    event.currentTarget;   // element the listener is attached to
    event.type;            // "click"
    event.clientX;         // X coordinate of mouse
    event.clientY;         // Y coordinate of mouse
    event.key;             // key pressed (for keyboard events)
    event.preventDefault();  // prevent default behavior
    event.stopPropagation(); // stop event bubbling
});
```

**Why it exists:** Without the event object, you can't know WHAT was clicked, WHERE the mouse was, or WHAT key was pressed. The event object provides all context about the event.

**Where it's used:** Every event handler — need to know what element, what key, what position, or prevent default behavior.

**What goes wrong without it:**
- `event.target` vs `event.currentTarget`: `target` = the element that was actually clicked (could be a child). `currentTarget` = the element with the listener. Different in bubbling.
- `event.key` vs `event.keyCode`: `keyCode` is deprecated. Use `event.key` ("Enter", "a", "1") for modern code.
- Forgetting `event` parameter → `event is not defined`. Always include it (or use `e`).

---

## Event Types

**What:** Common DOM events:

```javascript
// Mouse events
"click"          // click and release
"dblclick"       // double click
"mousedown"      // mouse button pressed
"mouseup"        // mouse button released
"mouseenter"     // mouse enters element (no bubbling)
"mouseleave"     // mouse leaves element (no bubbling)
"mousemove"      // mouse moves over element

// Keyboard events
"keydown"        // key pressed down (fires repeatedly)
"keyup"          // key released
"keypress"       // deprecated, use keydown

// Form events
"submit"         // form submitted
"change"         // input value changed (on blur)
"input"          // input value changing (real-time)
"focus"          // element gained focus
"blur"           // element lost focus

// Other events
"scroll"         // page or element scrolled
"resize"         // window resized
"load"           // page or resource loaded
"DOMContentLoaded"  // DOM fully parsed
```

**Why it exists:** Different user actions trigger different events. Knowing which event to use is key to building responsive UIs.

**Where it's used:** Every interactive feature — buttons (click), forms (submit, input), search (input), keyboard shortcuts (keydown), infinite scroll (scroll).

**What goes wrong without it:**
- `change` vs `input`: `change` fires when the input loses focus (after editing). `input` fires on every keystroke. For real-time search, use `input`.
- `keydown` vs `keyup`: `keydown` fires when key is pressed (before release). `keyup` fires after release. For shortcuts, use `keydown`.
- `keypress` is deprecated → use `keydown` instead.

---

## Event Bubbling and Capturing

**What:** Events flow through the DOM in three phases:
1. **Capturing** — from document down to the target (top-down)
2. **Target** — at the target element
3. **Bubbling** — from target up to document (bottom-up)

```html
<div id="outer">
    <div id="inner">
        <button id="btn">Click</button>
    </div>
</div>
```

```javascript
// Bubbling (default): btn → inner → outer
document.querySelector("#outer").addEventListener("click", () => {
    console.log("Outer clicked");  // fires LAST (bubbles up)
});

// Capturing: outer → inner → btn
document.querySelector("#outer").addEventListener("click", () => {
    console.log("Outer clicked (capture)");  // fires FIRST
}, true);  // true = capturing phase

// Stop bubbling
button.addEventListener("click", (e) => {
    e.stopPropagation();  // event doesn't bubble to outer
});
```

**Why it exists:** Bubbling enables event delegation (one listener on parent handles all children). Capturing is less common but useful for intercepting events before they reach the target.

**Where it's used:** Event delegation (bubbling), preventing unwanted parent handlers (stopPropagation), custom event systems.

**What goes wrong without it:**
- Clicking a button inside a card → both button AND card click handlers fire → unexpected behavior. Use `stopPropagation()` if needed.
- `stopPropagation()` prevents the event from reaching other ancestors, but NOT other listeners on the same element. Use `stopImmediatePropagation()` for that.
- Capturing is rarely needed. Most developers use bubbling (default).

---

## Event Delegation

**What:** Instead of adding listeners to each child, add ONE listener to the parent. Use `event.target` to determine which child was clicked.

```javascript
// BAD: add listener to each item
document.querySelectorAll(".item").forEach(item => {
    item.addEventListener("click", () => console.log(item.textContent));
});

// GOOD: one listener on parent (event delegation)
document.querySelector(".list").addEventListener("click", (e) => {
    if (e.target.classList.contains("item")) {
        console.log(e.target.textContent);
    }
});

// Even better: use closest() for nested structures
document.querySelector(".list").addEventListener("click", (e) => {
    const item = e.target.closest(".item");
    if (item) {
        console.log(item.textContent);
    }
});
```

**Why it exists:** Without delegation, adding listeners to 100 items → 100 listeners → memory and performance issues. Delegation → 1 listener → efficient. Also handles dynamically added items automatically.

**Where it's used:** Lists with many items, dynamically generated content, tables, menus, any repeating structure.

**What goes wrong without it:**
- Forgetting to check `e.target` → clicking a child element (like an icon inside the item) → wrong element logged. Use `closest(".item")` to find the right element.
- Adding listeners to each item → dynamically added items don't have listeners → broken. Delegation handles new items automatically.
- `e.target` might be the parent itself (clicked between items) → check if it matches the expected selector.

---

## preventDefault

**What:** Stop the default browser behavior for an event.

```javascript
// Prevent form from submitting (page reload)
form.addEventListener("submit", (e) => {
    e.preventDefault();
    // handle form with JS (AJAX, fetch, etc.)
});

// Prevent link from navigating
link.addEventListener("click", (e) => {
    e.preventDefault();
    // handle navigation with JS (SPA routing)
});

// Prevent context menu (right-click)
document.addEventListener("contextmenu", (e) => {
    e.preventDefault();
    // show custom menu instead
});
```

**Why it exists:** Without `preventDefault`, forms reload the page, links navigate away, right-click shows browser menu. For SPAs and dynamic apps, you need to handle these with JavaScript instead.

**Where it's used:** Form handling (AJAX submit), SPA routing, custom context menus, drag-and-drop, keyboard shortcuts.

**What goes wrong without it:**
- Forgetting `preventDefault()` on form submit → page reloads → all state lost → user sees a flash.
- `preventDefault()` on ALL clicks → links don't work → broken navigation. Only prevent specific events.
- `preventDefault()` doesn't stop bubbling. Use `stopPropagation()` separately if needed.

---

## Keyboard Events

**What:** Handle keyboard input.

```javascript
document.addEventListener("keydown", (e) => {
    console.log(e.key);       // "Enter", "a", "1", "ArrowUp"
    console.log(e.code);      // "KeyA", "Digit1", "ArrowUp"
    console.log(e.ctrlKey);   // true if Ctrl is held
    console.log(e.shiftKey);  // true if Shift is held
    console.log(e.altKey);    // true if Alt is held
    console.log(e.metaKey);   // true if Cmd (Mac) or Win key

    // Keyboard shortcut
    if (e.ctrlKey && e.key === "s") {
        e.preventDefault();
        saveDocument();
    }
});
```

**Why it exists:** Without keyboard events, you can't build keyboard shortcuts, games, text editors, or accessible interfaces. Keyboard events are essential for power users and accessibility.

**Where it's used:** Keyboard shortcuts (Ctrl+S, Ctrl+K), games (arrow keys), search (Enter to search), accessibility (Tab navigation).

**What goes wrong without it:**
- `e.key` vs `e.code`: `e.key` = the character ("a", "A" — affected by Shift). `e.code` = the physical key ("KeyA" — not affected by Shift). Use `e.key` for characters, `e.code` for game controls.
- `keydown` fires repeatedly while key is held → use a flag or debounce for actions that should fire once.
- Global keyboard listeners → can interfere with form inputs (Ctrl+S while typing in a form). Check `e.target` to avoid.

---

## removeEventListener

**What:** Remove a previously added event listener.

```javascript
function handleClick(e) {
    console.log("Clicked");
}

button.addEventListener("click", handleClick);
// Later...
button.removeEventListener("click", handleClick);  // removes the listener

// IMPORTANT: must be the SAME function reference
button.addEventListener("click", () => console.log("Hi"));
// Can't remove this — the arrow function is a new reference each time
```

**Why it exists:** Without removing listeners, they accumulate → memory leaks, especially for dynamically created elements. Also useful for one-time events (remove after first trigger).

**Where it's used:** Cleanup when removing elements, one-time events, conditional listeners (enable/disable based on state).

**What goes wrong without it:**
- Can't remove anonymous functions: `addEventListener("click", () => {})` → no reference to remove. Always use named functions if you need to remove.
- Forgetting to remove listeners on dynamically removed elements → element is removed from DOM but listener still holds a reference → memory leak.
- `removeEventListener` must match: same event type, same function, same capture flag. Mismatch → silently doesn't remove.

---

## DOMContentLoaded vs load

**What:** Know when the page is ready for JavaScript.

```javascript
// DOM is parsed (HTML ready, but images may not be loaded)
document.addEventListener("DOMContentLoaded", () => {
    // Safe to select and manipulate DOM elements
    document.querySelector("#app").textContent = "Ready!";
});

// Everything is loaded (images, stylesheets, etc.)
window.addEventListener("load", () => {
    // Safe to measure image sizes, canvas dimensions, etc.
    const imgWidth = document.querySelector("img").naturalWidth;
});
```

**Why it exists:** Without these events, JS might run before the DOM is ready → `querySelector` returns `null` → errors. These events tell you when it's safe to interact with the page.

**Where it's used:** Every script that manipulates the DOM. `DOMContentLoaded` is most common — runs as soon as HTML is parsed, without waiting for images.

**What goes wrong without it:**
- Script in `<head>` without `DOMContentLoaded` → DOM not ready → `querySelector("#app")` → `null` → error. Move script to end of `<body>` or use `DOMContentLoaded`.
- `load` is slower than `DOMContentLoaded` → waits for all resources. Use `DOMContentLoaded` unless you need image dimensions.
- `defer` attribute on `<script>` → script runs after DOM is parsed → equivalent to `DOMContentLoaded` but cleaner. Use `<script defer src="app.js">`.

---

## Custom Events

**What:** Create and dispatch your own events.

```javascript
// Create a custom event
const event = new CustomEvent("userLoggedIn", {
    detail: { userId: 123, name: "Akash" }
});

// Listen for it
document.addEventListener("userLoggedIn", (e) => {
    console.log(`Welcome, ${e.detail.name}!`);
});

// Dispatch it
document.dispatchEvent(event);
// → "Welcome, Akash!"
```

**Why it exists:** Without custom events, components can't communicate without direct references. Custom events enable decoupled architecture — a login component emits "userLoggedIn" → any component can listen without knowing about the login component.

**Where it's used:** Component communication, pub/sub patterns, state management, plugin systems.

**What goes wrong without it:**
- Custom event data is in `event.detail`, not `event.data` or directly on the event. Forgetting `.detail` → undefined.
- Overusing custom events → hard to trace which component emits and which listens → debugging nightmare. Use sparingly.
- Custom events on `document` → global. Consider scoping to a specific element for better encapsulation.
