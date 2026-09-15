// Lesson 18 — Hard P03: UI Kit demo
import { clsx } from "clsx";
import { useState } from "react";

const btnVariants = { primary: "bg-blue-500 text-white hover:bg-blue-600", secondary: "bg-gray-200 hover:bg-gray-300", danger: "bg-red-500 text-white hover:bg-red-600", success: "bg-green-500 text-white hover:bg-green-600", outline: "border border-gray-300 hover:bg-gray-100" };
function Button({ variant = "primary", className, children, ...props }) {
  return <button className={clsx("px-4 py-2 rounded transition-colors", btnVariants[variant], className)} {...props}>{children}</button>;
}
function Input({ label, error, className, ...props }) {
  return <div><label className="block text-sm font-medium mb-1">{label}</label><input className={clsx("w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400", error ? "border-red-500" : "border-gray-300", className)} {...props} /></div>;
}
function Select({ label, options, className, ...props }) {
  return <div><label className="block text-sm font-medium mb-1">{label}</label><select className={clsx("w-full px-3 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400", className)} {...props}>{options.map((o) => <option key={o.value} value={o.value}>{o.label}</option>)}</select></div>;
}
function Card({ className, children }) { return <div className={clsx("bg-white rounded-lg shadow p-6", className)}>{children}</div>; }
function Badge({ color = "blue", children }) { return <span className={`px-2 py-1 rounded text-xs bg-${color}-100 text-${color}-700`}>{children}</span>; }
function Alert({ type = "info", children }) { const colors = { info: "bg-blue-100 text-blue-700", success: "bg-green-100 text-green-700", error: "bg-red-100 text-red-700" }; return <div className={clsx("p-4 rounded", colors[type])}>{children}</div>; }
function Modal({ open, onClose, children }) { if (!open) return null; return <div onClick={onClose} className="fixed inset-0 bg-black/50 flex items-center justify-center"><div onClick={(e) => e.stopPropagation()} className="bg-white rounded-lg p-6 max-w-md">{children}</div></div>; }
function Tabs({ tabs, active, onChange }) { return <div className="border-b flex gap-4">{tabs.map((t) => <button key={t} onClick={() => onChange(t)} className={clsx("py-2 px-4 border-b-2", active === t ? "border-blue-500 text-blue-500" : "border-transparent")}>{t}</button>)}</div>; }
function Accordion({ sections }) { const [open, setOpen] = useState(null); return <div>{sections.map((s, i) => <div key={i} className="border-b"><button onClick={() => setOpen(open === i ? null : i)} className="w-full text-left py-3">{s.title}</button>{open === i && <div className="py-2 text-gray-600">{s.content}</div>}</div>)}</div>; }

function UIKitDemo() {
  const [modalOpen, setModalOpen] = useState(false);
  const [activeTab, setActiveTab] = useState("Tab 1");
  return (
    <div className="p-8 space-y-8 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold">UI Kit Demo</h1>
      <section><h2 className="font-bold mb-2">Buttons</h2><div className="flex gap-2 flex-wrap">{Object.keys(btnVariants).map((v) => <Button key={v} variant={v}>{v}</Button>)}</div></section>
      <section><h2 className="font-bold mb-2">Inputs</h2><div className="grid grid-cols-2 gap-4"><Input label="Name" placeholder="John" /><Input label="Email" error placeholder="Invalid" /></div></section>
      <section><h2 className="font-bold mb-2">Card + Badge</h2><Card><div className="flex justify-between items-center"><span>Product</span><Badge color="green">New</Badge></div></Card></section>
      <section><Alert type="success">Successfully saved!</Alert></section>
      <section><Tabs tabs={["Tab 1", "Tab 2", "Tab 3"]} active={activeTab} onChange={setActiveTab} /><p className="mt-2">Active: {activeTab}</p></section>
      <section><Accordion sections={[{ title: "Section 1", content: "Content 1" }, { title: "Section 2", content: "Content 2" }]} /></section>
      <Button onClick={() => setModalOpen(true)}>Open Modal</Button>
      <Modal open={modalOpen} onClose={() => setModalOpen(false)}><h3 className="font-bold mb-2">Modal Title</h3><p>Modal content here.</p><Button onClick={() => setModalOpen(false)} className="mt-4">Close</Button></Modal>
    </div>
  );
}
export default UIKitDemo;
