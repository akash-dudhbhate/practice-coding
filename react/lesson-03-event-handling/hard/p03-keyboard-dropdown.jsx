/*
LESSON 03 — Event Handling
HARD P03 — Keyboard-Navigable Dropdown
============================================
CONCEPT: Making a div focusable with `tabIndex={0}` lets it receive `onKeyDown`, so Enter/ArrowUp/ArrowDown/Escape can drive open + selected state.
PROBLEM: Build a `KeyboardDropdown` with `items` constant, `open` and `selected` state. The wrapper div has `tabIndex={0}` and `onKeyDown`: Enter toggles open, ArrowDown/ArrowUp move `selected` (clamped), Escape closes. Render the open list with the selected item highlighted; clicking an item selects + closes.
TRY THIS: Render `<KeyboardDropdown />`, focus it, press Enter, ArrowDown, Enter.
EXPECTED OUTPUT: Enter opens the menu; arrows move the highlight; Enter/Escape close it.
CHECK: python3 check.py hard/p03
*/
// TODO: write your component from scratch
