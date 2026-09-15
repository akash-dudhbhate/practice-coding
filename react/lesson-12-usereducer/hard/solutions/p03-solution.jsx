// Lesson 12 — Hard P03: Combined app state with useReducer + Context
import { useReducer, createContext, useContext } from "react";
const initialState = { auth: { user: null }, theme: "light", notifications: [] };
const reducer = (state, action) => {
  switch (action.type) {
    case "LOGIN": return { ...state, auth: { user: action.user } };
    case "LOGOUT": return { ...state, auth: { user: null } };
    case "TOGGLE_THEME": return { ...state, theme: state.theme === "dark" ? "light" : "dark" };
    case "ADD_NOTIFICATION": return { ...state, notifications: [...state.notifications, action.notification] };
    case "REMOVE_NOTIFICATION": return { ...state, notifications: state.notifications.filter((n) => n.id !== action.id) };
    default: return state;
  }
};
const AppContext = createContext(null);
function AppProvider({ children }) {
  const [state, dispatch] = useReducer(reducer, initialState);
  return <AppContext.Provider value={{ state, dispatch }}>{children}</AppContext.Provider>;
}
function Header() {
  const { state, dispatch } = useContext(AppContext);
  return (
    <header style={{ background: state.theme === "dark" ? "#222" : "#eee" }}>
      {state.auth.user ? `Hello, ${state.auth.user}` : "Guest"}
      <button onClick={() => dispatch({ type: "TOGGLE_THEME" })}>Theme</button>
      {state.auth.user ? <button onClick={() => dispatch({ type: "LOGOUT" })}>Logout</button> : <button onClick={() => dispatch({ type: "LOGIN", user: "Alice" })}>Login</button>}
    </header>
  );
}
function Notifications() {
  const { state, dispatch } = useContext(AppContext);
  return <div>{state.notifications.map((n) => <p key={n.id} onClick={() => dispatch({ type: "REMOVE_NOTIFICATION", id: n.id })}>{n.text}</p>)}</div>;
}
function App() {
  return <AppProvider><Header /><Notifications /></AppProvider>;
}
export default App;
