# Lesson 19 — Concepts Explained (JS Objects & DOM)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Object Basics

**What:** Objects store key-value pairs (like dictionaries in Python).

```javascript
const user = {
    name: "Akash",
    age: 25,
    isActive: true,
    hobbies: ["coding", "reading"],
    address: {
        city: "Mumbai",
        country: "India"
    },
    greet() {
        return `Hello, I'm ${this.name}`;
    }
};

user.name           // "Akash" (dot notation)
user["age"]         // 25 (bracket notation — for dynamic keys)
user.address.city   // "Mumbai" (nested access)
user.greet()        // "Hello, I'm Akash" (method call)
```

**Why it exists:** Without objects, you'd use parallel arrays (`names = []`, `ages = []`) → no relationship between data. Objects group related data → one entity, one variable.

**Where it's used:** Everywhere — API responses, configuration, user data, game state, DOM elements.

**What goes wrong without it:**
- Dot notation only works with valid identifier keys: `user.first-name` → syntax error (hyphen). Use `user["first-name"]`.
- `const obj = {}; obj.name = "Akash"` → works (mutating the object, not reassigning the variable). `const` prevents reassignment, not mutation.
- Deleting: `delete obj.key` → removes the key. Setting `obj.key = undefined` → key still exists (value is undefined). Use `delete` to remove.

---

## Object Methods

**What:** Functions stored as object properties.

```javascript
const calculator = {
    value: 0,
    add(n) { this.value += n; return this; },
    subtract(n) { this.value -= n; return this; },
    reset() { this.value = 0; return this; },
    getValue() { return this.value; }
};

// Method chaining (because methods return `this`)
calculator.add(5).add(3).subtract(2).getValue();  // 6
```

**Why it exists:** Without methods, data and behavior are separate → `add(calculator, 5)` instead of `calculator.add(5)`. Methods keep related behavior with the data → OOP principle.

**Where it's used:** Every object with behavior — user objects, game entities, utility objects, builders.

**What goes wrong without it:**
- `this` in arrow functions: `{ method: () => this.value }` → `this` is NOT the object → `undefined`. Use regular functions for object methods.
- Method chaining requires returning `this`. Forgetting `return this` → `calculator.add(5).add(3)` → `TypeError: Cannot read property 'add' of undefined`.
- Extracting methods: `const add = calculator.add; add(5)` → `this` is lost → `this.value` → error. Use `.bind(calculator)`.

---

## Object Destructuring & Spread

**What:** Extract values and merge objects.

```javascript
// Destructuring
const { name, age } = user;
const { name: fullName, age: userAge = 0 } = user;  // rename + default
const { address: { city } } = user;  // nested destructuring

// Spread (merge objects)
const defaults = { theme: "light", fontSize: 16 };
const userPrefs = { fontSize: 20 };
const settings = { ...defaults, ...userPrefs };  // { theme: "light", fontSize: 20 }

// Update object immutably
const updatedUser = { ...user, age: 26 };  // new object, age changed
```

**Why it exists:** Without destructuring, `const name = user.name; const age = user.age;` → verbose. Without spread, `Object.assign({}, obj1, obj2)` → less readable. These make object manipulation concise.

**Where it's used:** React (props, state updates), API responses, configuration merging, function parameters.

**What goes wrong without it:**
- Spread is shallow: `{ ...user }` → top-level copy, nested objects (`address`) are still references → mutating `copy.address.city` mutates `user.address.city`.
- Destructuring with rename: `const { name: fullName } = user` → variable is `fullName`, not `name`. `name` is undefined.
- Order matters: `{ ...defaults, ...overrides }` → overrides win. Reversed → defaults win (wrong).

---

## Object Methods (Object.keys, values, entries)

**What:** Iterate over object properties.

```javascript
const user = { name: "Akash", age: 25, city: "Mumbai" };

Object.keys(user);    // ["name", "age", "city"]
Object.values(user);  // ["Akash", 25, "Mumbai"]
Object.entries(user); // [["name", "Akash"], ["age", 25], ["city", "Mumbai"]]

// Iterate with entries
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}

// Check if key exists
"name" in user;              // true
user.hasOwnProperty("name"); // true (older syntax)
```

**Why it exists:** Without these, you'd use `for...in` which includes inherited properties → bugs. `Object.keys/values/entries` only return OWN properties → safe.

**Where it's used:** Iterating objects, converting objects to arrays, serialization, debugging.

**What goes wrong without it:**
- `for...in` includes prototype chain properties → usually not what you want. Use `Object.keys()` + `for...of`.
- `Object.keys()` returns strings, even for numeric keys: `Object.keys({1: "a", 2: "b"})` → `["1", "2"]`.
- Order: integer keys are sorted numerically, string keys are in insertion order. Don't rely on order for objects.

---

## DOM: Selecting Elements

**What:** The DOM (Document Object Model) is the browser's representation of HTML. JavaScript can select and manipulate DOM elements.

```javascript
// Select by CSS selector (most common)
document.querySelector("#myId");          // first matching element
document.querySelector(".myClass");       // first matching element
document.querySelectorAll(".items");     // ALL matching elements (NodeList)

// Older methods (still work)
document.getElementById("myId");
document.getElementsByClassName("items");  // HTMLCollection (live)
document.getElementsByTagName("div");

// Modern: querySelector with any CSS selector
document.querySelector("div.card > p.title");
document.querySelector("input[type='email']");
```

**Why it exists:** Without DOM selection, JavaScript can't interact with the page → no dynamic content, no interactivity. Selecting elements is the first step in any DOM manipulation.

**Where it's used:** Every interactive web page — forms, buttons, dynamic content, SPAs.

**What goes wrong without it:**
- `querySelector` returns `null` if not found → `null.textContent` → `TypeError`. Always check: `if (el) { ... }`.
- `querySelectorAll` returns a NodeList → has `.forEach()` but not array methods (`.map`, `.filter`). Convert: `[...document.querySelectorAll(".x")]`.
- `getElementsByClassName` returns a LIVE collection → changes as DOM changes → can cause infinite loops if you remove elements while iterating.

---

## DOM: Modifying Elements

**What:** Change element content, attributes, and styles.

```javascript
const el = document.querySelector("#title");

