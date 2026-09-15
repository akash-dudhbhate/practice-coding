# Medium Project 03 — Recipe Finder with Filters

> **Type:** Medium Project
> **Subject:** React
> **Estimated sell price:** $200–500
> **Difficulty:** Intermediate
> **Prerequisites:** Lessons 01–10 (React Core + Hooks)

## Project Brief

Build a recipe finder app that searches recipes via a free API, displays results in a grid, and allows filtering by cuisine, diet, and intolerances. Users can save favorites to localStorage. This is a sellable product for food blogs, meal planning services, and health apps.

## What you'll build

A React app with:
- Search bar (debounced) to find recipes by name or ingredient
- Filter sidebar: cuisine (Italian, Mexican, Asian, etc.), diet (vegan, vegetarian, etc.), intolerances (gluten, dairy, etc.)
- Recipe grid: cards with image, title, cooking time, servings
- Recipe detail modal: full ingredients, instructions, nutrition
- Favorites: save/unsave recipes, persisted in localStorage
- Loading skeletons, error states, empty states
- Responsive (grid adjusts columns)

## Skills you'll demonstrate

- React state (useState, useReducer for filters)
- useEffect for API calls
- Custom hooks (useDebounce, useLocalStorage)
- Conditional rendering (loading, error, empty)
- Lists and keys (recipe grid)
- Forms (search, filters)
- API integration (fetch + free recipe API like Spoonacular or TheMealDB)
- Responsive design

## Requirements

- [ ] Search bar with debounce (300ms delay)
- [ ] Filter sidebar with: cuisine, diet, intolerances (checkboxes/dropdowns)
- [ ] Recipe grid with cards (image, title, time, servings)
- [ ] Click card → opens detail modal with full recipe
- [ ] Favorite button on each recipe (heart icon, toggles)
- [ ] Favorites saved to localStorage and persist on reload
- [ ] Favorites page/section showing saved recipes
- [ ] Loading skeleton cards while fetching
- [ ] Error state with retry button
- [ ] Empty state when no results
- [ ] Responsive: 1 column mobile, 2 tablet, 3-4 desktop
- [ ] Clean, food-app-inspired design

## Deliverables

- Complete React app
- Uses free API (TheMealDB is free, Spoonacular has free tier)
- README with setup and API key instructions
