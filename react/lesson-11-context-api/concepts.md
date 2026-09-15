# Lesson 11 — Concepts Explained (Context API)

> Read this before solving the problems. Each concept explains:
> **What** it is · **Why** it exists · **Where** it's used · **What goes wrong** without it.

---

## Prop Drilling Problem

**What:** Passing props through multiple levels of components that don't need them, just to reach a deeply nested child.

```jsx
// Without Context: prop drilling
function App() {
    const [user, setUser] = useState({ name: "Akash" });
    return <Layout user={user} />;           // Layout doesn't need user
}

function Layout({ user }) {
    return <Sidebar user={user} />;          // Sidebar doesn't need user
}

function Sidebar({ user }) {
    return <UserProfile user={user} />;      // UserProfile needs user
}

function UserProfile({ user }) {
    return <h1>{user.name}</h1>;             // Finally uses it!
}
```

**Why it exists:** Without context, every intermediate component must accept and pass the prop → verbose, fragile (forget to pass it → undefined), hard to refactor. Context provides a way to skip intermediate levels.

**Where it's used:** Any data needed by deeply nested components — user auth, theme, language, app config.

**What goes wrong without it:**
- Adding a new prop → must pass through every level → touch 5 files for one change.
- Intermediate components receive props they don't use → confusing API.
- Refactoring → move a component → break the prop chain → `undefined` errors.

---

## createContext

**What:** `createContext` creates a context object that components can provide and consume.

```jsx
import { createContext, useContext } from 'react';

const UserContext = createContext(null);  // default value is null

// Provider: wraps components that need the context
function App() {
    const [user, setUser] = useState({ name: "Akash", role: "admin" });
    return (
        <UserContext.Provider value={user}>
            <Layout />
        </UserContext.Provider>
    );
}

// Consumer: any child can access the context
function UserProfile() {
    const user = useContext(UserContext);  // gets user without props!
    return <h1>{user.name}</h1>;
}
```

**Why it exists:** Without `createContext`, there's no way to share data across the component tree without prop drilling. Context creates a "tunnel" — the Provider sets the value, any descendant can access it with `useContext`.

**Where it's used:** Theme (dark/light), user authentication, language/i18n, feature flags, app configuration.

**What goes wrong without it:**
- No Provider → `useContext` returns the default value (null) → `user.name` → `TypeError: Cannot read property 'name' of null`. Always wrap the tree in a Provider.
- Default value is rarely useful → if you forget the Provider, you get `null` → crash. Set a meaningful default or always provide.
- Context value changes → ALL consumers re-render → performance issue for frequently changing values.

---

## Provider and Consumer

**What:** Provider sets the context value. Consumer (via `useContext`) reads it.

```jsx
// Provider — usually at the top of the app
function App() {
    const [theme, setTheme] = useState("light");

    return (
        <ThemeContext.Provider value={{ theme, setTheme }}>
            <Header />
            <Main />
            <Footer />
        </ThemeContext.Provider>
    );
}

// Consumer — any descendant, no matter how deep
function Header() {
    const { theme, setTheme } = useContext(ThemeContext);
    return (
        <header className={theme}>
            <button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
                Toggle Theme
            </button>
        </header>
    );
}

// Deeply nested consumer — no prop drilling!
function DeepComponent() {
    const { theme } = useContext(ThemeContext);
    return <div className={theme}>Themed content</div>;
}
```

**Why it exists:** Provider/Consumer pattern separates data provision from data consumption. The Provider doesn't need to know which components consume the context. Consumers don't need to know where the data comes from.

**Where it's used:** Every context — one Provider at the top, many Consumers throughout the tree.

**What goes wrong without it:**
- Provider value as an object `{ theme, setTheme }` → new object every render → ALL consumers re-render even if theme didn't change. Memoize the value: `useMemo(() => ({ theme, setTheme }), [theme])`.
- Multiple Providers of the same context → nearest Provider wins. Inner Provider overrides outer.
- Consumer outside any Provider → gets default value → usually null → crash.

---

## useContext Hook

**What:** `useContext` reads the current context value and subscribes to changes.

```jsx
const value = useContext(MyContext);
// value updates automatically when the Provider's value changes
```

**Why it exists:** Before `useContext`, you had to use `<MyContext.Consumer>` with a render prop → verbose, nested. `useContext` is a clean one-liner.

**Where it's used:** Every component that needs context data.

**What goes wrong without it:**
- `useContext` in a component NOT wrapped by a Provider → returns default → usually null → crash.
- Context value changes → component re-renders. If the value is an object that changes reference every render → unnecessary re-renders. Memoize.
- `useContext` returns the ENTIRE context value. If you only need one field, you still re-render when any field changes. Split contexts or use selectors.

---

