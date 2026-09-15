// Lesson 04 — Medium P01: Loading State
import { useState } from "react";
function LoadingState() {
  const [loading, setLoading] = useState(true);
  if (loading) {
    return (
      <div>
        <p>Loading...</p>
        <button onClick={() => setLoading(false)}>Simulate Loaded</button>
      </div>
    );
  }
  return <div><p>Content loaded!</p></div>;
}
export default LoadingState;
