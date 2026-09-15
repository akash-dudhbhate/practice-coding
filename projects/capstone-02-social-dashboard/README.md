# Capstone Project 02 — Social Media Dashboard

> **Type:** Capstone Project
> **Subject:** React
> **Estimated sell price:** $500–1500
> **Difficulty:** Advanced
> **Prerequisites:** All 20 React lessons

## Project Brief

Build a complete social media dashboard frontend (like a simplified Twitter/Reddit feed). This is a sellable product — many companies need internal social feeds, community dashboards, or content aggregation UIs. The app includes a feed, post creation, likes, comments, user profiles, search, dark mode, and is fully responsive and tested.

## What you'll build

A React SPA with:
- **Feed** — scrollable list of posts with author, content, timestamp, likes, comments
- **Create post** — text area with character count, submit button
- **Like/unlike** — toggle like on any post
- **Comments** — expand comments on a post, add new comments
- **User profiles** — view a user's posts and info
- **Search** — search posts by content or author
- **Dark mode** — toggle with Context API, persists in localStorage
- **Responsive** — mobile-first, sidebar collapses on mobile
- **Loading & error states** — skeletons while loading, error messages on failure
- **Tests** — component tests with React Testing Library

## Skills you'll demonstrate

- React components, props, state (useState, useReducer)
- useEffect for data fetching
- Context API for theme and auth
- React Router for navigation (feed, profile, post detail)
- Custom hooks (useFetch, useLocalStorage, useDebounce)
- Conditional rendering (loading, error, empty states)
- Lists and keys
- Forms (controlled components)
- Performance (useMemo, useCallback, React.memo)
- Testing (React Testing Library)
- Styling (Tailwind CSS)

## Sellable pitch

> "I'll build you a complete social media dashboard with feed, posts, likes, comments, user profiles, search, and dark mode. Fully responsive, tested, and production-ready. Built with React, React Router, and Tailwind CSS."

## Requirements

- [ ] Feed page with scrollable post list
- [ ] Each post shows: author avatar, name, timestamp, content, like count, comment count
- [ ] Create post form with character count (max 280 chars)
- [ ] Like/unlike functionality (optimistic UI update)
- [ ] Comments: expand/collapse, add comment form
- [ ] User profile page showing user info and their posts
- [ ] Search bar that filters posts by content or author (debounced)
- [ ] Dark mode toggle (Context API + localStorage)
- [ ] Sidebar navigation (collapses to hamburger on mobile)
- [ ] Loading skeletons for feed and profile
- [ ] Error states with retry button
- [ ] Empty state when no posts found
- [ ] Responsive: mobile (single column), tablet (sidebar + feed), desktop (sidebar + feed + trending)
- [ ] React Router: / (feed), /profile/:userId, /post/:postId
- [ ] Tests for: post component, like button, create post form, search
- [ ] Clean, modern UI with Tailwind CSS

## Getting started

1. Design the component tree and data flow.
2. Set up React Router with routes.
3. Build the layout (sidebar, main content area).
4. Create mock data (JSON file with users and posts).
5. Build the feed component and post card.
6. Add like functionality with state.
7. Add comments (expand/collapse + add).
8. Build the create post form.
9. Build the profile page.
10. Add search with debounce.
11. Implement dark mode with Context.
12. Add loading and error states.
13. Write tests.
14. Style with Tailwind.
15. Test responsiveness.

## Deliverables

- Complete React app (organized components, hooks, context, pages)
- Mock data or integration with a mock API (JSON Server)
- Test suite with React Testing Library
- README with setup and run instructions
- Live deployment (Vercel, Netlify)
