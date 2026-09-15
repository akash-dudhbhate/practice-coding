// Lesson 08 — Medium P01: Stopwatch
import { useState, useRef } from "react";
function Stopwatch() {
  const [time, setTime] = useState(0);
  const intervalRef = useRef(null);
  const start = () => { if (intervalRef.current) return; intervalRef.current = setInterval(() => setTime((t) => t + 1), 100); };
  const stop = () => { clearInterval(intervalRef.current); intervalRef.current = null; };
  const reset = () => { stop(); setTime(0); };
  return (
    <div>
      <p>{(time / 10).toFixed(1)}s</p>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
      <button onClick={reset}>Reset</button>
    </div>
  );
}
export default Stopwatch;
