// Lesson 06 — Hard P02: Mouse Position Tracker
import { useState, useEffect } from "react";
function MouseTracker() {
  const [pos, setPos] = useState({ x: 0, y: 0 });
  useEffect(() => {
    const onMove = (e) => setPos({ x: e.clientX, y: e.clientY });
    window.addEventListener("mousemove", onMove);
    return () => window.removeEventListener("mousemove", onMove);
  }, []);
  return (
    <div>
      <p>X: {pos.x}, Y: {pos.y}</p>
      <div style={{ position: "fixed", left: pos.x, top: pos.y, width: 10, height: 10, background: "red", borderRadius: "50%", pointerEvents: "none" }} />
    </div>
  );
}
export default MouseTracker;
