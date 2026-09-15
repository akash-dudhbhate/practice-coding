// Lesson 06 — Easy P01: Document Title Updater
import { useState, useEffect } from "react";
function DocTitleCounter() {
  const [count, setCount] = useState(0);
  useEffect(() => { document.title = `Count: ${count}`; }, [count]);
  return <button onClick={() => setCount(count + 1)}>Count: {count}</button>;
}
export default DocTitleCounter;
