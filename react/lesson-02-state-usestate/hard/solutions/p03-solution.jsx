// Lesson 02 — Hard P03: Accordion
import { useState } from "react";
function Accordion({ sections }) {
  const [openIndex, setOpenIndex] = useState(null);
  return (
    <div>
      {sections.map((section, i) => (
        <div key={i} style={{ border: "1px solid #ddd", margin: "4px 0" }}>
          <button onClick={() => setOpenIndex(openIndex === i ? null : i)} style={{ width: "100%", textAlign: "left", padding: "12px" }}>
            {section.title}
          </button>
          {openIndex === i && <div style={{ padding: "12px" }}>{section.content}</div>}
        </div>
      ))}
    </div>
  );
}
export default Accordion;
