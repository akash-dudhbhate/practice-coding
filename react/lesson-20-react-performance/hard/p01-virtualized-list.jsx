/*
LESSON 20 — React Performance
HARD P01 — Virtualized List (react-window)
============================================
CONCEPT: Rendering 10,000 DOM nodes kills performance. `react-window`'s `FixedSizeList` mounts only the ~visible rows (viewport ÷ itemSize), recycling them on scroll — O(visible) DOM nodes regardless of data size.
PROBLEM: Build `VirtualizedList`: `search` state; `items` = memoized 10,000 strings; `filtered` = memoized `items.filter(includes search)` — filter the DATA, not the DOM. A `Row` component `({index, style}) => <div style={style}>` rendering `filtered[index]` (the `style` prop positions each row — required). Render the search input, a count, and `<List height={400} itemCount={filtered.length} itemSize={35} width="100%">{Row}</List>` (import `FixedSizeList as List` from "react-window").
TRY THIS: Render `<VirtualizedList />` and scroll hard — buttery smooth; inspect the DOM — only ~12 rows exist.
EXPECTED OUTPUT: 10k items scroll smoothly; search narrows the list instantly.
CHECK: python3 check.py hard/p01
*/
// TODO: write your component from scratch
