# Lesson 11 — Refactoring Challenges

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
