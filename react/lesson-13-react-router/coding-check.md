# Lesson 13 — Coding Check

## Easy

### p01-solve.jsx — Basic 3 routes + 404
- [ ] `BrowserRouter` wraps the app
- [ ] Routes for Home, About, Contact
- [ ] `Link` components for navigation
- [ ] `path="*"` 404 route exists
- [ ] 404 page shows for unknown URLs

### p02-solve.jsx — NavLink active state
- [ ] `NavLink` used (not Link)
- [ ] Active link gets "active" class
- [ ] 4 routes defined
- [ ] Active state changes when navigating
- [ ] CSS styles the active link differently

### p03-solve.jsx — Dynamic route with params
- [ ] Route `/user/:username` defined
- [ ] `useParams()` extracts username
- [ ] Username displayed on the page
- [ ] Links to 3 different profiles
- [ ] Each profile shows the correct username

## Medium

### p01-solve.jsx — Login redirect
- [ ] Login form with submit handler
- [ ] `useNavigate` used for redirect
- [ ] Redirects to `/dashboard` after submit
- [ ] Back button on dashboard uses `navigate(-1)`
- [ ] Back button returns to login page

### p02-solve.jsx — Nested dashboard routes
- [ ] Parent route `/dashboard` with layout component
- [ ] `<Outlet />` in the layout for child content
- [ ] Index route for `/dashboard` (overview)
- [ ] Child routes: `/dashboard/stats`, `/dashboard/settings`
- [ ] Sidebar present on all dashboard pages
- [ ] Only content area changes between sub-pages

### p03-solve.jsx — URL search params
- [ ] `useSearchParams` used
- [ ] Pagination: `?page=2` works
- [ ] Sorting: `?sort=price` works
- [ ] Buttons update URL params
- [ ] Current page and sort displayed
- [ ] URL is shareable (reload preserves state)

## Hard

### p01-solve.jsx — Blog app
- [ ] Home route shows post list
- [ ] `/post/:slug` shows single post
- [ ] `/category/:category` shows filtered posts
- [ ] `/admin` is protected (redirects to login if not auth)
- [ ] 404 page for unknown routes
- [ ] Navigation between routes works
- [ ] Category filter works correctly

### p02-solve.jsx — Multi-step wizard
- [ ] 4 routes: step1, step2, step3, review
- [ ] Each step saves data (useLocation state or context)
- [ ] Can't skip to step3 without completing step1
- [ ] Review page shows all collected data
- [ ] Back navigation preserves data
- [ ] Progress indicator shows current step

### p03-solve.jsx — E-commerce routing
- [ ] Home route `/`
- [ ] Product list `/products` with filters
- [ ] Product detail `/products/:id`
- [ ] Cart route `/cart`
- [ ] Checkout `/checkout` (protected)
- [ ] Account `/account` (protected) with nested routes
- [ ] `/account/orders` and `/account/settings` work
- [ ] Protected routes redirect to login
- [ ] 404 page exists
- [ ] Navigation is seamless (no page reloads)
