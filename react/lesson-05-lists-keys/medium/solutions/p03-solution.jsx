// Lesson 05 — Medium P03: Sortable List
import { useState } from "react";
const names = ["Charlie", "Alice", "Bob", "Diana"];
function SortableList() {
  const [ascending, setAscending] = useState(true);
  const sorted = [...names].sort((a, b) => ascending ? a.localeCompare(b) : b.localeCompare(a));
  return (
    <div>
      <button onClick={() => setAscending(!ascending)}>Sort: {ascending ? "↑" : "↓"}</button>
      <ul>{sorted.map((name, i) => <li key={i}>{name}</li>)}</ul>
    </div>
  );
}
export default SortableList;
