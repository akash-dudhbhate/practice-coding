// Lesson 15 — Hard P03: Toast/Notification system with portals
import { useState, useEffect } from "react";
import { createPortal } from "react-dom";
let toastId = 0;
const listeners = new Set();
export const toast = {
  success: (msg) => listeners.forEach((l) => l({ id: ++toastId, type: "success", msg })),
  error: (msg) => listeners.forEach((l) => l({ id: ++toastId, type: "error", msg })),
};
function ToastContainer() {
  const [toasts, setToasts] = useState([]);
  useEffect(() => {
    const listener = (toast) => {
      setToasts((prev) => [...prev, toast]);
      setTimeout(() => setToasts((prev) => prev.filter((t) => t.id !== toast.id)), 3000);
    };
    listeners.add(listener);
    return () => listeners.delete(listener);
  }, []);
  return createPortal(
    <div style={{ position: "fixed", top: 20, right: 20, display: "flex", flexDirection: "column", gap: 8, zIndex: 1000 }}>
      {toasts.map((t) => (
        <div key={t.id} onClick={() => setToasts((prev) => prev.filter((x) => x.id !== t.id))} style={{
          background: t.type === "success" ? "#2ecc71" : "#e74c3c", color: "#fff", padding: "12px 20px",
          borderRadius: 4, cursor: "pointer", animation: "slideIn 0.3s ease",
        }}>
          {t.msg}
        </div>
      ))}
    </div>,
    document.body
  );
}
function App() {
  return (
    <div>
      <button onClick={() => toast.success("Saved!")}>Success Toast</button>
      <button onClick={() => toast.error("Failed!")}>Error Toast</button>
      <ToastContainer />
    </div>
  );
}
export default App;
