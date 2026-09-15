# Lesson 12 — Concepts Explained (useReducer)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## useReducer Basics

**What:** `useReducer` is an alternative to `useState` for complex state logic. It uses a reducer function and actions.

```jsx
import { useReducer } from 'react';

// Reducer function: (currentState, action) => newState
function counterReducer(state, action) {
    switch (action.type) {
        case 'increment': return { count: state.count + 1 };
        case 'decrement': return { count: state.count - 1 };
        case 'reset':     return { count: 0 };
        case 'set':       return { count: action.payload };
        default:          return state;  // IMPORTANT: return state for unknown actions
    }
}

function Counter() {
    const [state, dispatch] = useReducer(counterReducer, { count: 0 });

    return (
        <>
            <p>Count: {state.count}</p>
            <button onClick={() => dispatch({ type: 'increment' })}>+</button>
            <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
            <button onClick={() => dispatch({ type: 'reset' })}>Reset</button>
            <button onClick={() => dispatch({ type: 'set', payload: 10 })}>Set 10</button>
        </>
    );
}
```

**Why it exists:** For complex state with multiple sub-values or when next state depends on previous in complex ways, `useState` leads to scattered logic. `useReducer` centralizes all state transitions in one function → easier to test, debug, and understand.

**Where it's used:** Forms with multiple fields, shopping carts, multi-step wizards, games, any state with complex transition logic.

**What goes wrong without it:**
- Forgetting `default: return state` → unknown action returns `undefined` → state is lost → component breaks.
- Mutating state in reducer: `state.count += 1` → React doesn't detect the change (same reference) → no re-render. Always return a NEW object.
- Action type typo: `dispatch({ type: 'incrment' })` → hits default → nothing happens → silent bug.

---

## useState vs useReducer

**What:** When to use which:

| useState | useReducer |
|---------|-----------|
| Simple values (string, number, boolean) | Complex state (objects with multiple fields) |
| Independent state variables | Related state that changes together |
| 1-2 state variables | Many state variables with interdependent logic |
| Simple updates (`setCount(c + 1)`) | Complex transitions (if X then Y else Z) |
| Quick to set up | More boilerplate but more structured |

```jsx
// useState — simple, good for independent values
const [name, setName] = useState("");
const [age, setAge] = useState(0);

// useReducer — better for related, complex state
const [form, dispatch] = useReducer(formReducer, {
    name: "",
    age: 0,
    errors: {},
    isSubmitting: false,
});
```

**Why it exists:** `useState` is simpler but doesn't scale to complex state. `useReducer` provides structure for complex state → testable reducer, clear action types, centralized logic.

**Where it's used:** Simple state → `useState`. Complex state → `useReducer`. Many React apps use both — `useState` for simple components, `useReducer` for complex ones.

**What goes wrong without it:**
- Using `useState` for complex state → multiple `setState` calls that depend on each other → race conditions, stale state.
- Using `useReducer` for simple state → unnecessary boilerplate (reducer function, action types, dispatch) → over-engineering.
- Rule: if you have 3+ related state variables, consider `useReducer`.

---

## Action Types and Payloads

**What:** Actions are objects with a `type` (what to do) and optional `payload` (data needed).

```jsx
// Simple action — no payload
dispatch({ type: 'reset' });

// Action with payload
dispatch({ type: 'add_item', payload: { id: 1, name: "Apple", price: 1.50 } });

// Action with simple payload
dispatch({ type: 'set_count', payload: 10 });

// Reducer handling payloads
function reducer(state, action) {
    switch (action.type) {
        case 'add_item':
            return { ...state, items: [...state.items, action.payload] };
        case 'set_count':
            return { ...state, count: action.payload };
        default:
            return state;
    }
}
```

**Why it exists:** Without a convention, state updates are ad-hoc → hard to trace what changed and why. Action types create a clear log of what happened → debuggable, testable.

**Where it's used:** Every `useReducer` call. Action types are the API of your state management.

**What goes wrong without it:**
- Inconsistent action shapes: sometimes `{type, payload}`, sometimes `{type, value}`, sometimes `{type, id, name}` → confusing. Be consistent.
- Putting too much in payload → reducer logic moves to the dispatch call → defeats the purpose of centralizing logic. Keep logic in the reducer.
- String action types → typos cause silent failures. Consider using constants: `const ADD_ITEM = 'ADD_ITEM'`.

---

## Complex Reducer Example

**What:** A real-world reducer for a form with validation.

```jsx
const initialState = {
    values: { name: "", email: "", password: "" },
    errors: { name: "", email: "", password: "" },
    isSubmitting: false,
    submitSuccess: false,
};

function formReducer(state, action) {
    switch (action.type) {
        case 'SET_FIELD':
            return {
                ...state,
                values: { ...state.values, [action.field]: action.value },
                errors: { ...state.errors, [action.field]: "" },  // clear error on edit
            };
        case 'SET_ERROR':
            return {
                ...state,
                errors: { ...state.errors, [action.field]: action.message },
            };
        case 'SUBMIT_START':
            return { ...state, isSubmitting: true, submitSuccess: false };
        case 'SUBMIT_SUCCESS':
            return { ...state, isSubmitting: false, submitSuccess: true };
        case 'SUBMIT_ERROR':
            return { ...state, isSubmitting: false, submitSuccess: false };
        case 'RESET':
            return initialState;
        default:
            return state;
    }
}

// Usage
function ContactForm() {
    const [state, dispatch] = useReducer(formReducer, initialState);

    const handleChange = (e) => {
        dispatch({ type: 'SET_FIELD', field: e.target.name, value: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        dispatch({ type: 'SUBMIT_START' });
        // validate, then submit...
    };

    // ...
}
```

