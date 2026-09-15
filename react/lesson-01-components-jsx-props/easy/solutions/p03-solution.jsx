// Lesson 01 — Easy P03: Badge Component with conditional color
function Badge({ text, variant }) {
  const colors = { success: "#2ecc71", danger: "#e74c3c", warning: "#f39c12", info: "#3498db" };
  const color = colors[variant] || "#999";
  return <span style={{ background: color, color: "#fff", padding: "2px 8px", borderRadius: "12px", fontSize: "12px" }}>{text}</span>;
}
export default Badge;
