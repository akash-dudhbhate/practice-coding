// Lesson 09 — Hard P01: DataTable with useMemo
import { useState, useMemo } from "react";
function DataTable() {
  const [rows] = useState(() => Array.from({ length: 1000 }, (_, i) => ({ id: i, name: `User ${i}`, age: 20 + (i % 50) })));
  const [search, setSearch] = useState("");
  const [sortKey, setSortKey] = useState("id");
  const [renderCount, setRenderCount] = useState(0);
  const processed = useMemo(() => {
    let result = rows.filter((r) => r.name.toLowerCase().includes(search.toLowerCase()));
    result = [...result].sort((a, b) => a[sortKey] - b[sortKey]);
    return result.slice(0, 20);
  }, [rows, search, sortKey]);
  return (
    <div>
      <p>Renders: {renderCount} <button onClick={() => setRenderCount(renderCount + 1)}>Re-render</button></p>
      <input value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Search..." />
      <button onClick={() => setSortKey("id")}>Sort by ID</button>
      <button onClick={() => setSortKey("age")}>Sort by Age</button>
      <table><tbody>{processed.map((r) => <tr key={r.id}><td>{r.id}</td><td>{r.name}</td><td>{r.age}</td></tr>)}</tbody></table>
    </div>
  );
}
export default DataTable;