**Why it exists:** This form has 4 pieces of related state (values, errors, isSubmitting, submitSuccess) that change together. With `useState`, you'd need 4 separate states and coordinate them → messy. `useReducer` handles all transitions in one place.

**Where it's used:** Forms, wizards, data fetching (loading/data/error), any multi-field state.

**What goes wrong without it:**
- Spreading state: `return { ...state, values: { ...state.values, [field]: value } }` → must spread at EVERY level. Forgetting one spread → overwrites the entire sub-object.
- `SET_FIELD` clearing the error for that field → good UX (error disappears when user starts typing). Forgetting this → error stays even after fixing.
- `SUBMIT_START` without `SUBMIT_SUCCESS`/`SUBMIT_ERROR` → `isSubmitting` stays true forever → loading spinner never stops.

---

## useReducer with Context

**What:** Share reducer state across the component tree via Context.

```jsx
const StoreContext = createContext();

function StoreProvider({ children }) {
    const [state, dispatch] = useReducer(storeReducer, initialState);
    return (
        <StoreContext.Provider value={{ state, dispatch }}>
            {children}
        </StoreContext.Provider>
    );
}

function useStore() {
    const context = useContext(StoreContext);
    if (!context) throw new Error('useStore must be used within StoreProvider');
    return context;
}

// Any component can access state and dispatch
function ProductList() {
    const { state, dispatch } = useStore();
    return state.products.map(p => <div key={p.id}>{p.name}</div>);
}

function AddProduct() {
    const { dispatch } = useStore();
    return <button onClick={() => dispatch({ type: 'ADD_PRODUCT', payload: newItem })}>Add</button>;
}
```

**Why it exists:** `useReducer` alone is local to one component. With Context, multiple components can dispatch actions and read state → lightweight Redux alternative.

**Where it's used:** App-wide state — shopping carts, auth, notifications, theme.

**What goes wrong without it:**
- `dispatch` is stable (same reference across renders) → safe to pass via context without `useCallback`. But `state` changes → all consumers re-render.
- Forgetting the Provider → `useStore` throws → good (clear error).
- Over-using this pattern for local state → unnecessary context wrapping. Use `useReducer` directly for component-local state.

---

## Lazy Initialization

**What:** Initialize the reducer state lazily (only on first render) — useful for expensive initial computations.

```jsx
function init(initialCount) {
    return {
        count: initialCount,
        history: Array(1000).fill(0),  // expensive initialization
    };
}

function reducer(state, action) {
    switch (action.type) {
        case 'increment': return { ...state, count: state.count + 1 };
        // ...
        default: return state;
    }
}

function Counter({ initialCount }) {
    const [state, dispatch] = useReducer(reducer, initialCount, init);
    // init(initialCount) runs only on first render
    // ...
}
```

**Why it exists:** Without lazy init, `useReducer(reducer, expensiveInit())` → `expensiveInit()` runs on EVERY render → wasted computation. The third argument (`init`) runs only once → performance.

**Where it's used:** When initial state requires computation (parsing localStorage, fetching, complex calculations).

**What goes wrong without it:**
- `useReducer(reducer, computeInitialState())` → `computeInitialState()` runs every render → slow. Use the third arg: `useReducer(reducer, initialArg, init)`.
- `init` function receives the second argument (`initialCount`) → must use it, not a global.
- `init` runs once → if the initial value prop changes later, the state doesn't update. This is by design (initial state is only initial).

---

## Testing Reducers

**What:** Reducers are pure functions → easy to test without React.

```javascript
// Reducer test
test('ADD_ITEM adds item to cart', () => {
    const initialState = { items: [], total: 0 };
    const action = { type: 'ADD_ITEM', payload: { id: 1, price: 10 } };
    const newState = cartReducer(initialState, action);

    expect(newState.items).toHaveLength(1);
    expect(newState.total).toBe(10);
});

test('REMOVE_ITEM removes item from cart', () => {
    const state = { items: [{ id: 1, price: 10 }], total: 10 };
    const action = { type: 'REMOVE_ITEM', payload: { id: 1 } };
    const newState = cartReducer(state, action);

    expect(newState.items).toHaveLength(0);
    expect(newState.total).toBe(0);
});
```

**Why it exists:** Reducers are pure functions (same input → same output, no side effects) → perfect for unit testing. You don't need to render components → fast, reliable tests.

**Where it's used:** Every reducer should be tested. Test each action type → verify state transitions.

**What goes wrong without it:**
- Not testing reducers → bugs in state transitions → hard to debug in the running app.
- Testing with impure reducers (side effects, API calls) → tests are flaky. Keep reducers pure.
- Not testing the `default` case → unknown actions should return state unchanged. Test this.
