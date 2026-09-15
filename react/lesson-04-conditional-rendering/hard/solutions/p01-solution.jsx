// Lesson 04 — Hard P01: Full Data Fetch States
import { useState } from "react";
function DataFetcher() {
  const [state, setState] = useState("idle");
  const fetchData = () => {
    setState("loading");
    setTimeout(() => {
      const success = Math.random() > 0.3;
      if (success) setState("success");
      else setState("error");
    }, 1000);
  };
  if (state === "idle") return <button onClick={fetchData}>Fetch Data</button>;
  if (state === "loading") return <p>Loading...</p>;
  if (state === "error") return <p style={{ color: "red" }}>Error loading data. <button onClick={fetchData}>Retry</button></p>;
  if (state === "success") return <p>Data loaded successfully!</p>;
  return null;
}
export default DataFetcher;
