// Lesson 12 — Easy P01: Counter with useReducer
import { useReducer } from "react";
const reducer = (state, action) => {
  switch (action) {
    case "increment": return state + 1;
    case "decrement": return state - 1;
    case "reset": return 0;
    default: return state;
  }
};
function Counter() {
  const [count, dispatch] = useReducer(reducer, 0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => dispatch("increment")}>+1</button>
      <button onClick={() => dispatch("decrement")}>-1</button>
      <button onClick={() => dispatch("reset")}>Reset</button>
    </div>
  );
}
export default Counter;
