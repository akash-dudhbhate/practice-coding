// Lesson 09 — Easy P01: useMemo sum
import { useState, useMemo } from "react";
function SumDemo() {
  const [nums] = useState([1, 2, 3, 4, 5]);
  const [text, setText] = useState("");
  const sum = useMemo(() => nums.reduce((a, b) => a + b, 0), [nums]);
  return (
    <div>
      <p>Sum: {sum}</p>
      <input value={text} onChange={(e) => setText(e.target.value)} placeholder="Typing here won't recompute sum" />
    </div>
  );
}
export default SumDemo;
