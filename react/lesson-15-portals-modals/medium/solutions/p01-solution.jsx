// Lesson 15 — Medium P01: Modal with escape key + scroll lock
import { useState, useEffect } from "react";
import { createPortal } from "react-dom";
function Modal({ onClose, children }) {
  useEffect(() => {
    const onKey = (e) => { if (e.key === "Escape") onClose(); };
    document.addEventListener("keydown", onKey);
    document.body.style.overflow = "hidden";
    return () => { document.removeEventListener("keydown", onKey); document.body.style.overflow = ""; };
  }, [onClose]);
  return createPortal(
    <div onClick={onClose} style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", display: "flex", alignItems: "center", justifyContent: "center" }}>
      <div onClick={(e) => e.stopPropagation()} style={{ background: "#fff", padding: 20, borderRadius: 8 }}>{children}<button onClick={onClose}>Close</button></div>
    </div>,
    document.body
  );
}
function App() {
  const [open, setOpen] = useState(false);
  return <div><button onClick={() => setOpen(true)}>Open</button>{open && <Modal onClose={() => setOpen(false)}><p>Press Escape to close</p></Modal>}</div>;
}
export default App;
