// Lesson 05 — Medium P02: Searchable List
import { useState } from "react";
const items = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"];
function SearchableList() {
  const [query, setQuery] = useState("");
  const filtered = items.filter((i) => i.toLowerCase().includes(query.toLowerCase()));
  return (
    <div>
      <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search..." />
      {filtered.length === 0 ? <p>No results</p> : <ul>{filtered.map((item, i) => <li key={i}>{item}</li>)}</ul>}
    </div>
  );
}
export default SearchableList;
