/*
LESSON 20 — React Performance
HARD P02 — useTransition for Non-Urgent Updates
============================================
CONCEPT: `useTransition` splits updates by urgency: `setQuery(value)` runs NOW (input stays responsive) while `startTransition(() => setFiltered(...))` schedules the expensive filter as interruptible background work. `isPending` flags the in-flight transition.
PROBLEM: Build `TransitionSearch`: `query` + `filtered` states; `[isPending, startTransition] = useTransition()`; memoized 10,000-item array. `handleChange` sets query immediately, then wraps `setFiltered(items.filter(i => i.includes(value)))` in `startTransition`. Render the input, "Filtering..." on `isPending`, the count, and first 20 results.
TRY THIS: Render `<TransitionSearch />` and hold a key down — input echoes instantly even though filtering 10k items per keystroke.
EXPECTED OUTPUT: Typing never blocks; "Filtering..." appears until each transition lands.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
