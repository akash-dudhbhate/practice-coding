// Lesson 14 — Medium P01: ErrorBoundary with logging
import { Component } from "react";
class ErrorBoundary extends Component {
  constructor(props) { super(props); this.state = { hasError: false, error: null }; }
  static getDerivedStateFromError(error) { return { hasError: true, error }; }
  componentDidCatch(error, errorInfo) {
    console.error("Error caught:", error.message);
    console.error("Component stack:", errorInfo.componentStack);
  }
  render() {
    if (this.state.hasError) return <div><h2>Error</h2><p>{this.state.error?.message}</p></div>;
    return this.props.children;
  }
}
export default ErrorBoundary;
