/*
LESSON 18 — Tailwind CSS
HARD P01 — Dashboard Layout
============================================
CONCEPT: A full app shell is pure utility composition: `flex h-screen` for the frame, a `w-64`/`w-16` collapsible `aside` with `transition-all`, a header `flex` bar, and a scrollable `main` grid of cards.
PROBLEM: Build `Dashboard` with `collapsed` in `useState`: outer `flex h-screen bg-gray-100`; an `aside` (w-64 ↔ w-16 toggle button, dark bg, nav links `hover:bg-gray-700`); a `flex-1 flex flex-col` column holding a `header` with a search input, and `main` (`flex-1 p-6 overflow-auto`) containing a responsive stat-card grid, a "Recent Orders" `<table>`, and a chart placeholder card.
TRY THIS: Render `<Dashboard />` and click the collapse button — the sidebar animates narrow.
EXPECTED OUTPUT: Collapsible sidebar, search header, 3 stat cards, styled table, chart placeholder.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
