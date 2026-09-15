// Lesson 20 — Medium P02: useDeferredValue for search
import { useState, useDeferredValue, useMemo } from "react";
function DeferredSearch() {
  const [query, setQuery] = useState("");
  const deferredQuery = useDeferredValue(query);
  const items = useMemo(() => Array.from({ length: 10000 }, (_, i) => `Item ${i}`), []);
  const filtered = useMemo(() => items.filter((i) => i.includes(deferredQuery)), [items, deferredQuery]);
  const isStale = query !== deferredQuery;
  return (
    <div>
      <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search 10,000 items..." />
      {isStale && <p style={{ color: "blue" }}>Filtering...</p>}
      <p>Showing {filtered.length} results (first 20):</p>
      <ul>{filtered.slice(0, 20).map((i, idx) => <li key={idx}>{i}</li>)}</ul>
    </div>
  );
}
export default DeferredSearch;
