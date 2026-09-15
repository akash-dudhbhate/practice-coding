// Lesson 20 — Hard P02: useTransition for non-urgent filtering
import { useState, useTransition, useMemo } from "react";
function TransitionSearch() {
  const [query, setQuery] = useState("");
  const [isPending, startTransition] = useTransition();
  const [filtered, setFiltered] = useState([]);
  const items = useMemo(() => Array.from({ length: 10000 }, (_, i) => `Item ${i}`), []);
  const handleChange = (e) => {
    const value = e.target.value;
    setQuery(value); // urgent: update input immediately
    startTransition(() => { // non-urgent: filter in background
      setFiltered(items.filter((i) => i.includes(value)));
    });
  };
  return (
    <div>
      <input value={query} onChange={handleChange} placeholder="Search..." />
      {isPending && <p style={{ color: "blue" }}>Filtering...</p>}
      <p>Results: {filtered.length} (showing first 20)</p>
      <ul>{filtered.slice(0, 20).map((i, idx) => <li key={idx}>{i}</li>)}</ul>
    </div>
  );
}
export default TransitionSearch;
