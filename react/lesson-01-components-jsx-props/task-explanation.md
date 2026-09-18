# Lesson 01 — Components, JSX & Props

## What you'll learn
- What a React component is.
- How JSX works (HTML-like syntax in JS).
- How to pass data into components with **props**.

## Lesson

A React component is a JavaScript function that returns **JSX** — syntax that looks like HTML but compiles to JavaScript.

```jsx
function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}
```
- `name` is a **prop** — data passed from a parent.
- `{name}` is a JS expression embedded in JSX (curly braces).
- Component names **must start with a capital letter**.

Using the component:
```jsx
function App() {
  return <Greeting name="Akash" />;
}
```

### Key rules
- One component per concept; keep them small and reusable.
- Props are **read-only** — never mutate them.
- You can render lists of components, but each needs a unique `key` (covered in Lesson 03).
- A component must return a **single root element** (or a Fragment `<>...</>`).

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-greeting-component.jsx` — component with one `name` prop, renders `<h1>`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------------------+
   | Hello, Dev!                      |   <- single <h1>
   +----------------------------------+
   ```
2. `easy/p02-button-component.jsx` — button with `label` and `color` props, inline style.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------+
   | [  Save  ] |   <- <button>, background #3498db (blue)
   +------------+
   ```
3. `easy/p03-badge-component.jsx` — badge with `text` and `variant` props, conditional color.

   WHAT IT SHOULD LOOK LIKE:
   ```
    ____
   ( New )    <- pill-shaped <span>, green bg for variant="success"
    ----
   ```

### Medium
4. `medium/p01-user-card.jsx` — user card with name/email/role props + App rendering 3 cards.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-------------------------------+
   | Alice                         |   <- <h3> name
   | alice@example.com             |   <- <p> email
   | [Admin]                       |   <- colored role tag (<span>)
   +-------------------------------+
   | Bob                           |
   | bob@example.com               |
   | [User]                        |
   +-------------------------------+
   | Carol                         |
   | carol@example.com             |
   | [Editor]                      |
   +-------------------------------+
      3 bordered cards, stacked
   ```
5. `medium/p02-price-list.jsx` — render a list from an array prop using `.map()` with keys.

   WHAT IT SHOULD LOOK LIKE:
   ```
   * Apple: $1.5
   * Bread: $2.25
      <- <ul> with one <li key> per item
   ```
6. `medium/p03-alert-component.jsx` — alert with message/type/show props, conditional render.

   WHAT IT SHOULD LOOK LIKE:
   ```
   show={true}:                    show={false}:
   +---------------------------+   (nothing on the page —
   | Saved!                    |    component returns null)
   +---------------------------+
     green banner for type="success"
   ```

### Hard
7. `hard/p01-reusable-table.jsx` — generic data table from `columns` and `rows` props.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-------+-----+
   | Name  | Age |    <- <thead> built from columns prop
   +-------+-----+
   | Amy   | 30  |    <- <tr> per row object
   | Ben   | 25  |
   +-------+-----+
   ```
8. `hard/p02-nested-comment-tree.jsx` — recursive Comment component rendering replies.

   WHAT IT SHOULD LOOK LIKE:
   ```
   | Amy
   | Great post!
   |  | Bob                          <- reply nested + indented
   |  | Thanks!                         (left border on each level)
   ```
9. `hard/p03-layout-composition.jsx` — Layout/Header/Footer using `children` prop pattern.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +--------------------------------------+
   | My Site Title                        |  <- <header> dark bar w/ <h1>
   +--------------------------------------+
   |                                      |
   | Welcome to my page                   |  <- <main> wraps children
   |                                      |
   +--------------------------------------+
   | (c) 2025 My Site                     |  <- <footer> bar
   +--------------------------------------+
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete component from scratch** below the TODO marker.
- Remove the TODO line when done.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
