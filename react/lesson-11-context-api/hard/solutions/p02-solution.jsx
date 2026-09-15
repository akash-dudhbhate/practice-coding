// Lesson 11 — Hard P02: Auth System with Context
import { createContext, useContext, useState } from "react";
const AuthContext = createContext(null);
function useAuth() { const ctx = useContext(AuthContext); if (!ctx) throw new Error("useAuth must be used within AuthProvider"); return ctx; }
function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const login = (email) => setUser({ email, name: email.split("@")[0] });
  const logout = () => setUser(null);
  const register = (name, email) => setUser({ name, email });
  return <AuthContext.Provider value={{ user, login, logout, register }}>{children}</AuthContext.Provider>;
}
function LoginForm() {
  const { login } = useAuth();
  const [email, setEmail] = useState("");
  return <form onSubmit={(e) => { e.preventDefault(); login(email); }}><input value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" /><button type="submit">Login</button></form>;
}
function Dashboard() {
  const { user, logout } = useAuth();
  if (!user) return <LoginForm />;
  return <div><p>Welcome, {user.name}</p><button onClick={logout}>Logout</button></div>;
}
function App() { return <AuthProvider><Dashboard /></AuthProvider>; }
export default App;
