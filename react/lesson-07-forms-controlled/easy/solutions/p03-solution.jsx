// Lesson 07 — Easy P03: Select Dropdown
import { useState } from "react";
function ColorSelect() {
  const [color, setColor] = useState("blue");
  return (
    <div>
      <select value={color} onChange={(e) => setColor(e.target.value)}>
        <option value="red">Red</option>
        <option value="green">Green</option>
        <option value="blue">Blue</option>
      </select>
      <p>Selected: {color}</p>
    </div>
  );
}
export default ColorSelect;
