// Lesson 17 — Medium P03: Persist middleware
import { create } from "zustand";
import { persist } from "zustand/middleware";
const usePrefsStore = create(persist(
  (set) => ({
    theme: "light",
    username: "",
    setTheme: (theme) => set({ theme }),
    setUsername: (username) => set({ username }),
  }),
  { name: "user-prefs", partialize: (state) => ({ theme: state.theme, username: state.username }) }
));
function App() {
  const { theme, username, setTheme, setUsername } = usePrefsStore();
  return (
    <div style={{ background: theme === "dark" ? "#222" : "#fff", color: theme === "dark" ? "#fff" : "#333", padding: 20 }}>
      <h3>Persisted Preferences</h3>
      <button onClick={() => setTheme(theme === "dark" ? "light" : "dark")}>Theme: {theme}</button>
      <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username (persisted)" />
      <p>Hello, {username}!</p>
    </div>
  );
}
export default App;
