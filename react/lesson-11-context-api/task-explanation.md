# Lesson 11 — Context API

## What you'll learn
- Prop drilling problem
- createContext and Provider/Consumer
- useContext hook
- Multiple contexts
- Context with useReducer
- Custom hook wrapper for context
- When to use Context vs Props vs Redux

## Lesson

### Create and use context
```jsx
const ThemeContext = createContext("light");
// Provider
<ThemeContext.Provider value="dark"><App /></ThemeContext.Provider>
// Consumer
const theme = useContext(ThemeContext);
```

### Custom hook wrapper
```jsx
function useTheme() {
    const ctx = useContext(ThemeContext);
    if (!ctx) throw new Error("useTheme must be inside ThemeProvider");
    return ctx;
}
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create a `ThemeContext` with light/dark values. Wrap an app in the Provider. A child component reads the theme via `useContext` and applies a className.

   WHAT IT SHOULD LOOK LIKE:
   ```
   +----------------------------------+
   | ###############################  |  <- <div className="dark">
   |  Current theme: dark             |
   +----------------------------------+
   ```
2. `easy/p02-solve.jsx` — Create a `UserContext` with `{name, role}`. Display the user's name in a deeply nested component (3+ levels deep) without prop drilling.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Welcome, Alice! Role: admin
      <- rendered by DeepChild (3 levels down, no props passed)
   ```
3. `easy/p03-solve.jsx` — Create a context for language preference ("en"/"es"/"fr"). A component displays a greeting based on the language. Add a button to switch languages.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Hello!                            <- greeting <p>
   [ EN ] [ ES ] [ FR ]              <- click FR -> "Bonjour!"
   ```

### Medium
4. `medium/p01-solve.jsx` — Create a `ThemeProvider` component that manages theme state and provides `{theme, toggleTheme}` via context. Multiple components consume it (header, sidebar, main). Toggling updates all.

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ Toggle theme ]
   +----------------------------------+
   | HEADER  (dark bg)                |
   +--------+-------------------------+
   | SIDE   | MAIN                    |
   | BAR    |  (all three flip        |
   | (dark) |   light <-> dark        |
   +--------+-------------------------+
   ```
5. `medium/p02-solve.jsx` — Create two separate contexts: `UserContext` and `ThemeContext`. Nest both Providers. Components consume from both independently. Show that changing one doesn't affect the other.

   WHAT IT SHOULD LOOK LIKE:
   ```
   LIGHT:                     DARK (after toggle):
   +------------------+       +------------------+
   | Alice - light    |       |##################|
   | (white bg)       |       | Alice - dark     |
   +------------------+       | (dark bg)        |
   [ Toggle ]                 +------------------+
   ```
6. `medium/p03-solve.jsx` — Create a `useTheme` custom hook that wraps `useContext` with error checking. Throw a clear error if used outside the Provider. Use it in a component.

   WHAT IT SHOULD LOOK LIKE:
   ```
   INSIDE PROVIDER:           OUTSIDE PROVIDER:
   Theme: dark                (thrown error: "useTheme must be
                              used within ThemeProvider")
   ```

### Hard
7. `hard/p01-solve.jsx` — Build a shopping cart with Context + useReducer: `CartProvider` manages `{items, total}` with ADD_ITEM, REMOVE_ITEM, UPDATE_QTY, CLEAR actions. Multiple components (cart icon, cart page, product list) consume the context.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Products:  [Apple +] [Bread +] [Milk +]
   Cart (2 items):
   * Apple  x2   [ + ][ - ][Remove]
   * Bread  x1   [ + ][ - ][Remove]
   Total: $5.25        [ Clear Cart ]
   ```
8. `hard/p02-solve.jsx` — Build an auth system with Context: `AuthProvider` manages `{user, login, logout, register}`. Protected components check auth via `useAuth()` hook. Show login form, protected dashboard, and logout button.

   WHAT IT SHOULD LOOK LIKE:
   ```
   LOGGED OUT:                LOGGED IN:
   +------------------+       Welcome, alice
   | alice@x.com      |       [ Logout ]
   +------------------+
   [ Login ]
   ```
9. `hard/p03-solve.jsx` — Build a multi-language app with Context: `LanguageProvider` manages current language and translation dictionary. `useTranslation()` hook returns `t(key)` function. Display a page with 5+ translated strings and a language switcher (en/es/fr).

   WHAT IT SHOULD LOOK LIKE:
   ```
   [ EN ] [ ES ] [ FR ]
   Welcome                    <- t("welcome")
   Profile                    <- t("profile")
   Settings                   <- t("settings")
   Goodbye                    <- t("goodbye")
   Logout                     <- t("logout")
   (clicking ES switches all to "Bienvenido..." etc.)
   ```

### How to work
- Write your complete React solution (context, provider, consumers).
- Remove the TODO comment when done.
- Test by importing into a React app or using a sandbox.
