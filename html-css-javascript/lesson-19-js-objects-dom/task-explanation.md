# Lesson 19 — JS Objects & DOM

## What you'll learn
- Object creation, properties, and methods
- Object destructuring and spread
- Object.keys, Object.values, Object.entries
- DOM selection (querySelector, getElementById)
- DOM modification (textContent, classList, style)
- Creating and appending elements
- DOM traversal (parent, children, siblings, closest)
- Form input values and FormData

## Lesson

### Object
```javascript
const user = { name: "Akash", age: 25, greet() { return `Hi ${this.name}`; } };
const { name, age } = user;
const updated = { ...user, age: 26 };
```

### DOM
```javascript
const el = document.querySelector("#title");
el.textContent = "New Title";
el.classList.toggle("active");
```

### Create element
```javascript
const div = document.createElement("div");
div.textContent = "Hello";
document.body.appendChild(div);
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.js` — Create an object `car` with properties (brand, model, year) and a method `getInfo()` that returns "Brand Model (Year)". Use `this`.

   ```
   EXPECTED CONSOLE OUTPUT:
   Toyota Camry (2024)
   ```
2. `easy/p02-solve.html` — Create an HTML page with a `<p id="text">Hello</p>`. Write JS to select it, change its text to "Modified by JS", and add a class "highlight".

   ```
   WHAT IT SHOULD LOOK LIKE:
   BEFORE (in markup):        AFTER the JS runs:
   Hello                      Modified by JS   <- text swapped by JS,
                                                 .highlight style applied
   ```
3. `easy/p03-solve.html` — Create a page with a button that, when clicked, creates a new `<li>` with text "New Item" and appends it to a `<ul>`.

   ```
   WHAT IT SHOULD LOOK LIKE:
   BEFORE:                  AFTER 2 clicks on [Add Item]:
   [ Add Item ]             [ Add Item ]
                            - New Item        <- one <li> appended
                            - New Item           per click
   ```

### Medium
4. `medium/p01-solve.js` — Write a function `mergeConfigs(defaults, userPrefs)` that merges two objects using spread. userPrefs overrides defaults. Return the merged config.

   ```
   EXPECTED CONSOLE OUTPUT:
   mergeConfigs({theme:"light",fontSize:14,lang:"en"},
                {theme:"dark",fontSize:16})
     -> { theme: "dark", fontSize: 16, lang: "en" }
   ```
5. `medium/p02-solve.html` — Create a form with name and email inputs. Write JS to read the values on button click, create a user object, and display it on the page. Use `FormData` or direct value access.

   ```
   WHAT IT SHOULD LOOK LIKE:
   BEFORE:                      AFTER Submit:
   Name:  [ Akash    ]        Name:  [ Akash    ]
   Email: [ a@b.com  ]        Email: [ a@b.com  ]
   [ Submit ]                 [ Submit ]
                              { "name":"Akash",     <- user JSON shown
                                "email":"a@b.com" }    inside #output
   ```
6. `medium/p03-solve.html` — Create a list of items. Write JS to use `querySelectorAll` to select all items, then use `forEach` to add a click handler that toggles a "selected" class on each item.

   ```
   WHAT IT SHOULD LOOK LIKE:
   - item one        <- normal
   - ITEM TWO        <- clicked once: highlighted (.selected)
   - item three
   - ITEM FOUR       <- clicked: highlighted
   - item five       <- each item toggles independently
   ```

### Hard
7. `hard/p01-solve.html` — Build a dynamic todo list: input field, add button, list. Each todo has text and a delete button. Use DOM creation (createElement), append, and remove. Store todos in an array and re-render on changes.

   ```
   WHAT IT SHOULD LOOK LIKE:
   [ type a todo       ] [ Add ]
   - Buy milk                    [Delete]
   - Call mom                    [Delete]   <- each row's Delete
   - Walk dog                    [Delete]      removes just that row
   (each Add appends a row; list re-renders from the array)
   ```
8. `hard/p02-solve.html` — Build a dynamic table from an array of user objects. Use `Object.keys` for headers, `Object.values` or `Object.entries` for rows. Add a search input that filters the table rows in real-time.

   ```
   WHAT IT SHOULD LOOK LIKE:
   Search: [ al____________ ]
   +-------+-----+--------+
   | name  | age | city   |    <- headers generated from Object.keys
   +-------+-----+--------+
   | Alice | 30  | Mumbai |    <- only matching rows remain as
   +-------+-----+--------+       you type (live filter)
   ```
9. `hard/p03-solve.html` — Build a modal component: button opens modal, close button (X) closes it, clicking outside closes it. Use DOM traversal (`closest`) and class manipulation. Add open/close animations with CSS transitions.

   ```
   WHAT IT SHOULD LOOK LIKE:
   CLOSED:                    OPEN (after click):
   [ Open Modal ]             +#########################+
                              |#  +----------------+  #|
                              |#  | Modal    [ X ] |  #|  <- fades+scales
                              |#  | content        |  #|     in over a dim
                              |#  +----------------+  #|     backdrop
                              +#########################+
                         (X button or clicking the backdrop closes it)
   ```

### How to work
- Write your complete HTML + CSS + JS solution.
- Remove the TODO comment when done.
- Open in browser to test.
