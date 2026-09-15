// Lesson 07 — Medium P01: Multi-Field Form
import { useState } from "react";
function MultiFieldForm() {
  const [form, setForm] = useState({ name: "", email: "", message: "" });
  const [submitted, setSubmitted] = useState(null);
  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });
  const handleSubmit = (e) => { e.preventDefault(); setSubmitted(form); };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input name="name" value={form.name} onChange={handleChange} placeholder="Name" /><br />
        <input name="email" value={form.email} onChange={handleChange} placeholder="Email" /><br />
        <textarea name="message" value={form.message} onChange={handleChange} placeholder="Message" /><br />
        <button type="submit">Submit</button>
      </form>
      {submitted && <pre>{JSON.stringify(submitted, null, 2)}</pre>}
    </div>
  );
}
export default MultiFieldForm;
