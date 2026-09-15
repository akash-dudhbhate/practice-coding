// Lesson 09 — Hard P03: PerformanceDemo (memoized vs non-memoized)
import { useState, useMemo, Profiler } from "react";
function PerformanceDemo() {
  const [memoized, setMemoized] = useState(true);
  const [count, setCount] = useState(0);
  const data = useMemo(() => Array.from({ length: 1000 }, (_, i) => i * count), [count]);
  const compute = memoized ? data : Array.from({ length: 1000 }, (_, i) => i * count);
  const onRender = (id, phase, actualTime) => console.log(`${id} ${phase}: ${actualTime}ms`);
  return (
    <div>
      <label><input type="checkbox" checked={memoized} onChange={(e) => setMemoized(e.target.checked)} /> Memoized</label>
      <button onClick={() => setCount(count + 1)}>Recompute (count: {count})</button>
      <Profiler id="list" onRender={onRender}>
        <p>First 5: {compute.slice(0, 5).join(", ")}</p>
      </Profiler>
    </div>
  );
}
export default PerformanceDemo;
