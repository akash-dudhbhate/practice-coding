// Lesson 04 — Medium P03: Conditional CSS Classes
import { useState } from "react";
function ConditionalButton() {
  const [state, setState] = useState("active");
  const className = `btn ${state === "active" ? "btn-active" : state === "inactive" ? "btn-inactive" : "btn-disabled"}`;
  return (
    <div>
      <button className={className} disabled={state === "disabled"} onClick={() => setState(state === "active" ? "inactive" : "active")}>
        {state}
      </button>
      <button onClick={() => setState("disabled")}>Disable</button>
    </div>
  );
}
export default ConditionalButton;
