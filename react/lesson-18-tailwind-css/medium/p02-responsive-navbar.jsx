/*
LESSON 18 — Tailwind CSS
MEDIUM P02 — Responsive Navbar with Hamburger
============================================
CONCEPT: `hidden md:flex` shows the link row only on tablet+; `md:hidden` shows the ☰ button only on mobile. The mobile menu's open state still needs `useState` — Tailwind handles visibility, React handles interaction.
PROBLEM: Build `Navbar`: a `nav` (flex, justify-between, shadow) with a bold "Logo" div, a link row `hidden md:flex gap-4` (4 links, `hover:text-blue-500`), a `md:hidden` hamburger button toggling `open` state, and a conditional `md:hidden` dropdown panel with the same links stacked.
TRY THIS: Render `<Navbar />` and narrow the window — links collapse into a working ☰ menu.
EXPECTED OUTPUT: Inline links on desktop; hamburger + dropdown on mobile.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
