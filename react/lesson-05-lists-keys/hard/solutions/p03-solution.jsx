// Lesson 05 — Hard P03: Reorderable List (stable IDs)
import { useState } from "react";
function ReorderableList() {
  const [items, setItems] = useState([
    { id: 1, text: "First" }, { id: 2, text: "Second" }, { id: 3, text: "Third" },
  ]);
  const move = (index, dir) => {
    const newItems = [...items];
    const target = index + dir;
    if (target < 0 || target >= newItems.length) return;
    [newItems[index], newItems[target]] = [newItems[target], newItems[index]];
    setItems(newItems);
  };
  return (
    <ul>
      {items.map((item, i) => (
        <li key={item.id}>
          {item.text}
          <button onClick={() => move(i, -1)}>↑</button>
          <button onClick={() => move(i, 1)}>↓</button>
        </li>
      ))}
    </ul>
  );
}
export default ReorderableList;
