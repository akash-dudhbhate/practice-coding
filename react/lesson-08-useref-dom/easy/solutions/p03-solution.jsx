// Lesson 08 — Easy P03: Track clicks with useRef (not state)
import { useRef } from "react";
function RefCounter() {
  const countRef = useRef(0);
  return (
    <div>
      <button onClick={() => { countRef.current++; console.log("Clicks:", countRef.current); }}>
        Click me (check console)
      </button>
      <p>Ref count won't update UI: {countRef.current}</p>
    </div>
  );
}
export default RefCounter;
