// Lesson 01 — Medium P01: User Card
function UserCard({ name, email, role }) {
  return (
    <div style={{ border: "1px solid #ddd", borderRadius: "8px", padding: "16px", margin: "8px", width: "250px" }}>
      <h3>{name}</h3>
      <p>{email}</p>
      <span style={{ background: "#667eea", color: "#fff", padding: "2px 8px", borderRadius: "4px", fontSize: "12px" }}>{role}</span>
    </div>
  );
}
function App() {
  return (
    <div>
      <UserCard name="Alice" email="alice@example.com" role="Admin" />
      <UserCard name="Bob" email="bob@example.com" role="Editor" />
      <UserCard name="Charlie" email="charlie@example.com" role="Viewer" />
    </div>
  );
}
export default App;
