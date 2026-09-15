# Lesson 11 — Common Mistakes

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