// Content
el.textContent = "New Title";        // text only (safe from XSS)
el.innerHTML = "<b>Bold</b>";        // HTML (XSS risk if user input!)

// Attributes
el.setAttribute("data-id", "123");
el.getAttribute("data-id");           // "123"
el.removeAttribute("data-id");
el.id = "newId";                      // direct property

// Classes
el.classList.add("active");
el.classList.remove("active");
el.classList.toggle("active");        // add if absent, remove if present
el.classList.contains("active");      // true/false

// Styles
el.style.color = "red";
el.style.backgroundColor = "#f0f0f0";  // camelCase, not kebab-case
el.style.cssText = "color: red; font-size: 20px;";  // multiple styles

// Data attributes
el.dataset.userId = "123";            // <div data-user-id="123">
el.dataset.userId;                    // "123"
```

**Why it exists:** Without DOM modification, pages are static — content never changes after load. Modification enables dynamic content, user feedback, and interactivity.

**Where it's used:** Every dynamic web page — updating text, toggling classes, changing styles, form validation feedback.

**What goes wrong without it:**
- `innerHTML` with user input → XSS attack. User enters `<script>alert('hack')</script>` → script executes. Use `textContent` for user input.
- `el.style.color` → inline style (high specificity). Overrides stylesheet styles. For maintainability, use classes (`classList.add`) instead of inline styles.
- `el.style.background-color` → invalid (hyphen). Use `el.style.backgroundColor` (camelCase).

---

## DOM: Creating & Appending Elements

**What:** Create new elements and add them to the page.

```javascript
// Create element
const div = document.createElement("div");
div.textContent = "Hello, World!";
div.classList.add("card");

// Append to parent
document.body.appendChild(div);
document.body.append(div);  // newer, can append multiple + text nodes

// Insert at specific position
parentEl.insertBefore(newEl, referenceEl);

// Modern: insertAdjacentHTML
el.insertAdjacentHTML("beforeend", "<p>Appended</p>");
el.insertAdjacentHTML("afterbegin", "<p>Prepended</p>");
el.insertAdjacentHTML("beforebegin", "<p>Before el</p>");
el.insertAdjacentHTML("afterend", "<p>After el</p>");

// Remove element
el.remove();
parentEl.removeChild(el);  // older way

// Replace element
parentEl.replaceChild(newEl, oldEl);
```

**Why it exists:** Without creating elements, you can only modify existing HTML → can't add new content dynamically. Creating elements enables dynamic lists, notifications, modals, and SPAs.

**Where it's used:** Adding list items, showing notifications, creating modals, rendering API data, building UIs dynamically.

**What goes wrong without it:**
- `appendChild` returns the appended node. `append` (newer) doesn't return anything but can append multiple items and text.
- `insertAdjacentHTML` with user input → XSS. Sanitize input or use `textContent`.
- Creating many elements in a loop → slow (each triggers reflow). Use `DocumentFragment` to batch: create all, append once.

---

## DOM: Traversing

**What:** Navigate between elements (parent, children, siblings).

```javascript
const el = document.querySelector(".card");

el.parentNode;           // parent element
el.parentElement;        // parent element (null if not element node)
el.children;             // children (elements only)
el.childNodes;           // children (all nodes including text/comments)
el.firstChild;           // first child (could be text node)
el.firstElementChild;    // first child element
el.lastElementChild;     // last child element
el.nextElementSibling;   // next sibling element
el.previousElementSibling; // previous sibling element

// Closest (find nearest ancestor matching selector)
el.closest(".container");  // nearest ancestor with class "container"
el.closest("div");         // nearest div ancestor
```

**Why it exists:** Without traversal, you can only access elements you directly select. Traversal lets you navigate from a known element to related elements → essential for event delegation and component logic.

**Where it's used:** Event delegation (find the parent that handles the event), component navigation, finding related elements.

**What goes wrong without it:**
- `children` (elements only) vs `childNodes` (all nodes including text). `childNodes` includes whitespace text nodes → usually not what you want.
- `firstChild` might be a text node (whitespace). Use `firstElementChild` for the first element.
- `closest()` includes the element itself: `el.closest(".card")` → returns `el` if `el` has class "card". Starts from the element, not just ancestors.

---

## Forms and Input Values

**What:** Read and set form input values.

```javascript
const input = document.querySelector("#username");
const checkbox = document.querySelector("#agree");
const select = document.querySelector("#country");

// Text input
input.value;                // current value
input.value = "Akash";      // set value

// Checkbox
checkbox.checked;           // true/false
checkbox.checked = true;    // check it

// Select dropdown
select.value;               // selected option value
select.value = "india";     // set selection

// Form data (all inputs at once)
const form = document.querySelector("form");
const formData = new FormData(form);
const data = Object.fromEntries(formData);  // { username: "Akash", ... }
```

**Why it exists:** Without form access, you can't read user input → no interactive forms, no validation, no submissions. Form access is the bridge between user input and JavaScript.

**Where it's used:** Every form — login, registration, search, settings, checkout.

**What goes wrong without it:**
- `input.value` is always a string, even for `type="number"`. Use `Number(input.value)` for numeric input.
- `checkbox.checked` is a boolean, not a string. Don't compare with `"true"`.
- `FormData` doesn't include unchecked checkboxes or disabled inputs → data might be incomplete.
