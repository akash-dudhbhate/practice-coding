// Lesson 08 — Easy P02: Focus input on button click
import { useRef } from "react";
function FocusOnButton() {
  const inputRef = useRef(null);
  return (
    <div>
      <input ref={inputRef} type="text" placeholder="Click button to focus" />
      <button onClick={() => inputRef.current.focus()}>Focus Input</button>
    </div>
  );
}
export default FocusOnButton;
