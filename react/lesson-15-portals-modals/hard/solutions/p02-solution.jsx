// Lesson 15 — Hard P02: Animated modal with enter/exit transitions
import { useState, useEffect } from "react";
import { createPortal } from "react-dom";
function AnimatedModal({ onClose, children }) {
  const [visible, setVisible] = useState(false);
  const [closing, setClosing] = useState(false);
  useEffect(() => { requestAnimationFrame(() => setVisible(true)); }, []);
  const handleClose = () => {
    setClosing(true);
    setVisible(false);
    setTimeout(onClose, 300);
  };
  return createPortal(
    <div onClick={handleClose} style={{
      position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", display: "flex", alignItems: "center", justifyContent: "center",
      opacity: visible ? 1 : 0, transition: "opacity 0.3s",
    }}>
      <div onClick={(e) => e.stopPropagation()} style={{
        background: "#fff", padding: 20, borderRadius: 8,
        transform: visible ? "translateY(0)" : "translateY(50px)", transition: "transform 0.3s",
      }}>
        {children}<button onClick={handleClose}>Close</button>
      </div>
    </div>,
    document.body
  );
}
function App() {
  const [open, setOpen] = useState(false);
  return <div><button onClick={() => setOpen(true)}>Open</button>{open && <AnimatedModal onClose={() => setOpen(false)}><p>Animated!</p></AnimatedModal>}</div>;
}
export default App;
