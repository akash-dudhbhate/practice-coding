# Lesson 01 — Concepts Explained (Components, JSX & Props)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## React Component

**What:** A component is a reusable piece of UI — like a LEGO block for your website. It's a JavaScript function that returns JSX.

```jsx
function Greeting() {
  return <h1>Hello!</h1>;
}
// Usage: <Greeting />
```

Component names MUST start with a capital letter (`Greeting`, not `greeting`).

**Why it exists:** Before components, web pages were one giant HTML file. Change a button? Find it in 2000 lines. Components let you split UI into small, reusable, testable pieces — like functions for UI.

**Where it's used:** Every React app is a tree of components. A page = `<Layout>` containing `<Header>`, `<Sidebar>`, `<Article>`, each containing smaller components.

**What goes wrong without it:**
- One giant file — impossible to maintain, no reuse, can't test individual pieces.
- Same UI duplicated across pages — fix a button in one place, forget the other 10.
- Lowercase component names → React treats them as HTML tags (renders nothing or a warning).

---

## JSX

**What:** JSX is syntax that lets you write HTML-like code inside JavaScript. It looks like HTML but compiles to JavaScript.

```jsx
const element = <h1>Hello, world!</h1>;
const name = "Akash";
const element = <h1>Hello, {name}!</h1>;  // {} embeds JS expressions
```

JSX must return a SINGLE root element. Wrap multiple elements in a Fragment: `<>...</>`.

**Why it exists:** Before JSX, React used `React.createElement()` calls — verbose and hard to read. JSX lets you write UI in a familiar HTML-like syntax while having full JavaScript power. It's the best of both worlds.

**Where it's used:** Every React component's return statement. Anywhere you describe what should render on screen.

**What goes wrong without it:**
- Using `React.createElement('h1', null, 'Hello')` instead of `<h1>Hello</h1>` — extremely verbose, unreadable for complex UIs.
- Forgetting curly braces: `<h1>Hello, name!</h1>` renders literal text "name!" not the variable. You need `{name}`.
- Multiple root elements: `return <h1>A</h1><p>B</p>` → syntax error. Must wrap in `<>...</>` or a `<div>`.

---

## Props

**What:** Props (properties) are how you pass data from a parent component to a child — like arguments to a function.

```jsx
function Greeting({ name }) {        // receive 'name' prop
  return <h1>Hello, {name}!</h1>;
}
<Greeting name="Akash" />            // pass name="Akash"
```

Props are READ-ONLY — never modify them inside the component.

**Why it exists:** Without props, every component would be identical — you couldn't customize a button's label, color, or click handler. Props make components reusable by letting parents configure them.

**Where it's used:** Every component that needs to be customizable. Buttons get `label` and `color` props, cards get `title` and `content` props, lists get `items` props.

**What goes wrong without it:**
- Hardcoded components — `<Button />` always says "Click me" in blue. Can't reuse it.
- Mutating props → React doesn't re-render correctly, data gets out of sync. Props are read-only by design.
- Forgetting to destructure: using `props.name` everywhere instead of `{ name }` → verbose, error-prone.

---

## Single Prop

**What:** The simplest form of props — passing one piece of data.

```jsx
function Greeting({ name }) {
  return <h1>Hi, {name}</h1>;
}
<Greeting name="Akash" />   // one prop: name
```

**Why it exists:** Many components only need one piece of data. Starting simple builds understanding before adding complexity.

**Where it's used:** Simple components — a greeting with a name, a label with text, an image with a src.

**What goes wrong without it:**
- Overcomplicating simple components with 10 props when 1 is enough.
- Not understanding single props makes multiple props harder to grasp.

---

## Multiple Props

**What:** Pass several props to a component, separated by spaces.

```jsx
function UserCard({ name, age, city }) {
  return <p>{name}, {age}, {city}</p>;
}
<UserCard name="Akash" age={25} city="Mumbai" />
```

String props use quotes (`name="Akash"`), number/boolean/expression props use curly braces (`age={25}`).

**Why it exists:** Real components need multiple pieces of data — a user card needs name, age, and city. A button needs label, color, size, and onClick.

**Where it's used:** Most real-world components accept multiple props.

**What goes wrong without it:**
- Using quotes for numbers: `age="25"` → age is a STRING "25", not number 25. `age + 1` gives "251" not 26.
- Forgetting curly braces for booleans: `disabled="false"` → it's the string "false" which is truthy! Use `disabled={false}`.

---

## Children Prop

**What:** The `children` prop is whatever you put BETWEEN the opening and closing tags of a component.

```jsx
function Card({ children }) {
  return <div className="card">{children}</div>;
}
<Card>
  <h1>Title</h1>     // this is 'children'
  <p>Content</p>     // this too
</Card>
```

