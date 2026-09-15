// Lesson 15 — Medium P03: Smart positioning tooltip
import { useState, useRef } from "react";
import { createPortal } from "react-dom";
function SmartTooltip({ text, children }) {
  const [show, setShow] = useState(false);
  const ref = useRef(null);
  const [pos, setPos] = useState({ top: 0, left: 0 });
  const handleEnter = () => {
    const rect = ref.current.getBoundingClientRect();
    const vw = window.innerWidth, vh = window.innerHeight;
    const tooltipWidth = 120, tooltipHeight = 30;
    const top = rect.bottom + tooltipHeight > vh ? rect.top - tooltipHeight - 8 : rect.bottom + 8;
    const left = rect.right + tooltipWidth > vw ? rect.left - tooltipWidth : rect.left;
    setPos({ top, left });
    setShow(true);
  };
  return (
    <>
      <span ref={ref} onMouseEnter={handleEnter} onMouseLeave={() => setShow(false)}>{children}</span>
      {show && createPortal(<div style={{ position: "fixed", top: pos.top, left: pos.left, background: "#333", color: "#fff", padding: "4px 8px", borderRadius: 4, fontSize: 12, maxWidth: 120 }}>{text}</div>, document.body)}
    </>
  );
}
function App() { return <div style={{ padding: 50 }}><SmartTooltip text="Smart tooltip!">Hover me</SmartTooltip></div>; }
export default App;
