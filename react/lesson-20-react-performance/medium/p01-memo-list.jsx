/*
LESSON 20 — React Performance
MEDIUM P01 — 100 Memoized Items + useCallback Delete
============================================
CONCEPT: The list pattern: `memo` each row AND `useCallback` the per-row handler — deleting one item must not re-render the other 99. Both halves are required; either alone leaks re-renders.
PROBLEM: Create `const ListItem = memo(({item, onDelete}) => ...)` logging `Item N rendered` and rendering `item.text` + a Delete button calling `onDelete(item.id)`. Build `LargeList` with 100 items (`useState(() => ...)`), `handleDelete = useCallback((id) => setItems(prev => prev.filter(...)), [])`, and a `<ul>` mapping items to `<ListItem key={item.id} item onDelete={handleDelete} />`.
TRY THIS: Render `<LargeList />`, delete item 5 — console shows only ONE re-render, not 99.
EXPECTED OUTPUT: Initial 100 render logs; each delete logs exactly one item.
CHECK: python3 check.py medium/p01
*/
// TODO: write your component from scratch
