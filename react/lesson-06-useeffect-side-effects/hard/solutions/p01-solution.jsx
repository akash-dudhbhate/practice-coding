// Lesson 06 — Hard P01: Live Search with Debounce
import { useState, useEffect } from "react";
function LiveSearch() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  useEffect(() => {
    if (!query) { setResults([]); return; }
    const timer = setTimeout(() => {
      fetch(`https://jsonplaceholder.typicode.com/users?name_like=${query}`)
        .then((res) => res.json())
        .then(setResults);
    }, 500);
    return () => clearTimeout(timer);
  }, [query]);
  return (
    <div>
      <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search users..." />
      <ul>{results.map((r) => <li key={r.id}>{r.name}</li>)}</ul>
    </div>
  );
}
export default LiveSearch;
