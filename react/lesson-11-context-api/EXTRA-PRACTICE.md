# lesson-11-context-api — Extra Practice
Everything beyond the core lesson lives here, in order:
mental quizzes → debug drills → mistakes → refactoring → comparisons.

---

## Intuition Checks — predict before you run

## Check 01: Context vs Props
When should you use Context?
<details><summary>Answer</summary>
When data is needed by many components at different nesting levels (theme, auth, locale). Avoids "prop drilling" — passing props through many layers.
</details>

## Check 02: createContext default
```jsx
const Context = createContext("default");
```
<details><summary>Answer</summary>
Default value used when no Provider wraps the consumer. Useful for testing or standalone components.
</details>

## Check 03: useContext
```jsx
const value = useContext(MyContext);
```
<details><summary>Answer</summary>
Hook that subscribes to context. Re-renders when context value changes. Replaces `<Context.Consumer>` render prop pattern.
</details>

## Check 04: Performance
Does Context cause performance issues?
<details><summary>Answer</summary>
Yes — when context value changes, ALL consumers re-render, even if they only use part of the value. Split contexts or use memoization to mitigate.
</details>

## Check 05: Nested providers
```jsx
<ThemeContext.Provider value="dark">
  <AuthContext.Provider value={user}>
    <App />
  </AuthContext.Provider>
</ThemeContext.Provider>
```
<details><summary>Answer</summary>
Providers can nest. Each provides its own context. Components can use multiple contexts.
</details>

---

## Debug Exercises — find and fix the bug

## Debug 01 (Easy: Consumer Outside Provider
```jsx
const ThemeContext = createContext("light");
function Component() {
  const theme = useContext(ThemeContext);
  return <div>{theme}</div>;
}
// Component rendered without <ThemeContext.Provider>
```
<details><summary>Answer</summary>
**Bug:** Component uses context but no Provider wraps it. Gets default value "light" (may not be intended).
**Fix:** Wrap app in `<ThemeContext.Provider value="dark">`.
</details>

## Debug 02 (Medium): Value Object Recreated
```jsx
<ThemeContext.Provider value={{ theme: "dark", toggle: handleToggle }}>
```
<details><summary>Answer</summary>
**Bug:** New object every render → all consumers re-render even if values didn't change.
**Fix:** `const value = useMemo(() => ({ theme, toggle }), [theme, toggle]);`.
</details>

## Debug 03 (Hard): Context Not Updating
```jsx
const [theme, setTheme] = useState("light");
// Provider value is hardcoded
<ThemeContext.Provider value="dark">
```
<details><summary>Answer</summary>
**Bug:** Provider value is hardcoded "dark", not using state. Changing state doesn't update context.
**Fix:** `<ThemeContext.Provider value={theme}>`.
</details>

---

## Common Mistakes — the traps learners hit

## Mistake 01: Using Context for everything
```jsx
// WRONG — Context for local state
const LocalContext = createContext();
function Component() {
  const [state, setState] = useState(0);
  return <LocalContext.Provider value={{ state, setState }}>...</LocalContext.Provider>;
}
// CORRECT — just use props for local state
```

## Mistake 02: Recreating provider value
```jsx
// WRONG — new object every render
<Context.Provider value={{ a, b }}>
// CORRECT — memoize
const value = useMemo(() => ({ a, b }), [a, b]);
<Context.Provider value={value}>
```

## Mistake 03: Default value instead of Provider
```jsx
// WRONG — relies on default, no Provider
const Context = createContext({ user: null });
// CORRECT — explicit Provider
<Context.Provider value={{ user }}>
```

## Mistake 04: Single mega-context
```jsx
// WRONG — everything in one context
const AppContext = createContext();
// Changing any value re-renders all consumers
// CORRECT — split by concern
const ThemeContext = createContext();
const AuthContext = createContext();
```

## Mistake 05: Not exporting context
```jsx
// Context must be exported for consumers to use it
export const ThemeContext = createContext();
```

---

## Refactoring Challenges — make working code better

## Refactor 01 (Easy): Prop Drilling
### Before
```jsx
<App theme={theme} />
  <Layout theme={theme} />
    <Sidebar theme={theme} />
      <Button theme={theme} />
```
### After
```jsx
<ThemeContext.Provider value={theme}>
  <Layout><Sidebar><Button /></Sidebar></Layout>
</ThemeContext.Provider>
```

## Refactor 02 (Medium): Context for Everything
### Before
```jsx
<UserContext.Provider><ThemeContext.Provider><AuthContext.Provider>
```
### After
```jsx
// Only use context for truly global state
// Local state stays in components
```

## Refactor 03 (Hard): Context Value Recreating
### Before
```jsx
const value = { user, login, logout };
<UserContext.Provider value={value}> // new object every render
```
### After
```jsx
const value = useMemo(() => ({ user, login, logout }), [user, login, logout]);
<UserContext.Provider value={value}>
```

---

## Approach Comparison — different ways to solve it

## Problem: Theme Management

### Approach 1: Prop drilling
```jsx
<App theme="dark">
  <Header theme="dark">
    <Nav theme="dark">
```
**Cons:** Verbose, every layer needs the prop.

### Approach 2: Context
```jsx
<ThemeContext.Provider value="dark">
  <App />
</ThemeContext.Provider>
// Any component: const theme = useContext(ThemeContext);
```

**Winner:** Approach 2 — no prop drilling.

---

## Problem: Split Contexts

### Approach 1: Single context
```jsx
const AppContext = createContext();
<AppContext.Provider value={{ theme, user, cart }}>
```
**Cons:** Any change re-renders all consumers.

### Approach 2: Multiple contexts
```jsx
<ThemeContext.Provider value={theme}>
  <UserContext.Provider value={user}>
    <CartContext.Provider value={cart}>
```

**Winner:** Approach 2 — only consumers of changed context re-render.
