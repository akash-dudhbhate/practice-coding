# Lesson 11 — Debug Exercises

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
