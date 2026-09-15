// Lesson 14 — Easy P03: ErrorBoundary with missing prop
import { Component } from "react";
class ErrorBoundary extends Component {
  constructor(props) { super(props); this.state = { hasError: false }; }
  static getDerivedStateFromError() { return { hasError: true }; }
  render() {
    if (this.state.hasError) return <div style={{ color: "red" }}><h2>Oops! Something broke.</h2><p>Please refresh the page.</p></div>;
    return this.props.children;
  }
}
function UserCard({ user }) {
  if (!user) throw new Error("user prop is required");
  return <h3>{user.name}</h3>;
}
function App() {
  return (
    <ErrorBoundary>
      <UserCard />
    </ErrorBoundary>
  );
}
export default App;
