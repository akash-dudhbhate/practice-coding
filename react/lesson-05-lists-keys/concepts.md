# Lesson 05 — Concepts Explained (Lists & Keys)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Rendering Lists with .map()

**What:** In React, you transform arrays of data into arrays of elements using the `.map()` method.

```jsx
function FruitList({ fruits }) {
  return (
    <ul>
      {fruits.map(fruit => (
        <li key={fruit.id}>{fruit.name}</li>
      ))}
    </ul>
  );
}

const fruits = [
  { id: 1, name: "Apple" },
  { id: 2, name: "Banana" },
  { id: 3, name: "Cherry" },
];
<FruitList fruits={fruits} />
```

`.map()` returns a new array of JSX elements. React renders each element in the array.

**Why it exists:** Data almost always comes as arrays (API responses, database queries). `.map()` is the cleanest way to convert data into UI — one line transforms a data array into an element array.

**Where it's used:** Every list in React — navigation menus, data tables, card grids, dropdown options, todo lists, search results.

**What goes wrong without it:**
- Using `for` loops in JSX → doesn't work (JSX expressions must be single values). You'd need to build an array manually with `.push()` — verbose and ugly.
- Forgetting to return from `.map()`: `fruits.map(fruit => { <li>{fruit.name}</li> })` → returns `undefined` (missing `return`). Use arrow function with implicit return: `fruits.map(fruit => <li>{fruit.name}</li>)` or explicit: `fruits.map(fruit => { return <li>{fruit.name}</li>; })`.
- Not wrapping in a parent → multiple array elements without a parent `<ul>` or Fragment → invalid JSX.

---

## The key Prop

**What:** Every element rendered in a `.map()` must have a unique `key` prop. Keys help React identify which items changed, were added, or were removed.

```jsx
// GOOD — unique id as key
{todos.map(todo => <li key={todo.id}>{todo.text}</li>)}

// BAD — no key (React warning)
{todos.map(todo => <li>{todo.text}</li>)}

// ACCEPTABLE BUT RISKY — index as key
{todos.map((todo, index) => <li key={index}>{todo.text}</li>)}
```

Keys must be UNIQUE among siblings. They don't need to be globally unique — just unique within the list.

**Why it exists:** React uses keys to match elements between re-renders. When you add an item to the middle of a list, React uses keys to know which elements are new vs. existing. Without keys, React might re-render the wrong items or lose component state.

**Where it's used:** Every list rendered with `.map()`. No exceptions — React will warn in the console if you forget.

**What goes wrong without it:**
- Missing keys → React console warning: "Each child in a list should have a unique key prop."
- Duplicate keys → React warning: "Encountered two children with the same key." Only one renders, or state gets mixed up.
- Using index as key with reordering → React confuses items, component state (like input values) gets attached to the wrong item.

---

## Index as Key — When It's Safe and When It's Not

**What:** Using the array index as the key (`key={index}`) is acceptable for STATIC lists that never reorder, add, or remove items. It's dangerous for dynamic lists.

```jsx
// SAFE — static list that never changes
const staticOptions = ["Option A", "Option B", "Option C"];
{staticOptions.map((option, index) => <li key={index}>{option}</li>)}

// DANGEROUS — dynamic list that can reorder/add/remove
{todos.map((todo, index) => (
  <li key={index}>
    <input type="checkbox" />  {/* state attached to index, not todo */}
    {todo.text}
  </li>
))}
// If you delete the first todo, the checkbox state of item 2
// moves to item 3's position — state is now on the wrong item!
```

**Why it exists:** Sometimes you don't have a unique ID (e.g., array of strings). Index is the fallback. But it breaks when the list order changes because React tracks items by index, not by identity.

**Where it's used:** Static lists (navigation items, fixed options), lists where items have no natural ID and never change.

**What goes wrong without it:**
- Deleting an item from the middle → React shifts all items down by index → component state (inputs, checkboxes) moves to the wrong item.
- Inserting at the beginning → all indices shift → React re-renders everything (performance hit) and state gets mismatched.
- Reordering (drag-and-drop, sorting) → items keep their old index-based key → React renders them in the wrong order with wrong state.

