# Lesson 03 — Concepts Explained (Event Handling in React)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Event Handling in React

**What:** React lets you respond to user actions (clicks, typing, hovering, submitting) by passing a function to an event prop like `onClick`, `onChange`, `onSubmit`.

```jsx
function Button() {
  const handleClick = () => {
    console.log("Button clicked!");
  };
  return <button onClick={handleClick}>Click me</button>;
}
```

In React, event props use camelCase (`onClick`, not `onclick`). You pass a FUNCTION, not a string of code.

**Why it exists:** Without event handling, components are static displays. Event handling makes UIs interactive — buttons do things, inputs capture data, forms submit.

**Where it's used:** Every interactive element — buttons, links, inputs, forms, dropdowns, drag-and-drop, keyboard shortcuts.

**What goes wrong without it:**
- Using HTML syntax: `onclick="handleClick()"` → React ignores it (needs `onClick={handleClick}`).
- Calling the function instead of passing it: `onClick={handleClick()}` → runs immediately on render, not on click. Must be `onClick={handleClick}` (no parentheses).
- Using lowercase: `onclick={handleClick}` → React doesn't recognize it (needs camelCase `onClick`).

---

## onClick Handler

**What:** `onClick` fires when a user clicks an element (button, div, link, etc.).

```jsx
function LikeButton() {
  const [likes, setLikes] = useState(0);
  return <button onClick={() => setLikes(likes + 1)}>❤ {likes}</button>;
}

// Passing arguments with arrow function
function ItemList({ items, onSelect }) {
  return items.map(item => (
    <li key={item.id} onClick={() => onSelect(item.id)}>
      {item.name}
    </li>
  ));
}
```

**Why it exists:** Clicking is the most common user interaction. `onClick` provides a clean way to respond to clicks without manual event listener setup (`addEventListener`).

**Where it's used:** Buttons (submit, like, delete), list item selection, card clicks, tab switching, menu toggles.

**What goes wrong without it:**
- `onClick={handleClick()}` → function runs during render, not on click. The return value (often `undefined`) becomes the handler — clicking does nothing.
- Passing arguments directly: `onClick={handleClick(item.id)}` → runs immediately. Must wrap: `onClick={() => handleClick(item.id)}`.
- Forgetting the handler on a `<div>` without a role → not accessible. Use `<button>` for clickable things.

---

## onChange Handler

**What:** `onChange` fires when the value of an input, textarea, or select changes (every keystroke for text inputs).

```jsx
function NameInput() {
  const [name, setName] = useState("");
  return (
    <input
      type="text"
      value={name}
      onChange={(e) => setName(e.target.value)}
      placeholder="Enter your name"
    />
  );
}
```

`e.target.value` gives the current value of the input. For checkboxes, use `e.target.checked` instead.

**Why it exists:** You need to capture user input as they type. `onChange` fires on every keystroke, letting you update state in real time and keep the input in sync.

**Where it's used:** Text inputs, textareas, selects, checkboxes, radio buttons, search bars, any field where user types or selects.

