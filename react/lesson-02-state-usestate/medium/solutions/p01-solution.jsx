// Lesson 02 — Medium P01: Todo List Add/Remove
import { useState } from "react";
function TodoList() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState("");
  const addTodo = () => {
    if (input.trim()) { setTodos([...todos, { id: Date.now(), text: input.trim() }]); setInput(""); }
  };
  const removeTodo = (id) => setTodos(todos.filter((t) => t.id !== id));
  return (
    <div>
      <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Add todo" />
      <button onClick={addTodo}>Add</button>
      <ul>{todos.map((t) => <li key={t.id} onClick={() => removeTodo(t.id)}>{t.text}</li>)}</ul>
    </div>
  );
}
export default TodoList;
