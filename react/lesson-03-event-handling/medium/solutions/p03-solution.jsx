// Lesson 03 — Medium P03: Search with Enter Key
import { useState } from "react";
function SearchEnter() {
  const [query, setQuery] = useState("");
  const [searched, setSearched] = useState("");
  const handleKeyDown = (e) => {
    if (e.key === "Enter") { setSearched(query); setQuery(""); }
    if (e.key === "Escape") { setQuery(""); setSearched(""); }
  };
  return (
    <div>
      <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} onKeyDown={handleKeyDown} placeholder="Search..." />
      <p>Search result: {searched}</p>
    </div>
  );
}
export default SearchEnter;
