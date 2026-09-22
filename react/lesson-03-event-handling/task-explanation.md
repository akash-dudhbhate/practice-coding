# Lesson 03 — Event Handling in React

## What you'll learn
- How to handle clicks, input changes, and form submissions in React.
- The synthetic event object and its key properties.
- How to prevent default browser behavior with `preventDefault()`.
- Event propagation (bubbling) and how to stop it.

## Lesson

React events use camelCase (`onClick`, not `onclick`) and receive a function, not a string.

```jsx
function App() {
  const handleClick = (e) => {
    e.preventDefault();
    console.log("Clicked!", e.target);
  };
  return <button onClick={handleClick}>Click me</button>;
}
```

### Key event types
- **`onClick`** — element is clicked.
- **`onChange`** — input value changes (fires on every keystroke for text inputs).
- **`onSubmit`** — form is submitted (always call `e.preventDefault()` first).
- **`onKeyDown`** — a key is pressed (use `e.key` to check which key).

### Key rules
- Pass the **function reference**, not the call: `onClick={handleClick}`, not `onClick={handleClick()}`.
- To pass arguments, wrap in an arrow function: `onClick={() => handleClick(id)}`.
- Always call `e.preventDefault()` in form `onSubmit` handlers to stop page reload.
- Use `e.stopPropagation()` when a child click shouldn't trigger the parent's handler.
- Access input values via `e.target.value`; checkboxes via `e.target.checked`.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.jsx` — **Click Counter:** A button that increments a counter on click. Display the count. Practice `onClick` with a state update.

   WHAT IT SHOULD LOOK LIKE:
   ```
   BEFORE:                  AFTER 2 CLICKS:
   +----------------+       +----------------+
   | [ Clicked: 0 ] |       | [ Clicked: 2 ] |
   +----------------+       +----------------+
   ```
2. `easy/p02-solve.jsx` — **Text Echo:** An input where each keystroke updates a paragraph below with the current text. Practice `onChange` and `e.target.value`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   | react                |   <- <input>
   +----------------------+
   react                       <- <p> mirrors each keystroke
   ```
3. `easy/p03-solve.jsx` — **Double-Click Alert:** A box that changes color on single click and shows a message on double click (`onDoubleClick`). Practice multiple event handlers.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------+        +----------+
   | ######## |        | %%%%%%%% |   <- 100px box; click flips
   | ######## |  click | %%%%%%%% |      its color
   +----------+        +----------+
   double-click -> browser alert: "Double clicked!"
   ```

### Medium
4. `medium/p01-solve.jsx` — **Login Form:** A form with email and password inputs. On submit, prevent default and display the entered credentials. Practice `onSubmit` + `preventDefault`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   | a@b.com              |   <- email input
   +----------------------+
   | ********             |   <- password input
   +----------------------+
   [ Login ]
   Email: a@b.com, Password: secret   <- <p> appears after submit
   ```
5. `medium/p02-solve.jsx` — **Todo with Delete Buttons:** A todo list where each item has a delete button. Clicking delete removes that item (pass the id to the handler). Practice passing arguments to handlers.

   WHAT IT SHOULD LOOK LIKE:
   ```
   * Buy milk        [Delete]
   * Walk the dog    [Delete]
     <- clicking Delete removes only that <li>
   ```
6. `medium/p03-solve.jsx` — **Search with Enter Key:** A search input that triggers search on Enter key and clears on Escape. Practice `onKeyDown` and `e.key`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   | react                |   <- type, press Enter
   +----------------------+
   Search result: react           <- <p> after Enter
   (Escape clears input + result)
   ```

### Hard
7. `hard/p01-solve.jsx` — **Clickable Card with Inner Button:** A card that logs "Card clicked" when clicked, with a "Details" button inside that logs "Details" WITHOUT triggering the card click. Practice `stopPropagation`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------------+
   |  Card content                |
   |                  [ Details ] |  <- inner button: logs only
   +------------------------------+      "Details" (stopPropagation)
   Log: Card clicked, Details         <- <p> log grows on clicks
   ```
8. `hard/p02-solve.jsx` — **Multi-Input Form with Validation:** A registration form with name, email, and password. Validate on submit (all fields required, email must contain "@"). Show errors inline. Practice form submission + validation.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------+
   |                      |   <- name input
   +----------------------+
   Name is required           <- red <span> error
   +----------------------+
   | bad-email            |
   +----------------------+
   Email must contain @       <- red <span> error
   +----------------------+
   |                      |
   +----------------------+
   Password is required       <- red <span> error
   [ Register ]
   ```
9. `hard/p03-solve.jsx` — **Keyboard-Navigable Dropdown:** A dropdown menu you can open with Enter, navigate with arrow keys, and close with Escape. Practice keyboard events + state management.

   WHAT IT SHOULD LOOK LIKE:
   ```
   CLOSED:                  OPEN (after Enter):
   +------------------+     +------------------+
   | Select...      v |     | Select...      ^ |
   +------------------+     +------------------+
                            | Apple            |
                            |> Banana          |  <- highlighted via
                            | Cherry           |     arrow keys
                            +------------------+
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete component from scratch** below the TODO marker.
- Remove the TODO line when done.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
