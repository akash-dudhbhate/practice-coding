# Lesson 19 — Coding Check

## Easy

### p01-solve.js — Car object
- [ ] `car` has brand, model, year properties
- [ ] `car.getInfo()` returns "Brand Model (Year)"
- [ ] Uses `this` inside the method
- [ ] Method returns a string (not console.log)

### p02-solve.html — Modify DOM element
- [ ] `<p id="text">` exists in HTML
- [ ] JS selects it with `querySelector` or `getElementById`
- [ ] Text changes to "Modified by JS"
- [ ] Class "highlight" is added
- [ ] Changes are visible in browser

### p03-solve.html — Add list items
- [ ] Button exists in HTML
- [ ] Click handler creates a new `<li>` element
- [ ] `createElement` and `appendChild` used
- [ ] Each click adds a new "New Item" to the list

## Medium

### p01-solve.js — mergeConfigs
- [ ] Merges defaults and userPrefs
- [ ] userPrefs overrides defaults for same keys
- [ ] Returns new object (doesn't mutate inputs)
- [ ] Uses spread operator
- [ ] mergeConfigs({a:1,b:2}, {b:3,c:4}) → {a:1, b:3, c:4}

### p02-solve.html — Form to object
- [ ] Form has name and email inputs
- [ ] Button click reads input values
- [ ] Creates user object {name, email}
- [ ] Displays the object on the page
- [ ] Uses FormData or direct `.value` access

### p03-solve.html — Toggle list items
- [ ] List with multiple `<li>` items
- [ ] `querySelectorAll` selects all items
- [ ] `forEach` adds click handler to each
- [ ] Click toggles "selected" class
- [ ] Visual change is visible (CSS for .selected)

## Hard

### p01-solve.html — Dynamic todo list
- [ ] Input field and add button
- [ ] Each todo has text and delete button
- [ ] `createElement` used to create elements
- [ ] `appendChild` adds todos to list
- [ ] Delete button removes the todo
- [ ] Todos stored in an array
- [ ] List re-renders on add/delete

### p02-solve.html — Dynamic table with search
- [ ] Array of user objects (at least 5)
- [ ] Table headers from `Object.keys`
- [ ] Table rows from object values
- [ ] Search input filters rows in real-time
- [ ] Filtering uses `filter` + `includes`
- [ ] Table updates on each keystroke

### p03-solve.html — Modal component
- [ ] Button opens the modal
- [ ] Close button (X) closes it
- [ ] Clicking outside modal content closes it
- [ ] Uses `closest()` to detect outside clicks
- [ ] CSS transitions for open/close animation
- [ ] Modal is hidden by default
- [ ] Class toggle controls visibility
