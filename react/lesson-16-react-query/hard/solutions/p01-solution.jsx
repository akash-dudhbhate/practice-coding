// Lesson 16 — Hard P01: Debounced search with useQuery
import { useState, useEffect } from "react";
import { useQuery } from "@tanstack/react-query";
function useDebounce(value, delay = 500) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => { const t = setTimeout(() => setDebounced(value), delay); return () => clearTimeout(t); }, [value, delay]);
  return debounced;
}
function SearchUsers() {
  const [query, setQuery] = useState("");
  const debouncedQuery = useDebounce(query);
  const { data, isLoading, isFetching } = useQuery({
    queryKey: ["search", debouncedQuery],
    queryFn: () => fetch(`https://jsonplaceholder.typicode.com/users?name_like=${debouncedQuery}`).then((r) => r.json()),
    enabled: !!debouncedQuery,
  });
  return (
    <div>
      <input value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Search users..." />
      {isFetching && <p>Searching...</p>}
      {!debouncedQuery && <p>Type to search</p>}
      {data && data.length === 0 && <p>No results</p>}
      {data && data.length > 0 && <ul>{data.map((u) => <li key={u.id}>{u.name}</li>)}</ul>}
    </div>
  );
}
export default SearchUsers;
