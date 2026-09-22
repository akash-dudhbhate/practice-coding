/*
LESSON 11 — Context API
EASY P03 — Language Context with Switcher
============================================
CONCEPT: A Provider's value can come from state, so changing the state re-renders every consumer automatically. This is how real theme/language switchers work.
PROBLEM: Create a `LangContext` (default "en") and a `greetings` map `{en, es, fr}`. Build a `Greeting` component that reads the language via `useContext` and renders the matching greeting. `App` holds `lang` in `useState`, provides it, and renders three buttons that call `setLang` with "en"/"es"/"fr".
TRY THIS: Render `<App />` and click the ES button — the greeting flips to "Hola!".
EXPECTED OUTPUT: "Hello!" by default; clicking FR shows "Bonjour!".
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
