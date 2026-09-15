// Lesson 09 — Easy P02: React.memo child + useCallback
import { useState, useCallback, memo } from "react";
const Child = memo(({ onClick }) => { console.log("Child rendered"); return <button onClick={onClick}>Child Button</button>; });
function Parent() {
  const [count, setCount] = useState(0);
  const handleClick = useCallback(() => console.log("Clicked"), []);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <Child onClick={handleClick} />
    </div>
  );
}
export default Parent;
