/*
LESSON 11 — Context API
EASY P01 — Theme Context
============================================
CONCEPT: Context lets a component read data from far up the tree without prop drilling. createContext makes a context object, its Provider supplies the value, and useContext reads it in any descendant.
PROBLEM: Create a `ThemeContext` with default value "light". Build a `ThemedComponent` that reads the theme via `useContext(ThemeContext)` and renders a div with `className={theme}` showing the theme text. An `App` component wraps it in `<ThemeContext.Provider value="dark">`.
TRY THIS: Render `<App />`. Then change the Provider value from "dark" to "light".
EXPECTED OUTPUT: A div reading "Current theme: dark" with className "dark".
CHECK: python3 check.py easy/p01
*/
// TODO: write your component from scratch
