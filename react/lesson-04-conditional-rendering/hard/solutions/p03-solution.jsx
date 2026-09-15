// Lesson 04 — Hard P03: Permission-Based Dashboard
import { useState } from "react";
function Dashboard() {
  const [role, setRole] = useState("viewer");
  return (
    <div>
      <select value={role} onChange={(e) => setRole(e.target.value)}>
        <option value="admin">Admin</option>
        <option value="editor">Editor</option>
        <option value="viewer">Viewer</option>
      </select>
      <div>
        <h3>Dashboard ({role})</h3>
        <p>View Content</p>
        {role === "admin" && <p>Admin Panel - Delete Users, Settings</p>}
        {(role === "admin" || role === "editor") && <p>Edit Tools - Create, Edit Posts</p>}
      </div>
    </div>
  );
}
export default Dashboard;
