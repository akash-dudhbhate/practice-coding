/*
LESSON 18 — Tailwind CSS
HARD P02 — Dark Mode Toggle
============================================
CONCEPT: Tailwind's `dark:` variant activates when a `dark` class sits on `<html>`. React's job: toggle `document.documentElement.classList` in a `useEffect` and persist the choice in `localStorage` (read lazily in `useState`'s initializer).
PROBLEM: Build `DarkModeApp`: `dark` state initialized from `localStorage.getItem("theme") === "dark"`; a `useEffect` that `classList.toggle("dark", dark)` on `document.documentElement` and saves `localStorage.setItem("theme", ...)`. Render a `min-h-screen` container using `dark:` variants throughout (`dark:bg-gray-900`, `dark:text-white`…), a toggle button, and a grid of 3 dark-aware cards.
TRY THIS: Render `<DarkModeApp />`, toggle dark — everything inverts; reload — your choice persists.
EXPECTED OUTPUT: Full light↔dark theme flip via `dark:` classes; survives page reload.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
