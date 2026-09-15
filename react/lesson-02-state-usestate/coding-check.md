# Lesson 02 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01-solve.jsx (Counter)
- [ ] Uses `useState(0)` for initial count.
- [ ] Button text shows current count: `Clicked {count} times`.
- [ ] `onClick` calls `setCount(count + 1)`.
- [ ] Count increments by 1 on each click.
- [ ] Test: Click 5 times → count shows 5.
- [ ] Test: Click 10 times rapidly → count shows 10 (no stale state issues).

### p02-solve.jsx (Toggle Text)
- [ ] Uses `useState(false)` or `useState(true)` for boolean state.
- [ ] Button text shows "ON" when true, "OFF" when false.
- [ ] `onClick` calls `setToggle(!toggle)` or `setToggle(prev => !prev)`.
- [ ] Test: Click once → text changes from OFF to ON.
- [ ] Test: Click again → text changes back to OFF.
- [ ] Test: Click 10 times rapidly → ends in correct state (ON if even clicks from OFF).

### p03-solve.jsx (Text Input Display)
- [ ] Uses `useState("")` for text state.
- [ ] Input is controlled: `value={text}`.
- [ ] `onChange` calls `setText(e.target.value)`.
- [ ] Text displays below the input in a `<p>` tag.
- [ ] Test: Type "Hello" → "Hello" appears below.
- [ ] Test: Clear the input → display clears too.
- [ ] Test: Type special characters like `!@#` → they appear correctly.

## Medium

### p01-solve.jsx (Todo List Add/Remove)
- [ ] Uses `useState([])` for todos array.
- [ ] Input field for new todo text (controlled with string state).
- [ ] Add button uses `setTodos([...todos, newTodo])` — NOT `todos.push()`.
- [ ] Each todo has a unique id (use `Date.now()` or a counter).
- [ ] Remove uses `setTodos(todos.filter(t => t.id !== id))` — NOT `todos.splice()`.
- [ ] Test: Add "Buy milk" → appears in list.
- [ ] Test: Add 3 items → all 3 appear in order.
- [ ] Test: Click remove on item 2 → items 1 and 3 remain.
- [ ] Test: Adding empty string is prevented (button disabled or guard check).

### p02-solve.jsx (Counter with Increment/Decrement/Reset)
- [ ] Uses `useState(0)` for count.
- [ ] Increment uses `setCount(prev => prev + 1)`.
- [ ] Decrement uses `setCount(prev => prev - 1)`.
- [ ] Reset uses `setCount(0)`.
- [ ] Count never goes below 0 (guard: `if (count > 0)` or `Math.max(0, prev - 1)`).
- [ ] Test: Click +1 three times → count is 3.
- [ ] Test: Click -1 from 0 → count stays 0 (not -1).
- [ ] Test: Click +1 five times, then Reset → count is 0.
- [ ] Test: Rapidly click +1 ten times → count is 10 (functional update works).

### p03-solve.jsx (Form with Multiple Fields)
- [ ] Uses `useState({ name: "", email: "" })` for form object.
- [ ] Both inputs are controlled: `value={form.name}` and `value={form.email}`.
- [ ] `onChange` uses spread: `setForm({ ...form, [e.target.name]: e.target.value })`.
- [ ] Values display below the form.
- [ ] Test: Type "Akash" in name → name shows below, email stays empty.
- [ ] Test: Type "test@test.com" in email → email shows, name is preserved.
- [ ] Test: Type in name, then email → both values preserved (spread works).
- [ ] Test: Clear name field → email still has its value (no data loss).

## Hard

### p01-solve.jsx (Shopping Cart)
- [ ] Uses `useState([])` for cart array.
- [ ] Products list is hardcoded array of `{ id, name, price }`.
- [ ] Add to cart: if item exists, increment quantity; else add with qty 1.
- [ ] Quantity update uses `.map()` with spread: `cart.map(item => item.id === id ? { ...item, qty: item.qty + 1 } : item)`.
- [ ] Remove uses `.filter()`.
- [ ] Total price computed during render: `cart.reduce((sum, item) => sum + item.price * item.qty, 0)`.
- [ ] Test: Add "Apple" ($1) → cart shows 1 Apple, total $1.
- [ ] Test: Add "Apple" again → qty becomes 2, total $2.
- [ ] Test: Add "Banana" ($2) → cart has 2 items, total $4.
- [ ] Test: Remove "Apple" → only Banana remains, total $2.
- [ ] Test: Decrement qty to 0 → item removed or qty shows 0.

### p02-solve.jsx (Multi-Step Form)
- [ ] Uses `useState({ step: 1, name: "", email: "" })` or separate states.
- [ ] Step 1 shows name input, Step 2 shows email input, Step 3 shows review.
- [ ] Next button validates current step (name not empty for step 1, email has "@" for step 2).
- [ ] Back button decreases step (disabled on step 1).
- [ ] Review step shows entered name and email.
- [ ] Test: Click Next on step 1 with empty name → stays on step 1, shows error.
- [ ] Test: Enter name, click Next → step 2 appears.
- [ ] Test: Enter email without "@", click Next → stays on step 2, shows error.
- [ ] Test: Fill both, reach step 3 → review shows correct name and email.
- [ ] Test: Click Back from step 2 → returns to step 1 with name preserved.

### p03-solve.jsx (Accordion)
- [ ] Uses `useState(0)` or `useState(null)` for open section index.
- [ ] Renders 3+ sections from an array of `{ title, content }`.
- [ ] Clicking a section title toggles it open/closed.
- [ ] Only one section open at a time — opening one closes others.
- [ ] Clicking the open section closes it (toggle behavior).
- [ ] Test: Click section 1 → it expands, others are closed.
- [ ] Test: Click section 2 while section 1 is open → section 1 closes, section 2 opens.
- [ ] Test: Click open section again → it collapses (all closed).
- [ ] Test: Content of each section is different and matches the data.
