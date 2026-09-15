// Lesson 10 — Medium P03: useDebounce
import { useState, useEffect } from "react";
function useDebounce(value, delay = 500) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer);
  }, [value, delay]);
  return debounced;
}
function DebounceSearch() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const debouncedQuery = useDebounce(query, 500);
  useEffect(() => {
    if (!debouncedQuery) { setResults([]); return; }
    fetch(`https://jsonplaceholder.typicode.com/users?name_like=${debouncedQuery}`)
      .then((res) => res.json())
      .then(setResults);
  }, [debouncedQuery]);
  return (
    <div>
      <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search (debounced)..." />
      <ul>{results.map((r) => <li key={r.id}>{r.name}</li>)}</ul>
    </div>
  );
}
export default DebounceSearch;
