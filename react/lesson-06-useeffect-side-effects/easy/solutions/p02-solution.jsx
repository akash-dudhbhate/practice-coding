// Lesson 06 — Easy P02: Mount Message
import { useEffect } from "react";
function MountMessage() {
  useEffect(() => { console.log("Component mounted"); }, []);
  return <p>Check the console</p>;
}
export default MountMessage;
