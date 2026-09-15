// Lesson 10 — Medium P02: useLocalStorage
import { useState, useEffect } from "react";
function useLocalStorage(key, initial) {
  const [value, setValue] = useState(() => {
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initial;
  });
  useEffect(() => { localStorage.setItem(key, JSON.stringify(value)); }, [key, value]);
  return [value, setValue];
}
function LocalStorageDemo() {
  const [theme, setTheme] = useLocalStorage("theme", "light");
  const [name, setName] = useLocalStorage("name", "");
  return (
    <div style={{ background: theme === "dark" ? "#222" : "#fff", color: theme === "dark" ? "#fff" : "#333", padding: 20 }}>
      <button onClick={() => setTheme(theme === "dark" ? "light" : "dark")}>Toggle Theme</button>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Name (persisted)" />
      <p>Hello, {name}!</p>
    </div>
  );
}
export default LocalStorageDemo;