**Why it exists:** Without `children`, you can't build wrapper/layout components. `children` lets a component wrap ANY content — the component provides structure, the parent decides what goes inside.

**Where it's used:** Layout components, cards, modals, sidebars, any component that wraps other content.

**What goes wrong without it:**
- Can't build reusable layouts — every page would need its own full structure.
- Hardcoding content inside a component → not reusable.
- Forgetting to render `{children}` → the wrapped content disappears.

---

## Conditional Inline Styles

**What:** In React, you apply styles dynamically using the `style` attribute with an object.

```jsx
function Badge({ variant }) {
  const colors = { success: "green", error: "red" };
  return <span style={{ color: colors[variant] }}>Text</span>;
}
```

Style uses an OBJECT with camelCase properties: `style={{ backgroundColor: "blue" }}`, NOT CSS strings.

**Why it exists:** Sometimes styles depend on data (status color, dynamic size). Inline styles let you compute styles in JavaScript without writing separate CSS files for every variation.

**Where it's used:** Dynamic styling — status badges, progress bars, themes, anything where the style changes based on state/props.

**What goes wrong without it:**
- Using CSS string syntax: `style="color: red"` → React ignores it (needs object syntax).
- Using CSS property names: `background-color` → doesn't work (must be camelCase `backgroundColor`).
- Overusing inline styles → hard to maintain. Use CSS classes for static styles, inline only for dynamic.

---

## Arrays of Objects

**What:** A common data structure — a list where each item is an object with named fields.

```jsx
const users = [
  { name: "Akash", age: 25 },
  { name: "Bob", age: 30 }
];
// Access: users[0].name -> "Akash"
```

**Why it exists:** Real data from APIs comes as arrays of objects. A user list, product list, or post list — each item has multiple fields. This structure maps naturally to rendering a list of components.

**Where it's used:** Rendering lists from API responses, displaying tables, user lists, product grids.

**What goes wrong without it:**
- Using separate arrays (`names = [...]`, `ages = [...]`) → data gets out of sync, hard to manage.
- Accessing wrong field: `user.title` when the field is `user.name` → renders `undefined`.

---

## .map() Method

**What:** `.map()` transforms each item in an array into something else and returns a NEW array.

```jsx
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2);  // [2, 4, 6]

// In React:
items.map(item => <li key={item.name}>{item.name}</li>)
```

Each element rendered by `.map()` MUST have a unique `key` prop.

**Why it exists:** In React, you constantly need to convert data arrays into element arrays. `.map()` is the cleanest way — it transforms data into UI in one line.

**Where it's used:** Rendering any list in React — dropdowns, tables, cards, navigation items.

**What goes wrong without it:**
- Using `for` loops in JSX → doesn't work cleanly, you'd need to build an array manually.
- Forgetting `key` → React warnings, potential rendering bugs when items reorder.
- Mutating inside `.map()` → it returns a new array, the original is unchanged. If you need to modify, use the result.

---

## Nested .map()

**What:** When you have arrays inside arrays (rows with cells), you use `.map()` inside `.map()`.

```jsx
rows.map(row =>
  <tr>
    {columns.map(col => <td key={col.key}>{row[col.key]}</td>)}
  </tr>
)
```

**Why it exists:** Some data is two-dimensional — a table has rows, each row has cells. You need an outer map for rows and an inner map for cells within each row.

**Where it's used:** Data tables, grids, nested lists, any 2D data structure.

**What goes wrong without it:**
- Flat mapping → you get a flat list of cells with no row grouping → broken table.
- Forgetting keys on inner map → same React warnings and bugs as missing keys on outer map.
- Confusing which data to map: mapping columns when you should map rows → wrong table structure.

---

## Dynamic Keys in React

**What:** When rendering a list with `.map()`, React requires a `key` prop on each item.

```jsx
items.map(item => <li key={item.id}>{item.name}</li>)
```

Keys must be UNIQUE among siblings. Good keys: `item.id`, `item.name`. Bad but acceptable: array index.

**Why it exists:** React uses keys to identify which items changed, were added, or were removed. Without keys, React might re-render the wrong items or lose state.

**Where it's used:** Every list rendered with `.map()`.

**What goes wrong without it:**
- Missing keys → React console warning, potential bugs when items reorder/insert/delete.
- Using index as key when list reorders → React confuses items, state gets attached to wrong item.
- Non-unique keys → React can't distinguish items → rendering bugs.

---

## Recursion

**What:** Recursion is when a function calls ITSELF to solve a smaller version of the same problem.

```jsx
function countDown(n) {
  if (n <= 0) return;       // base case: stop condition
  console.log(n);
  countDown(n - 1);          // recursive call: smaller problem
}
```

