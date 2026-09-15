// Lesson 12 — Easy P02: Toggle with useReducer
import { useReducer } from "react";
const reducer = (state, action) => {
  switch (action) {
    case "toggle": return !state;
    case "on": return true;
    case "off": return false;
    default: return state;
  }
};
function Toggle() {
  const [isOn, dispatch] = useReducer(reducer, false);
  return (
    <div>
      <p>{isOn ? "ON" : "OFF"}</p>
      <button onClick={() => dispatch("toggle")}>Toggle</button>
      <button onClick={() => dispatch("on")}>On</button>
      <button onClick={() => dispatch("off")}>Off</button>
    </div>
  );
}
export default Toggle;
