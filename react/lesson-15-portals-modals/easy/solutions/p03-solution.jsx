// Lesson 15 — Easy P03: Tooltip with portals
import { useState, useRef } from "react";
import { createPortal } from "react-dom";
function Tooltip({ text, children }) {
  const [show, setShow] = useState(false);
  const ref = useRef(null);
  const [pos, setPos] = useState({ top: 0, left: 0 });
  const handleEnter = () => {
    const rect = ref.current.getBoundingClientRect();
    setPos({ top: rect.bottom + 8, left: rect.left });
    setShow(true);
  };
  return (
    <>
      <span ref={ref} onMouseEnter={handleEnter} onMouseLeave={() => setShow(false)}>{children}</span>
      {show && createPortal(
        <div style={{ position: "fixed", top: pos.top, left: pos.left, background: "#333", color: "#fff", padding: "4px 8px", borderRadius: 4, fontSize: 12 }}>{text}</div>,
        document.body
      )}
    </>
  );
}
function App() { return <p>Hover <Tooltip text="I'm a tooltip!">this text</Tooltip></p>; }
export default App;
