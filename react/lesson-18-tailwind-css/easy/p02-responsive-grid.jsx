/*
LESSON 18 — Tailwind CSS
EASY P02 — Responsive Grid
============================================
CONCEPT: Breakpoint prefixes (`md:`, `lg:`) make a class apply only above that screen width. `grid-cols-1 md:grid-cols-2 lg:grid-cols-3` reads: 1 column on mobile, 2 on tablet, 3 on desktop.
PROBLEM: Build `ResponsiveGrid`: a `div` with `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4` mapping `[1..6]` to colored box divs (alternate blue/purple, `text-white p-8 rounded-lg text-center`, `key` each).
TRY THIS: Render `<ResponsiveGrid />` and resize the browser — watch columns go 1 → 2 → 3.
EXPECTED OUTPUT: 1-col stack on mobile, 2 cols at md, 3 cols at lg breakpoints.
CHECK: python3 check.py easy/p02
*/
// TODO: write your component from scratch
