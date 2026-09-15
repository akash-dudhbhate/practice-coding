// Lesson 11 — Easy P02: UserContext (no prop drilling)
import { createContext, useContext } from "react";
const UserContext = createContext(null);
function DeepChild() {
  const user = useContext(UserContext);
  return <p>Welcome, {user.name}! Role: {user.role}</p>;
}
function Middle() { return <DeepChild />; }
function Top() { return <Middle />; }
function App() {
  return (
    <UserContext.Provider value={{ name: "Alice", role: "admin" }}>
      <Top />
    </UserContext.Provider>
  );
}
export default App;
