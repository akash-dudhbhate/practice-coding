// Lesson 17 — Medium P01: Auth store with async login
import { create } from "zustand";
import { useState } from "react";
const useAuthStore = create((set) => ({
  user: null,
  loading: false,
  error: null,
  login: async (username, password) => {
    set({ loading: true, error: null });
    try {
      await new Promise((r) => setTimeout(r, 500));
      if (password.length < 4) throw new Error("Password too short");
      set({ user: { name: username }, loading: false });
    } catch (err) {
      set({ error: err.message, loading: false });
    }
  },
  logout: () => set({ user: null, error: null }),
}));
function LoginForm() {
  const { login, loading, error } = useAuthStore();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  return (
    <form onSubmit={(e) => { e.preventDefault(); login(username, password); }}>
      <input value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" />
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
      {error && <p style={{ color: "red" }}>{error}</p>}
      <button type="submit" disabled={loading}>{loading ? "Logging in..." : "Login"}</button>
    </form>
  );
}
function Dashboard() {
  const { user, logout } = useAuthStore();
  return <div><p>Welcome, {user.name}</p><button onClick={logout}>Logout</button></div>;
}
function App() {
  const user = useAuthStore((s) => s.user);
  return user ? <Dashboard /> : <LoginForm />;
}
export default App;
