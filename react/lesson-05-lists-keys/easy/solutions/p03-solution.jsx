// Lesson 05 — Easy P03: User Cards from Array
const users = [
  { id: 1, name: "Alice", email: "alice@example.com" },
  { id: 2, name: "Bob", email: "bob@example.com" },
  { id: 3, name: "Charlie", email: "charlie@example.com" },
];
function UserCards() {
  return (
    <div>
      {users.map((u) => (
        <div key={u.id} style={{ border: "1px solid #ddd", padding: "12px", margin: "8px" }}>
          <h3>{u.name}</h3><p>{u.email}</p>
        </div>
      ))}
    </div>
  );
}
export default UserCards;
