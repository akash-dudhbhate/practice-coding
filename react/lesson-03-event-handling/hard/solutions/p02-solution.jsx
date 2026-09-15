// Lesson 03 — Hard P02: Multi-Input Form with Validation
import { useState } from "react";
function RegistrationForm() {
  const [form, setForm] = useState({ name: "", email: "", password: "" });
  const [errors, setErrors] = useState({});
  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });
  const handleSubmit = (e) => {
    e.preventDefault();
    const errs = {};
    if (!form.name) errs.name = "Name is required";
    if (!form.email) errs.email = "Email is required";
    else if (!form.email.includes("@")) errs.email = "Email must contain @";
    if (!form.password) errs.password = "Password is required";
    setErrors(errs);
    if (Object.keys(errs).length === 0) alert("Registration successful!");
  };
  return (
    <form onSubmit={handleSubmit}>
      <input name="name" value={form.name} onChange={handleChange} placeholder="Name" />
      {errors.name && <span style={{ color: "red" }}>{errors.name}</span>}<br />
      <input name="email" value={form.email} onChange={handleChange} placeholder="Email" />
      {errors.email && <span style={{ color: "red" }}>{errors.email}</span>}<br />
      <input name="password" type="password" value={form.password} onChange={handleChange} placeholder="Password" />
      {errors.password && <span style={{ color: "red" }}>{errors.password}</span>}<br />
      <button type="submit">Register</button>
    </form>
  );
}
export default RegistrationForm;
