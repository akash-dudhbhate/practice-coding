// Lesson 15 — Hard P01: Accessible modal with focus trap
import { useState, useEffect, useRef } from "react";
import { createPortal } from "react-dom";
function AccessibleModal({ onClose, children }) {
  const modalRef = useRef(null);
  const previouslyFocused = useRef(null);
  useEffect(() => {
    previouslyFocused.current = document.activeElement;
    const modal = modalRef.current;
    modal?.focus();
    const onKey = (e) => {
      if (e.key === "Escape") { onClose(); return; }
      if (e.key === "Tab") {
        const focusable = modal?.querySelectorAll('button, a, input, [tabindex]');
        if (!focusable) return;
        const first = focusable[0], last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
        else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
      }
    };
    document.addEventListener("keydown", onKey);
    document.body.style.overflow = "hidden";
    return () => { document.removeEventListener("keydown", onKey); document.body.style.overflow = ""; previouslyFocused.current?.focus(); };
  }, [onClose]);
  return createPortal(
    <div onClick={onClose} style={{ position: "fixed", inset: 0, background: "rgba(0,0,0,0.5)", display: "flex", alignItems: "center", justifyContent: "center" }}>
      <div ref={modalRef} role="dialog" aria-modal="true" tabIndex={-1} onClick={(e) => e.stopPropagation()} style={{ background: "#fff", padding: 20, borderRadius: 8 }}>
        {children}<button onClick={onClose}>Close</button>
      </div>
    </div>,
    document.body
  );
}
function App() {
  const [open, setOpen] = useState(false);
  return <div><button onClick={() => setOpen(true)}>Open</button>{open && <AccessibleModal onClose={() => setOpen(false)}><p>Accessible modal</p></AccessibleModal>}</div>;
}
export default App;
