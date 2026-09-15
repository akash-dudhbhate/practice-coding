// Lesson 17 — Hard P01: Multi-slice store
import { create } from "zustand";
const createAuthSlice = (set) => ({
  user: null,
  login: (user) => set({ user }),
  logout: () => set({ user: null }),
});
const createCartSlice = (set) => ({
  cart: [],
  addToCart: (item) => set((s) => ({ cart: [...s.cart, item] })),
  clearCart: () => set({ cart: [] }),
});
const createThemeSlice = (set) => ({
  theme: "light",
  toggleTheme: () => set((s) => ({ theme: s.theme === "dark" ? "light" : "dark" })),
});
const useStore = create((...a) => ({
  ...createAuthSlice(...a),
  ...createCartSlice(...a),
  ...createThemeSlice(...a),
}));
function AuthComponent() {
  const { user, login, logout } = useStore((s) => ({ user: s.user, login: s.login, logout: s.logout }));
  return <div>{user ? <p>{user} <button onClick={logout}>Logout</button></p> : <button onClick={() => login("Alice")}>Login</button>}</div>;
}
function CartComponent() {
  const { cart, addToCart } = useStore((s) => ({ cart: s.cart, addToCart: s.addToCart }));
  return <div><button onClick={() => addToCart("Item")}>Add to Cart</button><p>Cart: {cart.length}</p></div>;
}
function ThemeComponent() {
  const { theme, toggleTheme } = useStore((s) => ({ theme: s.theme, toggleTheme: s.toggleTheme }));
  return <button onClick={toggleTheme}>Theme: {theme}</button>;
}
function App() { return <div><AuthComponent /><CartComponent /><ThemeComponent /></div>; }
export default App;