---

## Dynamic Lists (Add/Remove/Update)

**What:** Lists that change over time — items are added, removed, or updated based on user actions.

```jsx
function TodoApp() {
  const [todos, setTodos] = useState([
    { id: 1, text: "Learn React", done: false },
    { id: 2, text: "Build app", done: false },
  ]);

  // ADD — new array with new item
  const addTodo = (text) => {
    setTodos([...todos, { id: Date.now(), text, done: false }]);
  };

  // REMOVE — filter creates new array
  const removeTodo = (id) => {
    setTodos(todos.filter(todo => todo.id !== id));
  };

  // UPDATE — map creates new array with updated item
  const toggleTodo = (id) => {
    setTodos(todos.map(todo =>
      todo.id === id ? { ...todo, done: !todo.done } : todo
    ));
  };

  return (
    <ul>
      {todos.map(todo => (
        <li key={todo.id}>
          <input type="checkbox" checked={todo.done} onChange={() => toggleTodo(todo.id)} />
          {todo.text}
          <button onClick={() => removeTodo(todo.id)}>Delete</button>
        </li>
      ))}
    </ul>
  );
}
```

**Why it exists:** Real apps have dynamic data — users add/remove/edit items. Understanding how to update arrays immutably while keeping keys stable is essential.

**Where it's used:** Todo lists, shopping carts, task boards, chat messages, any user-managed collection.

**What goes wrong without it:**
- Mutating the array: `todos.push(newTodo)` → same reference → React doesn't re-render → new item doesn't appear.
- Using index as key → after delete, checkbox/input state jumps to wrong items.
- Generating IDs with `Math.random()` → different ID on every render → React thinks every item is new → re-renders everything. Use `Date.now()` or a stable counter.

---

## List Filtering and Searching

**What:** You can filter a list before rendering it — show only items that match a search query or condition.

```jsx
function SearchableList({ items }) {
  const [query, setQuery] = useState("");

  const filtered = items.filter(item =>
    item.name.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div>
      <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Search..." />
      {filtered.length === 0 ? (
        <p>No results found.</p>
      ) : (
        <ul>
          {filtered.map(item => <li key={item.id}>{item.name}</li>)}
        </ul>
      )}
    </div>
  );
}
```

**Why it exists:** Users need to find items in large lists. Filtering lets you show a subset without modifying the original data — the source array stays intact, only the rendered view changes.

**Where it's used:** Search bars, filter dropdowns (by category, status, date), sorted lists, paginated lists.

**What goes wrong without it:**
- Filtering the original state: `setItems(items.filter(...))` → loses the removed items permanently. Filter during render instead, keep original state intact.
- Case-sensitive search: `item.name.includes(query)` → "apple" doesn't match "Apple". Use `.toLowerCase()` on both.
- Empty results not handled → blank screen. Show "No results" when `filtered.length === 0`.

---

## List Sorting

**What:** You can sort a list before rendering — by name, date, price, or any field.

```jsx
function SortedList({ items }) {
  const [sortOrder, setSortOrder] = useState("asc");

  const sorted = [...items].sort((a, b) => {
    if (sortOrder === "asc") return a.name.localeCompare(b.name);
    return b.name.localeCompare(a.name);
  });

  return (
    <div>
      <button onClick={() => setSortOrder(sortOrder === "asc" ? "desc" : "asc")}>
        Sort: {sortOrder}
      </button>
      <ul>
        {sorted.map(item => <li key={item.id}>{item.name}</li>)}
      </ul>
    </div>
  );
}
```

**Why it exists:** Users need to organize data — alphabetical, by date, by price. Sorting during render (on a copy) keeps the original data intact while showing a sorted view.

**Where it's used:** Data tables, product lists, leaderboards, any list where users want control over order.

**What goes wrong without it:**
- `items.sort()` → mutates the original array! Always sort a copy: `[...items].sort()`.
- Sort changing key order → if you use index as key, sorting breaks state. Use stable IDs as keys.
- Forgetting to handle numbers: `.sort()` on numbers sorts alphabetically by default (10 comes before 2). Use `(a, b) => a - b` for numeric sort.

