// Lesson 11 — Medium P01: ThemeProvider with toggle
import { createContext, useContext, useState } from "react";
const ThemeContext = createContext();
function useTheme() { return useContext(ThemeContext); }
function Header() { const { theme } = useTheme(); return <header style={{ background: theme === "dark" ? "#222" : "#eee" }}>Header ({theme})</header>; }
function Sidebar() { const { theme } = useTheme(); return <aside style={{ background: theme === "dark" ? "#333" : "#f0f0f0" }}>Sidebar</aside>; }
function Main() { const { theme } = useTheme(); return <main style={{ background: theme === "dark" ? "#1a1a1a" : "#fff", color: theme === "dark" ? "#fff" : "#333" }}>Content</main>; }
function ThemeProvider({ children }) {
  const [theme, setTheme] = useState("light");
  const toggleTheme = () => setTheme(theme === "dark" ? "light" : "dark");
  return <ThemeContext.Provider value={{ theme, toggleTheme }}>{children}</ThemeContext.Provider>;
}
function App() {
  const { toggleTheme } = useTheme();
  return (
    <ThemeProvider>
      <button onClick={toggleTheme}>Toggle</button>
      <Header /><Sidebar /><Main />
    </ThemeProvider>
  );
}
export default App;
