// Lesson 03 — Hard P01: Clickable Card with Inner Button (stopPropagation)
import { useState } from "react";
function CardWithButton() {
  const [log, setLog] = useState([]);
  return (
    <div>
      <div onClick={() => setLog([...log, "Card clicked"])} style={{ border: "1px solid #333", padding: "20px", cursor: "pointer" }}>
        <p>Click the card or the button</p>
        <button onClick={(e) => { e.stopPropagation(); setLog([...log, "Details"]); }}>Details</button>
      </div>
      <p>Log: {log.join(", ")}</p>
    </div>
  );
}
export default CardWithButton;
