/*
LESSON 10 — Custom Hooks
EASY P03 — useWindowSize Hook
============================================
CONCEPT: The resize-listener-with-cleanup pattern becomes reusable the moment you wrap it in `useWindowSize` — components just read {width, height}.
PROBLEM: Build `useWindowSize()` with `{width, height}` state and a `[]`-deps effect adding/removing the window "resize" listener. Then a `WindowDemo` rendering "Window: W x H". Export `WindowDemo` default.
TRY THIS: Render `<WindowDemo />` and resize the browser.
EXPECTED OUTPUT: Dimensions text updates live as the window resizes.
CHECK: python3 check.py easy/p03
*/
// TODO: write your component from scratch
