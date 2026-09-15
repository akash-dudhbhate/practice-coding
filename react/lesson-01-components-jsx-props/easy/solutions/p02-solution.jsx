// Lesson 01 — Easy P02: Button Component with inline style
function Button({ label, color }) {
  return <button style={{ backgroundColor: color, color: "#fff", padding: "8px 16px", border: "none", borderRadius: "4px" }}>{label}</button>;
}
export default Button;
