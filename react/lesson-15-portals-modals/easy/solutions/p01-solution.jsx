// Lesson 15 — Easy P01: Simple modal with createPortal
import { useState } from "react";
import { createPortal } from "react-dom";
function Modal({ onClose }) {
  return createPortal(
    <div style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", display: "flex", alignItems: "center", justifyContent: "center" }}>
      <div style={{ background: "#fff", padding: 20, borderRadius: 8 }}>
        <p>Modal content</p>
        <button onClick={onClose}>Close</button>
      </div>
    </div>,
    document.body
  );
}
function App() {
  const [open, setOpen] = useState(false);
  return (
    <div>
      <button onClick={() => setOpen(true)}>Open Modal</button>
      {open && <Modal onClose={() => setOpen(false)} />}
    </div>
  );
}
export default App;
