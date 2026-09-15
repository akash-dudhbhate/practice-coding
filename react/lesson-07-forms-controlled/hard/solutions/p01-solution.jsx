// Lesson 07 — Hard P01: Registration Form with Validation
import { useState } from "react";
function RegistrationForm() {
  const [form, setForm] = useState({ name: "", email: "", password: "", confirm: "" });
  const [errors, setErrors] = useState({});
  const handleChange = (e) => { setForm({ ...form, [e.target.name]: e.target.value }); setErrors({ ...errors, [e.target.name]: "" }); };
  const validate = () => {
    const errs = {};
    if (!form.name) errs.name = "Required";
    if (!form.email.includes("@")) errs.email = "Invalid email";
    if (form.password.length < 8) errs.password = "Min 8 characters";
    if (form.password !== form.confirm) errs.confirm = "Passwords don't match";
    return errs;
  };
  const handleSubmit = (e) => { e.preventDefault(); const errs = validate(); setErrors(errs); if (Object.keys(errs).length === 0) alert("Registered!"); };
  return (
    <form onSubmit={handleSubmit}>
      <input name="name" value={form.name} onChange={handleChange} placeholder="Name" />
      {errors.name && <span style={{ color: "red" }}> {errors.name}</span>}<br />
      <input name="email" value={form.email} onChange={handleChange} placeholder="Email" />
      {errors.email && <span style={{ color: "red" }}> {errors.email}</span>}<br />
      <input name="password" type="password" value={form.password} onChange={handleChange} placeholder="Password" />
      {errors.password && <span style={{ color: "red" }}> {errors.password}</span>}<br />
      <input name="confirm" type="password" value={form.confirm} onChange={handleChange} placeholder="Confirm Password" />
      {errors.confirm && <span style={{ color: "red" }}> {errors.confirm}</span>}<br />
      <button type="submit">Register</button>
    </form>
  );
}
export default RegistrationForm;
