# lesson-17-zustand — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Zustand vs Context
Why use Zustand over Context?
<details><summary>Answer</summary>
Zustand: no provider needed, selective subscriptions (only re-renders when selected value changes), simpler API. Context: built-in, no dependency, but all consumers re-render on any change.
</details>

## Check 02: create
```jsx
const useStore = create((set) => ({
  count: 0,
  increment: () => set(state => ({ count: state.count + 1 })),
}));
```
<details><summary>Answer</summary>
`create` returns a hook. `set` updates state (merges by default). Call `useStore()` in components.
</details>

## Check 03: Selectors
```jsx
const count = useStore(state => state.count);
const increment = useStore(state => state.increment);
```
<details><summary>Answer</summary>
Selector function picks specific state. Component only re-renders when selected value changes. Performance optimization.
</details>

## Check 04: set
```jsx
set({ count: 1 });              // merge
set(state => ({ count: state.count + 1 })); // functional
set({ count: 1 }, false);       // replace (not merge)
```
<details><summary>Answer</summary>
Default: merge new state into old. `false` as second arg: replace entire state.
</details>

## Check 05: Middleware
```jsx
const useStore = create(persist((set) => ({ ... }), { name: "storage" }));
```
<details><summary>Answer</summary>
Middleware wraps store. `persist` saves to localStorage. Other middleware: devtools, immer, subscribeWithSelector.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Selecting Entire Store
```jsx
const store = useStore();
// re-renders on ANY state change
```
<details><summary>Answer</summary>
**Bug:** Selecting entire store causes re-render on any change, even unrelated ones.
**Fix:** `const count = useStore(s => s.count);` — select only what you need.
</details>

## Debug 02 (Medium): Mutating State Directly
```jsx
const increment = () => { count++; };
```
<details><summary>Answer</summary>
**Bug:** Direct mutation — Zustand won't detect change.
**Fix:** `set({ count: count + 1 });` or `set(state => ({ count: state.count + 1 }));`.
</details>

## Debug 03 (Hard): Creating Store Inside Component
```jsx
function App() {
  const store = createStore(...);
}
```
<details><summary>Answer</summary>
**Bug:** New store on every render. State doesn't persist.
**Fix:** Create store at module level: `const useStore = create(...)`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Selecting entire store
```jsx
// WRONG — re-renders on any change
const { count } = useStore();
// CORRECT — select specific
const count = useStore(s => s.count);
```

## Mistake 02: Mutating state
```jsx
// WRONG
state.count++;
// CORRECT
set(state => ({ count: state.count + 1 }));
```

## Mistake 03: Store inside component
```jsx
// WRONG — recreated every render
function App() {
  const store = create(...);
}
// CORRECT — module level
const useStore = create(...);
```

## Mistake 04: No selector optimization
```jsx
// WRONG — new object every render
const { count, name } = useStore(s => ({ count: s.count, name: s.name }));
// CORRECT — separate selectors
const count = useStore(s => s.count);
const name = useStore(s => s.name);
// or use shallow
const { count, name } = useStore(s => ({ count: s.count, name: s.name }), shallow);
```

## Mistake 05: Not using persist for important state
```jsx
// State lost on refresh
// Use persist middleware for user preferences
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Prop Drilling for Global State
### Before
```jsx
<App user={user} setUser={setUser} />
  <Header user={user} setUser={setUser} />
```
### After
```jsx
const useStore = create((set) => ({ user: null, setUser: (u) => set({ user: u }) }));
const user = useStore(s => s.user);
```

## Refactor 02 (Medium): Redux Boilerplate
### Before
```jsx
// actions, reducers, types, dispatch
const mapStateToProps = (state) => ({ user: state.user });
connect(mapStateToProps)(Component);
```
### After
```jsx
const user = useStore(s => s.user);
```

## Refactor 03 (Hard: No Selector
### Before
```jsx
const state = useStore(); // re-renders on ANY state change
```
### After
```jsx
const user = useStore(s => s.user); // only re-renders when user changes
```

---

## Approach Comparison — different ways to solve it

## Problem: Global State

### Approach 1: Context + useReducer
```jsx
const AppContext = createContext();
const [state, dispatch] = useReducer(reducer, initial);
<AppContext.Provider value={{ state, dispatch }}>
```

### Approach 2: Zustand
```jsx
const useStore = create((set) => ({ count: 0, increment: () => set(s => ({ count: s.count + 1 })) }));
```

**Winner:** Approach 2 — simpler, no provider, better performance.

---

## Problem: Persisted State

### Approach 1: Manual localStorage
```jsx
const [count, setCount] = useState(() => Number(localStorage.getItem("count")) || 0);
useEffect(() => { localStorage.setItem("count", count); }, [count]);
```

### Approach 2: Zustand persist
```jsx
const useStore = create(persist((set) => ({ count: 0 }), { name: "my-storage" }));
```

**Winner:** Approach 2 — automatic, cleaner.
