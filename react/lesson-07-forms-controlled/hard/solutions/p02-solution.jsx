// Lesson 07 — Hard P02: Controlled Form with Reset
import { useState } from "react";
function ContactForm() {
  const initial = { name: "", email: "", message: "" };
  const [form, setForm] = useState(initial);
  const [success, setSuccess] = useState(false);
  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });
  const handleSubmit = (e) => {
    e.preventDefault();
    setSuccess(true);
    setForm(initial);
    setTimeout(() => setSuccess(false), 3000);
  };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input name="name" value={form.name} onChange={handleChange} placeholder="Name" /><br />
        <input name="email" value={form.email} onChange={handleChange} placeholder="Email" /><br />
        <textarea name="message" value={form.message} onChange={handleChange} placeholder="Message" /><br />
        <button type="submit">Send</button>
      </form>
      {success && <p style={{ color: "green" }}>Message sent successfully!</p>}
    </div>
  );
}
export default ContactForm;
