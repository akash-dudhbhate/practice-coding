// Lesson 02 — Easy P03: Text Input Display
import { useState } from "react";
function TextInput() {
  const [text, setText] = useState("");
  return (
    <div>
      <input type="text" value={text} onChange={(e) => setText(e.target.value)} placeholder="Type here" />
      <p>{text}</p>
    </div>
  );
}
export default TextInput;
