// Lesson 11 — Easy P01: ThemeContext
import { createContext, useContext } from "react";
const ThemeContext = createContext("light");
function ThemedComponent() {
  const theme = useContext(ThemeContext);
  return <div className={theme}>Current theme: {theme}</div>;
}
function App() {
  return (
    <ThemeContext.Provider value="dark">
      <ThemedComponent />
    </ThemeContext.Provider>
  );
}
export default App;
