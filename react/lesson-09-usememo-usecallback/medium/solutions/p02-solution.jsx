// Lesson 09 — Medium P02: TodoList with React.memo items
import { useState, useCallback, memo } from "react";
const TodoItem = memo(({ todo, onDelete }) => { console.log("TodoItem rendered:", todo.id); return <li>{todo.text} <button onClick={() => onDelete(todo.id)}>x</button></li>; });
function TodoList() {
  const [todos, setTodos] = useState([{ id: 1, text: "Learn React" }, { id: 2, text: "Build app" }]);
  const [input, setInput] = useState("");
  const handleDelete = useCallback((id) => setTodos((prev) => prev.filter((t) => t.id !== id)), []);
  const addTodo = () => { if (input.trim()) { setTodos([...todos, { id: Date.now(), text: input.trim() }]); setInput(""); } };
  return (
    <div>
      <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Add todo" />
      <button onClick={addTodo}>Add</button>
      <ul>{todos.map((t) => <TodoItem key={t.id} todo={t} onDelete={handleDelete} />)}</ul>
    </div>
  );
}
export default TodoList;