Every recursive function needs a BASE CASE (when to stop) and a RECURSIVE CASE (calling itself with smaller input).

**Why it exists:** Some problems are naturally recursive — tree structures, nested data, fractals. Writing these with loops is much harder than with recursion.

**Where it's used:** Comment threads, file systems (folders containing folders), menus with submenus, JSON tree traversal.

**What goes wrong without it:**
- Missing base case → infinite recursion → stack overflow crash.
- Not shrinking the input → `countDown(n)` instead of `countDown(n-1)` → infinite recursion.
- Using recursion for simple linear problems → less efficient than a loop (recursion has overhead).

---

## Recursive Components

**What:** A React component can render itself — this builds tree structures like comment threads.

```jsx
function Comment({ text, replies }) {
  return (
    <div>
      <p>{text}</p>
      {replies.map(r => <Comment {...r} />)}  // calls itself!
    </div>
  );
}
```

**Why it exists:** Comment threads, file explorers, and nested menus have unknown depth — you don't know how many levels deep the data goes. Recursion handles arbitrary depth naturally.

**Where it's used:** Comment threads (Reddit-style), file trees, nested menus, org charts.

**What goes wrong without it:**
- Hardcoding 3 levels of nesting → breaks when data has 4 levels.
- Missing the base case (empty replies) → infinite render → React crash.
- Forgetting to spread props (`{...r}`) → child comment gets no data → renders empty.

---

## Composition Pattern

**What:** Composition means building complex UIs by combining simple, reusable components — like LEGO blocks.

```jsx
<Layout>           {/* provides page structure */}
  <Sidebar />      {/* provides navigation */}
  <Content>        {/* wraps main content */}
    <Article />    {/* the actual article */}
  </Content>
</Layout>
```

**Why it exists:** React doesn't use inheritance (class extends). Instead, you compose components. This is more flexible — you can swap any piece without affecting others.

**Where it's used:** Every React app. Layouts, page templates, card structures.

**What goes wrong without it:**
- One giant component with everything → can't reuse, can't test, can't swap parts.
- Inheritance hierarchies → changing a parent breaks all children. Composition avoids this.
- Tight coupling → components that depend on each other's internals → can't change one without breaking the other.

---

## Layout Components

**What:** Components that provide STRUCTURE, not content. They wrap other components using `children`.

```jsx
function Layout({ children }) {
  return (
    <div className="layout">
      <Header />
      <main>{children}</main>
      <Footer />
    </div>
  );
}
```

**Why it exists:** Every page needs the same header/footer/nav. Without layout components, you'd copy-paste the header into every page. With them, you write the layout once and pass different content as `children`.

**Where it's used:** Page templates, auth wrappers (login required), sidebar layouts.

**What goes wrong without it:**
- Header/footer duplicated on every page → change the header, edit 50 files.
- Inconsistent layout → some pages have header, some don't → broken UX.
- Forgetting `{children}` → page content doesn't render, only the layout shell appears.

---

## Conditional Rendering

**What:** Showing or hiding content based on a condition. Three common ways:

```jsx
// 1. && (show only if true)
{showMessage && <p>Hello!</p>}

// 2. Ternary ? : (show one or the other)
{isLoggedIn ? <LogoutBtn /> : <LoginBtn />}

// 3. if in function body
if (!show) return null;
return <p>Hello!</p>;
```

**Why it exists:** UIs are dynamic — show a loading spinner while waiting, show an error if something fails, show different content for logged-in vs. anonymous users. Conditional rendering makes this possible.

**Where it's used:** Everywhere — loading states, error states, auth-gated content, feature toggles, form validation messages.

**What goes wrong without it:**
- Everything always shows → no loading states, no error handling, no auth.
- Using `&&` with numbers: `{count && <p>{count}</p>}` → if count is 0, React renders "0" (0 is falsy but React renders it). Use `{count > 0 && ...}` instead.
- Returning `undefined` instead of `null` → React may render "undefined" text.

---

## Default Props

**What:** Give props default values so the component works even if the parent doesn't pass them.

```jsx
function Alert({ type = "info", show = true }) {
  // if parent doesn't pass 'type', it's "info"
}
<Alert />             // type="info", show=true
<Alert type="error" /> // type="error", show=true
```

**Why it exists:** Not every parent needs to specify every prop. Defaults make components easier to use — you only pass what you want to customize.

**Where it's used:** Reusable components — buttons with default colors, alerts with default types, inputs with default placeholders.

**What goes wrong without it:**
- Missing prop → `undefined` → `colors[undefined]` → `undefined` → broken styling.
- Component crashes when parent forgets a prop → bad developer experience.
- Every parent must pass every prop → verbose, annoying to use.
