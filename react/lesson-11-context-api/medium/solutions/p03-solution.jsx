// Lesson 11 — Medium P03: useTheme hook with error checking
import { createContext, useContext } from "react";
const ThemeContext = createContext(null);
function useTheme() {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error("useTheme must be used within ThemeProvider");
  return ctx;
}
function ThemedComponent() {
  const { theme } = useTheme();
  return <p>Theme: {theme}</p>;
}
function ThemeProvider({ children }) {
  return <ThemeContext.Provider value={{ theme: "dark" }}>{children}</ThemeContext.Provider>;
}
function App() {
  return <ThemeProvider><ThemedComponent /></ThemeProvider>;
}
export default App;
