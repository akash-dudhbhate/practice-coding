// Lesson 18 — Medium P03: Styled form
import { useState } from "react";
function StyledForm() {
  const [form, setForm] = useState({ name: "", email: "", password: "", role: "", agree: false });
  const [errors, setErrors] = useState({});
  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setForm({ ...form, [name]: type === "checkbox" ? checked : value });
    setErrors({ ...errors, [name]: "" });
  };
  return (
    <form className="max-w-md mx-auto p-4 space-y-4">
      <div><label className="block text-sm font-medium mb-1">Name</label><input name="name" value={form.name} onChange={handleChange} className={`w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400 ${errors.name ? "border-red-500" : "border-gray-300"}`} /></div>
      <div><label className="block text-sm font-medium mb-1">Email</label><input type="email" name="email" value={form.email} onChange={handleChange} className={`w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400 ${errors.email ? "border-red-500" : "border-gray-300"}`} /></div>
      <div><label className="block text-sm font-medium mb-1">Password</label><input type="password" name="password" value={form.password} onChange={handleChange} className={`w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400 ${errors.password ? "border-red-500" : "border-gray-300"}`} /></div>
      <div><label className="block text-sm font-medium mb-1">Role</label><select name="role" value={form.role} onChange={handleChange} className="w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"><option value="">Select...</option><option value="user">User</option><option value="admin">Admin</option></select></div>
      <label className="flex items-center gap-2"><input type="checkbox" name="agree" checked={form.agree} onChange={handleChange} className="rounded" /><span className="text-sm">I agree to terms</span></label>
    </form>
  );
}
export default StyledForm;
