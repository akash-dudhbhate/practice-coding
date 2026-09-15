// Lesson 04 — Easy P01: Show/Hide Toggle
import { useState } from "react";
function ShowHide() {
  const [show, setShow] = useState(false);
  return (
    <div>
      <button onClick={() => setShow(!show)}>{show ? "Hide" : "Show"}</button>
      {show && <p>Hello, I'm visible!</p>}
    </div>
  );
}
export default ShowHide;
