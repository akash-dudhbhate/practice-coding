// Lesson 10 — Hard P03: Composed hooks - useUserDashboard
import { useState, useEffect } from "react";

function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    if (!url) return;
    setLoading(true);
    fetch(url).then((r) => r.json()).then((d) => { setData(d); setLoading(false); });
  }, [url]);
  return { data, loading };
}

function useDebounce(value, delay = 500) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(t);
  }, [value, delay]);
  return debounced;
}

function useLocalStorage(key, initial) {
  const [value, setValue] = useState(() => localStorage.getItem(key) || initial);
  useEffect(() => { localStorage.setItem(key, value); }, [key, value]);
  return [value, setValue];
}

function useUserDashboard(userId) {
  const { data: user, loading } = useFetch(`https://jsonplaceholder.typicode.com/users/${userId}`);
  const [search, setSearch] = useState("");
  const debouncedSearch = useDebounce(search);
  const { data: searchResults } = useFetch(
    debouncedSearch ? `https://jsonplaceholder.typicode.com/users?name_like=${debouncedSearch}` : null
  );
  const [theme, setTheme] = useLocalStorage("dashboard-theme", "light");
  return { user, loading, search, setSearch, searchResults, theme, setTheme };
}

function Dashboard({ userId = 1 }) {
  const { user, loading, search, setSearch, searchResults, theme, setTheme } = useUserDashboard(userId);
  if (loading) return <p>Loading...</p>;
  return (
    <div style={{ background: theme === "dark" ? "#222" : "#fff", color: theme === "dark" ? "#fff" : "#333", padding: 20 }}>
      <h3>{user.name}</h3>
      <p>{user.email}</p>
      <button onClick={() => setTheme(theme === "dark" ? "light" : "dark")}>Toggle Theme ({theme})</button>
      <input value={search} onChange={(e) => setSearch(e.target.value)} placeholder="Search users..." />
      {searchResults && <ul>{searchResults.map((r) => <li key={r.id}>{r.name}</li>)}</ul>}
    </div>
  );
}
export default Dashboard;
