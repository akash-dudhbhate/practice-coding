// Lesson 03 — Easy P02: Text Echo
import { useState } from "react";
function TextEcho() {
  const [text, setText] = useState("");
  return (
    <div>
      <input type="text" onChange={(e) => setText(e.target.value)} placeholder="Type here" />
      <p>{text}</p>
    </div>
  );
}
export default TextEcho;
