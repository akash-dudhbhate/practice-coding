# Lesson 13 — React Router

## What you'll learn
- Client-side routing (BrowserRouter, Routes, Route)
- Link vs NavLink (active states)
- Dynamic routes and useParams
- useNavigate (programmatic navigation)
- Nested routes and Outlet
- URL search parameters (useSearchParams)
- Protected routes (auth checks)
- 404 (NotFound) routes
- useLocation (current URL info)

## Lesson

### Basic routing
```jsx
<BrowserRouter>
  <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/users/:id" element={<User />} />
    <Route path="*" element={<NotFound />} />
  </Routes>
</BrowserRouter>
```

### Navigation
```jsx
<Link to="/about">About</Link>
const { id } = useParams();
const navigate = useNavigate();
```

---

## Your Tasks

### Easy
1. `easy/p01-solve.jsx` — Create an app with 3 routes: Home, About, Contact. Use `Link` for navigation. Include a 404 route for unknown paths.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Home | About | Contact          <- nav links
   ----------------------------------
   Home                             <- <h1> swaps per route

   /nope  ->  404 - Page Not Found
   ```
2. `easy/p02-solve.jsx` — Create a navigation bar with `NavLink` that highlights the active page. Include 4 routes.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Home | *About* | Services | Contact
        (active link is RED, others blue)
   ----------------------------------
   About                            <- <h1>
   ```
3. `easy/p03-solve.jsx` — Create a dynamic route `/user/:username` that displays the username from `useParams`. Add links to 3 different user profiles.

   WHAT IT SHOULD LOOK LIKE:
   ```
   alice | bob | charlie            <- 3 links, same route pattern
   ----------------------------------
   Profile: bob                     <- <h1> shows the param
   ```

### Medium
4. `medium/p01-solve.jsx` — Create a login form that uses `useNavigate` to redirect to `/dashboard` after submit. Include a back button on the dashboard using `navigate(-1)`.

   WHAT IT SHOULD LOOK LIKE:
   ```
   / (login):              /dashboard (after submit):
   +----------------+      Dashboard               <- <h1>
   | user@x.com     |      [ Back ]                <- navigate(-1)
   +----------------+
   [ Login ]
   ```
5. `medium/p02-solve.jsx` — Create a dashboard with nested routes: `/dashboard` (overview), `/dashboard/stats`, `/dashboard/settings`. Use `<Outlet>` for the shared layout (sidebar + content area).

   WHAT IT SHOULD LOOK LIKE:
   ```
   +-----------+------------------------+
   | Overview  |                        |
   | Stats     |   Stats                |  <- <Outlet/> swaps the
   | Settings  |   (child route h2)     |     <h2> per child route
   +-----------+------------------------+
     sidebar stays put while content swaps
   ```
6. `medium/p03-solve.jsx` — Create a product list with `useSearchParams` for pagination (`?page=2`) and sorting (`?sort=price`). Buttons update the URL params. Display current page and sort.

   WHAT IT SHOULD LOOK LIKE:
   ```
   URL: /?page=2&sort=price
   Page: 2, Sort: price              <- <p>
   [ Prev ] [ Next ]  [ Sort: name ] [ Sort: price ]
   ```

### Hard
7. `hard/p01-solve.jsx` — Build a blog app with routes: home (post list), `/post/:slug` (single post), `/category/:category` (filtered list), `/admin` (protected). Include a 404 page and protected route for admin.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Home | Admin                          <- nav
   ----------------------------------
   * My first post        (/post/my-first-post)
   * React tips           (/post/react-tips)
   Category: react -> shows filtered list
   /post/bad-slug -> "Post not found"; /xyz -> 404
   ```
8. `hard/p02-solve.jsx` — Build a multi-step wizard: `/wizard/step1`, `/wizard/step2`, `/wizard/step3`, `/wizard/review`. Each step saves data. Use `useLocation` state to pass data between steps. Can't skip to step3 without completing step1.

   WHAT IT SHOULD LOOK LIKE:
   ```
   /wizard/step1:           /wizard/step3 (after steps 1+2):
   Name: [ Ada____ ]        Name:  Ada
          [ Next ]          Email: ada@x.com
   (jumping straight to step3 shows
    "Complete step 1 first" + link back)
   ```
9. `hard/p03-solve.jsx` — Build a complete e-commerce routing structure: `/` (home), `/products` (list with filters), `/products/:id` (detail), `/cart`, `/checkout` (protected), `/account` (protected), `/account/orders`, `/account/settings`. Include nested routes for account.

   WHAT IT SHOULD LOOK LIKE:
   ```
   Home | Products | Cart | Account      <- top nav
   ----------------------------------
   /products/42  ->  Product 42          <- detail from param
   /account:
   +----------+------------------+
   | Orders   |  Orders          |       <- AccountLayout sidebar
   | Settings |  (<Outlet/>)      |          + nested routes
   +----------+------------------+
   ```

### How to work
- Write your complete React solution (router, pages, components).
- Remove the TODO comment when done.
- Test by importing into a React app with react-router-dom installed.
