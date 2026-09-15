# Lesson 11 — Coding Check

## Easy

### p01-solve.jsx — ThemeContext
- [ ] `createContext` used to create ThemeContext
- [ ] Provider wraps the app with a theme value
- [ ] Child component uses `useContext(ThemeContext)`
- [ ] Theme value applied as className
- [ ] No prop drilling (child accesses context directly)

### p02-solve.jsx — UserContext deep nesting
- [ ] UserContext created with user object
- [ ] Provider at the top level
- [ ] Consumer is 3+ levels deep
- [ ] No props passed through intermediate components
- [ ] User name displayed in the deep component

### p03-solve.jsx — Language context
- [ ] Language context created
- [ ] Provider manages current language
- [ ] Component displays greeting based on language
- [ ] Button switches between languages
- [ ] Greeting updates when language changes

## Medium

### p01-solve.jsx — ThemeProvider with toggle
- [ ] `ThemeProvider` component manages theme state
- [ ] Provides `{theme, toggleTheme}` via context
- [ ] Multiple components consume the context
- [ ] Toggling theme updates ALL consuming components
- [ ] No prop drilling

### p02-solve.jsx — Multiple contexts
- [ ] `UserContext` and `ThemeContext` are separate
- [ ] Both Providers nested in the app
- [ ] Components consume from both contexts
- [ ] Changing theme doesn't re-render user-only consumers (ideally)
- [ ] Both work independently

### p03-solve.jsx — useTheme custom hook
- [ ] `useTheme()` hook wraps `useContext`
- [ ] Throws clear error if used outside Provider
- [ ] Error message: "useTheme must be used within ThemeProvider"
- [ ] Returns context value when used correctly
- [ ] Component uses `useTheme()` instead of `useContext`

## Hard

### p01-solve.jsx — Shopping cart with reducer
- [ ] `CartProvider` uses `useReducer`
- [ ] Actions: ADD_ITEM, REMOVE_ITEM, UPDATE_QTY, CLEAR
- [ ] Cart icon shows item count
- [ ] Cart page lists items with quantities
- [ ] Product list can add items to cart
- [ ] Total price calculated
- [ ] All components access cart via context (no props)

### p02-solve.jsx — Auth system
- [ ] `AuthProvider` manages user state
- [ ] `login(username, password)` function
- [ ] `logout()` function
- [ ] `useAuth()` custom hook with error checking
- [ ] Login form calls login function
- [ ] Protected dashboard only shows when logged in
- [ ] Logout button clears user state
- [ ] Protected components check auth status

### p03-solve.jsx — Multi-language app
- [ ] `LanguageProvider` manages current language
- [ ] Translation dictionary with 5+ keys for each language
- [ ] `useTranslation()` hook returns `t(key)` function
- [ ] `t("greeting")` returns translated string
- [ ] Language switcher (en/es/fr)
- [ ] All text updates when language changes
- [ ] Falls back to English if key missing in selected language
