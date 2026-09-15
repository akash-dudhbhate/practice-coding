// Lesson 17 — Easy P03: Todo store
import { create } from "zustand";
import { useState } from "react";
const useTodoStore = create((set) => ({
  todos: [],
  addTodo: (text) => set((s) => ({ todos: [...s.todos, { id: Date.now(), text, done: false }] })),
  toggleTodo: (id) => set((s) => ({ todos: s.todos.map((t) => t.id === id ? { ...t, done: !t.done } : t) })),
  deleteTodo: (id) => set((s) => ({ todos: s.todos.filter((t) => t.id !== id) })),
}));
function TodoApp() {
  const { todos, addTodo, toggleTodo, deleteTodo } = useTodoStore();
  const [input, setInput] = useState("");
  return (
    <div>
      <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Add todo" />
      <button onClick={() => { if (input.trim()) { addTodo(input.trim()); setInput(""); } }}>Add</button>
      <ul>{todos.map((t) => <li key={t.id} onClick={() => toggleTodo(t.id)}>{t.done ? "✓ " : ""}{t.text} <button onClick={(e) => { e.stopPropagation(); deleteTodo(t.id); }}>x</button></li>)}</ul>
    </div>
  );
}
export default TodoApp;
