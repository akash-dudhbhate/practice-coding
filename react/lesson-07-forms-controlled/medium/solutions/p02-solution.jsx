// Lesson 07 — Medium P02: Radio Button Group
import { useState } from "react";
function SizeSelector() {
  const [size, setSize] = useState("medium");
  return (
    <div>
      {["small", "medium", "large"].map((s) => (
        <label key={s}>
          <input type="radio" name="size" value={s} checked={size === s} onChange={(e) => setSize(e.target.value)} />
          {s.charAt(0).toUpperCase() + s.slice(1)}
        </label>
      ))}
      <p>Selected size: {size}</p>
    </div>
  );
}
export default SizeSelector;
