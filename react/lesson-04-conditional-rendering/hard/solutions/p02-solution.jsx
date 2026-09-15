// Lesson 04 — Hard P02: Object Map Status Display
import { useState } from "react";
function StatusDisplay() {
  const [status, setStatus] = useState("loading");
  const content = {
    loading: <p>Loading...</p>,
    success: <p style={{ color: "green" }}>Success!</p>,
    error: <p style={{ color: "red" }}>Error occurred</p>,
    empty: <p>No data found</p>,
  };
  return (
    <div>
      {content[status]}
      <div>
        <button onClick={() => setStatus("loading")}>Loading</button>
        <button onClick={() => setStatus("success")}>Success</button>
        <button onClick={() => setStatus("error")}>Error</button>
        <button onClick={() => setStatus("empty")}>Empty</button>
      </div>
    </div>
  );
}
export default StatusDisplay;
