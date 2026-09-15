// Lesson 07 — Easy P02: Checkbox Toggle
import { useState } from "react";
function SubscribeCheckbox() {
  const [subscribed, setSubscribed] = useState(false);
  return (
    <div>
      <label><input type="checkbox" checked={subscribed} onChange={(e) => setSubscribed(e.target.checked)} /> Subscribe to newsletter</label>
      <p>{subscribed ? "Subscribed!" : "Not subscribed"}</p>
    </div>
  );
}
export default SubscribeCheckbox;
