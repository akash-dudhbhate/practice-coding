// Lesson 04 — Easy P02: Login/Logout Button
import { useState } from "react";
function LoginLogout() {
  const [loggedIn, setLoggedIn] = useState(false);
  return <button onClick={() => setLoggedIn(!loggedIn)}>{loggedIn ? "Logout" : "Login"}</button>;
}
export default LoginLogout;
