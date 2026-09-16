/*
LESSON 06 — useEffect & Side Effects
HARD P03 — Multiple Effects Chat
============================================
CONCEPT: One component can hold several useEffects, each with its own dep array — split unrelated side effects instead of merging them.
PROBLEM: Build a `Chat({ roomId })` component with `messages` state. Effect 1 (`[roomId]`): clear messages, fetch posts for that userId, keep 5 titles. Effect 2 (`[roomId]`): set `document.title` to the room. Effect 3 (`[]`): open a mock WebSocket object and `close()` it in cleanup. Render room heading + message list.
TRY THIS: Render `<Chat roomId={1} />` then switch to `roomId={2}`.
EXPECTED OUTPUT: Tab title shows the room; message list reloads when roomId changes.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
