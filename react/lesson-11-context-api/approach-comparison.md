# Lesson 11 — Approach Comparison

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
