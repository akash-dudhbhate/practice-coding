// Lesson 14 — Hard P01: Reusable ErrorBoundary with render prop
import { Component } from "react";
class ErrorBoundary extends Component {
  constructor(props) { super(props); this.state = { hasError: false, error: null }; }
  static getDerivedStateFromError(error) { return { hasError: true, error }; }
  componentDidCatch(error, errorInfo) {
    // Log to mock error service
    console.log("Error service:", { error: error.message, stack: errorInfo.componentStack });
  }
  reset = () => this.setState({ hasError: false, error: null });
  render() {
    if (this.state.hasError) return this.props.fallback(this.state.error, this.reset);
    return this.props.children;
  }
}
// Usage: <ErrorBoundary fallback={(error, reset) => <div><p>{error.message}</p><button onClick={reset}>Retry</button></div>}>...</ErrorBoundary>
export default ErrorBoundary;
