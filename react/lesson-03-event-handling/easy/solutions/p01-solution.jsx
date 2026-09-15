// Lesson 03 — Easy P01: Click Counter
import { useState } from "react";
function ClickCounter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>Clicked: {count}</button>;
}
export default ClickCounter;
