// Lesson 01 — Medium P03: Alert Component with conditional render
function Alert({ message, type, show }) {
  if (!show) return null;
  const styles = { success: "#2ecc71", error: "#e74c3c", warning: "#f39c12", info: "#3498db" };
  return (
    <div style={{ background: styles[type] || "#999", color: "#fff", padding: "12px", borderRadius: "4px", margin: "8px 0" }}>
      {message}
    </div>
  );
}
export default Alert;
