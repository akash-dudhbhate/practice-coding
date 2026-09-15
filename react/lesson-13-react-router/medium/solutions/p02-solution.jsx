// Lesson 13 — Medium P02: Nested routes with Outlet
import { BrowserRouter, Routes, Route, Link, Outlet } from "react-router-dom";
function DashboardLayout() {
  return (
    <div>
      <aside><Link to="/dashboard">Overview</Link> | <Link to="/dashboard/stats">Stats</Link> | <Link to="/dashboard/settings">Settings</Link></aside>
      <main><Outlet /></main>
    </div>
  );
}
function Overview() { return <h2>Overview</h2>; }
function Stats() { return <h2>Stats</h2>; }
function Settings() { return <h2>Settings</h2>; }
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/dashboard" element={<DashboardLayout />}>
          <Route index element={<Overview />} />
          <Route path="stats" element={<Stats />} />
          <Route path="settings" element={<Settings />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
export default App;
