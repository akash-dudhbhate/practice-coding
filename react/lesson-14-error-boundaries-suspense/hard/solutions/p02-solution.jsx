// Lesson 14 — Hard P02: Dashboard with per-widget ErrorBoundary
import { Component } from "react";
class ErrorBoundary extends Component {
  constructor(props) { super(props); this.state = { hasError: false }; }
  static getDerivedStateFromError() { return { hasError: true }; }
  reset = () => this.setState({ hasError: false });
  render() {
    if (this.state.hasError) return <div><p>Widget crashed</p><button onClick={this.reset}>Retry</button></div>;
    return this.props.children;
  }
}
function StatsWidget() { return <div>Stats: 100 users</div>; }
function ChartWidget() { return <div>Chart: [bar chart]</div>; }
function BuggyWidget() { throw new Error("Widget crashed!"); }
function Dashboard() {
  return (
    <div style={{ display: "flex", gap: 20 }}>
      <ErrorBoundary><StatsWidget /></ErrorBoundary>
      <ErrorBoundary><ChartWidget /></ErrorBoundary>
      <ErrorBoundary><BuggyWidget /></ErrorBoundary>
    </div>
  );
}
export default Dashboard;
