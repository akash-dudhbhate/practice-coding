// Lesson 07 — Medium P03: Form with Validation
import { useState } from "react";
function SignupForm() {
  const [form, setForm] = useState({ email: "", password: "" });
  const [errors, setErrors] = useState({});
  const handleChange = (e) => { setForm({ ...form, [e.target.name]: e.target.value }); setErrors({ ...errors, [e.target.name]: "" }); };
  const handleSubmit = (e) => {
    e.preventDefault();
    const errs = {};
    if (!form.email.includes("@")) errs.email = "Email must contain @";
    if (form.password.length < 8) errs.password = "Password must be 8+ characters";
    setErrors(errs);
    if (Object.keys(errs).length === 0) alert("Signup successful!");
  };
  return (
    <form onSubmit={handleSubmit}>
      <input name="email" value={form.email} onChange={handleChange} placeholder="Email" />
      {errors.email && <span style={{ color: "red" }}>{errors.email}</span>}<br />
      <input name="password" type="password" value={form.password} onChange={handleChange} placeholder="Password" />
      {errors.password && <span style={{ color: "red" }}>{errors.password}</span>}<br />
      <button type="submit">Sign Up</button>
    </form>
  );
}
export default SignupForm;
