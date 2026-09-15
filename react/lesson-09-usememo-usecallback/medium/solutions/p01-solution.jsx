// Lesson 09 — Medium P01: SearchFilter with useMemo
import { useState, useMemo } from "react";
function SearchFilter() {
  const items = useMemo(() => Array.from({ length: 100 }, (_, i) => `Item ${i + 1}` }), []);
  const [query, setQuery] = useState("");
  const [unrelated, setUnrelated] = useState(0);
  const filtered = useMemo(() => items.filter((i) => i.toLowerCase().includes(query.toLowerCase())), [items, query]);
  return (
    <div>
      <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search..." />
      <button onClick={() => setUnrelated(unrelated + 1)}>Unrelated: {unrelated}</button>
      <ul>{filtered.map((item, i) => <li key={i}>{item}</li>)}</ul>
    </div>
  );
}
export default SearchFilter;
