// Lesson 01 — Hard P03: Layout Composition with children
function Header({ children }) {
  return <header style={{ background: "#333", color: "#fff", padding: "16px" }}>{children}</header>;
}
function Footer({ children }) {
  return <footer style={{ background: "#eee", padding: "12px", textAlign: "center" }}>{children}</footer>;
}
function Layout({ children }) {
  return (
    <div style={{ minHeight: "100vh", display: "flex", flexDirection: "column" }}>
      <Header><h1>My App</h1></Header>
      <main style={{ flex: 1, padding: "20px" }}>{children}</main>
      <Footer><p>&copy; 2024</p></Footer>
    </div>
  );
}
export default Layout;
