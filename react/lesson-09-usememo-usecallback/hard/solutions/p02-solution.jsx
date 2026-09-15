// Lesson 09 — Hard P02: Form with memo fields
import { useState, memo, useCallback } from "react";
const Field = memo(({ label, value, onChange }) => { console.log(`${label} rendered`); return <div><label>{label}: <input value={value} onChange={(e) => onChange(e.target.value)} /></label></div>; });
function MemoForm() {
  const [form, setForm] = useState({ name: "", email: "", phone: "" });
  const handleName = useCallback((v) => setForm((f) => ({ ...f, name: v })), []);
  const handleEmail = useCallback((v) => setForm((f) => ({ ...f, email: v })), []);
  const handlePhone = useCallback((v) => setForm((f) => ({ ...f, phone: v })), []);
  return (
    <div>
      <Field label="Name" value={form.name} onChange={handleName} />
      <Field label="Email" value={form.email} onChange={handleEmail} />
      <Field label="Phone" value={form.phone} onChange={handlePhone} />
    </div>
  );
}
export default MemoForm;
