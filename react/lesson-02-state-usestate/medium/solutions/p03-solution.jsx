// Lesson 02 — Medium P03: Form with Multiple Fields
import { useState } from "react";
function Form() {
  const [form, setForm] = useState({ name: "", email: "" });
  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });
  return (
    <div>
      <input name="name" value={form.name} onChange={handleChange} placeholder="Name" />
      <input name="email" value={form.email} onChange={handleChange} placeholder="Email" />
      <p>Name: {form.name}</p>
      <p>Email: {form.email}</p>
    </div>
  );
}
export default Form;
