# Lesson 06 — Coding Check

Use this to verify your solutions before asking me to review.

## Easy

### p01-solve.jsx (Document Title Updater)
- [ ] Uses `useEffect` with `[count]` dependency array.
- [ ] Effect sets `document.title` to include the count.
- [ ] Has a button to increment count.
- [ ] Test: Click counter 5 times → browser tab title shows count 5.
- [ ] Test: Title updates on every count change, not just on mount.
- [ ] Test: No infinite loop (effect doesn't set state that triggers re-run).

### p02-solve.jsx (Mount Message)
- [ ] Uses `useEffect` with `[]` (empty dependency array).
- [ ] Effect calls `console.log("Component mounted")`.
- [ ] Test: On mount → console shows "Component mounted" once.
- [ ] Test: Re-renders (from state changes) → message does NOT log again.
- [ ] Test: No dependency warnings from linter.

### p03-solve.jsx (Window Width Tracker)
- [ ] Uses `useEffect` with `[]` for adding resize listener.
- [ ] `window.addEventListener("resize", handler)` in effect.
- [ ] Returns cleanup: `return () => window.removeEventListener("resize", handler)`.
- [ ] Handler uses a named function (not inline arrow) so it can be removed.
- [ ] Test: Resize window → width updates on screen.
- [ ] Test: Component unmounts → no errors, listener removed (no memory leak).

## Medium

### p01-solve.jsx (Fetch User on Mount)
- [ ] Uses `useEffect` with `[]` to fetch on mount.
- [ ] Has `loading` state set to `true` initially, `false` after fetch.
- [ ] Has `error` state for error handling.
- [ ] Has `user` state for the fetched data.
- [ ] Shows "Loading..." while loading.
- [ ] Shows user data (name, email) after fetch.
- [ ] Test: On mount → shows "Loading...".
- [ ] Test: After fetch completes → shows user data.
- [ ] Test: If fetch fails → shows error message.
- [ ] Test: No infinite re-fetch loop.

### p02-solve.jsx (Countdown Timer)
- [ ] Uses `useState(10)` for countdown value.
- [ ] Uses `useEffect` with `setInterval` to decrement every second.
- [ ] Uses functional update: `setSeconds(prev => prev - 1)`.
- [ ] Returns cleanup: `return () => clearInterval(interval)`.
- [ ] Stops at 0 (clears interval when seconds reaches 0).
- [ ] Test: Starts at 10, counts down: 9, 8, 7...
- [ ] Test: Reaches 0 and stops (doesn't go to -1).
- [ ] Test: Unmount during countdown → no errors, interval cleared.

### p03-solve.jsx (Re-fetch on Prop Change)
- [ ] Uses `useEffect` with `[userId]` dependency.
- [ ] Fetches user data for the current `userId`.
- [ ] Shows loading state when `userId` changes (re-fetching).
- [ ] Test: Mount with userId=1 → fetches and shows user 1.
- [ ] Test: Change userId to 2 → re-fetches, shows user 2.
- [ ] Test: Loading state appears during re-fetch.
- [ ] Test: No stale data (user 1's data replaced by user 2's).

## Hard

### p01-solve.jsx (Live Search with Debounce)
- [ ] Has a search input with `onChange` updating query state.
- [ ] Uses `useEffect` with `[query]` dependency.
- [ ] Sets a `setTimeout` of 500ms before "fetching" (or logging).
- [ ] Returns cleanup: `return () => clearTimeout(timeout)` to cancel previous timeout.
- [ ] Test: Type "r" → no immediate search.
- [ ] Test: Type "react" quickly → only ONE search after 500ms of inactivity.
- [ ] Test: Type "r", wait 500ms, type "e" → two searches (one for "r", one for "re" after debounce).
- [ ] Test: Rapid typing → no duplicate or overlapping searches (cleanup works).

### p02-solve.jsx (Mouse Position Tracker)
- [ ] Uses `useState` for x and y coordinates.
- [ ] Uses `useEffect` with `[]` to add `mousemove` listener.
- [ ] Handler updates state: `setPos({ x: e.clientX, y: e.clientY })`.
- [ ] Returns cleanup: `removeEventListener("mousemove", handler)`.
- [ ] Handler is a named function (not inline) so it can be removed.
- [ ] Test: Move mouse → x/y coordinates update in real time.
- [ ] Test: Unmount → no errors, listener removed.
- [ ] Test: No memory leak warnings in console.

### p03-solve.jsx (Multiple Effects Chat)
- [ ] Has 3 separate `useEffect` calls (not one giant effect).
- [ ] Effect 1: fetches messages when `roomId` changes (`[roomId]` dep).
- [ ] Effect 2: updates `document.title` when `roomId` changes (`[roomId]` dep).
- [ ] Effect 3: sets up a mock WebSocket/polling with cleanup (`[roomId]` dep).
- [ ] Each effect that sets up something returns a cleanup function.
- [ ] Test: Change roomId → messages re-fetch, title updates, WebSocket reconnects.
- [ ] Test: Unmount → all cleanups run (no leaks, no errors).
- [ ] Test: Effects don't interfere with each other.
- [ ] Test: No infinite loops from state updates in effects.
