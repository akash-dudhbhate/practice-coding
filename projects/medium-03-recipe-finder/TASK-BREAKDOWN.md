# Recipe Finder (React + API) — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
medium-03-recipe-finder/
├── src/App.jsx, src/components/SearchBar.jsx, src/components/RecipeCard.jsx, src/components/RecipeModal.jsx, src/components/Favorites.jsx, src/hooks/useRecipes.js, src/hooks/useFavorites.js
└── README.md
```

---

## Implementation Steps

### Step 1: API Setup

Use TheMealDB API (free, no key). useRecipes composable.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: SearchBar

Search by ingredient or dish name. Debounced. Recent searches dropdown.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: RecipeCard

Image, name, category, area. Click to view details. Favorite button (heart).

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: RecipeModal

Full recipe: ingredients with measurements, instructions, video link.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: Favorites

useFavorites hook with localStorage. Favorites page/tab. Remove favorite.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Filters

Filter by category (dessert, main, etc.) and area (Italian, Mexican, etc.).

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Loading/Empty States

Skeleton loading, no results message, error state with retry.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Responsive

Grid of cards. Modal scrollable. Mobile-friendly.

**Checkpoint:** Step 8 is complete when the described functionality works.

---

## Final Checklist

- [ ] Search by name/ingredient
- [ ] Recipe cards in grid
- [ ] Recipe detail modal
- [ ] Favorites with localStorage
- [ ] Category and area filters
- [ ] Loading skeleton
- [ ] Empty and error states
- [ ] Responsive grid

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
