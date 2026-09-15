// Lesson 09 — Easy P03: useMemo for sorting
import { useState, useMemo } from "react";
function SortDemo() {
  const [nums, setNums] = useState(() => Array.from({ length: 1000 }, () => Math.floor(Math.random() * 10000)));
  const [text, setText] = useState("");
  const sorted = useMemo(() => [...nums].sort((a, b) => a - b), [nums]);
  return (
    <div>
      <p>First 5 sorted: {sorted.slice(0, 5).join(", ")}</p>
      <button onClick={() => setNums(Array.from({ length: 1000 }, () => Math.floor(Math.random() * 10000)))}>Regenerate</button>
      <input value={text} onChange={(e) => setText(e.target.value)} placeholder="Typing here won't re-sort" />
    </div>
  );
}
export default SortDemo;
