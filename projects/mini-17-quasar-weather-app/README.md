# Mini Project 17 — Quasar Weather App

> **Type:** Mini Project
> **Subject:** Quasar
> **Estimated sell price:** $100–200
> **Difficulty:** Beginner–Intermediate
> **Prerequisites:** Lessons 01–10 (Quasar basics through API integration)

## Project Brief

Build a weather app with Quasar that searches for cities, displays current weather and 5-day forecast, and saves favorite cities. Uses a free weather API (OpenWeatherMap or Open-Meteo).

## What you'll build

A Quasar app with:
- Search bar to find cities
- Current weather card: temperature, condition, icon, humidity, wind
- 5-day forecast: cards with high/low temps and icons
- Favorites: save cities, quick access from favorites list
- Pinia store for favorites (persisted in localStorage)
- Loading and error states
- Responsive design

## Skills you'll demonstrate

- Quasar components (q-card, q-input, q-btn, q-list)
- Vue 3 Composition API (ref, computed)
- Pinia state management (favorites store)
- API integration (axios/fetch)
- Quasar Notify for errors
- localStorage persistence

## Requirements

- [ ] Search bar with autocomplete (or city name input)
- [ ] Current weather card: temp, condition, icon, humidity, wind speed, feels like
- [ ] 5-day forecast row: daily high/low, condition icon
- [ ] Favorite button (star icon) to save current city
- [ ] Favorites list in sidebar/drawer for quick access
- [ ] Favorites persisted in localStorage (Pinia + persist plugin)
- [ ] Loading state while fetching (q-spinner)
- [ ] Error state with Notify (city not found, API error)
- [ ] Empty state when no city selected
- [ ] Responsive: cards stack on mobile
- [ ] Uses free API (Open-Meteo is free, no API key needed)

## Deliverables

- Complete Quasar project
- Uses free weather API
- README with setup instructions
