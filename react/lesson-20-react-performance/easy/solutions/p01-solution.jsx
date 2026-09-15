// Lesson 20 — Easy P01: React.memo child doesn't re-render
import { useState, memo } from "react";
const Child = memo(({ label }) => { console.log("Child rendered"); return <div>{label}</div>; });
function Parent() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <Child label="Static child" />
    </div>
  );
}
export default Parent;
