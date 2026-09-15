// Lesson 07 — Hard P03: Dynamic Form Fields
import { useState } from "react";
function DynamicEmails() {
  const [emails, setEmails] = useState([{ id: 1, value: "" }]);
  const addEmail = () => setEmails([...emails, { id: Date.now(), value: "" }]);
  const removeEmail = (id) => setEmails(emails.filter((e) => e.id !== id));
  const updateEmail = (id, value) => setEmails(emails.map((e) => e.id === id ? { ...e, value } : e));
  const handleSubmit = (e) => {
    e.preventDefault();
    const valid = emails.filter((e) => e.value.includes("@"));
    alert(`Valid emails: ${valid.map((e) => e.value).join(", ")}`);
  };
  return (
    <form onSubmit={handleSubmit}>
      {emails.map((email) => (
        <div key={email.id}>
          <input type="email" value={email.value} onChange={(e) => updateEmail(email.id, e.target.value)} placeholder="Email" />
          <button type="button" onClick={() => removeEmail(email.id)}>Remove</button>
        </div>
      ))}
      <button type="button" onClick={addEmail}>Add Email</button>
      <button type="submit">Submit</button>
    </form>
  );
}
export default DynamicEmails;
