# Lesson 05 — Lists & Keys

## What you'll learn
- How to render arrays of data as lists using `.map()`.
- Why the `key` prop is required and what makes a good key.
- Why using array index as key is dangerous for dynamic lists.
- How to filter, sort, and nest lists.

## Lesson

React renders arrays of elements. You create them with `.map()`:

```jsx
function FruitList({ fruits }) {
  return (
    <ul>
      {fruits.map(fruit => <li key={fruit.id}>{fruit.name}</li>)}
    </ul>
  );
}
```

### Key rules
- Every item in a `.map()` MUST have a unique `key` prop.
- Good keys: stable, unique IDs (`item.id`). Bad keys: `Math.random()` (changes every render).
- Index as key is OK for **static** lists, dangerous for **dynamic** lists (add/remove/reorder).
- Keys only need to be unique among **siblings**, not globally.
- The `key` goes on the outer element in the `.map()`, not inside a child component.
- Never mutate the array — use spread, `.filter()`, `.map()` to create new arrays.

---

## Your Tasks

This lesson has **9 practice problems** across three difficulty levels. Start with `easy/` and work your way up. Each problem file has the description at the top — **write your complete component from scratch below** to practice remembering syntax.

### Easy (start here)
1. `easy/p01-solve.jsx` — **Fruit List:** Render a static array of fruit names as `<li>` elements. Each fruit has an `id`. Practice `.map()` with `key={fruit.id}`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   * Apple
   * Banana
   * Cherry
      <- <ul> of <li key={id}> items
   ```
2. `easy/p02-solve.jsx` — **Number List:** Render numbers 1-10 as a list. Use index as key (safe for static lists). Practice `.map()` with index parameter.

   WHAT IT SHOULD LOOK LIKE:
   ```
   * 1
   * 2
   * 3
   ...
   * 10
      <- <ul> listing numbers 1 through 10
   ```
3. `easy/p03-solve.jsx` — **User Cards from Array:** Render an array of user objects (`{id, name, email}`) as cards. Each card shows name and email. Practice rendering objects with keys.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------------+
   | Alice                  |   <- <h3>
   | alice@x.com            |   <- <p>
   +------------------------+
   | Bob                    |
   | bob@x.com              |
   +------------------------+
   | Charlie                |
   | charlie@x.com          |
   +------------------------+
   ```

### Medium
4. `medium/p01-solve.jsx` — **Dynamic Todo List:** Add/remove todos. Each todo has a unique `id` (use `Date.now()`). Practice dynamic lists with stable keys.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------+ +-----+
   | Buy milk       | | Add |
   +----------------+ +-----+
   * Buy milk       [x]      <- x removes only that item
   * Walk the dog   [x]
   ```
5. `medium/p02-solve.jsx` — **Searchable List:** A list with a search input. Filter items by name as you type. Show "No results" when empty. Practice list filtering.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +------------------+
   | an               |          <- search input
   +------------------+
   * Banana           * Orange     <- only matches remain

   (typing gibberish shows:  No results)
   ```
6. `medium/p03-solve.jsx` — **Sortable List:** A list with a sort button (ascending/descending by name). Sort a COPY of the array, not the original. Practice list sorting.

   WHAT IT SHOULD LOOK LIKE:
   ```
   ASCENDING:               DESCENDING (after click):
   [ Sort: Z-A ]            [ Sort: A-Z ]
   * Alice                  * Charlie
   * Bob                    * Bob
   * Charlie                * Alice
   ```

### Hard
7. `hard/p01-solve.jsx` — **Nested Category List:** Categories with items inside. Use nested `.map()` — outer for categories, inner for items. Both need unique keys.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Fruits                       <- <h3> per category
     * Apple
     * Banana
   Vegetables
     * Carrot
     * Spinach
   ```
8. `hard/p02-solve.jsx` — **Todo List with Item Components:** Extract each todo into a `TodoItem` component. The `key` goes on `<TodoItem>`, not inside it. Practice component extraction.

   WHAT IT SHOULD LOOK LIKE:
   ```
   * Buy milk        [Delete]    <- each <li> is a <TodoItem>
   * Walk the dog    [Delete]       key={t.id} on the component
   ```
9. `hard/p03-solve.jsx` — **Reorderable List with State:** A list where you can move items up/down. Demonstrate why index-as-key breaks (use stable IDs instead). Practice key stability with reordering.

   WHAT IT SHOULD LOOK LIKE:
   ```
   BEFORE:                  AFTER moving "First" down:
   * First   [up] [down]    * Second  [up] [down]
   * Second  [up] [down]    * First   [up] [down]
   * Third   [up] [down]    * Third   [up] [down]
   ```

### How to work
- Open a problem file, read the description in the header comment.
- Write your **complete component from scratch** below the TODO marker.
- Remove the TODO line when done.
- When done, tell me and I'll review. Say **"give me next task"** to advance.
