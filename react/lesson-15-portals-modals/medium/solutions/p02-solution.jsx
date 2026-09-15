// Lesson 15 — Medium P02: Confirmation dialog
import { useState } from "react";
import { createPortal } from "react-dom";
function ConfirmDialog({ message, onConfirm, onCancel }) {
  return createPortal(
    <div onClick={onCancel} style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", display: "flex", alignItems: "center", justifyContent: "center" }}>
      <div onClick={(e) => e.stopPropagation()} style={{ background: "#fff", padding: 20, borderRadius: 8, textAlign: "center" }}>
        <p>{message}</p>
        <button onClick={onConfirm}>Confirm</button>
        <button onClick={onCancel}>Cancel</button>
      </div>
    </div>,
    document.body
  );
}
function App() {
  const [show, setShow] = useState(false);
  return (
    <div>
      <button onClick={() => setShow(true)}>Delete Item</button>
      {show && <ConfirmDialog message="Are you sure?" onConfirm={() => { alert("Deleted!"); setShow(false); }} onCancel={() => setShow(false)} />}
    </div>
  );
}
export default App;
