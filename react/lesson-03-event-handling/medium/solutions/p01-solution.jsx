// Lesson 03 — Medium P01: Login Form
import { useState } from "react";
function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [creds, setCreds] = useState(null);
  const handleSubmit = (e) => { e.preventDefault(); setCreds({ email, password }); };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" />
        <button type="submit">Login</button>
      </form>
      {creds && <p>Email: {creds.email}, Password: {creds.password}</p>}
    </div>
  );
}
export default LoginForm;
