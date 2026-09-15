// Lesson 15 — Easy P02: Modal closes on overlay click
import { useState } from "react";
import { createPortal } from "react-dom";
function Modal({ onClose }) {
  return createPortal(
    <div onClick={onClose} style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", display: "flex", alignItems: "center", justifyContent: "center" }}>
      <div onClick={(e) => e.stopPropagation()} style={{ background: "#fff", padding: 20, borderRadius: 8 }}>
        <p>Click outside to close</p>
        <button onClick={onClose}>Close</button>
      </div>
    </div>,
    document.body
  );
}
function App() {
  const [open, setOpen] = useState(false);
  return <div><button onClick={() => setOpen(true)}>Open</button>{open && <Modal onClose={() => setOpen(false)} />}</div>;
}
export default App;
