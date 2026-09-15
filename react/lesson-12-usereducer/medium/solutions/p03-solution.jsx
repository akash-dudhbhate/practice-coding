// Lesson 12 — Medium P03: TodoProvider with useReducer + Context
import { useReducer, createContext, useContext } from "react";
const TodoContext = createContext(null);
const reducer = (state, action) => {
  switch (action.type) {
    case "ADD": return [...state, { id: Date.now(), text: action.text, done: false }];
    case "TOGGLE": return state.map((t) => t.id === action.id ? { ...t, done: !t.done } : t);
    case "DELETE": return state.filter((t) => t.id !== action.id);
    case "CLEAR_COMPLETED": return state.filter((t) => !t.done);
    default: return state;
  }
};
function TodoProvider({ children }) {
  const [todos, dispatch] = useReducer(reducer, []);
  return <TodoContext.Provider value={{ todos, dispatch }}>{children}</TodoContext.Provider>;
}
function TodoApp() {
  const { todos, dispatch } = useContext(TodoContext);
  return (
    <TodoProvider>
      <div>
        <button onClick={() => dispatch({ type: "ADD", text: "New todo" })}>Add</button>
        <ul>{todos.map((t) => <li key={t.id} onClick={() => dispatch({ type: "TOGGLE", id: t.id })}>{t.done ? "✓" : ""} {t.text}</li>)}</ul>
        <p>Total: {todos.length}, Done: {todos.filter((t) => t.done).length}</p>
      </div>
    </TodoProvider>
  );
}
export default TodoApp;
