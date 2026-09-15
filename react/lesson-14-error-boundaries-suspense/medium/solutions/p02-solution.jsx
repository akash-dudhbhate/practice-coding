// Lesson 14 — Medium P02: ErrorBoundary with reset
import { Component } from "react";
class ErrorBoundary extends Component {
  constructor(props) { super(props); this.state = { hasError: false }; }
  static getDerivedStateFromError() { return { hasError: true }; }
  reset = () => this.setState({ hasError: false });
  render() {
    if (this.state.hasError) return <div><h2>Error occurred</h2><button onClick={this.reset}>Try Again</button></div>;
    return this.props.children;
  }
}
export default ErrorBoundary;
