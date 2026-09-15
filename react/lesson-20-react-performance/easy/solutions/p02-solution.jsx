// Lesson 20 — Easy P02: useMemo for expensive sort
import { useState, useMemo } from "react";
function SortedList() {
  const [nums] = useState(() => Array.from({ length: 1000 }, () => Math.floor(Math.random() * 10000)));
  const [text, setText] = useState("");
  const sorted = useMemo(() => [...nums].sort((a, b) => a - b), [nums]);
  return (
    <div>
      <p>First 5: {sorted.slice(0, 5).join(", ")}</p>
      <input value={text} onChange={(e) => setText(e.target.value)} placeholder="Typing here won't re-sort" />
    </div>
  );
}
export default SortedList;
