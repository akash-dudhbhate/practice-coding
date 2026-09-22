/*
LESSON 09 — useMemo & useCallback
MEDIUM P02 — TodoList with Memo Items
============================================
CONCEPT: React.memo children re-render only when props change — but a fresh inline function IS a new prop, so the delete handler needs useCallback with a functional setState.
PROBLEM: Build `TodoItem = memo(({ todo, onDelete }) => <li>{todo.text} <button>x</button></li>)` logging each render, then a `TodoList` with `todos`/`input` state, `handleDelete = useCallback(id => setTodos(prev => prev.filter(...)), [])`, and an Add flow. Map todos to `<TodoItem key={t.id} ... />`. Export `TodoList` default.
TRY THIS: Render `<TodoList />` and add a third todo.
EXPECTED OUTPUT: Only the new TodoItem logs a render — existing items stay memoized.
CHECK: python3 check.py medium/p02
*/
// TODO: write your component from scratch