**What goes wrong without it:**
- No `onChange` on a controlled input with `value={state}` → React warns: input is read-only. You can't type.
- Using `e.value` instead of `e.target.value` → `undefined`. Must be `e.target.value`.
- Forgetting to update state in `onChange` → input appears frozen (can't type because `value` never changes).
- Checkbox: using `e.target.value` → always "on". Must use `e.target.checked` for boolean.

---

## onSubmit Handler

**What:** `onSubmit` fires when a form is submitted (user presses Enter or clicks a submit button).

```jsx
function LoginForm() {
  const [email, setEmail] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();  // CRITICAL — stops page reload
    console.log("Form submitted with:", email);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={email} onChange={(e) => setEmail(e.target.value)} />
      <button type="submit">Login</button>
    </form>
  );
}
```

**Why it exists:** Forms are fundamental to web apps — login, signup, search, checkout. `onSubmit` gives you a single place to handle the entire form submission, collecting all field values at once.

**Where it's used:** Login forms, signup forms, search bars, contact forms, checkout forms, any data submission.

**What goes wrong without it:**
- Missing `e.preventDefault()` → the browser reloads the page and your data is lost. This is the #1 form bug.
- Putting `onClick` on the submit button instead of `onSubmit` on the form → pressing Enter doesn't submit (only button click works).
- Button type not set: `<button>` defaults to `type="submit"` inside a form. If you don't want it to submit, use `type="button"`.
- `onSubmit` on a `<div>` instead of `<form>` → doesn't work. `onSubmit` only works on `<form>` elements.

---

## Synthetic Events

**What:** React wraps native browser events in a `SyntheticEvent` — a cross-browser wrapper that behaves identically across all browsers.

```jsx
const handleClick = (e) => {
  console.log(e.type);        // "click"
  console.log(e.target);      // the DOM element clicked
  console.log(e.currentTarget); // the element with the handler
  console.log(e.clientX, e.clientY); // mouse coordinates
};

const handleChange = (e) => {
  console.log(e.target.value);  // input's current value
  console.log(e.target.name);   // input's name attribute
};
```

The `e` object has the same properties as native events (`target`, `currentTarget`, `preventDefault()`, `stopPropagation()`, `key`, `keyCode`, etc.) but works consistently across browsers.

**Why it exists:** Before React, different browsers had different event objects (IE vs. Firefox vs. Chrome). Synthetic events normalize this — you write one handler, it works everywhere.

**Where it's used:** Every event handler in React. You access `e.target.value` for inputs, `e.key` for keyboard events, `e.preventDefault()` for forms.

**What goes wrong without it:**
- Accessing `e` asynchronously: `setTimeout(() => console.log(e.target.value), 100)` → `e` is null! React pools and recycles synthetic events. Use `e.persist()` or extract the value first: `const value = e.target.value; setTimeout(() => console.log(value), 100)`.
- Confusing `e.target` (element that triggered event) vs `e.currentTarget` (element with the listener) → wrong element accessed in bubbling scenarios.
- Using native event API directly: `e.nativeEvent` → usually unnecessary and browser-specific.

---

## preventDefault

**What:** `e.preventDefault()` stops the browser's default behavior for an event.

```jsx
const handleSubmit = (e) => {
  e.preventDefault();  // stops form from reloading the page
  // now handle submission with JavaScript
};

const handleLinkClick = (e) => {
  e.preventDefault();  // stops navigation
  // do custom routing instead
};
```

**Why it exists:** HTML forms reload the page on submit by default. Links navigate to a new URL by default. In a React SPA (single-page app), you don't want page reloads — you want to handle everything in JavaScript. `preventDefault` lets you override browser defaults.

**Where it's used:** Form submissions (prevent reload), link clicks (prevent navigation in SPAs), right-click menus (prevent context menu), keyboard shortcuts (prevent default browser actions).

**What goes wrong without it:**
- Form submit without `preventDefault()` → page reloads → all state is lost → user sees a blank page. This is the most common React form bug.
- Link without `preventDefault()` → browser navigates away from your SPA → app reloads.
- Calling `preventDefault()` after async operations → too late, the default already happened. Call it synchronously at the top of the handler.

---

## Event Object Properties

**What:** The event object (`e`) contains useful properties about what happened.

```jsx
// Input events
const handleChange = (e) => {
  console.log(e.target.value);  // current input value
  console.log(e.target.name);   // name attribute
  console.log(e.target.type);   // "text", "checkbox", etc.
  console.log(e.target.checked); // for checkboxes: true/false
};

// Keyboard events
const handleKeyDown = (e) => {
  console.log(e.key);   // "Enter", "Escape", "a", etc.
  if (e.key === "Enter") {
    // handle Enter key
  }
};

// Mouse events
const handleClick = (e) => {
  console.log(e.clientX, e.clientY);  // mouse position
  console.log(e.button);  // 0=left, 1=middle, 2=right
};
```

**Why it exists:** You need to know WHAT the user did — what key they pressed, what value they typed, which element they clicked. The event object carries all this information.

**Where it's used:** Form inputs (get typed value), keyboard shortcuts (check which key), drag-and-drop (mouse position), checkboxes (checked state).

**What goes wrong without it:**
- Using `e.value` instead of `e.target.value` → `undefined`. The value is on the DOM element (`target`), not the event itself.
- Checkbox: `e.target.value` → always "on" regardless of checked state. Must use `e.target.checked`.
- Keyboard: `e.keyCode` → deprecated. Use `e.key` for the key name ("Enter", "Escape").

---

## Passing Arguments to Handlers

**What:** When you need to pass extra arguments to an event handler, wrap it in an arrow function.

```jsx
function ItemList({ items, onDelete }) {
  return items.map(item => (
    <div key={item.id}>
      {item.name}
      {/* WRONG: runs immediately */}
      <button onClick={handleDelete(item.id)}>Delete</button>

      {/* RIGHT: runs on click */}
      <button onClick={() => handleDelete(item.id)}>Delete</button>
    </div>
  ));
}
```

**Why it exists:** `onClick={handleDelete(item.id)}` calls the function during render (it executes immediately). Wrapping in `() =>` creates a new function that runs only when clicked, with `item.id` captured from the closure.

**Where it's used:** List items with delete/edit buttons, passing row data to handlers, any time you need to pass custom arguments to an event handler.

**What goes wrong without it:**
- `onClick={handleDelete(item.id)}` → function runs on EVERY render for EVERY item → deletes items immediately, not on click.
- `onClick={handleDelete}` → no way to pass `item.id` — the handler only gets the event object.
- Performance: creating arrow functions in render creates new function references each render. For most cases this is fine; for heavy lists, use `useCallback` (covered in Lesson 09).

---

## Event Propagation (Bubbling & Delegation)

**What:** Events in the DOM bubble up — when you click a child, the event also fires on all parent elements. `e.stopPropagation()` stops this.

```jsx
function Card({ onDelete }) {
  const handleClick = (e) => {
    e.stopPropagation();  // stops click from reaching the card
    onDelete();
  };

  return (
    <div onClick={() => console.log("Card clicked")}>
      <h3>Card Title</h3>
      <button onClick={handleClick}>Delete</button>
    </div>
  );
}
// Without stopPropagation: clicking Delete logs "Card clicked" AND calls onDelete.
// With stopPropagation: only onDelete runs.
```

**Why it exists:** Without `stopPropagation`, clicking a button inside a clickable card triggers BOTH handlers — the button's and the card's. This causes unexpected behavior (delete + navigate, or close + open a modal).

**Where it's used:** Buttons inside clickable cards, modals inside overlay click handlers, dropdown items inside a toggle button, nested interactive elements.

**What goes wrong without it:**
- Delete button inside a clickable row → clicking delete also triggers row click → item gets deleted AND navigated to.
- Modal close on overlay click → clicking inside the modal also closes it (event bubbles to overlay). Use `stopPropagation` on the modal container.
- Forgetting `stopPropagation` → double actions, modals closing immediately, dropdowns toggling on item click.

---

## Keyboard Events

**What:** React provides `onKeyDown`, `onKeyPress`, and `onKeyUp` for handling keyboard input. `onKeyDown` is the most commonly used.

```jsx
function SearchBar({ onSearch }) {
  const [query, setQuery] = useState("");

  const handleKeyDown = (e) => {
    if (e.key === "Enter") {
      onSearch(query);
    }
    if (e.key === "Escape") {
      setQuery("");
    }
  };

  return (
    <input
      value={query}
      onChange={(e) => setQuery(e.target.value)}
      onKeyDown={handleKeyDown}
      placeholder="Search... (Enter to search, Esc to clear)"
    />
  );
}
```

**Why it exists:** Keyboard interactions are essential for accessibility and power-user features — Enter to submit, Escape to close, arrow keys to navigate, shortcuts.

**Where it's used:** Search inputs (Enter to search), modals (Escape to close), dropdowns (arrow keys to navigate), keyboard shortcuts, games.

**What goes wrong without it:**
- Using `onKeyPress` → deprecated, doesn't fire for some keys (like Escape, Backspace). Use `onKeyDown`.
- Checking `e.keyCode` → deprecated and browser-inconsistent. Use `e.key` which gives readable names ("Enter", "Escape", "ArrowUp").
- Forgetting keyboard handling → app is not accessible (screen reader users can't navigate).
- `onKeyDown` on a `<div>` → divs aren't focusable by default. Add `tabIndex={0}` or use a button/input.
