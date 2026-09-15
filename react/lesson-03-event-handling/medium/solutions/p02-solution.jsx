// Lesson 03 — Medium P02: Todo with Delete Buttons
import { useState } from "react";
function TodoDelete() {
  const [todos, setTodos] = useState([{ id: 1, text: "Learn React" }, { id: 2, text: "Build app" }]);
  const deleteTodo = (id) => setTodos(todos.filter((t) => t.id !== id));
  return (
    <ul>
      {todos.map((t) => (
        <li key={t.id}>{t.text} <button onClick={() => deleteTodo(t.id)}>Delete</button></li>
      ))}
    </ul>
  );
}
export default TodoDelete;