---

## Nested Lists

**What:** When data has nested arrays (categories with items, rows with cells), you use `.map()` inside `.map()`.

```jsx
function CategoryList({ categories }) {
  return (
    <div>
      {categories.map(category => (
        <div key={category.id}>
          <h3>{category.name}</h3>
          <ul>
            {category.items.map(item => (
              <li key={item.id}>{item.name}</li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

const categories = [
  { id: 1, name: "Fruits", items: [{ id: 11, name: "Apple" }, { id: 12, name: "Banana" }] },
  { id: 2, name: "Vegetables", items: [{ id: 21, name: "Carrot" }, { id: 22, name: "Spinach" }] },
];
```

**Why it exists:** Real data is often hierarchical — categories contain items, departments contain employees, threads contain replies. Nested maps handle this naturally.

**Where it's used:** Category lists, data tables (rows × columns), file trees, comment threads, menu structures.

**What goes wrong without it:**
- Forgetting keys on the inner map → same React warnings and bugs as missing keys on the outer map.
- Using the same key in inner and outer maps → keys only need to be unique among SIBLINGS, so inner and outer can both use `item.id` as long as they're in different scopes.
- Flat-mapping nested data → loses the hierarchy, all items at one level.

---

## Keys and Component State

**What:** When list items have their own state (inputs, checkboxes, expanded/collapsed), keys determine which state belongs to which item.

```jsx
function ExpandableList({ items }) {
  return items.map(item => (
    <div key={item.id}>
      <button onClick={() => { /* toggle expand */ }}>{item.title}</button>
      {item.expanded && <p>{item.content}</p>}
    </div>
  ));
}

// If you change the key from item.id to index:
// {items.map((item, index) => <div key={index}>...</div>)}
// And then remove the first item → item 2 becomes index 0
// → React thinks it's the same component → keeps item 1's expanded state
// → wrong content is expanded!
```

**Why it exists:** React associates component state with keys. If the key stays the same, React preserves the state. If the key changes, React creates a fresh component (state resets). This is how React knows what to keep vs. recreate.

**Where it's used:** Any list where items have internal state — expandable sections, editable rows, items with checkboxes or inputs.

**What goes wrong without it:**
- Index as key + delete first item → state from item 1 "moves" to item 2's position → wrong state on wrong item.
- Changing key on every render (e.g., `key={Math.random()}`) → React remounts every item every render → all state resets, terrible performance.
- Two items with the same key → React only renders one, state gets confused.

---

## Extracting List Items into Components

**What:** Instead of writing JSX directly in `.map()`, extract each item into its own component for readability and performance.

```jsx
// BEFORE — inline JSX in map
{todos.map(todo => (
  <li key={todo.id}>
    <input type="checkbox" checked={todo.done} onChange={() => toggle(todo.id)} />
    {todo.text}
    <button onClick={() => remove(todo.id)}>Delete</button>
  </li>
))}

// AFTER — extracted component
function TodoItem({ todo, onToggle, onRemove }) {
  return (
    <li>
      <input type="checkbox" checked={todo.done} onChange={() => onToggle(todo.id)} />
      {todo.text}
      <button onClick={() => onRemove(todo.id)}>Delete</button>
    </li>
  );
}

{todos.map(todo => (
  <TodoItem key={todo.id} todo={todo} onToggle={toggle} onRemove={remove} />
))}
```

**Why it exists:** Inline JSX in `.map()` gets unwieldy for complex items. Extracting into a component makes the code cleaner, testable, and allows `React.memo` for performance (skip re-rendering unchanged items).

**Where it's used:** Complex list items — todo items with multiple actions, product cards, table rows, comment items.

**What goes wrong without it:**
- The `key` goes on the COMPONENT (`<TodoItem key={todo.id} />`), NOT inside the component's root element. Putting key inside → React still warns about missing key on the list item.
- Forgetting to pass callbacks → item can't communicate with parent (can't toggle, delete, etc.).
- Inline arrow functions in props (`onChange={() => onToggle(todo.id)}`) → new function each render. For most cases fine; for large lists, pass `todo.id` and handle inside the component.
