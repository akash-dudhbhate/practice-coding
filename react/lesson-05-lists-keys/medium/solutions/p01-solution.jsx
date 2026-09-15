// Lesson 05 — Medium P01: Dynamic Todo List
import { useState } from "react";
function DynamicTodo() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState("");
  const add = () => { if (input.trim()) { setTodos([...todos, { id: Date.now(), text: input.trim() }]); setInput(""); } };
  const remove = (id) => setTodos(todos.filter((t) => t.id !== id));
  return (
    <div>
      <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Add todo" />
      <button onClick={add}>Add</button>
      <ul>{todos.map((t) => <li key={t.id}>{t.text} <button onClick={() => remove(t.id)}>x</button></li>)}</ul>
    </div>
  );
}
export default DynamicTodo;