## Multiple Contexts

**What:** Use multiple contexts for different concerns.

```jsx
const ThemeContext = createContext("light");
const UserContext = createContext(null);
const LanguageContext = createContext("en");

function App() {
    return (
        <ThemeContext.Provider value="dark">
            <UserContext.Provider value={{ name: "Akash" }}>
                <LanguageContext.Provider value="en">
                    <Header />
                </LanguageContext.Provider>
            </UserContext.Provider>
        </ThemeContext.Provider>
    );
}

function Header() {
    const theme = useContext(ThemeContext);
    const user = useContext(UserContext);
    const lang = useContext(LanguageContext);
    // ...
}
```

**Why it exists:** One context for everything → any change re-renders all consumers. Multiple contexts → only consumers of the changed context re-render. Better performance.

**Where it's used:** When you have independent pieces of global state — theme, user, language, notifications.

**What goes wrong without it:**
- Nesting too many Providers → "provider hell" → deeply nested JSX. Can flatten with a compose helper.
- Related values in separate contexts → need both → two `useContext` calls. If they always change together, combine them.
- Forgetting to wrap a Provider → consumer gets default → null → crash.

---

## Context with Reducer

**What:** Combine Context with `useReducer` for complex state management.

```jsx
const CartContext = createContext();

function cartReducer(state, action) {
    switch (action.type) {
        case 'ADD_ITEM':
            return { ...state, items: [...state.items, action.item] };
        case 'REMOVE_ITEM':
            return { ...state, items: state.items.filter(i => i.id !== action.id) };
        case 'CLEAR':
            return { ...state, items: [] };
        default:
            return state;
    }
}

function CartProvider({ children }) {
    const [state, dispatch] = useReducer(cartReducer, { items: [] });

    return (
        <CartContext.Provider value={{ state, dispatch }}>
            {children}
        </CartContext.Provider>
    );
}

// Usage
function Cart() {
    const { state, dispatch } = useContext(CartContext);
    return (
        <>
            {state.items.map(item => (
                <div key={item.id}>
                    {item.name}
                    <button onClick={() => dispatch({ type: 'REMOVE_ITEM', id: item.id })}>
                        Remove
                    </button>
                </div>
            ))}
        </>
    );
}
```

**Why it exists:** Context + `useReducer` is a lightweight alternative to Redux. Context provides the tunnel, `useReducer` provides structured state management. Good for medium-complexity apps.

**Where it's used:** Shopping carts, multi-step forms, app state that multiple components need to read and update.

**What goes wrong without it:**
- `dispatch` is stable (doesn't change between renders) → safe to pass without `useCallback`. But `state` changes → all consumers re-render.
- Forgetting to wrap the Provider → `useContext` returns `undefined` → `state.items` → crash.
- Over-using Context + Reducer for everything → even local state goes through context → over-engineering. Use context only for truly global state.

---

## Custom Hook with Context

**What:** Create a custom hook that wraps `useContext` for a cleaner API and error checking.

```jsx
function useCart() {
    const context = useContext(CartContext);
    if (context === undefined) {
        throw new Error('useCart must be used within a CartProvider');
    }
    return context;
}

// Usage — cleaner and safer
function Cart() {
    const { state, dispatch } = useCart();  // error if no Provider
    // ...
}
```

**Why it exists:** Without the custom hook, `useContext(CartContext)` returns `undefined` if no Provider → cryptic error later. The custom hook throws a clear error immediately → better debugging.

**Where it's used:** Every context — always create a `useXxx` hook alongside the context.

**What goes wrong without it:**
- Forgetting the Provider → `useContext` returns default (undefined) → `state.items` → `TypeError`. The custom hook catches this with a clear message.
- Not checking for undefined → error happens deep in the component → hard to trace. The hook's error message points directly to the missing Provider.

---

## When to Use Context (vs Props vs Redux)

**What:** Decision framework:

| Use Props when... | Use Context when... | Use Redux when... |
|---|---|---|
| Data is used by 1-2 levels | Data is needed by many deeply nested components | App has complex state interactions |
| Data is component-specific | Data is app-wide (theme, user, language) | State changes frequently and performance is critical |
| Simple parent-child | Medium complexity | Large-scale app with many reducers |

**Why it exists:** Over-using Context for everything → performance issues (all consumers re-render on any change). Under-using Context → prop drilling hell. Knowing when to use each is a key React skill.

**Where it's used:** Architecture decisions for every React app.

**What goes wrong without it:**
- Context for frequently changing state → all consumers re-render on every change → performance issues. Use Redux or Zustand for high-frequency updates.
- Props for deeply nested data → prop drilling → fragile, hard to maintain.
- Redux for simple state → over-engineering → unnecessary complexity. Context is simpler for most cases.
