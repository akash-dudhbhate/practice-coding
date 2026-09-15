// Lesson 14 — Easy P02: React.lazy + Suspense
import { lazy, Suspense } from "react";
const LazyComponent = lazy(() => import("./SomeComponent"));
function App() {
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <LazyComponent />
    </Suspense>
  );
}
export default App;
