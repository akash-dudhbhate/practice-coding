/*
LESSON 08 — useRef & DOM Access
MEDIUM P01 — Stopwatch
============================================
CONCEPT: Interval IDs are mutable bookkeeping, not UI — store them in a ref so start/stop don't trigger renders; the visible time stays in state.
PROBLEM: Build a `Stopwatch` with `time` state and `intervalRef`. `start` sets `setInterval(() => setTime(t => t + 1), 100)` (guarded so it can't double-start), `stop` clears the interval and nulls the ref, `reset` stops + zeroes. Render seconds and three buttons.
TRY THIS: Render `<Stopwatch />`, Start, wait ~1s, Stop, Reset.
EXPECTED OUTPUT: Time ticks up in tenths, freezes on Stop, zeroes on Reset.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
