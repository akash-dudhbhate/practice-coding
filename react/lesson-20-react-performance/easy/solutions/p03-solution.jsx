// Lesson 20 — Easy P03: useCallback with React.memo child
import { useState, useCallback, memo } from "react";
const Child = memo(({ onClick }) => { console.log("Child rendered"); return <button onClick={onClick}>Click me</button>; });
function Parent() {
  const [count, setCount] = useState(0);
  const [text, setText] = useState("");
  const handleClick = useCallback(() => console.log("Clicked"), []);
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <input value={text} onChange={(e) => setText(e.target.value)} placeholder="Type here" />
      <Child onClick={handleClick} />
    </div>
  );
}
export default Parent;
