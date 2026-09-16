/*
LESSON 10 — Custom Hooks
HARD P01 — useEventListener Hook
============================================
CONCEPT: useEventListener(event, handler, element=window) turns add/removeEventListener + cleanup into a one-line declaration you can stack for keys, scroll, clicks.
PROBLEM: Build `useEventListener(eventName, handler, element = window)` with a `[eventName, handler, element]` effect doing add + cleanup-remove. Then `EventListenerDemo` uses it twice: Escape key closes a modal div, scroll logs `window.scrollY`; `modalOpen` state controls the modal. Export `EventListenerDemo` default.
TRY THIS: Render `<EventListenerDemo />`, press Escape, scroll the page.
EXPECTED OUTPUT: Escape closes the modal; console logs scroll positions.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
