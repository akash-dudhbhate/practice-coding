// Lesson 17 — Easy P02: Theme store
import { create } from "zustand";
const useThemeStore = create((set) => ({
  theme: "light",
  toggleTheme: () => set((s) => ({ theme: s.theme === "dark" ? "light" : "dark" })),
}));
function Header() { const theme = useThemeStore((s) => s.theme); return <header style={{ background: theme === "dark" ? "#222" : "#eee" }}>Header ({theme})</header>; }
function Main() { const theme = useThemeStore((s) => s.theme); return <main style={{ background: theme === "dark" ? "#1a1a1a" : "#fff", color: theme === "dark" ? "#fff" : "#333" }}>Content</main>; }
function Footer() { const theme = useThemeStore((s) => s.theme); return <footer style={{ background: theme === "dark" ? "#222" : "#eee" }}>Footer</footer>; }
function App() {
  const toggleTheme = useThemeStore((s) => s.toggleTheme);
  return <div><button onClick={toggleTheme}>Toggle</button><Header /><Main /><Footer /></div>;
}
export default App;
