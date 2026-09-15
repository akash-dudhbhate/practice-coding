# Lesson 18 — Common Mistakes

## Mistake 01: Using window on server
```javascript
// WRONG
if (window.innerWidth < 600)
// CORRECT
if (process.env.CLIENT && window.innerWidth < 600)
```

## Mistake 02: localStorage in setup
```javascript
// WRONG — runs on server
setup() { const x = localStorage.getItem("key"); }
// CORRECT — onMounted
onMounted(() => { const x = localStorage.getItem("key"); });
```

## Mistake 03: Hydration mismatch
```javascript
// WRONG — different output server vs client
const time = Date.now();
// CORRECT — consistent or onMounted
```

## Mistake 04: Not using preFetch
```javascript
// Fetch data on server for SEO
preFetch: async ({ store }) => { await store.dispatch("load"); }
```

## Mistake 05: Not handling SSR state
```javascript
// Server state must transfer to client
// Quasar handles this automatically with Pinia
```
