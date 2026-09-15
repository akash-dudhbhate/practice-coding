// Lesson 03 — Easy P03: Double-Click Alert
import { useState } from "react";
function DoubleClickBox() {
  const [color, setColor] = useState("#667eea");
  return (
    <div
      onClick={() => setColor(color === "#667eea" ? "#e74c3c" : "#667eea")}
      onDoubleClick={() => alert("Double clicked!")}
      style={{ width: "100px", height: "100px", background: color, cursor: "pointer" }}
    />
  );
}
export default DoubleClickBox;
