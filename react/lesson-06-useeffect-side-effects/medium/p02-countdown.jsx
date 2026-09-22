/*
LESSON 06 — useEffect & Side Effects
MEDIUM P02 — Countdown Timer
============================================
CONCEPT: setInterval in an effect needs `clearInterval` in cleanup — and with `[count]` deps each tick swaps in a fresh timer.
PROBLEM: Build a `Countdown` component with `count` state starting at 10. In a `[count]`-deps effect: bail when count hits 0, else `setInterval` decrements via functional update every 1s; cleanup clears it. Render the number or "Done!".
TRY THIS: Render `<Countdown />` and watch.
EXPECTED OUTPUT: Counts 10 → 0 once per second, then shows "Done!".
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
