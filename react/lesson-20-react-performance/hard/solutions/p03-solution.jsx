// Lesson 20 — Hard P03: Performance comparison demo
import { useState, useMemo, useCallback, memo, Profiler, useTransition } from "react";

const MemoItem = memo(({ item, onDelete }) => { console.log("MemoItem rendered"); return <li>{item} <button onClick={onDelete}>x</button></li>; });
const NonMemoItem = ({ item, onDelete }) => { console.log("NonMemoItem rendered"); return <li>{item} <button onClick={onDelete}>x</button></li>; };

function PerformanceDemo() {
  const [optimized, setOptimized] = useState(true);
  const [count, setCount] = useState(0);
  const [renderTimes, setRenderTimes] = useState({ largeList: 0, expensiveCalc: 0, frequentUpdates: 0 });
  const [isPending, startTransition] = useTransition();

  const largeData = useMemo(() => Array.from({ length: 1000 }, (_, i) => `Item ${i}`), []);
  const expensiveResult = useMemo(() => {
    let result = 0;
    for (let i = 0; i < 100000; i++) result += Math.sqrt(i);
    return result;
  }, []);

  const handleDelete = useCallback(() => {}, []);
  const Item = optimized ? MemoItem : NonMemoItem;

  const onRender = (id) => setRenderTimes((prev) => ({ ...prev, [id]: prev[id] + 1 }));

  return (
    <div className="p-8 space-y-6">
      <label className="block">
        <input type="checkbox" checked={optimized} onChange={(e) => setOptimized(e.target.checked)} />
        Optimized mode {optimized ? "ON" : "OFF"}
      </label>

      <Profiler id="largeList" onRender={() => onRender("largeList")}>
        <section>
          <h3>Large List ({optimized ? "memoized" : "non-memoized"})</h3>
          <p>Renders: {renderTimes.largeList}</p>
          <ul>{largeData.slice(0, 20).map((item, i) => <Item key={i} item={item} onDelete={handleDelete} />)}</ul>
        </section>
      </Profiler>

      <Profiler id="expensiveCalc" onRender={() => onRender("expensiveCalc")}>
        <section>
          <h3>Expensive Calculation</h3>
          <p>Renders: {renderTimes.expensiveCalc}</p>
          <p>Result: {expensiveResult.toFixed(2)}</p>
        </section>
      </Profiler>

      <Profiler id="frequentUpdates" onRender={() => onRender("frequentUpdates")}>
        <section>
          <h3>Frequent Updates {isPending && "(pending...)"}</h3>
          <p>Renders: {renderTimes.frequentUpdates}</p>
          <p>Count: {count}</p>
          <button onClick={() => setCount(count + 1)}>Increment</button>
        </section>
      </Profiler>
    </div>
  );
}
export default PerformanceDemo;
