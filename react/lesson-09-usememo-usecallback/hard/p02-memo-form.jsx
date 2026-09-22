/*
LESSON 09 — useMemo & useCallback
HARD P02 — Form with Memoized Fields
============================================
CONCEPT: One memo'd Field component + one useCallback handler per field means typing in Name re-renders ONLY the Name field — each handler uses functional setState to stay stable.
PROBLEM: Build `Field = memo(({ label, value, onChange }) => <div><label>{label}: <input .../></label></div>)` logging renders. Build `MemoForm` with `form` ({name,email,phone}) state and three `useCallback` handlers using `setForm(f => ({...f, key: v}))`. Render three `<Field>`s. Export `MemoForm` default.
TRY THIS: Render `<MemoForm />` and type one letter in Name.
EXPECTED OUTPUT: Console logs only "Name rendered" — Email and Phone don't re-render.
CHECK: python3 check.py hard/p02
*/
// TODO: write your component from scratch
