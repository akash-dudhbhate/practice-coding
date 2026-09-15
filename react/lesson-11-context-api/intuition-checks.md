# Lesson 11 — Intuition Checks

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
