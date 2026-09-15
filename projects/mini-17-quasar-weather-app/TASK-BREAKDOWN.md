# Quasar Weather App — Task Breakdown

> **Step-by-step implementation guide.** Follow each step in order.

---

## File Structure

```
mini-17-quasar-weather-app/
├── src/pages/Weather.vue, src/components/WeatherCard.vue, src/components/SearchBar.vue, src/composables/useWeather.js
└── README.md
```

---

## Implementation Steps

### Step 1: API Setup

Get OpenWeatherMap API key. Create useWeather composable.

**Checkpoint:** Step 1 is complete when the described functionality works.

### Step 2: SearchBar

QInput with debounce. Search by city name. Show suggestions.

**Checkpoint:** Step 2 is complete when the described functionality works.

### Step 3: WeatherCard

Current weather: temp, condition, icon, humidity, wind. Styled card.

**Checkpoint:** Step 3 is complete when the described functionality works.

### Step 4: Forecast

5-day forecast section. Horizontal scroll on mobile.

**Checkpoint:** Step 4 is complete when the described functionality works.

### Step 5: useWeather Composable

fetchWeather(city), loading, error, data. Handle API errors.

**Checkpoint:** Step 5 is complete when the described functionality works.

### Step 6: Geolocation

Use navigator.geolocation for 'current location' button.

**Checkpoint:** Step 6 is complete when the described functionality works.

### Step 7: Unit Toggle

Celsius/Fahrenheit toggle. Convert values. Persist preference.

**Checkpoint:** Step 7 is complete when the described functionality works.

### Step 8: Styling

Weather-appropriate colors. Icons for conditions. Responsive.

**Checkpoint:** Step 8 is complete when the described functionality works.

---

## Final Checklist

- [ ] City search with debounce
- [ ] Current weather display
- [ ] 5-day forecast
- [ ] Geolocation support
- [ ] Celsius/Fahrenheit toggle
- [ ] Loading and error states
- [ ] Weather icons
- [ ] Responsive design

---

## Common Pitfalls

1. **Skipping steps** — each step builds on the previous. Don't jump ahead.
2. **Not testing incrementally** — test after each step, not just at the end.
3. **Ignoring error states** — handle empty states, loading, and errors from the start.
4. **Not making it responsive** — test on mobile from the beginning, not as an afterthought.
5. **Hardcoding values** — use environment variables for API keys, URLs, and configuration.
