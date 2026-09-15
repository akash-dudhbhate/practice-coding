# Movie Search App (React + API) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-06-movie-search/
├── src/App.jsx, src/components/SearchBar.jsx, src/components/MovieCard.jsx, src/components/MovieList.jsx, src/components/MovieModal.jsx, src/hooks/useMovieSearch.js
└── README.md
```

---

## Implementation Steps

### Step 1: Setup

create-vite react. Get OMDB API key from omdbapi.com.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: useMovieSearch Hook

State: query, results, loading, error, selected. Fetch from OMDB API. Debounce.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: SearchBar Component

Input with search icon. Debounced API call. Show loading spinner.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: MovieCard Component

Poster, title, year, type. Click to show details. Hover effect.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: MovieList Component

Grid of MovieCards. Loading skeleton. Empty state. Error state.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: MovieModal Component

Full details: plot, cast, ratings, runtime. Close button. Backdrop click to close.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: App Component

Compose. Manage state. Handle API errors gracefully.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Styling

Grid layout, card shadows, modal overlay. Responsive.

**Checkpoint:** Step 8 is complete when the described functionality works.

### Step 9: Debouncing

Use setTimeout or lodash debounce. Cancel old requests.

**Checkpoint:** Step 9 is complete when the described functionality works.

---

## Final Checklist

- [ ] Search bar with debounce
- [ ] Movie cards in a grid
- [ ] Movie detail modal
- [ ] Loading state (spinner or skeleton)
- [ ] Error state (message + retry)
- [ ] Empty state (no results)
- [ ] Responsive grid
- [ ] API key in env variable

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
