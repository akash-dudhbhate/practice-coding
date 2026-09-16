/*
LESSON 11 — Context API
HARD P03 — Multi-Language App (useTranslation)
============================================
CONCEPT: Real i18n is context plus a lookup function: a `t(key)` translator that resolves keys against a dictionary for the current language. Wrapping `t` in useCallback keeps its identity stable across re-renders.
PROBLEM: Build a `translations` dictionary keyed by `en`/`es`/`fr`, each holding at least 5 keys (welcome, goodbye, settings, profile, logout…). Create `LanguageContext`, a `LanguageProvider({children})` holding `lang` in `useState("en")` and providing `{lang, setLang}`, and a `useTranslation()` hook returning `{t, lang}` where `t(key)` looks up `translations[lang][key]` (falling back to the key itself). `App` renders 5+ strings via `t("…")` and three buttons calling `setLang`.
TRY THIS: Render `<App />` and click ES — every translated string flips to Spanish at once.
EXPECTED OUTPUT: "Welcome" in English; all strings switch to "Bienvenido…" on ES, "Bienvenue…" on FR.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
