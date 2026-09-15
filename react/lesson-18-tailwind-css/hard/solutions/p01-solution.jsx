// Lesson 18 — Hard P01: Dashboard layout
import { useState } from "react";
function Dashboard() {
  const [collapsed, setCollapsed] = useState(false);
  return (
    <div className="flex h-screen bg-gray-100">
      <aside className={`${collapsed ? "w-16" : "w-64"} bg-gray-800 text-white transition-all p-4`}>
        <button onClick={() => setCollapsed(!collapsed)} className="mb-4">{collapsed ? "→" : "← Collapse"}</button>
        <nav className="space-y-2">
          <a href="#" className="block px-4 py-2 rounded hover:bg-gray-700">Dashboard</a>
          <a href="#" className="block px-4 py-2 rounded hover:bg-gray-700">Users</a>
          <a href="#" className="block px-4 py-2 rounded hover:bg-gray-700">Settings</a>
        </nav>
      </aside>
      <div className="flex-1 flex flex-col">
        <header className="bg-white shadow p-4"><input type="text" placeholder="Search..." className="px-4 py-2 border rounded w-64" /></header>
        <main className="flex-1 p-6 overflow-auto">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
            {["Revenue", "Users", "Orders"].map((s) => (
              <div key={s} className="bg-white rounded-lg shadow p-6"><h3 className="text-gray-500 text-sm">{s}</h3><p className="text-2xl font-bold">${Math.floor(Math.random() * 10000)}</p></div>
            ))}
          </div>
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="font-bold mb-4">Recent Orders</h3>
            <table className="w-full"><thead><tr className="border-b"><th className="text-left py-2">ID</th><th className="text-left py-2">Customer</th><th className="text-left py-2">Amount</th></tr></thead>
              <tbody>{[1, 2, 3].map((i) => <tr key={i} className="border-b"><td className="py-2">#{i}</td><td className="py-2">User {i}</td><td className="py-2">${i * 50}</td></tr>)}</tbody>
            </table>
          </div>
          <div className="bg-white rounded-lg shadow p-6 mt-4"><h3 className="font-bold mb-4">Chart Placeholder</h3><div className="h-48 bg-gray-100 rounded flex items-center justify-center text-gray-400">Chart goes here</div></div>
        </main>
      </div>
    </div>
  );
}
export default Dashboard;
