// Lesson 20 — Medium P01: 100 memo items with useCallback delete
import { useState, memo, useCallback } from "react";
const ListItem = memo(({ item, onDelete }) => { console.log(`Item ${item.id} rendered`); return <li>{item.text} <button onClick={() => onDelete(item.id)}>Delete</button></li>; });
function LargeList() {
  const [items, setItems] = useState(() => Array.from({ length: 100 }, (_, i) => ({ id: i, text: `Item ${i}` })));
  const handleDelete = useCallback((id) => setItems((prev) => prev.filter((i) => i.id !== id)), []);
  return <ul>{items.map((item) => <ListItem key={item.id} item={item} onDelete={handleDelete} />)}</ul>;
}
export default LargeList;
