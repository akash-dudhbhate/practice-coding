// Lesson 12 — Easy P03: Text input with useReducer
import { useReducer } from "react";
const reducer = (state, action) => {
  if (action.type === "SET_TEXT") return action.payload;
  return state;
};
function TextInput() {
  const [text, dispatch] = useReducer(reducer, "");
  return (
    <div>
      <input value={text} onChange={(e) => dispatch({ type: "SET_TEXT", payload: e.target.value })} placeholder="Type here" />
      <p>Text: {text}</p>
      <p>Characters: {text.length}</p>
    </div>
  );
}
export default TextInput;
