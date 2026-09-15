// Lesson 20 — Hard P01: Virtualized list with react-window
import { useState, useMemo } from "react";
import { FixedSizeList as List } from "react-window";
function VirtualizedList() {
  const [search, setSearch] = useState("");
  const items = useMemo(() => Array.from({ length: 10000 }, (_, i) => `Item ${i}`), []);
  const filtered = useMemo(() => items.filter((i) => i.includes(search)), [items, search]);
  const Row = ({ index, style }) => <div style={style} className="border-b px-4 py-2">{filtered[index]}</div>;
  return (
    <div>
      <input value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Search 10,000 items..." />
      <p>Showing {filtered.length} items (virtualized)</p>
      <List height={400} itemCount={filtered.length} itemSize={35} width="100%">{Row}</List>
    </div>
  );
}
export default VirtualizedList;
