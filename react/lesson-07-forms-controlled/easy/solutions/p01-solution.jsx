// Lesson 07 — Easy P01: Name Input
import { useState } from "react";
function NameInput() {
  const [name, setName] = useState("");
  return (
    <div>
      <input type="text" value={name} onChange={(e) => setName(e.target.value)} placeholder="Enter name" />
      <p>Hello, {name}!</p>
    </div>
  );
}
export default NameInput;
