// Lesson 04 — Medium P02: Empty List Message
import { useState } from "react";
function EmptyList() {
  const [todos, setTodos] = useState([]);
  return (
    <div>
      <button onClick={() => setTodos([...todos, `Item ${todos.length + 1}`])}>Add</button>
      {todos.length === 0 ? <p>No todos yet!</p> : <ul>{todos.map((t, i) => <li key={i}>{t}</li>)}</ul>}
    </div>
  );
}
export default EmptyList;
