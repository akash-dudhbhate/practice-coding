/*
LESSON 09 — useMemo & useCallback
MEDIUM P03 — Dashboard with Memo Widgets
============================================
CONCEPT: Memoization composes: memo() each widget, useMemo each data prop, useCallback each handler — then only the widget whose data actually changed re-renders.
PROBLEM: Build `Stats`, `Chart`, `Table` as `memo(...)` components taking `data` (+ `onUpdate` for Table). Build `Dashboard` with three state values, `useMemo` for stats/chart data, and `updateTable = useCallback(() => setTableData("6 rows"), [])`. Render all three widgets. Export `Dashboard` default.
TRY THIS: Render `<Dashboard />` and press Table's Update button.
EXPECTED OUTPUT: Only the Table widget re-renders; Stats and Chart stay untouched.
CHECK: python3 check.py medium/p03
*/
// TODO: write your component from scratch
