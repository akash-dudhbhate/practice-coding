# Lesson 13 — Refactoring Challenges

## Refactor 01 (Easy): Manual Navigation State
### Before
```jsx
const [page, setPage] = useState("home");
page === "about" && <About />
```
### After
```jsx
<Routes>
  <Route path="/about" element={<About />} />
</Routes>
```

## Refactor 02 (Medium): Hardcoded URLs
### Before
```jsx
navigate("/users/" + userId);
```
### After
```jsx
navigate(`/users/${userId}`);
// or better: named routes
```

## Refactor 03 (Hard): No Lazy Loading
### Before
```jsx
import Home from "./Home";
import About from "./About";
import Admin from "./Admin"; // all loaded upfront
```
### After
```jsx
const Home = lazy(() => import("./Home"));
const About = lazy(() => import("./About"));
const Admin = lazy(() => import("./Admin"));
<Suspense fallback={<Spinner />}><Routes>...</Routes></Suspense>
```
