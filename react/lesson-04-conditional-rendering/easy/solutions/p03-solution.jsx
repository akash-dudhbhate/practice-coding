// Lesson 04 — Easy P03: Even/Odd Display
import { useState } from "react";
function EvenOdd() {
  const [num, setNum] = useState(0);
  return (
    <div>
      <input type="number" value={num} onChange={(e) => setNum(Number(e.target.value))} />
      <p>{num % 2 === 0 ? "Even" : "Odd"}</p>
    </div>
  );
}
export default EvenOdd;
