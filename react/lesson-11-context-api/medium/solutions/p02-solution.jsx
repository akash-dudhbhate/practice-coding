// Lesson 11 — Medium P02: Two separate contexts
import { createContext, useContext, useState } from "react";
const UserContext = createContext();
const ThemeContext = createContext();
function Component() {
  const user = useContext(UserContext);
  const theme = useContext(ThemeContext);
  return <div style={{ background: theme === "dark" ? "#222" : "#fff", color: theme === "dark" ? "#fff" : "#333" }}>{user.name} - {theme}</div>;
}
function App() {
  const [theme, setTheme] = useState("light");
  return (
    <UserContext.Provider value={{ name: "Alice" }}>
      <ThemeContext.Provider value={theme}>
        <Component />
        <button onClick={() => setTheme(theme === "dark" ? "light" : "dark")}>Toggle Theme</button>
      </ThemeContext.Provider>
    </UserContext.Provider>
  );
}
export default App;
