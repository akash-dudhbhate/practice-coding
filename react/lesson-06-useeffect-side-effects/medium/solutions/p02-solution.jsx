// Lesson 06 — Medium P02: Countdown Timer
import { useState, useEffect } from "react";
function Countdown() {
  const [count, setCount] = useState(10);
  useEffect(() => {
    if (count === 0) return;
    const timer = setInterval(() => setCount((c) => c - 1), 1000);
    return () => clearInterval(timer);
  }, [count]);
  return <p>{count === 0 ? "Done!" : count}</p>;
}
export default Countdown;
