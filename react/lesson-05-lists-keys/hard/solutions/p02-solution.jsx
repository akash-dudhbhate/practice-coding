// Lesson 05 — Hard P02: Todo List with Item Components
import { useState } from "react";
function TodoItem({ todo, onDelete }) {
  return <li>{todo.text} <button onClick={() => onDelete(todo.id)}>Delete</button></li>;
}
function TodoWithComponents() {
  const [todos, setTodos] = useState([{ id: 1, text: "Learn React" }, { id: 2, text: "Build app" }]);
  const remove = (id) => setTodos(todos.filter((t) => t.id !== id));
  return (
    <ul>
      {todos.map((t) => <TodoItem key={t.id} todo={t} onDelete={remove} />)}
    </ul>
  );
}
export default TodoWithComponents;
