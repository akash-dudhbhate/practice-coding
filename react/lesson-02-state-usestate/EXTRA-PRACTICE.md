# lesson-02-state-usestate — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: useState returns
```jsx
const [state, setState] = useState(0);
```
What are the two elements of the array?
<details><summary>Answer</summary>
`state` — current value. `setState` — function to update it. Array destructuring assigns names.
</details>

## Check 02: Async state updates
```jsx
const [count, setCount] = useState(0);
const handleClick = () => {
  setCount(1);
  console.log(count); // ?
};
```
<details><summary>Answer</summary>
Prints `0` — state updates are async. `count` doesn't change until re-render. Use the value passed to setCount or useEffect.
</details>

## Check 03: Functional updates
```jsx
setCount(count + 1);  // A
setCount(c => c + 1); // B
```
<details><summary>Answer</summary>
A uses the current `count` from closure (may be stale). B uses the latest state from React. Use B when updating based on previous state.
</details>

## Check 04: Object state
```jsx
setUser({ name: "B" }); // What happens to age?
```
<details><summary>Answer</summary>
`age` is lost — `setUser` replaces the entire object, doesn't merge. Use spread: `setUser({ ...user, name: "B" })`.
</details>

## Check 05: Initial state function
```jsx
const [data, setData] = useState(() => expensiveComputation());
```
<details><summary>Answer</summary>
Lazy initialization — function runs only on first render. Use when initial state is expensive to compute. Without `() =>`, it runs on every render.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy): Direct State Mutation
```jsx
const [count, setCount] = useState(0);
count = count + 1;
```
<details><summary>Answer</summary>
**Bug:** Directly modifying state variable. React doesn't detect the change, no re-render.
**Fix:** `setCount(count + 1);`
</details>

## Debug 02 (Medium): Stale Closure
```jsx
const [count, setCount] = useState(0);
const increment = () => {
  setCount(count + 1);
  setCount(count + 1);
};
```
<details><summary>Answer</summary>
**Bug:** Both calls use the same `count` value (stale closure). Only increments by 1.
**Fix:** Use functional update: `setCount(c => c + 1); setCount(c => c + 1);`
</details>

## Debug 03 (Hard): Object State Mutation
```jsx
const [user, setUser] = useState({ name: "A", age: 25 });
user.age = 26;
```
<details><summary>Answer</summary>
**Bug:** Mutating state object directly. React doesn't detect the change.
**Fix:** `setUser({ ...user, age: 26 });` — create new object.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Mutating state directly
```jsx
// WRONG
count++;
// CORRECT
setCount(count + 1);
```

## Mistake 02: Mutating object state
```jsx
// WRONG
user.age = 26;
// CORRECT
setUser({ ...user, age: 26 });
```

## Mistake 03: Stale closures
```jsx
// WRONG — uses old count
setCount(count + 1);
setCount(count + 1);
// CORRECT — functional update
setCount(c => c + 1);
setCount(c => c + 1);
```

## Mistake 04: Forgetting to spread arrays
```jsx
// WRONG — mutates original
items.push(newItem);
setItems(items);
// CORRECT
setItems([...items, newItem]);
```

## Mistake 05: Expensive initial state
```jsx
// WRONG — runs every render
const [data] = useState(expensiveFunc());
// CORRECT — runs once
const [data] = useState(() => expensiveFunc());
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Separate States for Related Data
### Before
```jsx
const [name, setName] = useState("");
const [email, setEmail] = useState("");
const [age, setAge] = useState(0);
```
### After
```jsx
const [form, setForm] = useState({ name: "", email: "", age: 0 });
```

## Refactor 02 (Medium): Object State Mutation
### Before
```jsx
setForm(form.name = "John"); // mutates directly
```
### After
```jsx
setForm(prev => ({ ...prev, name: "John" }));
```

## Refactor 03 (Hard): Derived State in useState
### Before
```jsx
const [items, setItems] = useState([]);
const [count, setCount] = useState(0);
useEffect(() => setCount(items.length), [items]);
```
### After
```jsx
const [items, setItems] = useState([]);
const count = items.length; // derived, no state
```

---

## Approach Comparison — different ways to solve it

## Problem: Toggle State

### Approach 1: Boolean state
```jsx
const [isOpen, setIsOpen] = useState(false);
const toggle = () => setIsOpen(!isOpen);
```

### Approach 2: Functional update
```jsx
const toggle = () => setIsOpen(prev => !prev);
```

**Winner:** Approach 2 — safer, avoids stale closure issues.

---

## Problem: Form State

### Approach 1: Individual states
```jsx
const [name, setName] = useState("");
const [email, setEmail] = useState("");
const [age, setAge] = useState(0);
```

### Approach 2: Object state
```jsx
const [form, setForm] = useState({ name: "", email: "", age: 0 });
const update = (field) => (e) => setForm({ ...form, [field]: e.target.value });
```

**Winner:** Approach 2 for many fields. Approach 1 for 2-3 fields.
